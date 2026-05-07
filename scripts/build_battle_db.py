from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = Workbook()

NAVY = "1F2A4A"
ORANGE = "C45A2E"
LIGHT = "F2EEE8"
WHITE = "FFFFFF"
GREEN = "2D7A3F"
RED = "B83A2E"

navy_fill = PatternFill("solid", fgColor=NAVY)
orange_fill = PatternFill("solid", fgColor=ORANGE)
light_fill = PatternFill("solid", fgColor=LIGHT)
green_fill = PatternFill("solid", fgColor="D4ECD8")
red_fill = PatternFill("solid", fgColor="F4D5CF")

thin = Side(border_style="thin", color="BBBBBB")
box = Border(top=thin, bottom=thin, left=thin, right=thin)

def header(cell):
    cell.font = Font(name="Arial", size=11, bold=True, color=WHITE)
    cell.fill = navy_fill
    cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    cell.border = box

def body(cell, bold=False, fill=None):
    cell.font = Font(name="Arial", size=10, bold=bold)
    cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
    cell.border = box
    if fill is not None:
        cell.fill = fill

def section(cell):
    cell.font = Font(name="Arial", size=12, bold=True, color=NAVY)
    cell.fill = light_fill
    cell.alignment = Alignment(horizontal="left", vertical="center")
    cell.border = box

# ============== Sheet 1: Past Winners & Adjacent Patterns ==============
ws = wb.active
ws.title = "Past Winners & Patterns"

cols = ["Event", "Year", "Project / Winner", "Builders", "What it did", "Tech Stack Notes", "Why it won (pattern)", "Source"]
widths = [22, 8, 28, 24, 50, 32, 40, 32]
for i, (c, w) in enumerate(zip(cols, widths), 1):
    cell = ws.cell(row=1, column=i, value=c)
    header(cell)
    ws.column_dimensions[get_column_letter(i)].width = w
ws.row_dimensions[1].height = 36

rows = [
    # Runway events
    ("Runway Characters Hackathon", "2026", "Various (Yining Shi-led)", "In-person, NYC", "Real-time interactive video agents on Characters (GWM-1) — first developer event for the new model.", "Characters API + custom audio drivers", "Novelty alignment: judges led by Yining Shi rewarded teams that pushed Characters past demo-stage.", "https://x.com/runwayml/status/2040114843215188127"),
    ("Runway Gen:48", "2025", "Multiple finalists; Gen:48 is a 48-hour AI-film comp", "Indie filmmaker teams worldwide", "48-hour AI-generated short films on a theme prompt.", "Mostly Gen-3 / Gen-4 + audio editors", "Storytelling craft + cinematic visual quality — narrative coherence beats novelty.", "https://runwayml.com/gen48/terms"),
    ("AIFF (AI Film Festival)", "2024-2025", "Curated selections, jury-judged", "Filmmaker teams; jury includes industry pros", "Annual AI-film festival with feature screenings, jury-selected winners.", "Multi-tool AI workflows; not API-focused", "Aesthetic + emotional resonance + technical ambition. Different rubric from this hackathon.", "https://aiff.runwayml.com/"),
    ("Runway API Hackathon", "May 2026", "TBD — this is the event we're entering", "Open registration, virtual", "Three-day virtual hackathon for agents/apps/tools/workflows on Runway API.", "Runway API + Modal + LLM + audio", "(Predicted) Practical problem-solving + sophisticated API integration + polish.", "https://runwayml.com/api-hackathon"),
    # Adjacent patterns from agent research
    ("Microsoft AI Agents Hackathon", "2025", "RiskWise ($20K)", "Solo/small team", "Supply-chain risk analysis agent with multi-turn reasoning over structured data.", "Azure AI + structured retrieval", "Vertical specificity (supply chain) + grounded data + practical ROI beat horizontal demos.", "https://microsoft.github.io/AI_Agents_Hackathon/winners/"),
    ("Microsoft AI Agents Hackathon", "2025", "Apollo Deep Research Meta-Agent", "Small team", "Multi-turn reasoning agent over research datasets.", "LLM + retrieval", "Multi-turn reasoning over single-call usage; production-feeling output.", "https://microsoft.github.io/AI_Agents_Hackathon/winners/"),
    ("Microsoft AI Agents Hackathon", "2025", "Tariffed", "Small team", "Tariff-management agent for customs workflows.", "Agent + structured APIs", "Vertical specificity in a B2B niche.", "https://microsoft.github.io/AI_Agents_Hackathon/winners/"),
    ("HuggingFace Agents-MCP Hackathon", "2025", "Immersia (formerly LLMGameHub)", "Small team", "Generative narrative agent: world + genre + character → AI-generated story with image + audio.", "MCP + generative image + adaptive audio", "Combined narrative agents + generative media + adaptive audio = compelling demo.", "https://huggingface.co/blog/kikikita/immersia-ai-games"),
    ("OpenAI Open Model Hackathon", "Feb 2026", "Rippletide", "Small team", "Multi-agent system for autonomous, continuous scientific discovery.", "Multi-agent loop + LLMs", "Systems that run autonomously between cycles beat one-shot tools.", "https://openai.com/blog/"),
    ("Vercel Gen CX Hackathon", "2025", "Gen CX winners (brand-content focus)", "Small teams", "Brand-content generation agents with rapid Vercel deployment.", "Vercel AI Gateway + v0 + partner LLMs", "Creator/marketing focus + integrated stack + one-click deploy.", "https://vercel.com/blog/"),
    ("Modal Hackathons (cumulative)", "2024-2026", "Various winners", "Small teams", "Various — typically GPU-heavy serverless inference apps.", "Modal serverless + GPUs + custom models", "Demonstrated infrastructure maturity + working production deploy.", "https://modal.com/blog"),
]
for r, row in enumerate(rows, start=2):
    for c, val in enumerate(row, start=1):
        body(ws.cell(row=r, column=c, value=val))
    ws.row_dimensions[r].height = 60

