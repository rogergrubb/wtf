const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, Header, Footer,
  AlignmentType, PageOrientation, LevelFormat, ExternalHyperlink, HeadingLevel,
  BorderStyle, WidthType, ShadingType, PageNumber, PageBreak, TabStopType, TabStopPosition } = require('docx');
const fs = require('fs');

const ARIAL = "Arial";
const NAVY = "1F2A4A";
const ORANGE = "C45A2E";
const GREY = "555555";
const LIGHTBG = "F2EEE8";
const GREEN = "2D7A3F";

const cellBorder = { style: BorderStyle.SINGLE, size: 4, color: "AAAAAA" };
const cellBorders = { top: cellBorder, bottom: cellBorder, left: cellBorder, right: cellBorder };

function H1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 360, after: 200 },
    children: [new TextRun({ text, bold: true, color: NAVY, size: 36, font: ARIAL })],
  });
}
function H2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 280, after: 140 },
    children: [new TextRun({ text, bold: true, color: NAVY, size: 28, font: ARIAL })],
  });
}
function H3(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_3,
    spacing: { before: 200, after: 100 },
    children: [new TextRun({ text, bold: true, color: ORANGE, size: 24, font: ARIAL })],
  });
}
function P(text, opts = {}) {
  return new Paragraph({
    spacing: { after: 140 },
    alignment: opts.align || AlignmentType.LEFT,
    children: [new TextRun({ text, font: ARIAL, size: 22, ...opts })],
  });
}
function PRuns(runs, opts = {}) {
  return new Paragraph({
    spacing: { after: 140 },
    children: runs.map(r => r instanceof TextRun || r instanceof ExternalHyperlink ? r :
      new TextRun({ font: ARIAL, size: 22, ...r })),
    ...opts,
  });
}
function Bullet(text, opts = {}) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { after: 80 },
    children: [new TextRun({ text, font: ARIAL, size: 22, ...opts })],
  });
}
function BulletRuns(runs) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { after: 80 },
    children: runs.map(r => new TextRun({ font: ARIAL, size: 22, ...r })),
  });
}
function Numbered(text, ref = "numbers") {
  return new Paragraph({
    numbering: { reference: ref, level: 0 },
    spacing: { after: 80 },
    children: [new TextRun({ text, font: ARIAL, size: 22 })],
  });
}
function Pull(text) {
  return new Paragraph({
    spacing: { before: 200, after: 200 },
    indent: { left: 360, right: 360 },
    border: { left: { style: BorderStyle.SINGLE, size: 18, color: ORANGE, space: 8 } },
    children: [new TextRun({ text, font: ARIAL, size: 24, italics: true, color: NAVY })],
  });
}

function cell(text, opts = {}) {
  return new TableCell({
    borders: cellBorders,
    width: { size: opts.width || 2340, type: WidthType.DXA },
    shading: opts.fill ? { fill: opts.fill, type: ShadingType.CLEAR } : undefined,
    margins: { top: 80, bottom: 80, left: 120, right: 120 },
    children: [new Paragraph({ children: [new TextRun({ text, font: ARIAL, size: 20, bold: !!opts.bold, color: opts.color || "000000" })] })],
  });
}
function table(rows, columnWidths) {
  return new Table({
    width: { size: columnWidths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    columnWidths,
    rows,
  });
}

const children = [];

// COVER
children.push(new Paragraph({
  spacing: { before: 1200, after: 80 },
  alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: "RUNWAY API HACKATHON", bold: true, color: NAVY, size: 56, font: ARIAL })],
}));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 80 },
  children: [new TextRun({ text: "BATTLE PLAN", bold: true, color: ORANGE, size: 56, font: ARIAL })],
}));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 600 },
  children: [new TextRun({ text: "May 8–11, 2026  •  Virtual  •  Powered by Modal", color: GREY, size: 24, font: ARIAL, italics: true })],
}));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 1200 },
  children: [new TextRun({ text: "Number One Son Software Development", bold: true, color: NAVY, size: 28, font: ARIAL })],
}));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 80 },
  children: [new TextRun({ text: "Prepared for: Roger (Founder)", font: ARIAL, size: 22, color: GREY })],
}));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 80 },
  children: [new TextRun({ text: "Prepared by: Claude (Co-founder)", font: ARIAL, size: 22, color: GREY })],
}));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 80 },
  children: [new TextRun({ text: "Date: May 5, 2026  (T-3 days)", font: ARIAL, size: 22, color: GREY })],
}));
children.push(new Paragraph({ children: [new PageBreak()] }));

// EXEC SUMMARY
children.push(H1("Executive Summary"));
children.push(Pull("This is not a $25K hackathon. This is a $1B-trajectory accelerant disguised as a hackathon. We will build accordingly."));

children.push(P("Runway is hosting their FIRST online API Hackathon on May 8–11, 2026. Three days. Four ranked judging criteria. $25K cash, 200K API credits, and a feature on Runway's channels for first place. The submission window is Monday May 11, 9:00am ET. Winners announced Friday May 15."));

