"""WTF Dress Rehearsal Build.
Assembles brand film end-to-end with:
- PIL placeholder cards for Act 1 photos (until Mastermind drops real files)
- Real Runway outputs for Act 2 (existing assets + 2 new shots)
- gTTS narration as voice placeholder (until Mastermind records)
- Text-card placeholder for closing shot (until Mastermind records)
- Real end card with brand lockup

Output: /sessions/dreamy-sleepy-archimedes/mnt/outputs/wtf_DRESS_REHEARSAL.mp4
"""
import os, subprocess, json, math, urllib.request
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = Path('/sessions/dreamy-sleepy-archimedes/mnt/outputs')
WORK = Path('/tmp/wtf_dress')
WORK.mkdir(parents=True, exist_ok=True)
NARR = WORK
FRAMES = WORK / 'frames'
FRAMES.mkdir(exist_ok=True)

W, H = 1920, 1080
DARK = (10, 14, 25)
NAVY = (15, 23, 42)
ORANGE = (220, 130, 60)
ORANGE_HOT = (255, 180, 100)
CREAM = (240, 234, 224)
GREY = (130, 135, 150)
GREY_DIM = (70, 75, 90)
WHITE = (255, 255, 255)
SEPIA_LIGHT = (245, 230, 200)
SEPIA_DARK = (40, 30, 20)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
FONT_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"

# Try a serif italic for caption flavor
FONT_SERIF_ITALIC = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf"

def get_font(p, sz):
    return ImageFont.truetype(p, sz)

