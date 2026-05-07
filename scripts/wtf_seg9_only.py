"""Build only segment 9 (cooking-teacher) using the same compose logic, then re-concat."""
import json, os, subprocess, math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Re-import logic from the parent script
import sys
sys.path.insert(0, '/sessions/dreamy-sleepy-archimedes/mnt/outputs')
exec(open('/sessions/dreamy-sleepy-archimedes/mnt/outputs/wtf_tooltray_compose.py').read().split('print("[1] Loading')[0])

OUT = Path('/sessions/dreamy-sleepy-archimedes/mnt/outputs')
WORK = Path('/tmp/wtf_tooltray')

with open('/tmp/wtf_9avatar/tasks.json') as f:
    avatar_tasks = json.load(f)
saved_segs = {t['idx']: t for t in avatar_tasks if t.get('saved')}

seg_idx = 9
src_video = saved_segs[seg_idx]['file']
src_dur = float(subprocess.check_output(
    ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
     '-of', 'default=noprint_wrappers=1:nokey=1', str(src_video)]).strip())
print(f"  seg 9 src dur: {src_dur:.1f}s")

beat = {
    'narration': "Number One Son did the homework. Builders Program — let us talk.",
    'active': {49, 50, 51},
    'fly_sequence': [(49, 0.0, 1.5), (50, 1.5, 3.0), (51, 3.0, 4.5)],
}
seg_dir = WORK / f"seg_{seg_idx:02d}_overlay_frames"
seg_dir.mkdir(exist_ok=True)
FPS = 15
n_frames = int(src_dur * FPS) + 1

for fi in range(n_frames):
    t = fi / FPS
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    flying = None
    for (sid, st, et) in beat['fly_sequence']:
        if st <= t < et:
            p = (t - st) / (et - st)
            flying = (sid, p)
            break
    draw.rectangle([0, 0, TRAY_W, H], fill=TRAY_BG + (255,))
    f_h = ImageFont.truetype(FONT_BOLD, 22)
    f_sub = ImageFont.truetype(FONT_REG, 13)
    draw.text((20, 20), "TOOL TRAY", font=f_h, fill=ORANGE + (255,))
    draw.text((20, 48), "Number One Son · 51 Soldiers", font=f_sub, fill=GREY + (255,))
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
            fill = (60, 35, 20, 255); border = ORANGE + (255,); num_color = ORANGE_HOT + (255,); name_color = CREAM + (255,)
        else:
            fill = PANEL_BG + (255,); border = GREY_DIM + (255,); num_color = GREY + (255,); name_color = GREY + (255,)
        if not is_flying:
            draw.rectangle([x, y, x + w, y + h], fill=fill, outline=border, width=1)
            draw.text((x + 4, y + h//2 - 5), f"{idx:02d}", font=f_sd, fill=num_color)
            draw.text((x + 22, y + h//2 - 5), soldiers[idx-1][:12], font=f_nm, fill=name_color)
    draw.rectangle([0, H - CAPTION_H, W, H], fill=PANEL_BG + (255,))
    draw.rectangle([0, H - CAPTION_H, W, H - CAPTION_H + 4], fill=ORANGE + (255,))
    f_lbl = ImageFont.truetype(FONT_BOLD, 16)
    f_cap = ImageFont.truetype(FONT_REG, 38)
    draw.text((40, H - CAPTION_H + 18), "MASTERMIND  ·  NARRATION", font=f_lbl, fill=ORANGE + (255,))
    words = beat['narration'].split()
    lines, cur = [], ""
    for wd in words:
        test = (cur + " " + wd).strip()
        bbox = draw.textbbox((0,0), test, font=f_cap)
        if bbox[2] - bbox[0] > W - 80:
            lines.append(cur); cur = wd
        else:
            cur = test
    if cur: lines.append(cur)
    cap_y = H - CAPTION_H + 60
    for ln in lines[:3]:
        draw.text((40, cap_y), ln, font=f_cap, fill=CREAM + (255,))
        cap_y += 50
    draw.rectangle([TRAY_W, 0, W, VIEW_H], outline=ORANGE_DIM + (255,), width=2)
    if flying:
        sid, p = flying
        slot = next(e for e in LAYOUT if e[0] == sid)
        sx = slot[1] + slot[3] // 2; sy = slot[2] + slot[4] // 2
        tx = TRAY_W + VIEW_W // 2; ty = VIEW_H // 2
        tt = 1 - (1 - p) ** 3
        x = sx + (tx - sx) * tt; y = sy + (ty - sy) * tt
        scale = 1 + 4 * tt
        bw, bh = int(70 * scale), int(30 * scale)
        f = ImageFont.truetype(FONT_BOLD, max(12, int(14 * scale)))
        fade = max(0, 1 - max(0, tt - 0.75) / 0.25)
        alpha = int(255 * fade)
        draw.rectangle([x - bw // 2, y - bh // 2, x + bw // 2, y + bh // 2],
                       outline=ORANGE_HOT + (alpha,), width=2)
        nb = draw.textbbox((0,0), soldiers[sid-1][:14], font=f)
        draw.text((x - (nb[2]-nb[0]) // 2, y - 10), soldiers[sid-1][:14], font=f, fill=ORANGE_HOT + (alpha,))
        for k in range(8):
            kt = max(0, tt - k * 0.04)
            if kt <= 0: break
            kx = sx + (tx - sx) * kt; ky = sy + (ty - sy) * kt
            kalpha = int(220 * (1 - k / 8))
            draw.ellipse([kx - 3, ky - 3, kx + 3, ky + 3], fill=ORANGE_HOT + (kalpha,))
    img.save(seg_dir / f"f_{fi:04d}.png")

print(f"  generated {n_frames} overlay frames")
overlay_video = WORK / f"overlay_{seg_idx:02d}.mov"
subprocess.run(['ffmpeg', '-y', '-framerate', str(FPS), '-i', f'{seg_dir}/f_%04d.png',
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
    print(f"  ffmpeg err: {res.stderr[-800:]}")
else:
    print(f"  ✓ seg 9 composed")

# Now re-concatenate all 5 in order: 1, 5, 3, 7, 9 (preferred order for narrative arc)
order = [1, 5, 3, 7, 9]
concat_list = WORK / 'concat5.txt'
with open(concat_list, 'w') as f:
    for i in order:
        p = WORK / f'final_{i:02d}.mp4'
        if p.exists():
            f.write(f"file '{p}'\n")
final = OUT / 'wtf_TOOLTRAY_documentary.mp4'
res = subprocess.run([
    'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', str(concat_list),
    '-c:v', 'libx264', '-c:a', 'aac', '-b:a', '192k', '-pix_fmt', 'yuv420p',
    '-preset', 'veryfast', str(final)
], capture_output=True, text=True)
if res.returncode != 0:
    print(f"  concat err: {res.stderr[-800:]}")
else:
    sz = final.stat().st_size
    dur = float(subprocess.check_output(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
         '-of', 'default=noprint_wrappers=1:nokey=1', str(final)]).strip())
    print(f"  ✓ FINAL: {final}")
    print(f"    {sz/1024/1024:.2f}MB, {dur:.1f}s, 5 segments")
  