"""WTF Dress Rehearsal Assembly.
Composes the brand film from generated frames + real Runway video assets + gTTS narration.
"""
import os, subprocess, json
from pathlib import Path

OUT = Path('/sessions/dreamy-sleepy-archimedes/mnt/outputs')
WORK = Path('/tmp/wtf_dress')
FRAMES = WORK / 'frames'
W, H = 1920, 1080
FPS = 30

def run(cmd, label=""):
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"  ✗ {label}: {res.stderr[-500:]}")
        return False
    return True

def img_to_mp4(png, mp4, dur):
    """Convert a still image to an mp4 of given duration, no audio."""
    return run(['ffmpeg', '-y', '-loop', '1', '-i', str(png),
                '-c:v', 'libx264', '-t', f'{dur}', '-pix_fmt', 'yuv420p',
                '-vf', f'scale={W}:{H}', '-r', str(FPS), str(mp4)],
               f"img→mp4 {png}")

def img_kb_mp4(png, mp4, dur, zoom_start=1.0, zoom_end=1.08):
    """Ken Burns zoom on a still image."""
    n_frames = int(dur * FPS)
    # zoompan filter
    z_step = (zoom_end - zoom_start) / n_frames
    return run(['ffmpeg', '-y', '-loop', '1', '-i', str(png),
                '-vf', f'scale={W*2}:{H*2},zoompan=z=\'min(zoom+{z_step:.6f},{zoom_end})\':d={n_frames}:s={W}x{H}:fps={FPS}',
                '-c:v', 'libx264', '-t', f'{dur}', '-pix_fmt', 'yuv420p',
                '-r', str(FPS), str(mp4)],
               f"kb {png}")

def std_video(src, mp4, max_dur=None):
    """Standardize a Runway video to 1920x1080@30fps with letterbox if needed."""
    args = ['ffmpeg', '-y', '-i', str(src),
            '-vf', f'scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:black',
            '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
            '-r', str(FPS), '-an']
    if max_dur:
        args.extend(['-t', f'{max_dur}'])
    args.append(str(mp4))
    return run(args, f"std {src}")

print("[1] Building cold open (10s)...")
img_to_mp4(FRAMES / 'cold_l1.png', WORK / 'cold_a.mp4', 5.0)
img_to_mp4(FRAMES / 'cold_l2.png', WORK / 'cold_b.mp4', 5.0)

print("[2] Building Act 1 photo cards with Ken Burns (25s)...")
# Map photo cards to durations matching narration beats
# Narration order: lived/worked/built furniture/built homes/built commercial/built businesses/built family/taught them to fly/world changed.../am i still living up.../then this happened
# We have 10 placeholder cards; map them to the narration timeline
act1_segments = [
    ('p1_1969.png', 4.5),    # Mom 25 + young Roger + sister (cold open dissolve target, holds for "So I lived. I worked.")
    ('p2_teen.png', 1.8),     # "I built furniture." - actually wait, list is: lived, worked, built furniture, built homes, ...
    ('p3_carpentry.png', 1.8),# I built furniture
    ('p4_house.png', 1.8),    # I built homes
    ('p5_commercial.png', 1.8),# commercial buildings
    ('p6_headshot.png', 1.6),  # businesses
    ('p7_partner.png', 1.6),   # (or family)
    ('p8_son.png', 1.8),       # built a family
    ('p9_flying.png', 1.6),    # taught them to fly
    ('p10_hospital.png', 6.0), # hospital — extended hold for "every time the world changed... am i still living up to it... then this happened"
]
for i, (png, dur) in enumerate(act1_segments):
    img_kb_mp4(FRAMES / png, WORK / f'a1_{i:02d}.mp4', dur, 1.0, 1.06)
    print(f"    {png}: {dur}s")

print("[3] Building Act 2 (workshop + 5 passes + gallery + closes)...")
# Use the workshop_establishing Runway shot
std_video(WORK / 'workshop_establishing.mp4', WORK / 'a2_workshop.mp4', max_dur=4.5)

