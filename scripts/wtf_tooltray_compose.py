"""WTF tool-tray composition — persistent left tray with 51 tools,
main viewport with avatar segments, tool highlights and fly-in animation,
caption strip at bottom.
"""
import json, os, subprocess, math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path('/sessions/dreamy-sleepy-archimedes/mnt/outputs')
WORK = Path('/tmp/wtf_tooltray')
WORK.mkdir(parents=True, exist_ok=True)

W, H = 1920, 1080
TRAY_W = 380
VIEW_W = W - TRAY_W
CAPTION_H = 230
VIEW_H = H - CAPTION_H

DARK = (10, 14, 25)
TRAY_BG = (16, 22, 36)
PANEL_BG = (20, 26, 40)
ORANGE = (255, 140, 60)
ORANGE_HOT = (255, 180, 100)
ORANGE_DIM = (140, 80, 40)
CREAM = (240, 234, 224)
GREY = (110, 115, 125)
GREY_DIM = (60, 65, 75)
WHITE = (255, 255, 255)
NAVY_TXT = (200, 210, 230)

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
    """Return list of (idx, x, y, w, h) for each soldier slot in the tray."""
    layout = []
    y = 80
    for sname, lo, hi in sergeants:
        # Sergeant header takes 28px
        sg_y = y
        y += 28
        # Soldier rows: at most 4 per row
        cnt = hi - lo + 1
        cols = min(4, cnt)
        rows = math.ceil(cnt / cols)
        slot_w = (TRAY_W - 24) // cols
        slot_h = 26
        for k in range(cnt):
            r = k // cols
            c = k % cols
            sx = 12 + c * slot_w
            sy = y + r * (slot_h + 2)
            layout.append((lo + k, sx, sy, slot_w - 4, slot_h, sname, sg_y))
        y += rows * (slot_h + 2) + 8
    return layout

LAYOUT = soldier_layout()

