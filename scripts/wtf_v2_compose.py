"""WTF v2 composition — louder gold halo, pulsing highlights, sergeant header glow.
Re-renders all 5 hero segments with v2 visuals. Replaces seg 9 with David-voiced version.
"""
import json, os, subprocess, math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import urllib.request

OUT = Path('/sessions/dreamy-sleepy-archimedes/mnt/outputs')
WORK = Path('/tmp/wtf_v2')
WORK.mkdir(parents=True, exist_ok=True)

W, H = 1280, 720
TRAY_W = 280
VIEW_W = W - TRAY_W
CAPTION_H = 160
VIEW_H = H - CAPTION_H

DARK = (10, 14, 25)
TRAY_BG = (16, 22, 36)
PANEL_BG = (20, 26, 40)
GOLD_HOT = (255, 200, 80)
GOLD_BRIGHT = (255, 220, 120)
GOLD_DIM = (140, 100, 50)
ORANGE = (255, 140, 60)
ORANGE_DIM = (140, 80, 40)
CREAM = (240, 234, 224)
GREY = (110, 115, 125)
GREY_DIM = (60, 65, 75)
WHITE = (255, 255, 255)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

soldiers = [
    "Gen-4.5", "Gen-4 Turbo", "Gen-3 Turbo", "seedance2", "veo3", "veo3.1", "veo3.1 fast", "Aleph",
    "gen4_image", "gen4_image_turbo", "gemini_2.5", "GWM Worlds", "Characters", "GWM Robotics",
    "Act-Two", "Inpainting", "Interpolation", "4K Upscale", "Super-Res", "Remove BG",
    "TTS Multi v2", "Voice Iso", "Dubbing", "Voice Conv", "Sound FX", "Custom Voice",
    "Skills FW", "avatars-react", "livekit", "agents-js", "MCP Server",
    "Python SDK", "Node SDK", "avatars-rpc", "Workflows", "Webhooks", "Async Tasks",
    "Ref Image", "Moderation", "Uploads", "Knowledge", "Org/Credits",
    "gen-video", "gen-image", "gen-audio", "characters-int", "documents-int", "use-runway-api",
    "Builders", "Fund", "Labs"
]
sergeants = [
    ("VIDEO", 1, 8), ("IMAGE", 9, 11), ("WORLD", 12, 14), ("PERFORM", 15, 15),
    ("EDITING", 16, 20), ("AUDIO", 21, 26), ("FRAMEWORK", 27, 31), ("SDKs", 32, 34),
    ("PLATFORM", 35, 42), ("SKILLS+ECO", 43, 51),
]

def soldier_layout():
    layout = []
    y = 90
    for sname, lo, hi in sergeants:
        sg_y = y
        y += 32
        cnt = hi - lo + 1
        cols = min(4, cnt)
        rows = math.ceil(cnt / cols)
        slot_w = (TRAY_W - 24) // cols
        slot_h = 28
        for k in range(cnt):
            r = k // cols
            c = k % cols
            sx = 12 + c * slot_w
            sy = y + r * (slot_h + 3)
            layout.append((lo + k, sx, sy, slot_w - 4, slot_h, sname, sg_y))
        y += rows * (slot_h + 3) + 10
    return layout

LAYOUT = soldier_layout()