ws.freeze_panes = "A2"

# ============== Sheet 2: Runway API Capability Matrix ==============
ws2 = wb.create_sheet("API Capabilities")
cols2 = ["Surface", "Released", "Cost (credits)", "Latency", "Best For", "Hackathon Novelty Weight", "DirectorOS Use"]
widths2 = [22, 14, 22, 18, 40, 22, 36]
for i, (c, w) in enumerate(zip(cols2, widths2), 1):
    cell = ws2.cell(row=1, column=i, value=c)
    header(cell)
    ws2.column_dimensions[get_column_letter(i)].width = w
ws2.row_dimensions[1].height = 36

caps = [
    ("Gen-4.5 (text/image-to-video)", "Feb 10, 2026", "12/sec (60–120 per clip)", "30–60 sec", "B-roll, scene generation, native audio", "MEDIUM (proven, stable)", "Primary B-roll engine"),
    ("Characters / GWM-1 (real-time avatar)", "Mar 9, 2026", "Not separately disclosed", "Real-time (<500ms target)", "Interactive avatars, narrator, conversational agents", "HIGHEST (newest)", "Narrator avatar; live-feeling preview"),
    ("Act-Two (performance capture)", "~Feb 2026", "Not separately disclosed", "Seconds", "Motion-cap from webcam → animated character", "HIGH (unique via API)", "Optional: creator-recorded performance shots"),
    ("Aleph (in-context cinematic editing)", "2025", "~12/sec est.", "60–120 sec", "Edit, relight, style match, scene regen", "MEDIUM", "Color/style consistency pass"),
    ("gen4_image", "2025", "5/image", "Seconds", "Reference frames, concept art, style anchors", "MEDIUM", "Character / style reference frames"),
    ("ElevenLabs TTS via Runway", "Sep 25, 2025", "~0.5/100 chars est.", "Seconds", "29-language VO, dubbing", "MEDIUM", "Multilingual VO"),
    ("ElevenLabs Dubbing via Runway", "Sep 25, 2025", "Bundled", "Seconds", "Translate video while preserving voice", "MEDIUM", "Per-platform/language outputs"),
    ("Custom Voice Training", "2025", "300/voice (one-time)", "Minutes", "Brand voices, creator clones", "LOW (table-stakes)", "Optional founder voice"),
    ("Webhooks (Svix)", "—", "Free", "Real-time event push", "Async pipelines without polling", "LOW", "Pipeline plumbing"),
    ("Runway Skills framework", "Mar 2026", "Free (open source)", "—", "Agent-callable skills", "MEDIUM (judge bait)", "Three custom skills shipped to GitHub"),
    ("Modal serverless (A100 40GB)", "—", "$2.10/hr base", "Seconds", "ffmpeg, post-processing, orchestration", "LOW", "Pipeline runtime"),
]
for r, row in enumerate(caps, start=2):
    for c, val in enumerate(row, start=1):
        body(ws2.cell(row=r, column=c, value=val))
    ws2.row_dimensions[r].height = 40