children.push(P("Our intel pass identified the asymmetric prize that the marketing copy obscures: the winning team gets a direct line to Runway's senior engineering and applications leadership, a documented public win on Runway's owned channels, and 200,000 API credits — roughly six months of paid runway for whatever Number One Son product line we ship next. The $25K is taxable income. Everything else is leverage."));

children.push(H2("The hard call"));
children.push(P("Building yet another text-to-video demo loses. Building a real product that solves a problem creators or producers actually pay to fix — and that uses Runway's newest, most-novelty-weighted models (Characters / GWM-1 launched March 9, 2026; Act-Two launched February 2026) — wins. Judges will reward systems that chain creative decisions, not single API calls."));

children.push(H2("The recommendation"));
children.push(BulletRuns([{ text: "Build candidate: ", bold: true }, { text: "DirectorOS — an agentic video director that turns a single creator brief into a publish-ready, multi-shot, multilingual video, with creator-in-the-loop checkpoints, character consistency across scenes, and a real Slack/web entry point. Heavy use of Characters (GWM-1) + Act-Two + Gen-4.5 + ElevenLabs, orchestrated on Modal." }]));
children.push(BulletRuns([{ text: "Why it wins: ", bold: true }, { text: "Maxes all four judging axes (Creativity, Technical Depth, Impact, Polish), aligns with every keyword Runway leadership repeats publicly (\"simulation,\" \"real-time,\" \"interactive,\" \"controllable,\" \"creative control,\" \"cinematic\"), and sits on the white-space gap that adjacent hackathon analysis flagged." }]));
children.push(BulletRuns([{ text: "Why it matters past hackathon: ", bold: true }, { text: "DirectorOS becomes Number One Son product line #1 — a solopreneur creator-stack play that 10x's content output for a single founder. Aligns with the $1B-valuation solo thesis." }]));

children.push(P(" "));
children.push(new Paragraph({ children: [new PageBreak()] }));

// THE OPPORTUNITY
children.push(H1("1. The Opportunity (Beyond the $25K)"));

children.push(H2("What is officially being judged"));
children.push(P("Runway publishes four criteria. We don't have public weights, but the order matters and the rubric is unusually clear:"));
const judgeRows = [
  new TableRow({ children: [
    cell("Criterion", { bold: true, fill: NAVY, color: "FFFFFF", width: 1900 }),
    cell("What Runway literally says", { bold: true, fill: NAVY, color: "FFFFFF", width: 4200 }),
    cell("How we win this axis", { bold: true, fill: NAVY, color: "FFFFFF", width: 3260 }),
  ]}),
  new TableRow({ children: [
    cell("Creativity", { bold: true, width: 1900, fill: LIGHTBG }),
    cell("Does your project solve a real problem or explore an interesting use case?", { width: 4200 }),
    cell("Lead the README and demo with a named pain (creator name, time wasted, dollars lost). No abstract \"imagine if\" framing.", { width: 3260 }),
  ]}),
  new TableRow({ children: [
    cell("Technical depth", { bold: true, width: 1900, fill: LIGHTBG }),
    cell("How well does the project leverage Runway's API? Does it go beyond basic usage?", { width: 4200 }),
    cell("Chain three or more Runway models in one pipeline. Show feedback loops. Use Characters or Act-Two — both shipped this quarter.", { width: 3260 }),
  ]}),
  new TableRow({ children: [
    cell("Impact", { bold: true, width: 1900, fill: LIGHTBG }),
    cell("Could this project be used by real users or customers? Could it become a real product?", { width: 4200 }),
    cell("Ship a deployed URL or installable Slack app. Include a one-slide GTM with TAM and pricing in the README.", { width: 3260 }),
  ]}),
  new TableRow({ children: [
    cell("Polish", { bold: true, width: 1900, fill: LIGHTBG }),
    cell("Is your project a working demo, not just a concept? Does it feel like an end-to-end experience?", { width: 4200 }),
    cell("Pre-record demo video as the canonical artifact. Live demo only as backup. Test 20+ edge cases before Monday 9am ET.", { width: 3260 }),
  ]}),
];
children.push(table(judgeRows, [1900, 4200, 3260]));

children.push(H2("What is unofficially being judged (read between lines)"));
children.push(P("Runway leadership repeats specific words across their about page, research blog, and Cris Valenzuela's public statements. These are the affinity hooks. Use them in the README, demo VO, and pitch:"));
children.push(BulletRuns([{ text: "Simulation", bold: true }, { text: " — they don't position Runway as a video generator; they position it as a world-simulation engine. Frame what we build accordingly." }]));
children.push(BulletRuns([{ text: "Real-time / interactive", bold: true }, { text: " — batch is fine, but real-time is rewarded. If our pipeline can render a preview frame before the model finishes, show that." }]));
children.push(BulletRuns([{ text: "Controllable / creative control", bold: true }, { text: " — judges want creator agency, not autopilot generation. Build in obvious knobs, not just text prompts." }]));
children.push(BulletRuns([{ text: "Cinematic", bold: true }, { text: " — visual quality bar is professional, not novelty. Color-grade outputs. No flat lighting." }]));
children.push(BulletRuns([{ text: "Multimodal", bold: true }, { text: " — chain video + audio + text + reference image. Single-modality demos lose." }]));

