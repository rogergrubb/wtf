# ChatGPT Deep-Dive Research — Raw Response (May 8, 2026)

**Source:** ChatGPT (GPT model, accessed via Claude side-panel browsing tool)
**Mastermind prompt:** "I need a deep dive research using GPT to find the best prompts to generate cinematic videos from the major video generation apps in 2026 two time of video generation used GPT I want to you you I want to use you as the backbone and I want to use GPT as the prompt generator Let's do this homework using GPT so go ahead and prompt GPT to get cinematic prompts"

**Why this matters:** Gabe Michael won Runway's Gen:48 Best Art Direction award TWICE and publicly documents using ChatGPT in his prompt-engineering workflow. This is the same intelligence channel the winner used.

---

## ChatGPT's executive summary

The strongest prompts in 2026 behave like a compact director's brief: shot type, camera movement, subject action, environment, lighting logic, style, timing, and sound. The pattern across OpenAI, Google DeepMind, Google Cloud, and Runway official guidance is consistent.

**Best 2026 formula:**
> [Shot / camera] + [subject] + [visible action] + [environment] + [lighting / palette] + [motion timing] + [sound / dialogue] + [output constraints]

**The key 2026 shift:** prompt motion, not just image quality. Static image prompts describe what something looks like. Video prompts must describe what changes over time.

---

## Per-model best practices ChatGPT surfaced

**Sora 2 / Sora 2 Pro:**
- API parameters (model, size, duration, character refs) MUST be set as parameters, not requested in prose
- Supports character references, 1080p in Pro, clips up to 20 seconds, video extension, batch generation
- Best style: structured blocks, precise physical beats, detailed lighting, restrained motion

**Veo 3 / Veo 3.1:**
- 720p or 1080p, 16:9 or 9:16, 4/6/8-second clips
- Rich audio + dialogue, reference-based consistency, first-and-last-frame transitions, SynthID watermarking
- Best style: full-scene description with audio and dialogue included
- Five-part formula: cinematography + subject + action + context + style/ambiance

**Runway Gen-4 / Gen-4.5 (THE ONE WE'RE USING):**
- Start simple, use a high-quality input image, describe motion, avoid negative prompting
- Refer to subjects in general terms ("the subject")
- Both image AND text prompt are part of the prompt — restating the image in high detail REDUCES motion quality
- Best style: SHORT, motion-first, positive phrasing
- Runway's recommendation: positive phrasing like "locked camera" instead of "no camera movement"

---

## Critical patterns ChatGPT identified

**Pattern: One Shot, One Action, One Camera Move** — model does not need to solve five different scenes simultaneously.

**Pattern: Beginning-Middle-End in One Clip** — even simple everyday objects become compelling with clear three-act structure within a single 8-second clip.

**Pattern: Cinematic Contrast** — visual hierarchy via still subject + moving environment + hard light + dark background.

**Pattern: Environmental Motion** — "Environmental motion is SAFER than complex human motion. Wind, rain, smoke, fog, dust, reflections, and light movement usually generate better cinematic results."

**Pattern: Reference-Ready Prompt** — when feeding image into image-to-video: focus only on what should MOVE, do not restate the image. "Animate the provided image as a single cinematic shot. The subject slowly [verb], [verb], [verb]. The camera performs a subtle [movement]."

---

## Hard rules ChatGPT articulated

**Rule 1: Put the style early.** Establishing style early frames all other visual choices. "1970s handheld documentary footage of..." beats "A man walks into a room. Make it look like a 1970s documentary."

**Rule 2: Use physical action beats.** "She takes four steps, pauses, then turns her head in the final second" — describe action in beats or counts for grounded timing.

**Rule 3: Keep clips short when quality matters.** Shorter clips follow instructions more reliably. Stitched 4-second clips often outperform single longer generations.

**Rule 4: Use image references for continuity.** Image inputs lock in character, wardrobe, set dressing, composition, aesthetic. Text prompt defines what happens NEXT.

**Rule 5: Audio is now part of the cinematic prompt.** Add diegetic sound: footsteps, rain, room tone, paper, wind, engine hum, distant traffic.

---

## Common failure modes ChatGPT warned about

**Failure 1 — Too much action:** "A man runs through a city, jumps into a helicopter, flies through a storm..." — splits the model's attention. Constrain to one chase, one obstacle, one resolution.

**Failure 2 — Abstract mood instead of visible behavior:** "Make it feel inspiring" produces nothing. "She places a key on a dusty table and smiles quietly as light fills the room" produces emotion.

**Failure 3 — Contradictory camera instructions:** "Locked camera, fast dolly-in, handheld shaky aerial shot" — pick ONE.

**Failure 4 — Vague cinematic language:** "Cinematic, ultra-realistic, beautiful, epic" generates generic. "Low-angle wide shot, 35mm film grain, golden-hour backlight, shallow depth of field, soft lens flare, warm amber and blue palette" generates specific.

---

## ChatGPT's Final Formula (the cleanest synthesis)

```
[Style first]. A [shot type] of [subject] in [specific location].
[Subject performs one clear action in 2-3 beats].
The camera [one specific movement].
[Lighting source + direction + quality].
Palette: [3-5 color anchors].
[Texture / lens / depth of field].
Audio: [diegetic sound].
Constraints: [positive constraints, no ambiguity].
```

---

## What ChatGPT did NOT contribute that our research had

- Gabe Michael as 2x Gen:48 winner specifically (ChatGPT did not surface this)
- Master Style Prompt as a formalized discipline (ChatGPT mentions style-first placement but doesn't formalize)
- Higgsfield Cinema Studio gallery reference
- Cross-model fallback strategy

## What ChatGPT contributed that our research did NOT have (and gets merged into v2 of playbook)

- **Bifurcation of prompt length by tool:** SHORT motion-first prompts for gen4.5; LONG style/transformation prompts for gen4_aleph (Runway specifically punishes restating the input image in long form)
- **Environmental motion is safer than human motion** — strategic principle that affects iteration budget
- **2026 shift framing:** prompt motion, not image quality
- **Action beats with explicit counts:** "She takes four steps, pauses, then turns her head in the final second" — more specific than timestamps alone
- **Categorical keyword inventories** with explicit "use only when they map to visible output"
- **Per-model differences** explicitly enumerated (Sora vs Veo vs Runway)
- **Pattern library** organized by shot purpose (Premium Film, Product Ad, Real Estate Walkthrough, Emotional Character Moment, Epic Establishing, Action Sequence, Dialogue Scene)