# 5-pass demonstration: alternate pass-cards with real Runway assets
img_to_mp4(FRAMES / 'pass1.png', WORK / 'a2_p1_card.mp4', 1.8)
std_video(OUT / 'wtf_phase1c_real_runway_image.png', WORK / 'a2_p1_real.mp4', max_dur=1.8)
img_to_mp4(FRAMES / 'pass2.png', WORK / 'a2_p2_card.mp4', 1.5)
std_video(OUT / 'wtf_phase2_real_runway_video.mp4', WORK / 'a2_p2_real.mp4', max_dur=2.0)
img_to_mp4(FRAMES / 'pass3.png', WORK / 'a2_p3_card.mp4', 1.5)
std_video(OUT / 'wtf_phase8_aleph_color_grade.mp4', WORK / 'a2_p3_real.mp4', max_dur=2.0)
img_to_mp4(FRAMES / 'pass4.png', WORK / 'a2_p4_card.mp4', 1.5)
# Pass 4 is voice — show waveform card or just hold
img_to_mp4(FRAMES / 'pass5.png', WORK / 'a2_p5_card.mp4', 1.5)
std_video(OUT / 'wtf_phase7_custom_avatar.mp4', WORK / 'a2_p5_real.mp4', max_dur=2.5)

# Closing lines
for i in range(1, 6):
    img_to_mp4(FRAMES / f'act2_close{i}.png', WORK / f'a2_cl_{i}.mp4', 2.5)

# Gallery hero (if available)
if (WORK / 'gallery_hero1.mp4').exists():
    std_video(WORK / 'gallery_hero1.mp4', WORK / 'a2_gallery1.mp4', max_dur=2.5)

print("[4] Building Act 3 + closing + end card...")
img_to_mp4(FRAMES / 'act3_a.png', WORK / 'a3_a.mp4', 2.0)
img_to_mp4(FRAMES / 'act3_b.png', WORK / 'a3_b.mp4', 2.5)
img_to_mp4(FRAMES / 'closing.png', WORK / 'closing.mp4', 5.5)
img_to_mp4(FRAMES / 'endcard.png', WORK / 'endcard.mp4', 4.0)

# ============ ASSEMBLY ============
print("[5] Concatenating video segments...")
segments = [
    WORK / 'cold_a.mp4',
    WORK / 'cold_b.mp4',
]
# Act 1 segments
for i in range(len(act1_segments)):
    segments.append(WORK / f'a1_{i:02d}.mp4')
# Act 2
segments.append(WORK / 'a2_workshop.mp4')
segments.append(WORK / 'a2_p1_card.mp4')
segments.append(WORK / 'a2_p1_real.mp4')
segments.append(WORK / 'a2_p2_card.mp4')
segments.append(WORK / 'a2_p2_real.mp4')
segments.append(WORK / 'a2_p3_card.mp4')
segments.append(WORK / 'a2_p3_real.mp4')
segments.append(WORK / 'a2_p4_card.mp4')
segments.append(WORK / 'a2_p5_card.mp4')
segments.append(WORK / 'a2_p5_real.mp4')
for i in range(1, 6):
    segments.append(WORK / f'a2_cl_{i}.mp4')
if (WORK / 'a2_gallery1.mp4').exists():
    segments.append(WORK / 'a2_gallery1.mp4')
# Act 3 + closing + end
segments.append(WORK / 'a3_a.mp4')
segments.append(WORK / 'a3_b.mp4')
segments.append(WORK / 'closing.mp4')
segments.append(WORK / 'endcard.mp4')

concat_list = WORK / 'video_concat.txt'
with open(concat_list, 'w') as f:
    for s in segments:
        if s.exists():
            f.write(f"file '{s}'\n")
        else:
            print(f"    MISSING: {s}")

silent_video = WORK / 'silent.mp4'
if not run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', str(concat_list),
            '-c', 'copy', str(silent_video)], "concat silent video"):
    raise SystemExit(1)

# Get duration
total_dur = float(subprocess.check_output(
    ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
     '-of', 'default=noprint_wrappers=1:nokey=1', str(silent_video)]).strip())
print(f"  silent video total: {total_dur:.1f}s")

print("[6] Building audio track (cold-open silence + narration acts)...")
# Cold open: 10s silence
# Act 1 narration starts around 10s
# Act 2 intro after Act 1 (~10 + ~24 = 34s)
# Act 2 passes during pass cards
# Act 2 close during closing cards
# Act 3 during act3_a/b
# Closing has its own audio (sfx if Roger hasn't recorded)

# Simpler approach: layer narration segments at calculated start times
# Calculate cumulative start times based on segment durations

cumulative = 0.0
schedule = []  # (label, start, audio_file_or_None)

# Cold open (10s)
schedule.append(('cold_a', cumulative, None)); cumulative += 5.0
schedule.append(('cold_b', cumulative, None)); cumulative += 5.0