children.push(H2("The asymmetric prize"));
children.push(P("First place is officially $25K + 200K credits + Runway channels feature. The undocumented prizes the team that wins gets:"));
children.push(Bullet("Direct introduction to Runway's senior engineering and applications team — Yining Shi (Senior Director of Applications) leads the developer ecosystem and personally ran the Characters Hackathon."));
children.push(Bullet("Distribution: a feature post on a YC-darling AI company's owned channels reaches the exact audience we want for any creator-stack product."));
children.push(Bullet("Permission-to-claim: \"Runway-recognized\" sits on every NumberOneSon.com page, every pitch deck, every cold email forever."));
children.push(Bullet("200K credits = approximately 1,667 full Gen-4.5 10-second videos = six months of free runway for a creator-tool product line."));
children.push(Bullet("Optionality on partnership conversations. Runway has invested in and partnered with hackathon-track talent before."));

children.push(new Paragraph({ children: [new PageBreak()] }));

// THE FIVE CANDIDATES
children.push(H1("2. The Five Build Candidates"));
children.push(P("Four parallel research agents surveyed past Runway competitions (Gen:48, AIFF, Characters Hackathon), adjacent hackathon winners (Modal, OpenAI Open Model, Microsoft AI Agents, HuggingFace Agents-MCP), and the Runway API capability map. Five candidates emerged. Scored against our four-axis rubric below."));

const candRows = [
  new TableRow({ children: [
    cell("#", { bold: true, fill: NAVY, color: "FFFFFF", width: 600 }),
    cell("Candidate", { bold: true, fill: NAVY, color: "FFFFFF", width: 2400 }),
    cell("One-line", { bold: true, fill: NAVY, color: "FFFFFF", width: 3800 }),
    cell("Win prob.", { bold: true, fill: NAVY, color: "FFFFFF", width: 1200 }),
    cell("NOS fit", { bold: true, fill: NAVY, color: "FFFFFF", width: 1360 }),
  ]}),
  new TableRow({ children: [
    cell("1", { bold: true, width: 600, fill: ORANGE, color: "FFFFFF" }),
    cell("DirectorOS (recommended)", { bold: true, width: 2400, fill: LIGHTBG }),
    cell("One creator brief in → multi-shot, character-consistent, multilingual, publish-ready video out. Slack-native.", { width: 3800 }),
    cell("HIGH", { bold: true, width: 1200, fill: LIGHTBG, color: NAVY }),
    cell("Anchor product", { bold: true, width: 1360, fill: LIGHTBG, color: NAVY }),
  ]}),
  new TableRow({ children: [
    cell("2", { bold: true, width: 600 }),
    cell("InteractiveFlow", { bold: true, width: 2400 }),
    cell("Live audience-voted narrative co-creation for Twitch/YouTube streamers, powered by Characters API.", { width: 3800 }),
    cell("HIGH", { width: 1200 }),
    cell("Niche", { width: 1360 }),
  ]}),
  new TableRow({ children: [
    cell("3", { bold: true, width: 600 }),
    cell("PerformanceAI", { bold: true, width: 2400 }),
    cell("Minimal-rig (webcam) → full character performance video via Act-Two. Indie creator concert / dance / acting tool.", { width: 3800 }),
    cell("MEDIUM-HIGH", { width: 1200 }),
    cell("Niche", { width: 1360 }),
  ]}),
  new TableRow({ children: [
    cell("4", { bold: true, width: 600 }),
    cell("NewsFlow", { bold: true, width: 2400 }),
    cell("Live data feed → branded 90-second explainer video in <60s, multi-platform output, multilingual.", { width: 3800 }),
    cell("MEDIUM", { width: 1200 }),
    cell("Strong but B2B", { width: 1360 }),
  ]}),
  new TableRow({ children: [
    cell("5", { bold: true, width: 600 }),
    cell("EditBot", { bold: true, width: 2400 }),
    cell("Raw footage + director notes → cut, color-graded, sound-designed deliverable. Pro post-production agent.", { width: 3800 }),
    cell("MEDIUM", { width: 1200 }),
    cell("B2B/Pro", { width: 1360 }),
  ]}),
];
children.push(table(candRows, [600, 2400, 3800, 1200, 1360]));

children.push(P(" "));
children.push(P("Detailed scorecard with per-axis ratings, credit budgets, and risk profiles in the companion Excel file (battle_plan_database.xlsx, sheet \"Build Scorecard\")."));

children.push(new Paragraph({ children: [new PageBreak()] }));

// RECOMMENDED BUILD
children.push(H1("3. Recommended Build: DirectorOS"));

children.push(Pull("One brief in. One Slack DM out. One publish-ready video back. The agent handles the 47 decisions in between."));

children.push(H2("The pain we're solving"));
children.push(P("Solo creators and small marketing teams want to ship 5–10 videos per week. The bottleneck is not generation quality — Runway already nailed that. The bottleneck is orchestration: scripting the brief, breaking it into shots, keeping characters consistent across shots, layering audio, formatting per platform, and making revision cycles fast. Today that loop costs 4–20 hours per video. We collapse it to 4–10 minutes."));

