"""Compose the integrated WTF real-API test video.
Stitches verified Runway-API outputs into a single demo MP4.
"""
import subprocess, os, shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path('/sessions/dreamy-sleepy-archimedes/mnt/outputs')
WORK = Path('/tmp/wtf_compose')
WORK.mkdir(parents=True, exist_ok=True)

W, H = 1280, 720
DARK = (10, 14, 25)
NAVY = (15, 23, 42)
ORANGE = (210, 110, 50)
CREAM = (240, 234, 224)
GREY = (140, 145, 155)
WHITE = (255, 255, 255)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

def card(filename, eyebrow, title, sub=""):
    img = Image.new('RGB', (W, H), DARK)
    d = ImageDraw.Draw(img)
    f_eb = ImageFont.truetype(FONT_REG, 18)
    f_t = ImageFont.truetype(FONT_BOLD, 70)
    f_s = ImageFont.truetype(FONT_REG, 22)
    bbox = d.textbbox((0,0), eyebrow, font=f_eb)
    d.text((W//2 - (bbox[2]-bbox[0])//2, H//2 - 110), eyebrow, font=f_eb, fill=ORANGE)
    bbox = d.textbbox((0,0), title, font=f_t)
    d.text((W//2 - (bbox[2]-bbox[0])//2, H//2 - 70), title, font=f_t, fill=CREAM)
    if sub:
        bbox = d.textbbox((0,0), sub, font=f_s)
        d.text((W//2 - (bbox[2]-bbox[0])//2, H//2 + 40), sub, font=f_s, fill=GREY)
    img.save(WORK / filename)

def card_with_image(filename, image_path, eyebrow, title):
    src = Image.open(image_path).convert('RGB')
    src = src.resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(src)
    # bottom strip with label
    d.rectangle([0, H-90, W, H], fill=(0,0,0))
    d.rectangle([0, H-90, W, H-86], fill=ORANGE)
    f_eb = ImageFont.truetype(FONT_REG, 14)
    f_t = ImageFont.truetype(FONT_BOLD, 24)
    d.text((30, H-78), eyebrow, font=f_eb, fill=ORANGE)
    d.text((30, H-58), title, font=f_t, fill=CREAM)
    src.save(WORK / filename)

# Static cards
card('00_open.png', "WTF — REAL API INTEGRATION TEST",
     "Number One Son", "Live output from 7 verified Runway endpoints")
card('01_label_image.png', "FACET 09 — gen4_image",
     "Text-to-image", "Soldier 1 generates the establishing shot")
card('02_label_video.png', "FACET 01 — gen4.5",
     "Text-to-video", "Soldier 1 brings the scene to life")
card('03_label_sfx.png', "FACET 25 — eleven_text_to_sound_v2",
     "Sound effect", "Soldier 25 scores the cut")
card('04_label_chars_preset.png', "FACET 13 — gwm1_avatars (preset)",
     "Characters", "Soldier 13: music-superstar preset")
card('05_label_chars_custom.png', "FACET 13 — gwm1_avatars (custom)",
     "The Mastermind speaks", "Custom avatar built from generated portrait")
card('99_end.png', "7 OF 23 ENDPOINTS — $1.63 SPENT",
     "Real output. Real pipeline.",
     "Friday rebuilds from scratch with the same components.")

# Image segments — turn the still PNG into 2-second video clips
def png_to_clip(png, out_mp4, duration):
    subprocess.run(['ffmpeg', '-y', '-loop', '1', '-i', str(png),
                    '-c:v', 'libx264', '-t', str(duration),
                    '-pix_fmt', 'yuv420p', '-vf', f'scale={W}:{H}',
                    '-r', '30', str(out_mp4)],
                   check=True, capture_output=True)

# Build clips
print("[1] Building static card clips...")
png_to_clip(WORK / '00_open.png', WORK / '00_open.mp4', 3.0)
png_to_clip(WORK / '01_label_image.png', WORK / '01_label.mp4', 1.5)
card_with_image('01_image_show.png', OUT / 'wtf_phase1c_real_runway_image.png',
                "Real output — gen4_image", "1.06MB PNG, 26 seconds, 5 credits")
png_to_clip(WORK / '01_image_show.png', WORK / '01_image.mp4', 3.5)

png_to_clip(WORK / '02_label_video.png', WORK / '02_label.mp4', 1.5)
# Phase 2 video is already a video — just transcode to consistent format
def std_video(src, dst, duration_limit=None):
    args = ['ffmpeg', '-y', '-i', str(src), '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
            '-vf', f'scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2',
            '-r', '30', '-an']
    if duration_limit:
        args.extend(['-t', str(duration_limit)])
    args.append(str(dst))
    subprocess.run(args, check=True, capture_output=True)

std_video(OUT / 'wtf_phase2_real_runway_video.mp4', WORK / '02_video.mp4')

png_to_clip(WORK / '03_label_sfx.png', WORK / '03_label.mp4', 1.5)
# SFX card with audio
sfx_card_silent = WORK / '03_sfx_silent.mp4'
png_to_clip(WORK / '03_label_sfx.png', sfx_card_silent, 3.5)
sfx_with_audio = WORK / '03_sfx.mp4'
subprocess.run(['ffmpeg', '-y', '-i', str(sfx_card_silent),
                '-i', str(OUT / 'wtf_phase3_real_runway_sfx.mp3'),
                '-c:v', 'copy', '-c:a', 'aac', '-shortest', str(sfx_with_audio)],
               check=True, capture_output=True)

png_to_clip(WORK / '04_label_chars_preset.png', WORK / '04_label.mp4', 1.5)
std_video(OUT / 'wtf_phase6c_preset_avatar.mp4', WORK / '04_chars_preset_silent.mp4')
# preserve original audio from preset avatar video
preset_with_audio = WORK / '04_chars_preset.mp4'
subprocess.run(['ffmpeg', '-y', '-i', str(OUT / 'wtf_phase6c_preset_avatar.mp4'),
                '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
                '-vf', f'scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2',
                '-r', '30', '-c:a', 'aac', str(preset_with_audio)],
               check=True, capture_output=True)

png_to_clip(WORK / '05_label_chars_custom.png', WORK / '05_label.mp4', 1.5)
custom_with_audio = WORK / '05_chars_custom.mp4'
subprocess.run(['ffmpeg', '-y', '-i', str(OUT / 'wtf_phase7_custom_avatar.mp4'),
                '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
                '-vf', f'scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2',
                '-r', '30', '-c:a', 'aac', str(custom_with_audio)],
               check=True, capture_output=True)

png_to_clip(WORK / '99_end.png', WORK / '99_end.mp4', 4.0)

# Concat — but segments have mixed audio (some silent, some with audio).
# Use concat with re-encoding (concat filter not demuxer) to handle mixed.
print("[2] Concatenating segments with re-encode...")
inputs = [
    WORK / '00_open.mp4',
    WORK / '01_label.mp4',
    WORK / '01_image.mp4',
    WORK / '02_label.mp4',
    WORK / '02_video.mp4',
    WORK / '03_label.mp4',
    WORK / '03_sfx.mp4',
    WORK / '04_label.mp4',
    WORK / '04_chars_preset.mp4',
    WORK / '05_label.mp4',
    WORK / '05_chars_custom.mp4',
    WORK / '99_end.mp4',
]
# Use concat filter for safety with mixed audio/silent
cmd = ['ffmpeg', '-y']
for i in inputs:
    cmd += ['-i', str(i)]
n = len(inputs)
# Build filter chain: each segment's video + (audio or silent)
filt = ''
for i in range(n):
    filt += f'[{i}:v]scale={W}:{H},setsar=1[v{i}];'
# Audio: probe each — those with audio get [i:a], else generate anullsrc
# Simpler: pass through any audio that exists; for segments without audio, generate silence
# We'll generate silence inputs via anullsrc filter
silent_audio_segs = {0, 1, 2, 3, 4, 5, 7, 9, 11}  # indexes with no audio (label cards, image clips, end)
# Actually 6 (sfx), 8 (preset chars), 10 (custom chars) have audio
# We generate matching-duration silence for the others using aevalsrc=0:d=DURATION
# Get durations
dur = {}
for i, p in enumerate(inputs):
    out = subprocess.check_output(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
         '-of', 'default=noprint_wrappers=1:nokey=1', str(p)]).strip()
    dur[i] = float(out)
# Now build audio chain
audio_inputs = []
audio_in_count = n
for i in range(n):
    if i in (6, 8, 10):
        filt += f'[{i}:a]aresample=44100,asetpts=PTS-STARTPTS[a{i}];'
    else:
        # generate silent audio for this segment via aevalsrc using lavfi
        # we'll add it as additional inputs after the regular ones
        filt += f'aevalsrc=0:d={dur[i]:.3f}:s=44100:c=stereo[a{i}];'
# Concatenate
parts = ''
for i in range(n):
    parts += f'[v{i}][a{i}]'
filt += f'{parts}concat=n={n}:v=1:a=1[outv][outa]'

cmd += ['-filter_complex', filt,
        '-map', '[outv]', '-map', '[outa]',
        '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', '30',
        '-c:a', 'aac', '-b:a', '192k',
        str(OUT / 'wtf_REAL_API_integrated.mp4')]
print(f"  segments: {n}, total approx duration: {sum(dur.values()):.1f}s")
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode != 0:
    print("  ffmpeg err:", res.stderr[-1500:])
    raise SystemExit(1)
print("[3] DONE")
final = OUT / 'wtf_REAL_API_integrated.mp4'
sz = final.stat().st_size
fdur = float(subprocess.check_output(
    ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
     '-of', 'default=noprint_wrappers=1:nokey=1', str(final)]).strip())
print(f"  file: {final}")
print(f"  size: {sz/1024/1024:.2f}MB  duration: {fdur:.1f}s")
