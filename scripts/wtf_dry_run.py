"""WTF Dry Run video producer.
Generates a structural mockup MP4 of the Number One Son documentary using
gTTS for narration, PIL for visual placeholders, and ffmpeg for assembly.
This is NOT the final film — it's a dry run to surface pacing problems.
"""
import os, subprocess, json, math, sys
from pathlib import Path
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont

OUT = Path('/sessions/dreamy-sleepy-archimedes/mnt/outputs')
WORK = Path('/tmp/wtf_dryrun')
WORK.mkdir(parents=True, exist_ok=True)

W, H = 1920, 1080
NAVY = (15, 23, 42)
ORANGE = (196, 90, 46)
CREAM = (240, 234, 224)
GREY = (130, 130, 130)
WHITE = (255, 255, 255)
DARK_BG = (10, 14, 25)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

soldiers = [
    "Gen-4.5", "Gen-4 Turbo", "Gen-3 Turbo", "seedance2", "veo3", "veo3.1", "veo3.1 fast", "Aleph",
    "gen4 image", "gen4 image turbo", "gemini 2.5 flash",
    "GWM Worlds", "Characters", "GWM Robotics",
    "Act-Two",
    "Inpainting", "Interpolation", "4K Upscale", "Super-Resolution", "Remove Background",
    "TTS Multilingual", "Voice Isolation", "Dubbing", "Voice Conversion", "Sound Effects", "Custom Voice",
    "Skills Framework", "avatars-react", "livekit-agents", "runway-agents-js", "MCP Server",
    "Python SDK", "Node SDK", "avatars-rpc",
    "Workflows", "Webhooks", "Async Tasks", "Reference Image", "Content Moderation", "File Uploads", "Knowledge Base", "Org and Credits",
    "rw-generate-video", "rw-generate-image", "rw-generate-audio", "rw-integrate-characters", "rw-integrate-documents", "use-runway-api",
    "Builders Program", "Runway Fund", "Runway Labs"
]
assert len(soldiers) == 51

cold_open = (
    "On Tuesday, May fifth, two thousand twenty-six, Number One Son Software Development asked one question. "
    "If you had to enter a hackathon hosted by the company that built every tool you would use to enter it, "
    "how would you represent yourself? "
    "Cherry-picking three or four facets felt like dishonesty. So we built an army."
)

act1 = (
    "Number One Son is a one-founder company on a one-billion-dollar trajectory. "
    "The next great companies do not have hundreds of employees. "
    "They have one Mastermind, and an army of agents. "
    "We built ours. Fifty-one soldiers, each a master of one Runway capability. "
    "Together, we make this. "
    "Ten Sergeants command. One General orchestrates. The Mastermind directs. "
    "And every shot you are about to see was produced by the army you are about to meet."
)

# Act 2: 51-soldier roll call
roll_call_lines = []
for i, name in enumerate(soldiers, start=1):
    roll_call_lines.append(f"Soldier {i}, {name}.")
act2 = (
    "Roll call. "
    + " ".join(roll_call_lines[:25])
    + " ... Push in. "
    + " ".join(roll_call_lines[25:])
    + " Fifty-one soldiers. Fifty-one capabilities. Every one of them ready to march."
)

act3 = (
    "The Mastermind issued a new order. "
    "Generate a thirty-second cinematic teaser for Number One Son Software Development. "
    "Narrate it in five languages. "
    "The General received the order. The Sergeants stood at attention. The Soldiers marched in. "
    "Sergeant Video, Soldier One. Sergeant World, Soldier Thirteen. "
    "Sergeant Audio, Soldiers Twenty-One through Twenty-Six. "
    "Sergeant Editing, Soldier Eight. "
    "Forty-eight seconds of orchestration. Fifteen soldiers contributed. "
    "The Mastermind never touched a tool. "
    "This is what Number One Son does at scale."
)

act4 = (
    "Everything you have just watched was produced this weekend, by this system. "
    "Every shot is a Runway facet. Every voice is mine, cloned. "
    "Every translation is the army speaking twenty-nine languages. "
    "The film about the system was made by the system. "
    "Fifty-one troopers are deployed. You can click any of them. They all work. "
    "Number One Son did the homework. The Mastermind earned the grade. "
    "Runway Builders Program — let us talk."
)

scripts = {
    "00_cold_open": cold_open,
    "01_act1": act1,
    "02_act2": act2,
    "03_act3": act3,
    "04_act4": act4,
}

print("[1/5] Generating narration audio via gTTS...")
audio_files = {}
for name, text in scripts.items():
    out = WORK / f"{name}.mp3"
    if not out.exists() or out.stat().st_size < 1000:
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(str(out))
    # measure duration
    dur = float(subprocess.check_output(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
         '-of', 'default=noprint_wrappers=1:nokey=1', str(out)]).strip())
    audio_files[name] = (out, dur)
    print(f"  {name}: {dur:.1f}s")