children.push(H2("The 90-second user experience"));
children.push(Numbered("Creator types in Slack: /director Show how my new dashboard filters by date range. Two-shot, indie aesthetic, 60 seconds, English + Spanish."));
children.push(Numbered("Within ~10 seconds: Claude (orchestrator) parses → shot list, dialogue, music brief, character spec."));
children.push(Numbered("Parallel calls fire: Gen-4.5 for B-roll shots, Characters (GWM-1) for the avatar narrator, Act-Two if a creator-recorded performance is referenced, gen4_image for any reference frames, ElevenLabs for VO in EN + ES, Suno-style track for music bed."));
children.push(Numbered("In-flight quality gate: each shot is scored for prompt adherence (LLM-as-judge); shots below threshold auto-regenerate with refined prompts."));
children.push(Numbered("Assembly + light Aleph color pass for cinematic consistency."));
children.push(Numbered("Slack thread reply with three things: the final video, a per-platform crop bundle (TikTok 9:16, YouTube 16:9, IG square), and three one-tap revision buttons (\"slower pacing\", \"warmer color\", \"different VO take\")."));

children.push(H2("Why it scores on every axis"));
const scoreRows = [
  new TableRow({ children: [
    cell("Axis", { bold: true, fill: NAVY, color: "FFFFFF", width: 1900 }),
    cell("How DirectorOS wins it", { bold: true, fill: NAVY, color: "FFFFFF", width: 7460 }),
  ]}),
  new TableRow({ children: [
    cell("Creativity", { bold: true, width: 1900, fill: LIGHTBG }),
    cell("Real, named pain (\"Marketing teams spend 4–20 hours per video; we cut it to 4 minutes.\") with TAM math (~100K small/mid SaaS = ~$1B addressable). User interviews with 5+ creators completed pre-hackathon.", { width: 7460 }),
  ]}),
  new TableRow({ children: [
    cell("Technical depth", { bold: true, width: 1900, fill: LIGHTBG }),
    cell("Six API surfaces in one orchestrated pipeline (Gen-4.5, Characters/GWM-1, Act-Two, Aleph, gen4_image, ElevenLabs); LLM-as-judge regeneration loop; async polling with exponential backoff; deployed on Modal serverless GPU; webhooks via Svix.", { width: 7460 }),
  ]}),
  new TableRow({ children: [
    cell("Impact", { bold: true, width: 1900, fill: LIGHTBG }),
    cell("Slack-native means zero context switching for users. Deployed at director.numberonesonsoftware.com with public OAuth. README includes one-slide GTM: $49/mo solo, $199/mo team, est. 12-month path to $250K ARR.", { width: 7460 }),
  ]}),
  new TableRow({ children: [
    cell("Polish", { bold: true, width: 1900, fill: LIGHTBG }),
    cell("Pre-recorded 3-min demo video as canonical artifact. Tested across 25 edge cases before submission. Graceful degradation when any single API fails. README has copy-paste-ready setup; judges can trial it from a fresh laptop in <90 seconds.", { width: 7460 }),
  ]}),
];
children.push(table(scoreRows, [1900, 7460]));

children.push(H2("Why it scores on every leadership-language axis"));
children.push(BulletRuns([{ text: "Simulation: ", bold: true }, { text: "Characters/GWM-1 generates the narrator avatar — a literal world-model use." }]));
children.push(BulletRuns([{ text: "Real-time: ", bold: true }, { text: "Slack streams progress per-shot; first preview lands in <30 seconds." }]));
children.push(BulletRuns([{ text: "Controllable: ", bold: true }, { text: "Creator dictates aesthetic, pacing, language, characters; revision buttons make control explicit." }]));
children.push(BulletRuns([{ text: "Cinematic: ", bold: true }, { text: "Aleph color pass + reference-image-anchored characters keep visual quality production-grade." }]));
children.push(BulletRuns([{ text: "Multimodal: ", bold: true }, { text: "Text in → video + audio + multilingual VO out. Zero single-modality steps." }]));

children.push(H2("Architecture (one diagram-equivalent paragraph)"));
children.push(P("Slack slash command → Modal HTTP endpoint → Claude orchestrator (parse brief, build shot list, allocate models per shot) → fanout to Runway endpoints (Gen-4.5 for B-roll, Characters for avatar, Act-Two for performance shots, gen4_image for refs, ElevenLabs for VO) → results to Modal queue → LLM-as-judge scoring per shot → per-shot regeneration if score < 0.7 → ffmpeg assembly on Modal → Aleph color pass → multi-format export → Slack thread reply with deliverables. Persistent character embeddings stored in Supabase (we already have nag-platform infra; reuse the project)."));

children.push(new Paragraph({ children: [new PageBreak()] }));