def draw_glow_rect(img, box, color, alpha_outer=80, alpha_mid=160, alpha_inner=255, layers=4):
    """Multi-layer glow around a rectangle. Draws on RGBA image."""
    overlay = Image.new('RGBA', img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    x0, y0, x1, y1 = box
    for k in range(layers, 0, -1):
        pad = k * 4
        a = int(alpha_outer + (alpha_mid - alpha_outer) * (1 - k / layers))
        draw.rectangle([x0 - pad, y0 - pad, x1 + pad, y1 + pad],
                       outline=color + (a,), width=2)
    # blur the glow
    img.alpha_composite(overlay)

def draw_pulse_ring(img, box, color, t, period=0.6):
    """Pulsing outer ring around a tool slot. t in seconds."""
    overlay = Image.new('RGBA', img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    pulse = 0.5 + 0.5 * math.sin(2 * math.pi * t / period)  # 0..1
    x0, y0, x1, y1 = box
    pad = int(3 + 8 * pulse)
    alpha = int(80 + 175 * pulse)
    draw.rectangle([x0 - pad, y0 - pad, x1 + pad, y1 + pad],
                   outline=color + (alpha,), width=3)
    img.alpha_composite(overlay)

def is_active_sergeant(sname, active_soldiers):
    """Return True if any soldier in this sergeant is active."""
    for sg_name, lo, hi in sergeants:
        if sg_name == sname:
            return any(s in active_soldiers for s in range(lo, hi + 1))
    return False

def render_overlay_frame(t, beat):
    """Render a single overlay frame at time t (seconds) with v2 visuals."""
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Tray background
    draw.rectangle([0, 0, TRAY_W, H], fill=TRAY_BG + (255,))
    # Header
    f_h = ImageFont.truetype(FONT_BOLD, 24)
    f_sub = ImageFont.truetype(FONT_REG, 13)
    draw.text((20, 22), "TOOL TRAY", font=f_h, fill=ORANGE + (255,))
    draw.text((20, 52), "Number One Son · 51 Soldiers", font=f_sub, fill=GREY + (255,))
    # Determine flying tool
    flying = None
    for (sid, st, et) in beat['fly_sequence']:
        if st <= t < et:
            p = (t - st) / (et - st)
            flying = (sid, p)
            break
    # Sergeant headers + soldier badges
    f_sg = ImageFont.truetype(FONT_BOLD, 13)
    f_sd = ImageFont.truetype(FONT_MONO, 11)
    f_nm = ImageFont.truetype(FONT_REG, 10)
    last_sg = None
    sg_active_now = set()
    for sg_name, lo, hi in sergeants:
        if any(s in beat['active'] for s in range(lo, hi + 1)):
            sg_active_now.add(sg_name)
    for entry in LAYOUT:
        idx, x, y, w, h, sname, sg_y = entry
        if sname != last_sg:
            sg_is_on = sname in sg_active_now
            if sg_is_on:
                # Sergeant header glow
                draw.rectangle([8, sg_y + 4, TRAY_W - 8, sg_y + 26],
                               fill=(50, 30, 12, 200))
                draw.rectangle([8, sg_y + 4, TRAY_W - 8, sg_y + 26],
                               outline=GOLD_HOT + (255,), width=1)
                draw.text((16, sg_y + 7), sname, font=f_sg, fill=GOLD_BRIGHT + (255,))
                # Glow accent
                draw_glow_rect(img, (8, sg_y + 4, TRAY_W - 8, sg_y + 26),
                               GOLD_HOT, alpha_outer=40, alpha_mid=80, layers=3)
                draw = ImageDraw.Draw(img)  # rebind
            else:
                draw.text((16, sg_y + 8), sname, font=f_sg, fill=GREY + (255,))
            last_sg = sname
        on = idx in beat['active']
        is_flying = flying and flying[0] == idx
        if on and not is_flying:
            # ACTIVE TOOL — bright gold halo + pulsing
            box = (x, y, x + w, y + h)
            # Pulsing outer ring
            draw_pulse_ring(img, box, GOLD_HOT, t)
            # Solid bright fill
            draw = ImageDraw.Draw(img)
            draw.rectangle(box, fill=(80, 50, 20, 255), outline=GOLD_HOT + (255,), width=3)
            # Glow halo
            draw_glow_rect(img, box, GOLD_HOT, alpha_outer=60, alpha_mid=140, layers=4)
            draw = ImageDraw.Draw(img)
            draw.text((x + 5, y + h//2 - 6), f"{idx:02d}", font=f_sd, fill=GOLD_BRIGHT + (255,))
            draw.text((x + 26, y + h//2 - 6), soldiers[idx-1][:13], font=f_nm, fill=CREAM + (255,))
        elif not is_flying:
            # Inactive
            draw.rectangle([x, y, x + w, y + h], fill=PANEL_BG + (255,),
                           outline=GREY_DIM + (255,), width=1)
            draw.text((x + 5, y + h//2 - 6), f"{idx:02d}", font=f_sd, fill=GREY + (255,))
            draw.text((x + 26, y + h//2 - 6), soldiers[idx-1][:13], font=f_nm, fill=GREY + (255,))
    # Caption strip
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, H - CAPTION_H, W, H], fill=PANEL_BG + (255,))
    draw.rectangle([0, H - CAPTION_H, W, H - CAPTION_H + 4], fill=ORANGE + (255,))
    f_lbl = ImageFont.truetype(FONT_BOLD, 16)
    f_cap = ImageFont.truetype(FONT_REG, 38)
    draw.text((40, H - CAPTION_H + 18), "MASTERMIND  ·  NARRATION", font=f_lbl, fill=ORANGE + (255,))
    words = beat['narration'].split()
    lines, cur = [], ""
    for wd in words:
        test = (cur + " " + wd).strip()
        bbox = draw.textbbox((0, 0), test, font=f_cap)
        if bbox[2] - bbox[0] > W - 80:
            lines.append(cur); cur = wd
        else:
            cur = test
    if cur: lines.append(cur)
    cap_y = H - CAPTION_H + 60
    for ln in lines[:3]:
        draw.text((40, cap_y), ln, font=f_cap, fill=CREAM + (255,))
        cap_y += 50
    # Viewport border
    draw.rectangle([TRAY_W, 0, W, VIEW_H], outline=ORANGE + (255,), width=3)
    # Flying tool
    if flying:
        sid, p = flying
        slot = next(e for e in LAYOUT if e[0] == sid)
        sx = slot[1] + slot[3] // 2; sy = slot[2] + slot[4] // 2
        tx = TRAY_W + VIEW_W // 2; ty = VIEW_H // 2
        tt = 1 - (1 - p) ** 3
        x = sx + (tx - sx) * tt; y = sy + (ty - sy) * tt
        scale = 1 + 4 * tt
        bw, bh = int(80 * scale), int(34 * scale)
        f = ImageFont.truetype(FONT_BOLD, max(13, int(15 * scale)))
        fade = max(0, 1 - max(0, tt - 0.75) / 0.25)
        alpha = int(255 * fade)
        # Draw with strong glow
        box = (x - bw // 2, y - bh // 2, x + bw // 2, y + bh // 2)
        draw_glow_rect(img, box, GOLD_HOT, alpha_outer=int(60*fade), alpha_mid=int(160*fade), layers=5)
        draw = ImageDraw.Draw(img)
        draw.rectangle(box, fill=(60, 35, 15, alpha), outline=GOLD_BRIGHT + (alpha,), width=3)
        nb = draw.textbbox((0, 0), soldiers[sid-1][:14], font=f)
        draw.text((x - (nb[2]-nb[0]) // 2, y - 11), soldiers[sid-1][:14], font=f, fill=GOLD_BRIGHT + (alpha,))
        # trail
        for k in range(8):
            kt = max(0, tt - k * 0.04)
            if kt <= 0: break
            kx = sx + (tx - sx) * kt; ky = sy + (ty - sy) * kt
            kalpha = int(220 * (1 - k / 8))
            r_dot = 4 + k
            draw.ellipse([kx - r_dot, ky - r_dot, kx + r_dot, ky + r_dot],
                         fill=GOLD_HOT + (kalpha // 2,), outline=GOLD_BRIGHT + (kalpha,))
    return img

def get_video_dur(p):
    return float(subprocess.check_output(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
         '-of', 'default=noprint_wrappers=1:nokey=1', str(p)]).strip())

# Segment beats
SEGMENT_BEATS = {
    1: {'narration': "We built an army.", 'active': {1, 9},
        'fly_sequence': [(1, 0.0, 1.5), (9, 1.5, 3.0)]},
    5: {'narration': "Each soldier owns one capability of Runway's platform.", 'active': {13, 21},
        'fly_sequence': [(13, 0.0, 2.0), (21, 2.0, 4.0)]},
    3: {'narration': "Tools fly from the tray. The film assembles itself.", 'active': {8, 15},
        'fly_sequence': [(8, 0.0, 2.0), (15, 2.0, 4.0)]},
    7: {'narration': "Every facet of Runway. In concert. In real time.", 'active': {23, 25, 27},
        'fly_sequence': [(23, 0.0, 1.5), (25, 1.5, 3.0), (27, 3.0, 4.5)]},
    9: {'narration': "Number One Son did the homework. Builders Program — let us talk.",
        'active': {49, 50, 51},
        'fly_sequence': [(49, 0.0, 1.5), (50, 1.5, 3.0), (51, 3.0, 4.5)]},
}

# Map segment idx -> source video file
SEGMENT_VIDEO_MAP = {
    1: '/tmp/wtf_9avatar/seg_01.mp4',
    3: '/tmp/wtf_9avatar/seg_03.mp4',
    5: '/tmp/wtf_9avatar/seg_05.mp4',
    7: '/tmp/wtf_9avatar/seg_07.mp4',
    9: None,  # to be filled with v2 task output
}

# Get seg 9 v2 output
import urllib.request
from runwayml import RunwayML
c = RunwayML()
with open('/tmp/wtf_9avatar/seg9_v2_task.txt') as f:
    seg9_v2_id = f.read().strip()
res = c.tasks.retrieve(seg9_v2_id)
print(f"  seg9_v2 status: {res.status}")
if res.status == 'SUCCEEDED' and res.output:
    seg9_path = '/tmp/wtf_9avatar/seg_09_v2.mp4'
    urllib.request.urlretrieve(res.output[0], seg9_path)
    SEGMENT_VIDEO_MAP[9] = seg9_path
    print(f"  ✓ seg9 v2 saved")
elif res.status in ('RUNNING', 'THROTTLED'):
    print(f"  seg9_v2 not ready, falling back to v1 (cooking-teacher female voice)")
    SEGMENT_VIDEO_MAP[9] = '/tmp/wtf_9avatar/seg_09.mp4'

print("[1] Rendering v2 overlay frames...")
FPS = 10  # lower fps for speed
HERO = [1, 5, 3, 7, 9]
segment_outputs = []
for seg_idx in HERO:
    src_video = SEGMENT_VIDEO_MAP.get(seg_idx)
    if not src_video or not os.path.exists(src_video):
        print(f"  seg {seg_idx}: SKIP (no source)")
        continue
    src_dur = get_video_dur(src_video)
    beat = SEGMENT_BEATS[seg_idx]
    print(f"  seg {seg_idx}: dur={src_dur:.1f}s, frames={int(src_dur*FPS)+1}")
    seg_dir = WORK / f"seg_{seg_idx:02d}_frames"
    seg_dir.mkdir(exist_ok=True)
    n_frames = int(src_dur * FPS) + 1
    # Skip if already complete
    last_frame = seg_dir / f"f_{n_frames-1:04d}.png"
    if last_frame.exists():
        print(f"    (cached, skipping render)")
    else:
        for fi in range(n_frames):
            t = fi / FPS
            img = render_overlay_frame(t, beat)
            img.save(seg_dir / f"f_{fi:04d}.png")
    overlay_video = WORK / f"overlay_{seg_idx:02d}.mov"
    subprocess.run(['ffmpeg', '-y', '-framerate', str(FPS),
                    '-i', f'{seg_dir}/f_%04d.png',
                    '-c:v', 'qtrle', '-pix_fmt', 'argb', str(overlay_video)],
                   check=True, capture_output=True)
    out_segment = WORK / f"final_{seg_idx:02d}.mp4"
    cmd = ['ffmpeg', '-y',
           '-f', 'lavfi', '-i', f'color=c=black:s={W}x{H}:d={src_dur}:r=30',
           '-i', str(src_video), '-i', str(overlay_video),
           '-filter_complex',
           f'[1:v]scale={VIEW_W-40}:{VIEW_H-40}:force_original_aspect_ratio=decrease[av];'
           f'[0:v][av]overlay={TRAY_W+20}:{20}[base];'
           f'[base][2:v]overlay=0:0:shortest=1[out]',
           '-map', '[out]', '-map', '1:a?',
           '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset', 'veryfast',
           '-r', '30', '-c:a', 'aac', '-b:a', '192k', str(out_segment)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"    ffmpeg err: {res.stderr[-500:]}")
        continue
    segment_outputs.append(str(out_segment))
    print(f"    ✓ composed")

print(f"[2] Concatenating {len(segment_outputs)} segments...")
concat_list = WORK / 'concat.txt'
with open(concat_list, 'w') as f:
    for s in segment_outputs:
        f.write(f"file '{s}'\n")
final = OUT / 'wtf_TOOLTRAY_v2.mp4'
res = subprocess.run([
    'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', str(concat_list),
    '-c:v', 'libx264', '-c:a', 'aac', '-b:a', '192k', '-pix_fmt', 'yuv420p',
    '-preset', 'veryfast', str(final)
], capture_output=True, text=True)
if res.returncode != 0:
    print(f"  concat err: {res.stderr[-500:]}")
else:
    sz = final.stat().st_size
    dur = get_video_dur(str(final))
    print(f"  ✓ FINAL v2: {final}")
    print(f"    {sz/1024/1024:.2f}MB, {dur:.1f}s, {len(segment_outputs)} segments")