total_audio = sum(d for _, d in audio_files.values())
print(f"  TOTAL AUDIO: {total_audio:.1f}s (target 390s, i.e. 6:30)")

print("[2/5] Generating visual placeholder frames...")

def text_image(path, lines, bg=NAVY, fg=CREAM, accent=None,
               font_paths=None, sizes=None, gap=20):
    img = Image.new('RGB', (W, H), bg)
    draw = ImageDraw.Draw(img)
    if font_paths is None:
        font_paths = [FONT_BOLD] * len(lines)
    if sizes is None:
        sizes = [80] * len(lines)
    fonts = [ImageFont.truetype(fp, sz) for fp, sz in zip(font_paths, sizes)]
    total_h = 0
    bboxes = []
    for line, font in zip(lines, fonts):
        bbox = draw.textbbox((0, 0), line, font=font)
        bboxes.append(bbox)
        total_h += (bbox[3] - bbox[1]) + gap
    total_h -= gap
    y = (H - total_h) // 2
    for i, (line, font, bbox) in enumerate(zip(lines, fonts, bboxes)):
        wpx = bbox[2] - bbox[0]
        x = (W - wpx) // 2
        color = accent if (accent and i == 0) else fg
        draw.text((x, y), line, font=font, fill=color)
        y += (bbox[3] - bbox[1]) + gap
    img.save(path)

# Cold Open frame
text_image(WORK / 'frame_cold.png',
    ["CODENAME", "WHISKEY TANGO FOXTROT", "", "Number One Son Software Development"],
    bg=DARK_BG, fg=CREAM, accent=ORANGE,
    font_paths=[FONT_REG, FONT_BOLD, FONT_REG, FONT_REG],
    sizes=[40, 100, 30, 56])

# Act 1 frame
text_image(WORK / 'frame_act1.png',
    ["ACT 1", "The Mission", "", "One Mastermind. An army of agents."],
    bg=NAVY, fg=CREAM, accent=ORANGE,
    font_paths=[FONT_REG, FONT_BOLD, FONT_REG, FONT_REG],
    sizes=[40, 110, 30, 50])

# Act 3 frame
text_image(WORK / 'frame_act3.png',
    ["ACT 3", "The Orchestration", "", "Mastermind → General → Sergeants → Soldiers"],
    bg=NAVY, fg=CREAM, accent=ORANGE,
    font_paths=[FONT_REG, FONT_BOLD, FONT_REG, FONT_REG],
    sizes=[40, 110, 30, 44])

# Act 4 frame
text_image(WORK / 'frame_act4.png',
    ["ACT 4", "The Reveal", "", "The film about the system, made by the system."],
    bg=NAVY, fg=CREAM, accent=ORANGE,
    font_paths=[FONT_REG, FONT_BOLD, FONT_REG, FONT_REG],
    sizes=[40, 110, 30, 40])