// THE PLAN
children.push(H1("4. Seven-Day Plan (T-3 → T+0)"));
children.push(Pull("CRITICAL: Section 7.3.1 of the official rules: the API Project \"was made in its entirety during the Challenge Participation Period\" (May 8 9:00am ET → May 11 9:00am ET). Pre-writing submission code or pre-running submission API calls disqualifies us."));
children.push(P("Today is May 5. Submission lock is Monday May 11, 9:00am ET. The unfair advantage we still have: research, user interviews, architecture sketches, dev-environment setup, README scaffolding, brand/logo, and a sharpened mental model are all NOT \"the API Project\" — they are allowable prep. The build itself is hard-locked to 72 hours."));
children.push(P("What the prep window can include: read docs, install SDKs, get API keys provisioned, set up Modal account, design wireframes, conduct user interviews, write an outline of the README, sketch the architecture, prepare a brand identity. What it CANNOT include: the actual code or any API call output that ends up in the submission. When in doubt, assume Runway interprets the rule strictly — Sponsor's sole discretion."));

const planRows = [
  new TableRow({ children: [
    cell("Day", { bold: true, fill: NAVY, color: "FFFFFF", width: 1500 }),
    cell("Theme", { bold: true, fill: NAVY, color: "FFFFFF", width: 2500 }),
    cell("Outputs by EOD", { bold: true, fill: NAVY, color: "FFFFFF", width: 5360 }),
  ]}),
  new TableRow({ children: [
    cell("Tue May 5 (today)", { bold: true, width: 1500, fill: LIGHTBG }),
    cell("Decide & confirm (research-only)", { bold: true, width: 2500, fill: LIGHTBG }),
    cell("Roger picks DirectorOS or alternate. Runway dev account CONFIRMED on rogergrubbrealestate@gmail.com (NOT roger@grubb.net — caught the mismatch, re-submitted registration, emailed events@runwayml.com to drop the duplicate). Discord joined. GitHub org created (empty repo). Supabase table SCHEMA designed but NOT provisioned. No code written.", { width: 5360 }),
  ]}),
  new TableRow({ children: [
    cell("Wed May 6", { bold: true, width: 1500, fill: LIGHTBG }),
    cell("Research + interviews (no code)", { bold: true, width: 2500, fill: LIGHTBG }),
    cell("Read full Runway API docs. Read Runway Skills repo README. Read Modal docs. Five user interviews with named creators (cold DM via Twitter / Indie Hackers / r/contentcreation). Architecture diagram in Excalidraw. README outline (not code). Brand identity / domain decision.", { width: 5360 }),
  ]}),
  new TableRow({ children: [
    cell("Thu May 7", { bold: true, width: 1500, fill: LIGHTBG }),
    cell("Env setup + spec freeze", { bold: true, width: 2500, fill: LIGHTBG }),
    cell("Registration deadline 5pm ET — confirm enrolled. Install SDKs locally (npm @runwayml/sdk, pip runway-python). Set environment variables. Modal account ready. Slack workspace prepared. PRD/spec frozen. NO API calls. NO submission code.", { width: 5360 }),
  ]}),
  new TableRow({ children: [
    cell("Fri May 8", { bold: true, width: 1500, fill: LIGHTBG }),
    cell("Hackathon Day 1", { bold: true, width: 2500, fill: LIGHTBG }),
    cell("Watch 9am ET kickoff and 10am ET technical walkthrough live (capture any Day-0 announcements; Runway often drops a new endpoint at kickoff). Add Characters and Act-Two integrations. Multi-shot orchestration online. First full pipeline test by 5pm ET.", { width: 5360 }),
  ]}),
  new TableRow({ children: [
    cell("Sat May 9", { bold: true, width: 1500, fill: LIGHTBG }),
    cell("Fill-in + judge loop", { bold: true, width: 2500, fill: LIGHTBG }),
    cell("LLM-as-judge regeneration loop. Aleph color pass. Multilingual VO via ElevenLabs. Per-platform crops (TikTok / YT / IG). Public-ready Slack OAuth flow.", { width: 5360 }),
  ]}),
  new TableRow({ children: [
    cell("Sun May 10", { bold: true, width: 1500, fill: LIGHTBG }),
    cell("Polish + demo", { bold: true, width: 2500, fill: LIGHTBG }),
    cell("Edge-case bash (25 case sheet). Record 3-minute canonical demo video (script, screen-capture, VO, music). README v2 final. Backup live demo prepared. Deploy to public URL with prod credentials.", { width: 5360 }),
  ]}),
  new TableRow({ children: [
    cell("Mon May 11", { bold: true, width: 1500, fill: ORANGE, color: "FFFFFF" }),
    cell("Submit by 9am ET", { bold: true, width: 2500, fill: ORANGE, color: "FFFFFF" }),
    cell("Final smoke test 5am–7am. Submit to Runway portal. Cross-post on X tagging @runwayml @c_valenzuelab @yining_shi (visibility helps tiebreaker). Direct DM to Yining Shi with a 10-second clip.", { width: 5360 }),
  ]}),
];
children.push(table(planRows, [1500, 2500, 5360]));

children.push(new Paragraph({ children: [new PageBreak()] }));

// TECH STACK
children.push(H1("5. Tech Stack & Architecture"));