# Act 1 photos (with Act 1 narration starting at first photo)
act1_start = cumulative
for i, (_, dur) in enumerate(act1_segments):
    schedule.append((f'a1_{i:02d}', cumulative, None))
    cumulative += dur

act1_end = cumulative

# Act 2 workshop
act2_workshop_start = cumulative
schedule.append(('a2_workshop', cumulative, None)); cumulative += 4.5

# Passes
act2_passes_start = cumulative
schedule.append(('a2_p1_card', cumulative, None)); cumulative += 1.8
schedule.append(('a2_p1_real', cumulative, None)); cumulative += 1.8
schedule.append(('a2_p2_card', cumulative, None)); cumulative += 1.5
schedule.append(('a2_p2_real', cumulative, None)); cumulative += 2.0
schedule.append(('a2_p3_card', cumulative, None)); cumulative += 1.5
schedule.append(('a2_p3_real', cumulative, None)); cumulative += 2.0
schedule.append(('a2_p4_card', cumulative, None)); cumulative += 1.5
schedule.append(('a2_p5_card', cumulative, None)); cumulative += 1.5
schedule.append(('a2_p5_real', cumulative, None)); cumulative += 2.5

# Closing lines
act2_close_start = cumulative
for i in range(1, 6):
    schedule.append((f'a2_cl_{i}', cumulative, None)); cumulative += 2.5
if (WORK / 'a2_gallery1.mp4').exists():
    schedule.append(('a2_gallery1', cumulative, None)); cumulative += 2.5

# Act 3
act3_start = cumulative
schedule.append(('a3_a', cumulative, None)); cumulative += 2.0
schedule.append(('a3_b', cumulative, None)); cumulative += 2.5

# Closing
closing_start = cumulative
schedule.append(('closing', cumulative, None)); cumulative += 5.5

# End card
endcard_start = cumulative
schedule.append(('endcard', cumulative, None)); cumulative += 4.0

print(f"  total scheduled: {cumulative:.1f}s")
print(f"  Act 1 narration starts: {act1_start:.1f}s")
print(f"  Act 2 intro: {act2_workshop_start:.1f}s")
print(f"  Act 2 passes: {act2_passes_start:.1f}s")
print(f"  Act 2 close: {act2_close_start:.1f}s")
print(f"  Act 3: {act3_start:.1f}s")

# Build audio with adelay filters
# ffmpeg can layer multiple audio inputs with adelay
narr_files = {
    'act1': (str(WORK / 'narr_act1.mp3'), int(act1_start * 1000)),
    'act2_intro': (str(WORK / 'narr_act2_intro.mp3'), int(act2_workshop_start * 1000)),
    'act2_passes': (str(WORK / 'narr_act2_passes.mp3'), int(act2_passes_start * 1000)),
    'act2_close': (str(WORK / 'narr_act2_close.mp3'), int(act2_close_start * 1000)),
    'act3': (str(WORK / 'narr_act3.mp3'), int(act3_start * 1000)),
}

# Construct ffmpeg command with adelay
cmd = ['ffmpeg', '-y']
for name, (path, _) in narr_files.items():
    cmd += ['-i', path]

filt = []
for i, (name, (path, delay_ms)) in enumerate(narr_files.items()):
    filt.append(f'[{i}:a]adelay={delay_ms}|{delay_ms},apad[a{i}]')
filt.append(f'{"".join(f"[a{i}]" for i in range(len(narr_files)))}amix=inputs={len(narr_files)}:duration=longest:dropout_transition=0[mixed]')
cmd += ['-filter_complex', ';'.join(filt),
        '-map', '[mixed]', '-t', f'{cumulative}',
        '-c:a', 'aac', '-b:a', '192k', str(WORK / 'audio_track.aac')]

if not run(cmd, "build audio track"):
    raise SystemExit(1)

print("[7] Mux video + audio → FINAL")
final = OUT / 'wtf_DRESS_REHEARSAL.mp4'
if not run(['ffmpeg', '-y', '-i', str(silent_video), '-i', str(WORK / 'audio_track.aac'),
            '-c:v', 'copy', '-c:a', 'copy', '-shortest', str(final)],
           "final mux"):
    raise SystemExit(1)

sz = final.stat().st_size
fdur = float(subprocess.check_output(
    ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
     '-of', 'default=noprint_wrappers=1:nokey=1', str(final)]).strip())
print(f"\n✓ DRESS REHEARSAL: {final}")
print(f"  size: {sz/1024/1024:.2f}MB  duration: {fdur:.1f}s ({int(fdur//60)}:{int(fdur%60):02d})")