def draw_tray(draw, active=set(), flying=None):
    """Draw the tool tray. flying = (idx, progress 0-1, target_x, target_y) for animated tool."""
    # Tray background
    draw.rectangle([0, 0, TRAY_W, H], fill=TRAY_BG)
    # Header
    f_h = ImageFont.truetype(FONT_BOLD, 22)
    f_sub = ImageFont.truetype(FONT_REG, 13)
    draw.text((20, 20), "TOOL TRAY", font=f_h, fill=ORANGE)
    draw.text((20, 48), "Number One Son · 51 Soldiers", font=f_sub, fill=GREY)
    # Sergeant headers + soldier badges
    f_sg = ImageFont.truetype(FONT_BOLD, 11)
    f_sd = ImageFont.truetype(FONT_MONO, 10)
    f_nm = ImageFont.truetype(FONT_REG, 9)
    last_sg = None
    for entry in LAYOUT:
        idx, x, y, w, h, sname, sg_y = entry
        if sname != last_sg:
            draw.text((12, sg_y + 6), sname, font=f_sg, fill=GREY)
            last_sg = sname
        on = idx in active
        is_flying = flying and flying[0] == idx
        if on:
            fill = (60, 35, 20)
            border = ORANGE
            num_color = ORANGE_HOT
            name_color = CREAM
        else:
            fill = PANEL_BG
            border = GREY_DIM
            num_color = GREY
            name_color = GREY
        if not is_flying:  # don't draw the flying tool in its slot
            draw.rectangle([x, y, x + w, y + h], fill=fill, outline=border, width=1)
            num = f"{idx:02d}"
            nb = draw.textbbox((0,0), num, font=f_sd)
            draw.text((x + 4, y + (h - (nb[3]-nb[1])) // 2 - 1), num, font=f_sd, fill=num_color)
            name = soldiers[idx-1]
            if len(name) > 12:
                name = name[:12]
            draw.text((x + 22, y + (h - 11) // 2), name, font=f_nm, fill=name_color)

def draw_caption(draw, text):
    """Draw the caption strip at bottom."""
    draw.rectangle([0, H - CAPTION_H, W, H], fill=PANEL_BG)
    draw.rectangle([0, H - CAPTION_H, W, H - CAPTION_H + 4], fill=ORANGE)
    f = ImageFont.truetype(FONT_REG, 36)
    f_lbl = ImageFont.truetype(FONT_BOLD, 16)
    # Word-wrap
    words = text.split()
    lines = []
    cur = ""
    for w_ in words:
        test = (cur + " " + w_).strip()
        bbox = draw.textbbox((0,0), test, font=f)
        if bbox[2] - bbox[0] > W - 80:
            lines.append(cur)
            cur = w_
        else:
            cur = test
    if cur:
        lines.append(cur)
    draw.text((40, H - CAPTION_H + 18), "MASTERMIND  ·  NARRATION", font=f_lbl, fill=ORANGE)
    y = H - CAPTION_H + 50
    for line in lines[:3]:
        draw.text((40, y), line, font=f, fill=CREAM)
        y += 50

def draw_viewport_placeholder(draw, label):
    """Draw the viewport area as a placeholder (will be replaced by video overlay)."""
    vx, vy = TRAY_W, 0
    draw.rectangle([vx, vy, W, VIEW_H], fill=DARK)
    draw.rectangle([vx + 12, vy + 12, W - 12, VIEW_H - 12], outline=GREY_DIM, width=1)
    f = ImageFont.truetype(FONT_REG, 28)
    draw.text((vx + 30, vy + 30), label, font=f, fill=GREY)

def draw_flying_tool(draw, idx, progress, view_center=(TRAY_W + VIEW_W // 2, VIEW_H // 2)):
    """Draw the flying tool badge traveling from its slot toward the viewport center."""
    # Find slot
    slot = next((e for e in LAYOUT if e[0] == idx), None)
    if not slot: return
    sx, sy = slot[1] + slot[3] // 2, slot[2] + slot[4] // 2
    tx, ty = view_center
    # Ease-out cubic
    t = 1 - (1 - progress) ** 3
    x = sx + (tx - sx) * t
    y = sy + (ty - sy) * t
    # Scale up as it travels
    scale = 1 + 5 * t
    bw = int(60 * scale)
    bh = int(28 * scale)
    fade = 1 - max(0, t - 0.7) / 0.3
    if fade <= 0: return
    bg_alpha = int(255 * fade)
    # Draw the tool badge
    badge_box = [x - bw // 2, y - bh // 2, x + bw // 2, y + bh // 2]
    draw.rectangle(badge_box, fill=(40 + bg_alpha // 4, 25 + bg_alpha // 8, 15, ),
                   outline=ORANGE_HOT, width=2)
    f = ImageFont.truetype(FONT_BOLD, max(12, int(14 * scale)))
    name = soldiers[idx-1][:14]
    bbox = draw.textbbox((0,0), name, font=f)
    tw = bbox[2] - bbox[0]
    draw.text((x - tw // 2, y - 8), name, font=f, fill=ORANGE_HOT)
    # Trail line
    for k in range(5):
        kt = max(0, t - k * 0.05)
        if kt <= 0: break
        kx = sx + (tx - sx) * kt
        ky = sy + (ty - sy) * kt
        draw.ellipse([kx - 2, ky - 2, kx + 2, ky + 2], fill=ORANGE_HOT)

# ---- Build per-segment overlays ----
print("[1] Loading segment metadata...")
with open('/tmp/wtf_9avatar/tasks.json') as f:
    avatar_tasks = json.load(f)
saved_segs = {t['idx']: t for t in avatar_tasks if t.get('saved')}
print(f"  {len(saved_segs)} segments available")

# Pick the strongest 5 (or all available up to 5)
HERO_PICKS = []
preferred_order = [1, 5, 3, 7, 9, 4, 6, 2, 8]  # by avatar appeal
for idx in preferred_order:
    if idx in saved_segs and len(HERO_PICKS) < 5:
        HERO_PICKS.append(idx)
print(f"  hero segments: {HERO_PICKS}")

# Per-segment narration + active soldiers + flying tool sequence
SEGMENT_BEATS = {
    1: {  # game-character
        'narration': "We built an army.",
        'active': {1, 9},  # Gen-4.5, gen4_image
        'fly_sequence': [(1, 0.0, 1.5), (9, 1.5, 3.0)],  # (soldier, start_t, end_t)
    },
    5: {  # influencer
        'narration': "Each soldier owns one capability of Runway's platform.",
        'active': {13, 21},
        'fly_sequence': [(13, 0.0, 2.0), (21, 2.0, 4.0)],
    },
    3: {  # game-character-man
        'narration': "Tools fly from the tray. The film assembles itself.",
        'active': {8, 15},
        'fly_sequence': [(8, 0.0, 2.0), (15, 2.0, 4.0)],
    },
    7: {  # human-resource
        'narration': "Every facet of Runway. In concert. In real time.",
        'active': {23, 25, 27},
        'fly_sequence': [(23, 0.0, 1.5), (25, 1.5, 3.0), (27, 3.0, 4.5)],
    },
    9: {  # cooking-teacher
        'narration': "Number One Son did the homework. Builders Program — let us talk.",
        'active': {49, 50, 51},
        'fly_sequence': [(49, 0.0, 1.5), (50, 1.5, 3.0), (51, 3.0, 4.5)],
    },
    4: {  # cat-character (fallback)
        'narration': "The Mastermind directs. The army responds.",
        'active': {12, 14},
        'fly_sequence': [(12, 0.0, 2.0), (14, 2.0, 4.0)],
    },
    6: {  # tennis-coach (fallback)
        'narration': "Forty-eight seconds of orchestration. Fifteen soldiers contributed.",
        'active': {35, 36, 37},
        'fly_sequence': [(35, 0.0, 1.5), (36, 1.5, 3.0), (37, 3.0, 4.5)],
    },
}

print("[2] Building per-segment overlay sequences...")
def get_video_dur(p):
    return float(subprocess.check_output(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
         '-of', 'default=noprint_wrappers=1:nokey=1', str(p)]).strip())

# For each hero segment, generate frames at 15fps for the duration of the avatar video
# Then composite: avatar video in viewport, overlay frames as full-frame transparent overlays
FPS = 15

segment_outputs = []
for seg_idx in HERO_PICKS:
    src_video = saved_segs[seg_idx]['file']
    src_dur = get_video_dur(src_video)
    beat = SEGMENT_BEATS.get(seg_idx, SEGMENT_BEATS[1])
    print(f"  segment {seg_idx} ({avatar_tasks[seg_idx-1]['avatar']}): dur={src_dur:.1f}s")
    seg_dir = WORK / f"seg_{seg_idx:02d}_overlay_frames"
    seg_dir.mkdir(exist_ok=True)
    n_frames = int(src_dur * FPS) + 1
    for fi in range(n_frames):
        t = fi / FPS
        img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        # Determine flying tool
        flying = None
        for (sid, st, et) in beat['fly_sequence']:
            if st <= t < et:
                p = (t - st) / (et - st)
                flying = (sid, p)
                break
        # Draw tray with active highlights
        draw.rectangle([0, 0, TRAY_W, H], fill=TRAY_BG + (255,))
        # Tray header
        f_h = ImageFont.truetype(FONT_BOLD, 22)
        f_sub = ImageFont.truetype(FONT_REG, 13)
        draw.text((20, 20), "TOOL TRAY", font=f_h, fill=ORANGE + (255,))
        draw.text((20, 48), "Number One Son · 51 Soldiers", font=f_sub, fill=GREY + (255,))
        # Tools
        f_sg = ImageFont.truetype(FONT_BOLD, 11)
        f_sd = ImageFont.truetype(FONT_MONO, 10)
        f_nm = ImageFont.truetype(FONT_REG, 9)
        last_sg = None
        for entry in LAYOUT:
            idx, x, y, w, h, sname, sg_y = entry
            if sname != last_sg:
                draw.text((12, sg_y + 6), sname, font=f_sg, fill=GREY + (255,))
                last_sg = sname
            on = idx in beat['active']
            is_flying = flying and flying[0] == idx
            if on:
                fill = (60, 35, 20, 255)
                border = ORANGE + (255,)
                num_color = ORANGE_HOT + (255,)
                name_color = CREAM + (255,)
            else:
                fill = PANEL_BG + (255,)
                border = GREY_DIM + (255,)
                num_color = GREY + (255,)
                name_color = GREY + (255,)
            if not is_flying:
                draw.rectangle([x, y, x + w, y + h], fill=fill, outline=border, width=1)
                num = f"{idx:02d}"
                draw.text((x + 4, y + h//2 - 5), num, font=f_sd, fill=num_color)
                name = soldiers[idx-1][:12]
                draw.text((x + 22, y + h//2 - 5), name, font=f_nm, fill=name_color)
        # Caption strip
        draw.rectangle([0, H - CAPTION_H, W, H], fill=PANEL_BG + (255,))
        draw.rectangle([0, H - CAPTION_H, W, H - CAPTION_H + 4], fill=ORANGE + (255,))
        f_lbl = ImageFont.truetype(FONT_BOLD, 16)
        f_cap = ImageFont.truetype(FONT_REG, 38)
        draw.text((40, H - CAPTION_H + 18), "MASTERMIND  ·  NARRATION",
                  font=f_lbl, fill=ORANGE + (255,))
        # Wrap
        words = beat['narration'].split()
        lines, cur = [], ""
        for w_ in words:
            test = (cur + " " + w_).strip()
            bbox = draw.textbbox((0,0), test, font=f_cap)
            if bbox[2] - bbox[0] > W - 80:
                lines.append(cur); cur = w_
            else:
                cur = test
        if cur: lines.append(cur)
        cap_y = H - CAPTION_H + 60
        for ln in lines[:3]:
            draw.text((40, cap_y), ln, font=f_cap, fill=CREAM + (255,))
            cap_y += 50
        # Viewport border (above the avatar video which goes underneath)
        draw.rectangle([TRAY_W, 0, W, VIEW_H], outline=ORANGE_DIM + (255,), width=2)
        # Flying tool overlay
        if flying:
            sid, p = flying
            slot = next(e for e in LAYOUT if e[0] == sid)
            sx = slot[1] + slot[3] // 2
            sy = slot[2] + slot[4] // 2
            tx = TRAY_W + VIEW_W // 2
            ty = VIEW_H // 2
            tt = 1 - (1 - p) ** 3
            x = sx + (tx - sx) * tt
            y = sy + (ty - sy) * tt
            scale = 1 + 4 * tt
            bw, bh = int(70 * scale), int(30 * scale)
            f = ImageFont.truetype(FONT_BOLD, max(12, int(14 * scale)))
            fade = max(0, 1 - max(0, tt - 0.75) / 0.25)
            alpha = int(255 * fade)
            draw.rectangle([x - bw // 2, y - bh // 2, x + bw // 2, y + bh // 2],
                           outline=ORANGE_HOT + (alpha,), width=2)
            name = soldiers[sid-1][:14]
            nb = draw.textbbox((0,0), name, font=f)
            draw.text((x - (nb[2]-nb[0]) // 2, y - 10), name,
                      font=f, fill=ORANGE_HOT + (alpha,))
            # trail
            for k in range(8):
                kt = max(0, tt - k * 0.04)
                if kt <= 0: break
                kx = sx + (tx - sx) * kt
                ky = sy + (ty - sy) * kt
                kalpha = int(220 * (1 - k / 8))
                draw.ellipse([kx - 3, ky - 3, kx + 3, ky + 3],
                             fill=ORANGE_HOT + (kalpha,))
        img.save(seg_dir / f"f_{fi:04d}.png")
    # Compose: avatar video (scaled to viewport) + overlay sequence
    # Step 1: convert overlay frames to a video
    overlay_video = seg_dir.parent / f"overlay_{seg_idx:02d}.mov"
    subprocess.run(['ffmpeg', '-y', '-framerate', str(FPS),
                    '-i', f'{seg_dir}/f_%04d.png',
                    '-c:v', 'qtrle', '-pix_fmt', 'argb',
                    str(overlay_video)], check=True, capture_output=True)
    # Step 2: composite avatar video + overlay
    out_segment = seg_dir.parent / f"final_{seg_idx:02d}.mp4"
    # Build base canvas: black 1920x1080, place avatar video in viewport area (centered, fit)
    cmd = [
        'ffmpeg', '-y',
        '-f', 'lavfi', '-i', f'color=c=black:s={W}x{H}:d={src_dur}:r=30',
        '-i', str(src_video),
        '-i', str(overlay_video),
        '-filter_complex',
        f'[1:v]scale={VIEW_W-40}:{VIEW_H-40}:force_original_aspect_ratio=decrease[av];'
        f'[0:v][av]overlay={TRAY_W+20}:{20}[base];'
        f'[base][2:v]overlay=0:0:shortest=1[out]',
        '-map', '[out]', '-map', '1:a?',
        '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
        '-preset', 'veryfast', '-r', '30',
        '-c:a', 'aac', '-b:a', '192k',
        str(out_segment)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"    ffmpeg err: {res.stderr[-800:]}")
        continue
    segment_outputs.append(str(out_segment))
    print(f"    ✓ composed segment {seg_idx}")

print(f"[3] Concatenating {len(segment_outputs)} segments...")
concat_list = WORK / 'concat.txt'
with open(concat_list, 'w') as f:
    for s in segment_outputs:
        f.write(f"file '{s}'\n")
final = OUT / 'wtf_TOOLTRAY_documentary.mp4'
res = subprocess.run([
    'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', str(concat_list),
    '-c:v', 'libx264', '-c:a', 'aac', '-b:a', '192k', '-pix_fmt', 'yuv420p',
    str(final)
], capture_output=True, text=True)
if res.returncode != 0:
    print(f"  concat err: {res.stderr[-800:]}")
else:
    sz = final.stat().st_size
    dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries',
                'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', str(final)]).strip())
    print(f"  ✓ final: {final}")
    print(f"    size: {sz/1024/1024:.2f}MB  dur: {dur:.1f}s")