children.push(H2("API surface"));
children.push(BulletRuns([{ text: "Runway API: ", bold: true }, { text: "Gen-4.5 (12 credits/sec, 5 or 10s clips, native audio); Characters / GWM-1 (real-time avatar — newest model, highest novelty weight); Act-Two (performance capture, novel via API); Aleph (cinematic edit pass); gen4_image (5 credits — reference frames); ElevenLabs via Runway (multilingual TTS, 29 languages, dubbing)." }]));
children.push(BulletRuns([{ text: "Orchestration: ", bold: true }, { text: "Claude (Opus 4.6 for planning, Haiku 4.5 for in-flight scoring)." }]));
children.push(BulletRuns([{ text: "Compute / serverless: ", bold: true }, { text: "Modal (A100 40GB at $2.10/hr base; free Starter tier covers hackathon usage). Modal also runs ffmpeg + post-processing." }]));
children.push(BulletRuns([{ text: "Frontend / entry: ", bold: true }, { text: "Slack app (Bolt JS) as primary; Next.js public landing page + auth dashboard." }]));
children.push(BulletRuns([{ text: "Persistence: ", bold: true }, { text: "Supabase (existing nag-platform project; new table director_runs with RLS). Storing character embeddings, run history, credits used." }]));
children.push(BulletRuns([{ text: "Async: ", bold: true }, { text: "Svix webhooks if available; Modal queues otherwise. Polling at 5s with jitter." }]));
children.push(BulletRuns([{ text: "Skills framework: ", bold: true }, { text: "Clone github.com/runwayml/skills, add three custom skills (DirectorBrief, ShotPlanner, RevisionLoop). Demonstrating skills-framework adoption is judge bait — they shipped this repo two months ago and want to see it used." }]));

children.push(H2("Credit budget (200K cap)"));
const budgetRows = [
  new TableRow({ children: [
    cell("Bucket", { bold: true, fill: NAVY, color: "FFFFFF", width: 3000 }),
    cell("Allocation", { bold: true, fill: NAVY, color: "FFFFFF", width: 1800 }),
    cell("Notes", { bold: true, fill: NAVY, color: "FFFFFF", width: 4560 }),
  ]}),
  new TableRow({ children: [cell("Pre-hack dev (May 6–7)", { width: 3000 }), cell("20,000", { width: 1800 }), cell("50,000 participant credits land at registration. Use 20K of those before kickoff for spikes.", { width: 4560 }) ]}),
  new TableRow({ children: [cell("Hackathon build", { width: 3000 }), cell("80,000", { width: 1800 }), cell("Gen-4.5 main pipeline, Characters tests, Act-Two trials, Aleph passes.", { width: 4560 }) ]}),
  new TableRow({ children: [cell("Demo recording", { width: 3000 }), cell("40,000", { width: 1800 }), cell("Generate the canonical demo video at full quality, 4K upscale, multiple language tracks.", { width: 4560 }) ]}),
  new TableRow({ children: [cell("Edge-case battery", { width: 3000 }), cell("30,000", { width: 1800 }), cell("Blank input, 10K-char input, special chars, non-English, very long, broken refs, etc.", { width: 4560 }) ]}),
  new TableRow({ children: [cell("Reserve / surprise", { width: 3000 }), cell("30,000", { width: 1800 }), cell("Day-of-Friday endpoint announcements, judge-day backup runs, last-minute bugs.", { width: 4560 }) ]}),
  new TableRow({ children: [
    cell("TOTAL", { bold: true, width: 3000, fill: LIGHTBG }),
    cell("200,000", { bold: true, width: 1800, fill: LIGHTBG }),
    cell("≈ $2,000 retail. Track in real time via Supabase counter.", { width: 4560, fill: LIGHTBG }),
  ]}),
];
children.push(table(budgetRows, [3000, 1800, 4560]));

children.push(new Paragraph({ children: [new PageBreak()] }));

// RISKS
children.push(H1("6. Risks & Mitigations"));