ws2.freeze_panes = "A2"

# ============== Sheet 3: Build Scorecard ==============
ws3 = wb.create_sheet("Build Scorecard")
cols3 = ["Candidate", "Creativity (1-5)", "Technical Depth (1-5)", "Impact (1-5)", "Polish-feasibility in 72h (1-5)", "Total (auto)", "NumberOneSon Fit (1-5)", "Combined (auto)", "Notes"]
widths3 = [22, 16, 18, 14, 22, 14, 18, 16, 50]
for i, (c, w) in enumerate(zip(cols3, widths3), 1):
    cell = ws3.cell(row=1, column=i, value=c)
    header(cell)
    ws3.column_dimensions[get_column_letter(i)].width = w
ws3.row_dimensions[1].height = 40

candidates = [
    ("DirectorOS (recommended)", 5, 5, 5, 4, 5, "Anchor product line; solopreneur creator stack play; productizable in 30 days post-event."),
    ("InteractiveFlow (live narrative voting)", 5, 5, 4, 3, 3, "Twitch-creator niche; real-time risk; novel interaction model wows judges."),
    ("PerformanceAI (Act-Two performance)", 4, 5, 4, 3, 3, "Heavy Act-Two use; novel; demo-worthy; smaller market."),
    ("NewsFlow (live data → video)", 4, 4, 4, 3, 3, "Strong vertical (news/finance) but B2B sales cycle is longer than NOS solo thesis prefers."),
    ("EditBot (agentic post-production)", 3, 5, 4, 2, 2, "Pro market; high technical complexity; harder to demo end-to-end in 72h."),
]
for r, row in enumerate(candidates, start=2):
    name, c1, c2, c3, c4, nos, notes = row
    body(ws3.cell(row=r, column=1, value=name), bold=(r==2), fill=(light_fill if r==2 else None))
    body(ws3.cell(row=r, column=2, value=c1), fill=(light_fill if r==2 else None))
    body(ws3.cell(row=r, column=3, value=c2), fill=(light_fill if r==2 else None))
    body(ws3.cell(row=r, column=4, value=c3), fill=(light_fill if r==2 else None))
    body(ws3.cell(row=r, column=5, value=c4), fill=(light_fill if r==2 else None))
    body(ws3.cell(row=r, column=6, value=f"=SUM(B{r}:E{r})"), bold=True, fill=(light_fill if r==2 else None))
    body(ws3.cell(row=r, column=7, value=nos), fill=(light_fill if r==2 else None))
    body(ws3.cell(row=r, column=8, value=f"=F{r}+G{r}"), bold=True, fill=(light_fill if r==2 else None))
    body(ws3.cell(row=r, column=9, value=notes), fill=(light_fill if r==2 else None))
    ws3.row_dimensions[r].height = 32
ws3.freeze_panes = "A2"

# ============== Sheet 4: Credit Budget ==============
ws4 = wb.create_sheet("Credit Budget")
cols4 = ["Bucket", "Allocation (credits)", "% of total", "Retail $", "Notes"]
widths4 = [30, 22, 14, 14, 60]
for i, (c, w) in enumerate(zip(cols4, widths4), 1):
    cell = ws4.cell(row=1, column=i, value=c)
    header(cell)
    ws4.column_dimensions[get_column_letter(i)].width = w
ws4.row_dimensions[1].height = 32