def text_centered(draw, text, font, y, color, x_center=W//2):
    bbox = draw.textbbox((0,0), text, font=font)
    tw = bbox[2]-bbox[0]
    draw.text((x_center - tw//2, y), text, font=font, fill=color)
    return bbox[3] - bbox[1]

# ----- COLD OPEN: black + white text -----
def cold_open_frame(filename, line1=True, line2=True):
    img = Image.new('RGB', (W, H), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    f = get_font(FONT_REG, 56)
    if line1:
        text_centered(draw, "My mother used to call me her Number One Son.",
                      f, H//2 - 60, CREAM)
    if line2:
        text_centered(draw, "And that gave me something to live up to.",
                      f, H//2 + 30, CREAM)
    img.save(FRAMES / filename)

cold_open_frame('cold_l1.png', line1=True, line2=False)
cold_open_frame('cold_l2.png', line1=True, line2=True)
print("✓ cold open frames")

# ----- ACT 1 PLACEHOLDER CARDS -----
def photo_placeholder(filename, label, year_caption=None, accent_color=ORANGE):
    """Render a dignified placeholder card representing a real photo."""
    img = Image.new('RGB', (W, H), DARK)
    draw = ImageDraw.Draw(img)
    # Frame
    frame_x, frame_y, frame_w, frame_h = 280, 140, 1360, 760
    draw.rectangle([frame_x, frame_y, frame_x+frame_w, frame_y+frame_h],
                   fill=NAVY, outline=accent_color, width=4)
    # Inner sepia gradient feel
    inner_x, inner_y = frame_x + 60, frame_y + 60
    inner_w, inner_h = frame_w - 120, frame_h - 120
    draw.rectangle([inner_x, inner_y, inner_x+inner_w, inner_y+inner_h],
                   fill=SEPIA_LIGHT)
    # Vintage-style scratches (subtle)
    import random
    rnd = random.Random(hash(filename) % 1000000)
    for _ in range(8):
        x = rnd.randint(inner_x + 20, inner_x + inner_w - 20)
        y1 = rnd.randint(inner_y + 20, inner_y + inner_h - 20)
        y2 = y1 + rnd.randint(40, 200)
        draw.line([(x, y1), (x + rnd.randint(-5, 5), min(y2, inner_y + inner_h - 10))],
                  fill=(220, 200, 170), width=1)
    # Center label
    f_lbl = get_font(FONT_SERIF_ITALIC, 56)
    f_year = get_font(FONT_MONO, 36)
    if year_caption:
        text_centered(draw, year_caption, f_year, inner_y + inner_h // 2 - 80,
                      SEPIA_DARK, x_center=inner_x + inner_w // 2)
    text_centered(draw, label, f_lbl, inner_y + inner_h // 2 - 20, SEPIA_DARK,
                  x_center=inner_x + inner_w // 2)
    # Sub label
    f_sub = get_font(FONT_REG, 22)
    text_centered(draw, "[ Real photograph — placeholder until file upload ]",
                  f_sub, inner_y + inner_h // 2 + 60, GREY,
                  x_center=inner_x + inner_w // 2)
    # Bottom strip with year stamp
    draw.rectangle([inner_x, inner_y + inner_h - 50, inner_x + inner_w, inner_y + inner_h],
                   fill=SEPIA_DARK)
    if year_caption:
        f_stamp = get_font(FONT_MONO, 26)
        text_centered(draw, year_caption, f_stamp, inner_y + inner_h - 42,
                      SEPIA_LIGHT, x_center=inner_x + inner_w // 2)
    img.save(FRAMES / filename)

photo_placeholder('p1_1969.png', 'Mom at 25 with young Roger and sister', 'AUG 69')
photo_placeholder('p2_teen.png', 'Teenage Roger', '~1980')
photo_placeholder('p3_carpentry.png', 'Building furniture', '1990s')
photo_placeholder('p4_house.png', 'Home he built', '1990s')
photo_placeholder('p5_commercial.png', 'Commercial building', '2000s')
photo_placeholder('p6_headshot.png', 'Roger, professional', '2010s')
photo_placeholder('p7_partner.png', 'Roger and his partner', '2010s')
photo_placeholder('p8_son.png', 'Roger and his son at the Golden Gate', '2020s')
photo_placeholder('p9_flying.png', 'Holding her hands so she can fly', '2020s')
photo_placeholder('p10_hospital.png', 'Three generations — Mom + Roger + newborn', 'recent')
print("✓ Act 1 placeholder cards (10)")

# ----- ACT 2 toolbox / pass cards -----
def workshop_card(filename, eyebrow="ACT 2", title="The smartest AI we've ever experienced"):
    img = Image.new('RGB', (W, H), DARK)
    draw = ImageDraw.Draw(img)
    f_eb = get_font(FONT_REG, 28)
    f_t = get_font(FONT_BOLD, 64)
    text_centered(draw, eyebrow, f_eb, H//2 - 60, ORANGE)
    text_centered(draw, title, f_t, H//2 - 20, CREAM)
    img.save(FRAMES / filename)

workshop_card('act2_intro.png')

def pass_card(filename, pass_num, pass_label, pass_phrase, tool_name):
    """Card for each of the 5 craftsman passes."""
    img = Image.new('RGB', (W, H), DARK)
    draw = ImageDraw.Draw(img)
    # Top label
    f_eb = get_font(FONT_REG, 26)
    draw.text((100, 60), f"PASS {pass_num} of 5", font=f_eb, fill=ORANGE)
    f_lbl = get_font(FONT_BOLD, 90)
    draw.text((100, 100), pass_label, font=f_lbl, fill=CREAM)
    f_phrase = get_font(FONT_SERIF_ITALIC, 36)
    draw.text((100, H - 240), f'"{pass_phrase}"', font=f_phrase, fill=GREY)
    # Tool callout
    f_tool = get_font(FONT_MONO, 22)
    draw.rectangle([100, H - 130, 600, H - 80], outline=ORANGE, width=2)
    draw.text((120, H - 117), f"TOOL: {tool_name}", font=f_tool, fill=ORANGE_HOT)
    img.save(FRAMES / filename)

pass_card('pass1.png', 1, 'Rough.', 'The shape of an idea.', 'gen4_image')
pass_card('pass2.png', 2, 'Clarity.', 'Detail emerges.', 'gen4.5')
pass_card('pass3.png', 3, 'The cut.', 'Tone, color, mood.', 'gen4_aleph')
pass_card('pass4.png', 4, 'The voice.', 'A heart for the work.', 'eleven_multilingual_v2')
pass_card('pass5.png', 5, 'The soul.', 'A face on the page.', 'gwm1_avatars')
print("✓ Act 2 pass cards (5)")

def gallery_card(filename, line):
    img = Image.new('RGB', (W, H), DARK)
    draw = ImageDraw.Draw(img)
    f = get_font(FONT_SERIF_ITALIC, 60)
    text_centered(draw, line, f, H//2 - 30, CREAM)
    img.save(FRAMES / filename)

gallery_card('act2_close1.png', '"Same craftsman. Same intent."')
gallery_card('act2_close2.png', '"Sharper blade with every tool in his hands."')
gallery_card('act2_close3.png', '"What used to take a hundred craftspeople, now takes one."')
gallery_card('act2_close4.png', '"The blade does not multiply noise."')
gallery_card('act2_close5.png', '"It multiplies one human\'s intention."')
print("✓ Act 2 closing cards (5)")

# ----- ACT 3 -----
def act3_card(filename, line, subline=""):
    img = Image.new('RGB', (W, H), DARK)
    draw = ImageDraw.Draw(img)
    f = get_font(FONT_BOLD, 80)
    text_centered(draw, line, f, H//2 - 40, CREAM)
    if subline:
        f_sub = get_font(FONT_SERIF_ITALIC, 44)
        text_centered(draw, subline, f_sub, H//2 + 60, ORANGE)
    img.save(FRAMES / filename)

act3_card('act3_a.png', 'Anyone can be a builder.')
act3_card('act3_b.png', 'Here\'s one.', '')
print("✓ Act 3 cards")

# ----- CLOSING SHOT PLACEHOLDER -----
def closing_placeholder(filename):
    img = Image.new('RGB', (W, H), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    f_eb = get_font(FONT_REG, 28)
    f_main = get_font(FONT_BOLD, 64)
    f_quote = get_font(FONT_SERIF_ITALIC, 56)
    f_note = get_font(FONT_MONO, 22)
    text_centered(draw, "[ CLOSING SHOT — REAL ROGER ON CAMERA ]", f_eb, 200, ORANGE)
    text_centered(draw, '"Cris,', f_quote, H//2 - 100, CREAM)
    text_centered(draw, "we're here for you.", f_quote, H//2 - 30, CREAM)
    text_centered(draw, "Let's talk.\"", f_quote, H//2 + 40, CREAM)
    text_centered(draw, "[ awaiting mastermind_closing_shot.mov ]",
                  f_note, H - 200, GREY)
    img.save(FRAMES / filename)

closing_placeholder('closing.png')
print("✓ closing placeholder")

# ----- END CARD -----
def end_card(filename):
    img = Image.new('RGB', (W, H), DARK)
    draw = ImageDraw.Draw(img)
    f_h = get_font(FONT_BOLD, 92)
    f_sub1 = get_font(FONT_REG, 38)
    f_sub2 = get_font(FONT_SERIF_ITALIC, 36)
    text_centered(draw, 'NUMBER ONE SON', f_h, H//2 - 120, CREAM)
    text_centered(draw, 'Software Development', f_sub1, H//2 - 30, ORANGE)
    text_centered(draw, 'Powered by Runway', f_sub2, H//2 + 50, GREY)
    text_centered(draw, "Builders Program — let us talk.",
                  f_sub2, H//2 + 110, ORANGE_HOT)
    img.save(FRAMES / filename)

end_card('endcard.png')
print("✓ end card")

print("\nAll static frames generated.")