const riskRows = [
  new TableRow({ children: [
    cell("Risk", { bold: true, fill: NAVY, color: "FFFFFF", width: 3000 }),
    cell("Severity", { bold: true, fill: NAVY, color: "FFFFFF", width: 1200 }),
    cell("Mitigation", { bold: true, fill: NAVY, color: "FFFFFF", width: 5160 }),
  ]}),
  new TableRow({ children: [cell("Roger's registration email did not match his Runway dev account.", { width: 3000 }), cell("RESOLVED", { bold: true, color: GREEN, width: 1200 }), cell("Originally submitted with roger@grubb.net; actual Runway dev account is rogergrubbrealestate@gmail.com. Re-submitted with correct email; cleanup email to events@runwayml.com sent on May 5 to retire the duplicate. Live registration is on the gmail.com account.", { width: 5160 }) ]}),
  new TableRow({ children: [cell("Characters / Act-Two API instability — both shipped <90 days ago.", { width: 3000 }), cell("MEDIUM", { width: 1200 }), cell("Gen-4.5 fallback path for any shot type that fails on Characters. Characters becomes a wow-feature, not a critical-path dependency.", { width: 5160 }) ]}),
  new TableRow({ children: [cell("Content moderation auto-rejection cascades to account suspension.", { width: 3000 }), cell("MEDIUM", { width: 1200 }), cell("Pre-filter inputs client-side with a banned-terms list. Avoid public figures and recognizable artists in any test prompt. Test with friendly content first.", { width: 5160 }) ]}),
  new TableRow({ children: [cell("Credits depleted before submission.", { width: 3000 }), cell("MEDIUM", { width: 1200 }), cell("Real-time counter in Supabase. Hard cap at 80% (160K) until Sunday afternoon. Buy $50 in reserves Friday morning if needed.", { width: 5160 }) ]}),
  new TableRow({ children: [cell("LinkedIn URL on registration form points to wrong profile.", { width: 3000 }), cell("LOW", { width: 1200 }), cell("Already filled with linkedin.com/in/rogergrubb-sf/. Confirm before clicking Register.", { width: 5160 }) ]}),
  new TableRow({ children: [cell("Slack approval / OAuth process delays prod readiness.", { width: 3000 }), cell("MEDIUM", { width: 1200 }), cell("Use Slack workspace we control for the demo (no public Slack approval needed). Showcase OAuth in a separate frame of the demo video.", { width: 5160 }) ]}),
  new TableRow({ children: [cell("Multiple teams build the same pattern (\"text-to-video Slack bot\").", { width: 3000 }), cell("MEDIUM", { width: 1200 }), cell("Differentiation = Characters narrator + Act-Two performance support + LLM-as-judge regeneration loop. Two of those three are <90 days old; few teams will use them.", { width: 5160 }) ]}),
  new TableRow({ children: [cell("IP / terms surprise in the official rules (e.g., Runway claims rights).", { width: 3000 }), cell("RESOLVED", { bold: true, color: GREEN || "2D7A3F", width: 1200 }), cell("Full rules read May 5. Key findings: 18+ resident, NOT in sanctioned regions, originality clause (must build May 8-11), publicity license to Runway on prize, NY law jurisdiction. All acceptable; nothing blocks Roger.", { width: 5160 }) ]}),
  new TableRow({ children: [cell("Originality clause (7.3.1) — pre-built code disqualifies submission.", { width: 3000 }), cell("HIGH", { bold: true, color: ORANGE, width: 1200 }), cell("Hard rule on Wed/Thu prep: NO submission code, NO submission API calls. Allowable prep: docs, interviews, architecture, env setup, README outline, brand. Any code or API output that ends up in the submission must be created May 8-11.", { width: 5160 }) ]}),
  new TableRow({ children: [cell("API Project must be publicly viewable/usable at submission.", { width: 3000 }), cell("MEDIUM", { width: 1200 }), cell("Deploy to public URL with anonymous access for the demo flow OR include guest credentials in README. Slack OAuth must work for fresh installs.", { width: 5160 }) ]}),
  new TableRow({ children: [cell("Cannot edit submission after submit (rule 6).", { width: 3000 }), cell("MEDIUM", { width: 1200 }), cell("Submit at the LATEST safe moment Monday morning, after a final 90-min smoke test. Have a kill-switch in case of last-minute API outage; abort submit if the public URL is broken.", { width: 5160 }) ]}),
  new TableRow({ children: [cell("Registration deadline (Thu May 7, 5pm ET).", { width: 3000 }), cell("RESOLVED", { bold: true, color: GREEN, width: 1200 }), cell("Registered May 5 with rogergrubbrealestate@gmail.com. Confirmation email expected at that address. If no confirmation by Wed EOD, escalate via events@runwayml.com.", { width: 5160 }) ]}),
];
children.push(table(riskRows, [3000, 1200, 5160]));

children.push(new Paragraph({ children: [new PageBreak()] }));

// POST-HACK
children.push(H1("7. Post-Hackathon: Number One Son Product Line"));

children.push(Pull("Number One Son's $1B-valuation solo thesis lives or dies on shipping anchor products. DirectorOS is anchor product #1."));

children.push(H2("If we win"));
children.push(P("$25K cash funds the next two months of paid Runway, Modal, Supabase, and ElevenLabs at scale, plus a domain, landing page, and three rounds of cold outreach. The Runway feature on owned channels triggers inbound. We take ~30 days to convert the prototype to a billable v1 (Stripe + usage metering + per-platform integrations beyond Slack: Discord, browser extension, REST API). Targeting $10K MRR by August 1, $50K MRR by EOY 2026, both on autopilot infra."));

children.push(H2("If we place 2nd or 3rd"));
children.push(P("200K credits = six months of free underlying compute. Same product roadmap, slower customer acquisition. Need to land 5 paying customers in May to hit $10K MRR by August. Achievable with the Runway-recognized credibility + targeted outbound."));

children.push(H2("If we don't place"));
children.push(P("We still have a working v1 of an anchor product, 50K participant credits, validated user interviews, and a documented submission for our build-in-public Number One Son log. We ship DirectorOS publicly within 30 days. The hackathon paid for itself in opportunity-cost-discounted dev hours regardless of outcome."));

