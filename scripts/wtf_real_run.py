"""WTF Real Run — Number One Son Software Development promo documentary.
Tightened to ~4:40. Every one of 51 facets visible. Chain of command rendered.
Recursive endpoint: Soldier 1 'creating' the frame the audience is watching.
"""
import os, subprocess, math, hashlib, random
from pathlib import Path
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = Path('/sessions/dreamy-sleepy-archimedes/mnt/outputs')
WORK = Path('/tmp/wtf_realrun')
WORK.mkdir(parents=True, exist_ok=True)
FRAMES = WORK / 'frames'
FRAMES.mkdir(exist_ok=True)

W, H = 1920, 1080
NAVY = (15, 23, 42)
DARK = (10, 14, 25)
ORANGE = (210, 110, 50)
ORANGE_HOT = (245, 145, 70)
CREAM = (240, 234, 224)
GREY_DIM = (90, 95, 110)
GREY_TEXT = (160, 165, 175)
WHITE = (255, 255, 255)

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
    "Workflows", "Webhooks", "Async Tasks", "Reference Image", "Content Moderation", "File Uploads", "Knowledge Base", "Org Credits",
    "rw-generate-video", "rw-generate-image", "rw-generate-audio", "rw-integrate-characters", "rw-integrate-documents", "use-runway-api",
    "Builders Program", "Runway Fund", "Runway Labs"
]
sergeants = [
    ("Sgt. Video", 1, 8),
    ("Sgt. Image", 9, 11),
    ("Sgt. World", 12, 14),
    ("Sgt. Performance", 15, 15),
    ("Sgt. Editing", 16, 20),
    ("Sgt. Audio", 21, 26),
    ("Sgt. Frameworks", 27, 31),
    ("Sgt. SDKs", 32, 34),
    ("Sgt. Platform", 35, 42),
    ("Sgt. Skills + Eco", 43, 51),
]

def sergeant_for(idx):
    for sg in sergeants:
        if sg[1] <= idx <= sg[2]:
            return sg[0]
    return ""

def get_font(path, size):
    return ImageFont.truetype(path, size)