budget = [
    ("Pre-hack dev (May 6-7)", 20000, "Use 20K of the 50K participant credits before Friday kickoff for Runway API spikes."),
    ("Hackathon build (Fri-Sun)", 80000, "Gen-4.5 main pipeline + Characters tests + Act-Two trials + Aleph passes."),
    ("Demo recording (Sun)", 40000, "Generate canonical demo at full quality + 4K upscale + multilingual VO."),
    ("Edge-case battery (Sun)", 30000, "Blank input, 10K-char input, special chars, non-English, very long, broken refs."),
    ("Reserve / surprise", 30000, "Day-of-Friday endpoint announcements, judging-day backup runs."),
]
total_row_idx = len(budget) + 2
for r, (b, alloc, notes) in enumerate(budget, start=2):
    body(ws4.cell(row=r, column=1, value=b))
    body(ws4.cell(row=r, column=2, value=alloc))
    body(ws4.cell(row=r, column=3, value=f"=B{r}/$B${total_row_idx}"))
    ws4.cell(row=r, column=3).number_format = "0.0%"
    body(ws4.cell(row=r, column=4, value=f"=B{r}*0.01"))
    ws4.cell(row=r, column=4).number_format = '"$"#,##0'
    body(ws4.cell(row=r, column=5, value=notes))
    ws4.row_dimensions[r].height = 30

body(ws4.cell(row=total_row_idx, column=1, value="TOTAL"), bold=True, fill=light_fill)
body(ws4.cell(row=total_row_idx, column=2, value=f"=SUM(B2:B{total_row_idx-1})"), bold=True, fill=light_fill)
body(ws4.cell(row=total_row_idx, column=3, value=f"=B{total_row_idx}/B{total_row_idx}"), bold=True, fill=light_fill)
ws4.cell(row=total_row_idx, column=3).number_format = "0.0%"
body(ws4.cell(row=total_row_idx, column=4, value=f"=B{total_row_idx}*0.01"), bold=True, fill=light_fill)
ws4.cell(row=total_row_idx, column=4).number_format = '"$"#,##0'
body(ws4.cell(row=total_row_idx, column=5, value="Cap; track real-time in Supabase counter."), fill=light_fill)
ws4.freeze_panes = "A2"

# ============== Sheet 5: 7-Day Plan ==============
ws5 = wb.create_sheet("7-Day Plan")
cols5 = ["Date", "Day", "Theme", "Outputs by EOD", "Owner", "Status"]
widths5 = [14, 16, 22, 70, 14, 14]
for i, (c, w) in enumerate(zip(cols5, widths5), 1):
    cell = ws5.cell(row=1, column=i, value=c)
    header(cell)
    ws5.column_dimensions[get_column_letter(i)].width = w
ws5.row_dimensions[1].height = 32

plan = [
    ("2026-05-05", "Tue T-3", "Decide & confirm (research-only)", "Roger picks build. Runway dev account confirmed on rogergrubbrealestate@gmail.com (NOT roger@grubb.net; caught mismatch, re-registered, emailed events@runwayml.com to drop dupe). Discord joined. GitHub org created (empty). NO code written.", "Roger + Claude", "in progress"),
    ("2026-05-06", "Wed T-2", "Research + interviews (no code)", "Read full Runway docs + Skills repo + Modal docs. 5 user interviews. Architecture diagram. README outline. Brand decision.", "Claude", "pending"),
    ("2026-05-07", "Thu T-1", "Env setup + spec freeze", "Registration deadline 5pm ET — confirm enrolled. Install SDKs locally. Modal account ready. Slack workspace prepared. PRD frozen. NO API calls. NO submission code.", "Claude", "pending"),
    ("2026-05-08", "Fri Day 1", "Hackathon Day 1", "Watch 9am ET kickoff + 10am ET walkthrough. Add Characters + Act-Two integrations. Multi-shot orchestration online. First full pipeline test by 5pm ET.", "Claude + Roger", "pending"),
    ("2026-05-09", "Sat Day 2", "Fill-in + judge loop", "LLM-as-judge regen loop. Aleph color pass. Multilingual VO. Per-platform crops.", "Claude + Roger", "pending"),
    ("2026-05-10", "Sun Day 3", "Polish + demo", "25-case edge battery. Record canonical 3-min demo video. README v2. Public deploy.", "Claude + Roger", "pending"),
    ("2026-05-11", "Mon Submit", "Submit by 9am ET", "Final smoke test. Submit. Cross-post on X tagging @runwayml @c_valenzuelab @yining_shi. DM Yining with clip.", "Roger", "pending"),
]
for r, row in enumerate(plan, start=2):
    for c, val in enumerate(row, start=1):
        cell = ws5.cell(row=r, column=c, value=val)
        body(cell)
        if c == 6:
            if val == "in progress":
                cell.fill = green_fill
            elif val == "blocked":
                cell.fill = red_fill
        if r == 8:  # submission row highlight
            cell.fill = orange_fill
            cell.font = Font(name="Arial", size=10, bold=True, color=WHITE)
    ws5.row_dimensions[r].height = 50