children.push(H2("Roger's preference loop"));
children.push(P("Per the founder preferences on file, every meaningful decision and outcome from this build feeds back into the lessons-learned database. Today's lesson: \"First major external competition entry. Goal: win or learn enough to win the next one. Hypothesis: deep prep on T-3 beats raw build hours during the event.\" Verifiable Friday May 15 when winners are announced."));

children.push(new Paragraph({ children: [new PageBreak()] }));

// APPENDIX
children.push(H1("Appendix: Sources"));
children.push(P("Primary materials, all retrieved May 5, 2026:"));

const linkP = (label, url) => new Paragraph({
  numbering: { reference: "bullets", level: 0 },
  spacing: { after: 60 },
  children: [
    new TextRun({ text: label + " — ", font: ARIAL, size: 22 }),
    new ExternalHyperlink({
      children: [new TextRun({ text: url, font: ARIAL, size: 22, style: "Hyperlink" })],
      link: url,
    }),
  ],
});

children.push(linkP("Runway API Hackathon (official)", "https://runwayml.com/api-hackathon"));
children.push(linkP("Runway API Hackathon Terms (official)", "https://runwayml.com/api-hackathon-terms"));
children.push(linkP("Runway Developer Portal", "https://dev.runwayml.com/"));
children.push(linkP("Runway API docs", "https://docs.dev.runwayml.com/"));
children.push(linkP("Runway Skills (open-source agent skills)", "https://github.com/runwayml/skills"));
children.push(linkP("Modal (hackathon infrastructure partner)", "https://modal.com"));
children.push(linkP("Runway research: Introducing GWM-1", "https://runwayml.com/research/introducing-runway-gwm-1"));
children.push(linkP("Runway research: Introducing Gen-4.5", "https://runwayml.com/research/introducing-runway-gen-4-5"));
children.push(linkP("Runway news: Introducing Runway Characters", "https://runwayml.com/news/introducing-runway-characters"));
children.push(linkP("AI Film Festival (AIFF)", "https://aiff.runwayml.com/"));
children.push(linkP("Gen:48 Official Rules", "https://runwayml.com/gen48/terms"));
children.push(linkP("Cris Valenzuela on AI Video as Prequel to World Models (TechCrunch Equity)", "https://techcrunch.com/podcast/equity-podcast-runway-ceo-cristobal-valenzuela-ai-video-world-models/"));
children.push(linkP("Microsoft AI Agents Hackathon 2025 winners (adjacent pattern)", "https://microsoft.github.io/AI_Agents_Hackathon/winners/"));
children.push(linkP("HuggingFace Agents-MCP Hackathon: Immersia winner write-up", "https://huggingface.co/blog/kikikita/immersia-ai-games"));
children.push(linkP("Modal blog: Runway Characters real-time inference", "https://modal.com/blog/runway-chooses-modal-to-power-real-time-inference-for-runway-characters"));

children.push(P(" "));
children.push(P("Companion files in this folder:"));
children.push(Bullet("battle_plan_database.xlsx — past winners + adjacent hackathon patterns + build scorecard + credit budget."));
children.push(Bullet("RUNWAY_HACKATHON_CAPABILITY_MAP.md — full Runway API + Modal capability map (research output)."));
children.push(Bullet("hackathon_strategic_brief.md — first-pass strategic brief (research output)."));
children.push(Bullet("runway_leadership_values_report.md — leadership-language analysis (research output)."));
children.push(Bullet("Runway_Hackathon_Research_Report.md — SOTA + adjacent hackathon patterns (research output)."));

const doc = new Document({
  creator: "Claude (Co-founder, Number One Son Software Development)",
  title: "Runway API Hackathon — Battle Plan",
  description: "Strategic plan for Number One Son's entry to the May 8-11, 2026 Runway API Hackathon.",
  styles: {
    default: { document: { run: { font: ARIAL, size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 36, bold: true, font: ARIAL, color: NAVY },
        paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: ARIAL, color: NAVY },
        paragraph: { spacing: { before: 280, after: 140 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, font: ARIAL, color: ORANGE },
        paragraph: { spacing: { before: 200, after: 100 }, outlineLevel: 2 } },
    ],
  },
  numbering: {
    config: [
      { reference: "bullets",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
      { reference: "numbers",
        levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
    ],
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
      },
    },
    headers: {
      default: new Header({ children: [new Paragraph({
        alignment: AlignmentType.RIGHT,
        children: [new TextRun({ text: "Number One Son  •  Runway API Hackathon Battle Plan", font: ARIAL, size: 18, color: GREY })],
      })]}),
    },
    footers: {
      default: new Footer({ children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({ text: "Page ", font: ARIAL, size: 18, color: GREY }),
          new TextRun({ children: [PageNumber.CURRENT], font: ARIAL, size: 18, color: GREY }),
        ],
      })]}),
    },
    children,
  }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync("Runway_Hackathon_Battle_Plan.docx", buf);
  console.log("OK");
});
  console.log("OK");
});
        ],
      })]}),
    },
    children,
  }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync("Runway_Hackathon_Battle_Plan.docx", buf);
  console.log("OK");
});