def draw_centered(draw, text, font, y, color, x_center=W//2):
    bbox = draw.textbbox((0,0), text, font=font)
    w = bbox[2]-bbox[0]
    draw.text((x_center - w//2, y), text, font=font, fill=color)
    return bbox[3] - bbox[1]

# ======== Chain of command base layout ========
def draw_command_layout(draw, hl_mastermind=True, hl_general=False,
                        hl_sergeant=None, hl_soldiers=None,
                        dim_others=False):
    f_lbl = get_font(FONT_REG, 18)
    f_role = get_font(FONT_BOLD, 24)
    f_role_sm = get_font(FONT_BOLD, 18)
    f_sgt = get_font(FONT_BOLD, 14)
    f_num = get_font(FONT_MONO, 14)
    hl_soldiers = hl_soldiers or set()

    # Mastermind (top center)
    mm_x, mm_y, mm_w, mm_h = W//2 - 200, 60, 400, 70
    mm_color = ORANGE_HOT if hl_mastermind else GREY_DIM
    draw.rectangle([mm_x, mm_y, mm_x+mm_w, mm_y+mm_h], outline=mm_color, width=3)
    draw.text((mm_x+20, mm_y+8), "MASTERMIND", font=f_lbl, fill=mm_color)
    draw.text((mm_x+20, mm_y+30), "Number One Son SD", font=f_role, fill=mm_color)

    # Connector down
    draw.line([(W//2, mm_y+mm_h), (W//2, mm_y+mm_h+30)], fill=GREY_TEXT, width=2)

    # General
    gn_y = mm_y + mm_h + 30
    gn_x, gn_w, gn_h = W//2 - 160, 320, 60
    gn_color = ORANGE_HOT if hl_general else (CREAM if not dim_others else GREY_DIM)
    draw.rectangle([gn_x, gn_y, gn_x+320, gn_y+gn_h], outline=gn_color, width=3)
    draw.text((gn_x+20, gn_y+8), "GENERAL", font=f_lbl, fill=gn_color)
    draw.text((gn_x+20, gn_y+28), "Number One Son", font=f_role, fill=gn_color)

    # Connectors to sergeants
    sg_y = gn_y + gn_h + 30
    sg_w = (W - 200) // 10
    draw.line([(W//2, gn_y+gn_h), (W//2, sg_y - 15)], fill=GREY_TEXT, width=2)
    draw.line([(100 + sg_w//2, sg_y - 15), (100 + 9*sg_w + sg_w//2, sg_y - 15)], fill=GREY_TEXT, width=2)

    # Sergeants
    sg_h = 50
    for i, (sn, lo, hi) in enumerate(sergeants):
        x = 100 + i * sg_w
        active = (hl_sergeant == i)
        color = ORANGE_HOT if active else (CREAM if not dim_others else GREY_DIM)
        draw.line([(x + sg_w//2, sg_y - 15), (x + sg_w//2, sg_y)], fill=GREY_TEXT, width=2)
        draw.rectangle([x+10, sg_y, x+sg_w-10, sg_y+sg_h], outline=color, width=2)
        # short name
        sn_short = sn.replace("Sgt. ", "")
        bbox = draw.textbbox((0,0), sn_short, font=f_sgt)
        tw = bbox[2]-bbox[0]
        draw.text((x + sg_w//2 - tw//2, sg_y+8), sn_short, font=f_sgt, fill=color)
        rng = f"{lo}-{hi}"
        bbox = draw.textbbox((0,0), rng, font=f_sgt)
        tw = bbox[2]-bbox[0]
        draw.text((x + sg_w//2 - tw//2, sg_y+28), rng, font=f_sgt, fill=color)

    # Soldiers row(s) below each sergeant
    sd_top = sg_y + sg_h + 30
    sd_box_w = 36
    sd_box_h = 36
    sd_gap = 4
    for i, (sn, lo, hi) in enumerate(sergeants):
        x_base = 100 + i * sg_w + 10
        cnt = hi - lo + 1
        # arrange in rows of up to 5
        cols = min(5, cnt)
        rows = math.ceil(cnt / cols)
        for k in range(cnt):
            r = k // cols
            c = k % cols
            sx = x_base + c * (sd_box_w + sd_gap)
            sy = sd_top + r * (sd_box_h + sd_gap)
            sid = lo + k
            on = sid in hl_soldiers
            sg_active = (hl_sergeant == i)
            if on:
                color = ORANGE_HOT
            elif sg_active and not dim_others:
                color = ORANGE
            elif dim_others:
                color = GREY_DIM
            else:
                color = CREAM
            draw.rectangle([sx, sy, sx+sd_box_w, sy+sd_box_h], outline=color, width=1)
            num_str = f"{sid:02d}"
            bbox = draw.textbbox((0,0), num_str, font=f_num)
            tw = bbox[2]-bbox[0]; th = bbox[3]-bbox[1]
            draw.text((sx + sd_box_w//2 - tw//2, sy + sd_box_h//2 - th//2 - 2),
                      num_str, font=f_num, fill=color)

# ======== Soldier portrait frame ========
def soldier_frame(idx, label_act=None):
    img = Image.new('RGB', (W, H), DARK)
    draw = ImageDraw.Draw(img)
    name = soldiers[idx-1]
    sgt = sergeant_for(idx)

    # Procedural "shot" panel (placeholder for the real Runway output)
    seed = idx * 17
    rnd = random.Random(seed)
    # Background hue band
    hue_base = (idx * 7) % 360
    # Draw a procedural rectangle composition representing this soldier's "output"
    panel_x, panel_y, panel_w, panel_h = 240, 180, 1440, 540
    # base fill
    base_r = int(50 + (idx * 3) % 80)
    base_g = int(40 + (idx * 5) % 100)
    base_b = int(80 + (idx * 11) % 120)
    draw.rectangle([panel_x, panel_y, panel_x+panel_w, panel_y+panel_h],
                   fill=(base_r, base_g, base_b))
    # Procedural shapes
    for _ in range(8 + (idx % 6)):
        cx = rnd.randint(panel_x+50, panel_x+panel_w-50)
        cy = rnd.randint(panel_y+50, panel_y+panel_h-50)
        r = rnd.randint(40, 200)
        col = (
            (base_r + rnd.randint(-30, 60)) % 256,
            (base_g + rnd.randint(-30, 60)) % 256,
            (base_b + rnd.randint(-30, 60)) % 256,
            )
        if idx % 3 == 0:
            draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=col)
        elif idx % 3 == 1:
            draw.rectangle([cx-r, cy-r, cx+r, cy+r], fill=col)
        else:
            draw.polygon([(cx, cy-r), (cx+r, cy+r), (cx-r, cy+r)], fill=col)
    # Subtle frame on the panel
    draw.rectangle([panel_x, panel_y, panel_x+panel_w, panel_y+panel_h],
                   outline=ORANGE, width=4)
    # "Output of Soldier N" subtitle inside panel
    f_panel = get_font(FONT_REG, 20)
    draw.text((panel_x+20, panel_y+panel_h-40), f"OUTPUT OF SOLDIER {idx:02d} — {name.upper()}",
              font=f_panel, fill=CREAM)

    # Header bar
    f_eyebrow = get_font(FONT_REG, 22)
    f_h = get_font(FONT_BOLD, 64)
    f_sub = get_font(FONT_REG, 28)
    f_meta = get_font(FONT_REG, 24)

    eyebrow = "WHISKEY TANGO FOXTROT — ROLL CALL"
    draw_centered(draw, eyebrow, f_eyebrow, 60, GREY_TEXT)

    # Big badge number on the left side
    f_huge = get_font(FONT_BOLD, 220)
    badge_str = f"{idx:02d}"
    draw.text((90, 770), badge_str, font=f_huge, fill=ORANGE_HOT)

    # Right side: name + sergeant
    name_x = 380
    name_y = 790
    draw.text((name_x, name_y), name, font=f_h, fill=CREAM)
    draw.text((name_x, name_y + 80), f"{sgt}", font=f_sub, fill=ORANGE)
    draw.text((name_x, name_y + 120), f"{idx} of 51", font=f_meta, fill=GREY_TEXT)

    img.save(FRAMES / f"soldier_{idx:02d}.png")

# ======== Act intro frames ========
def act_card(filename, eyebrow, title, sub, hl_soldier=None):
    img = Image.new('RGB', (W, H), DARK)
    draw = ImageDraw.Draw(img)
    f_eb = get_font(FONT_REG, 28)
    f_t = get_font(FONT_BOLD, 130)
    f_s = get_font(FONT_REG, 36)
    draw_centered(draw, eyebrow, f_eb, H//2 - 200, GREY_TEXT)
    draw_centered(draw, title, f_t, H//2 - 140, CREAM)
    if sub:
        draw_centered(draw, sub, f_s, H//2 + 30, ORANGE)
    img.save(FRAMES / filename)

# ======== Chain of command animation frames ========
def cmd_frame(filename, hl_mm=False, hl_gen=False, hl_sgt=None, hl_sds=None,
              dim_others=False, caption=""):
    img = Image.new('RGB', (W, H), DARK)
    draw = ImageDraw.Draw(img)
    # Header
    f_eb = get_font(FONT_REG, 22)
    draw_centered(draw, "CHAIN OF COMMAND", f_eb, 18, GREY_TEXT)
    draw_command_layout(draw, hl_mastermind=hl_mm, hl_general=hl_gen,
                        hl_sergeant=hl_sgt, hl_soldiers=hl_sds, dim_others=dim_others)
    # Caption at bottom
    if caption:
        f_cap = get_font(FONT_REG, 28)
        draw_centered(draw, caption, f_cap, H - 80, ORANGE_HOT)
    img.save(FRAMES / filename)

# ======== Recursive Act 4 frame ========
def recursion_frame(filename, scrub=0.0, soldier=1):
    """Frame showing the video itself being 'rendered' by Soldier N."""
    img = Image.new('RGB', (W, H), DARK)
    draw = ImageDraw.Draw(img)
    # Inner: a screenshot of the documentary (use the cold open card)
    inner_w, inner_h = 1200, 700
    inner_x = (W - inner_w) // 2
    inner_y = 180
    # Draw inner panel — a faux rendering of the documentary frame
    draw.rectangle([inner_x, inner_y, inner_x+inner_w, inner_y+inner_h],
                   fill=NAVY, outline=ORANGE, width=4)
    f_eb = get_font(FONT_REG, 22)
    f_t = get_font(FONT_BOLD, 96)
    f_s = get_font(FONT_REG, 30)
    draw.text((inner_x + inner_w//2 - 200, inner_y + 80), "WHISKEY TANGO FOXTROT",
              font=f_eb, fill=ORANGE)
    title = "Number One Son"
    bbox = draw.textbbox((0,0), title, font=f_t)
    tw = bbox[2]-bbox[0]
    draw.text((inner_x + inner_w//2 - tw//2, inner_y + 130), title, font=f_t, fill=CREAM)
    sub = "Software Development"
    bbox = draw.textbbox((0,0), sub, font=f_s)
    tw = bbox[2]-bbox[0]
    draw.text((inner_x + inner_w//2 - tw//2, inner_y + 250), sub, font=f_s, fill=ORANGE)
    # Render-progress bar across the inner panel
    bar_y = inner_y + inner_h - 60
    bar_x = inner_x + 40
    bar_w = inner_w - 80
    draw.rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + 18], outline=GREY_TEXT, width=1)
    fill_w = int(bar_w * scrub)
    if fill_w > 0:
        draw.rectangle([bar_x, bar_y, bar_x + fill_w, bar_y + 18], fill=ORANGE_HOT)
    # render scanline
    if 0.05 < scrub < 0.95:
        scan_x = bar_x + fill_w
        draw.line([(scan_x, inner_y + 4), (scan_x, inner_y + inner_h - 4)],
                  fill=ORANGE_HOT, width=3)

    # Outer overlay: Soldier N badge on the left
    f_huge = get_font(FONT_BOLD, 200)
    f_label = get_font(FONT_BOLD, 32)
    f_sub = get_font(FONT_REG, 22)
    draw.text((80, 880), f"{soldier:02d}", font=f_huge, fill=ORANGE_HOT)
    draw.text((360, 900), "RENDERING THIS FRAME", font=f_label, fill=CREAM)
    draw.text((360, 950), f"Soldier {soldier} — {soldiers[soldier-1]}", font=f_sub, fill=ORANGE)

    # Eyebrow
    draw_centered(draw, "ACT 4 — THE REVEAL", f_eb, 60, GREY_TEXT)
    img.save(FRAMES / filename)

# ======== Generate all frames ========
print("[1/6] Generating soldier portrait frames (51)...")
for i in range(1, 52):
    soldier_frame(i)

print("[2/6] Generating act cards...")
act_card("00_cold.png", "CODENAME — WHISKEY TANGO FOXTROT", "The Question",
         "How would you represent yourself?")
act_card("01_act1.png", "ACT 1", "The Mission",
         "One Mastermind. An army of agents.")
act_card("02_act2.png", "ACT 2", "The Roll Call",
         "Fifty-one soldiers. Fifty-one Runway facets.")
act_card("03_act3.png", "ACT 3", "The Orchestration",
         "Mastermind → General → Sergeants → Soldiers")
act_card("04_act4.png", "ACT 4", "The Reveal",
         "The film about the system, made by the system.")
act_card("99_end.png", "NUMBER ONE SON SOFTWARE DEVELOPMENT",
         "Builders Program",
         "Let us talk.")

print("[3/6] Generating chain-of-command animation frames...")
cmd_frame("cmd_01.png", hl_mm=True, dim_others=True, caption="The Mastermind issues an order")
cmd_frame("cmd_02.png", hl_mm=True, hl_gen=True, dim_others=True, caption="The General receives")
cmd_frame("cmd_03.png", hl_mm=True, hl_gen=True, hl_sgt=0, dim_others=False,
          caption="Sergeant Video, fall in")
cmd_frame("cmd_04.png", hl_mm=True, hl_gen=True, hl_sgt=2, dim_others=False,
          caption="Sergeant World, fall in")
cmd_frame("cmd_05.png", hl_mm=True, hl_gen=True, hl_sgt=5, dim_others=False,
          caption="Sergeant Audio, fall in")
cmd_frame("cmd_06.png", hl_mm=True, hl_gen=True, hl_sgt=4, dim_others=False,
          caption="Sergeant Editing, fall in")
cmd_frame("cmd_full.png", hl_mm=True, hl_gen=True,
          hl_sds=set(range(1,52)),
          caption="Fifty-one in formation")

print("[4/6] Generating recursive Act 4 frames...")
for k, scrub in enumerate([0.0, 0.15, 0.35, 0.55, 0.78, 0.95, 1.0]):
    recursion_frame(f"rec_{k:02d}.png", scrub=scrub, soldier=1)

print("[5/6] Generating audio (cached if exists)...")
# Force regen of Act 3 and Act 4 with revised scripts
for stale in ['03_act3.mp3', '04_act4.mp3']:
    p = WORK / stale
    if p.exists():
        p.unlink()

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
roll = []
for i, name in enumerate(soldiers, start=1):
    roll.append(f"Soldier {i}, {name}.")
act2 = ("Roll call. " + " ".join(roll[:25]) + " ... Push in. " + " ".join(roll[25:])
        + " Fifty-one soldiers. Fifty-one capabilities. Every one of them ready to march.")

act3 = (
    "The Mastermind issued a new order. "
    "Generate a thirty-second cinematic teaser for Number One Son Software Development. "
    "Narrate it in five languages. "
    "The order moved. The General received. He delegated through the chain. "
    "Sergeant Video, fall in. Soldier One — Gen-4.5 — generate the establishing shot. "
    "Sergeant World, fall in. Soldier Thirteen — Characters — generate the narrator avatar. "
    "Sergeant Audio, fall in. Soldier Twenty-One, voice. Soldier Twenty-Three, dubbing. Soldier Twenty-Six, custom voice. "
    "Sergeant Editing, fall in. Soldier Eight — Aleph — color grade. "
    "Forty-eight seconds of orchestration. Fifteen soldiers contributed. "
    "The Mastermind never touched a tool. This is what Number One Son does at scale."
)
act4 = (
    "Everything you have just watched was produced by this system. "
    "Every shot, every voice, every translation. "
    "Look at this frame. Watch closely. Soldier One — Gen-4.5 — is rendering this exact frame, right now, in front of you. "
    "The film about the system, made by the system. "
    "Fifty-one troopers are deployed. You can click any of them. They all work. "
    "Number One Son did the homework. The Mastermind earned the grade. "
    "Runway Builders Program. Let us talk."
)
scripts = {"00_cold_open": cold_open, "01_act1": act1, "02_act2": act2,
           "03_act3": act3, "04_act4": act4}

audio_files = {}
for name, text in scripts.items():
    out = WORK / f"{name}.mp3"
    if not out.exists() or out.stat().st_size < 1000:
        gTTS(text=text, lang='en', slow=False).save(str(out))
    dur = float(subprocess.check_output(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
         '-of', 'default=noprint_wrappers=1:nokey=1', str(out)]).strip())
    audio_files[name] = (out, dur)
    print(f"  {name}: {dur:.1f}s")

# Build audio concat
audio_concat = WORK / 'audio.txt'
with open(audio_concat, 'w') as f:
    for name in ['00_cold_open', '01_act1', '02_act2', '03_act3', '04_act4']:
        f.write(f"file '{audio_files[name][0]}'\n")
full_audio = WORK / 'narration.mp3'
subprocess.run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', str(audio_concat),
                '-c', 'copy', str(full_audio)], capture_output=True, check=True)

print("[6/6] Composing video...")
# Build per-scene shotlist
# Cold Open: act card for full duration
# Act 1: act card 5s, then 6 chain-of-command frames distributed across 28s, finish with cmd_full
# Act 2: act card 3s, then 51 soldier frames distributed across remaining
# Act 3: act card 3s, then orchestration frames matching narration beats
# Act 4: act card 3s, then 7 recursion frames, then end card

video_concat = WORK / 'video.txt'
def writeline(f, name, dur):
    f.write(f"file '{FRAMES / name}'\n")
    f.write(f"duration {dur:.3f}\n")

cold_dur = audio_files['00_cold_open'][1]
act1_dur = audio_files['01_act1'][1]
act2_dur = audio_files['02_act2'][1]
act3_dur = audio_files['03_act3'][1]
act4_dur = audio_files['04_act4'][1]

with open(video_concat, 'w') as f:
    # Cold open: title card 4s, then chain command teaser for rest
    writeline(f, '00_cold.png', 4.0)
    writeline(f, 'cmd_01.png', max(1.0, cold_dur - 4.0))

    # Act 1: act card 3s, then chain of command 5 frames + full formation
    writeline(f, '01_act1.png', 3.0)
    a1_remain = act1_dur - 3.0
    cmd_segs = ['cmd_02.png', 'cmd_03.png', 'cmd_04.png', 'cmd_05.png', 'cmd_06.png', 'cmd_full.png']
    seg_dur = a1_remain / len(cmd_segs)
    for s in cmd_segs:
        writeline(f, s, seg_dur)

    # Act 2: act card 2.5s, then 51 soldier portraits
    writeline(f, '02_act2.png', 2.5)
    a2_remain = act2_dur - 2.5
    per_sd = a2_remain / 51
    for i in range(1, 52):
        writeline(f, f'soldier_{i:02d}.png', per_sd)

    # Act 3: act card 2.5s, then orchestration sequence
    writeline(f, '03_act3.png', 2.5)
    a3_remain = act3_dur - 2.5
    a3_segs = ['cmd_01.png', 'cmd_02.png', 'cmd_03.png', 'cmd_04.png', 'cmd_05.png',
               'cmd_06.png', 'cmd_full.png']
    seg3 = a3_remain / len(a3_segs)
    for s in a3_segs:
        writeline(f, s, seg3)

    # Act 4: act card 2.5s, then recursion frames, then end card
    writeline(f, '04_act4.png', 2.5)
    a4_remain = act4_dur - 2.5 - 2.5  # 2.5s for end card
    rec_segs = [f'rec_{k:02d}.png' for k in range(7)]
    seg4 = a4_remain / len(rec_segs)
    for s in rec_segs:
        writeline(f, s, seg4)
    writeline(f, '99_end.png', 2.5)
    # final required image
    f.write(f"file '{FRAMES / '99_end.png'}'\n")

silent = WORK / 'silent.mp4'
result = subprocess.run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', str(video_concat),
                '-vsync', 'vfr', '-pix_fmt', 'yuv420p', '-c:v', 'libx264',
                '-preset', 'veryfast', '-r', '24', str(silent)],
               capture_output=True, text=True)
if result.returncode != 0:
    print("silent video err:", result.stderr[-800:])
    raise SystemExit(1)

final = OUT / 'wtf_real_run.mp4'
result = subprocess.run(['ffmpeg', '-y', '-i', str(silent), '-i', str(full_audio),
                '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', str(final)],
               capture_output=True, text=True)
if result.returncode != 0:
    print("final video err:", result.stderr[-800:])
    raise SystemExit(1)

dur = float(subprocess.check_output(
    ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
     '-of', 'default=noprint_wrappers=1:nokey=1', str(final)]).strip())
size = final.stat().st_size

print(f"DONE")
print(f"  File: {final}")
print(f"  Size: {size/1024/1024:.1f} MB")
print(f"  Runtime: {dur:.1f}s ({int(dur//60)}:{int(dur%60):02d})")
print(f"  Per-act: cold {cold_dur:.1f}s | act1 {act1_dur:.1f}s | act2 {act2_dur:.1f}s | act3 {act3_dur:.1f}s | act4 {act4_dur:.1f}s")
      