# Soldier formation grid frame for Act 2
def formation_image(path, highlight_count=51):
    img = Image.new('RGB', (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)
    title_font = ImageFont.truetype(FONT_BOLD, 60)
    sub_font = ImageFont.truetype(FONT_REG, 30)
    badge_font = ImageFont.truetype(FONT_MONO, 22)
    name_font = ImageFont.truetype(FONT_REG, 16)
    # Title
    title = "ACT 2 — The Roll Call"
    bbox = draw.textbbox((0, 0), title, font=title_font)
    draw.text(((W - (bbox[2]-bbox[0]))//2, 60), title, font=title_font, fill=CREAM)
    sub = "Fifty-one soldiers report. Each demonstrates one Runway facet."
    bbox2 = draw.textbbox((0, 0), sub, font=sub_font)
    draw.text(((W - (bbox2[2]-bbox2[0]))//2, 140), sub, font=sub_font, fill=GREY)
    # Grid: 17 columns x 3 rows = 51
    cols, rows = 17, 3
    grid_w = W - 200
    grid_h = 600
    box_w = grid_w // cols - 8
    box_h = grid_h // rows - 12
    start_x = 100
    start_y = 240
    for i in range(51):
        r = i // cols
        c = i % cols
        x = start_x + c * (box_w + 8)
        y = start_y + r * (box_h + 12)
        on = (i < highlight_count)
        fill = ORANGE if on else (40, 50, 70)
        draw.rectangle([x, y, x + box_w, y + box_h], fill=fill, outline=CREAM if on else GREY, width=1)
        # number
        num = f"{i+1:02d}"
        nb = draw.textbbox((0,0), num, font=badge_font)
        draw.text((x + (box_w - (nb[2]-nb[0]))//2, y + 8), num,
                  font=badge_font, fill=WHITE if on else GREY)
        # name (truncated)
        nm = soldiers[i][:14]
        nmb = draw.textbbox((0,0), nm, font=name_font)
        draw.text((x + (box_w - (nmb[2]-nmb[0]))//2, y + box_h - 28), nm,
                  font=name_font, fill=WHITE if on else GREY)
    # Footer
    foot = f"{highlight_count} of 51 active"
    fb = draw.textbbox((0, 0), foot, font=sub_font)
    draw.text(((W - (fb[2]-fb[0]))//2, H - 80), foot, font=sub_font, fill=ORANGE)
    img.save(path)

formation_image(WORK / 'frame_act2.png', highlight_count=51)

# Final card
text_image(WORK / 'frame_end.png',
    ["NUMBER ONE SON", "Software Development", "", "Runway Builders Program — let us talk."],
    bg=DARK_BG, fg=CREAM, accent=ORANGE,
    font_paths=[FONT_BOLD, FONT_REG, FONT_REG, FONT_REG],
    sizes=[100, 60, 30, 50])

print("[3/5] Concatenating audio into single track...")
# Build concat list for audio
audio_concat = WORK / 'audio_concat.txt'
with open(audio_concat, 'w') as f:
    for name in ['00_cold_open', '01_act1', '02_act2', '03_act3', '04_act4']:
        f.write(f"file '{audio_files[name][0]}'\n")

full_audio = WORK / 'narration.mp3'
subprocess.run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0',
                '-i', str(audio_concat), '-c', 'copy', str(full_audio)],
               capture_output=True, check=True)

# Get full audio duration
total_dur = float(subprocess.check_output(
    ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
     '-of', 'default=noprint_wrappers=1:nokey=1', str(full_audio)]).strip())
print(f"  Concatenated narration duration: {total_dur:.1f}s")

print("[4/5] Building video from frames + audio...")
# Build a video where each act's frame plays for the duration of that act's audio
# Use ffmpeg concat demuxer with image inputs

video_concat = WORK / 'video_concat.txt'
with open(video_concat, 'w') as f:
    durations = {
        '00_cold_open': audio_files['00_cold_open'][1],
        '01_act1': audio_files['01_act1'][1],
        '02_act2': audio_files['02_act2'][1],
        '03_act3': audio_files['03_act3'][1],
        '04_act4': audio_files['04_act4'][1] - 5,  # last 5s show end card
    }
    frames = {
        '00_cold_open': 'frame_cold.png',
        '01_act1': 'frame_act1.png',
        '02_act2': 'frame_act2.png',
        '03_act3': 'frame_act3.png',
        '04_act4': 'frame_act4.png',
    }
    for name in ['00_cold_open', '01_act1', '02_act2', '03_act3', '04_act4']:
        f.write(f"file '{WORK / frames[name]}'\n")
        f.write(f"duration {durations[name]:.2f}\n")
    # End card for last 5 seconds
    f.write(f"file '{WORK / 'frame_end.png'}'\n")
    f.write(f"duration 5.0\n")
    # final image (concat demuxer requirement)
    f.write(f"file '{WORK / 'frame_end.png'}'\n")

silent_video = WORK / 'silent.mp4'
subprocess.run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', str(video_concat),
                '-vsync', 'vfr', '-pix_fmt', 'yuv420p', '-c:v', 'libx264',
                '-r', '30', str(silent_video)],
               capture_output=True, check=True)

# Combine with audio
final = OUT / 'wtf_dry_run.mp4'
result = subprocess.run(['ffmpeg', '-y', '-i', str(silent_video), '-i', str(full_audio),
                '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', str(final)],
               capture_output=True, text=True)
if result.returncode != 0:
    print("ffmpeg combine error:", result.stderr[-500:])
    sys.exit(1)

final_size = final.stat().st_size
final_dur = float(subprocess.check_output(
    ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
     '-of', 'default=noprint_wrappers=1:nokey=1', str(final)]).strip())

print(f"[5/5] Done.")
print(f"  Final video: {final}")
print(f"  Size: {final_size/1024/1024:.1f} MB")
print(f"  Runtime: {final_dur:.1f}s ({int(final_dur//60)}:{int(final_dur%60):02d})")
print(f"  Target: 390s (6:30)")
print(f"  Delta: {final_dur - 390:+.1f}s")

# Per-act report
print("\nPER-ACT TIMING REPORT:")
print(f"  Cold Open:  {audio_files['00_cold_open'][1]:.1f}s   target 30s   delta {audio_files['00_cold_open'][1]-30:+.1f}s")
print(f"  Act 1:      {audio_files['01_act1'][1]:.1f}s   target 60s   delta {audio_files['01_act1'][1]-60:+.1f}s")
print(f"  Act 2:      {audio_files['02_act2'][1]:.1f}s  target 150s  delta {audio_files['02_act2'][1]-150:+.1f}s")
print(f"  Act 3:      {audio_files['03_act3'][1]:.1f}s   target 90s   delta {audio_files['03_act3'][1]-90:+.1f}s")
print(f"  Act 4:      {audio_files['04_act4'][1]:.1f}s   target 60s   delta {audio_files['04_act4'][1]-60:+.1f}s")
s   target 60s   delta {audio_files['04_act4'][1]-60:+.1f}s")