ws5.freeze_panes = "A2"

# ============== Sheet 6: Risk Register ==============
ws6 = wb.create_sheet("Risk Register")
cols6 = ["Risk", "Severity", "Probability", "Score (auto)", "Mitigation"]
widths6 = [50, 14, 14, 14, 70]
for i, (c, w) in enumerate(zip(cols6, widths6), 1):
    cell = ws6.cell(row=1, column=i, value=c)
    header(cell)
    ws6.column_dimensions[get_column_letter(i)].width = w
ws6.row_dimensions[1].height = 32

risks = [
    ("Originality clause (Section 7.3.1) — pre-built code disqualifies submission.", 5, 4, "HARD RULE on Wed/Thu prep: NO submission code, NO submission API calls. Allowable prep: docs, interviews, architecture, env setup, README outline, brand. Any code or API output that ends up in the submission must be created May 8-11."),
    ("Roger's registration email did not match his Runway dev account.", 5, 4, "RESOLVED May 5: originally submitted with roger@grubb.net; actual dev account is rogergrubbrealestate@gmail.com. Re-submitted with correct email; cleanup email to events@runwayml.com sent. Live registration is on the gmail.com account."),
    ("Registration deadline (Thu May 7, 5pm ET).", 5, 3, "RESOLVED May 5: registered with rogergrubbrealestate@gmail.com. Confirmation email expected. Escalate via events@runwayml.com if not received by Wed EOD."),
    ("Characters / Act-Two API instability — both shipped <90 days ago.", 4, 3, "Gen-4.5 fallback path for any shot type. Characters becomes a wow-feature, not critical-path."),
    ("Content moderation cascades to account suspension.", 5, 2, "Pre-filter inputs client-side. Avoid public figures and recognizable artists. Test friendly first."),
    ("Credits depleted before submission.", 4, 3, "Real-time Supabase counter. Hard cap at 80% (160K) until Sunday afternoon. $50 reserve buy if needed."),
    ("API Project must be publicly viewable/usable at submission.", 3, 3, "Deploy to public URL with anonymous access OR include guest credentials in README. Slack OAuth must work for fresh installs."),
    ("Cannot edit submission after submit (Rule 6).", 4, 2, "Submit at LATEST safe moment Monday morning after final 90-min smoke test. Kill-switch if public URL broken."),
    ("LinkedIn URL on registration form points to wrong profile.", 2, 1, "Already filled with linkedin.com/in/rogergrubb-sf/. Confirm before clicking Register."),
    ("Slack OAuth approval delays prod readiness.", 3, 3, "Use Slack workspace we control for the demo. Showcase OAuth in demo video frame, not live."),
    ("Multiple teams build the same pattern.", 3, 4, "Differentiate via Characters narrator + Act-Two performance + LLM-as-judge regen loop."),
]
for r, (risk, sev, prob, mit) in enumerate(risks, start=2):
    body(ws6.cell(row=r, column=1, value=risk))
    body(ws6.cell(row=r, column=2, value=sev))
    body(ws6.cell(row=r, column=3, value=prob))
    score_cell = ws6.cell(row=r, column=4, value=f"=B{r}*C{r}")
    body(score_cell, bold=True)
    if sev * prob >= 15:
        score_cell.fill = red_fill
    elif sev * prob >= 9:
        score_cell.fill = PatternFill("solid", fgColor="FBE2C0")
    else:
        score_cell.fill = green_fill
    body(ws6.cell(row=r, column=5, value=mit))
    ws6.row_dimensions[r].height = 38
ws6.freeze_panes = "A2"

# Move main sheet to front
wb.active = 0

wb.save("battle_plan_database.xlsx")
print("OK")
