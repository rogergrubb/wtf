# Cinematic Prompt Playbook (2026)

**Synthesized from:** Curious Refuge, LTX Studio, Gabe Michael's Cinematic AI Prompt Method, Higgsfield Cinema Studio gallery, and Runway's official gen4.5 + gen4_aleph documentation.

**Use this for every prompt we write Friday.** It exists so we don't argue prompt structure at 2am — we follow the formula, iterate the wording, and ship.

---

## Why this playbook exists

Five independent sources teach the same shape. Whatever language they use — CCR, 5W+H, storyboard-block, image-to-video formula — the underlying anatomy is the same. The differences are vocabulary, not method. This playbook unifies the vocabulary, applies it to Runway gen4.5 + gen4_aleph specifically, and gives us reusable templates.

Source weighting note: **Gabe Michael won Runway Gen:48 Best Art Direction twice.** Where his guidance differs from the others, his wins. He's not theorizing — he's documenting what the Runway judges already rewarded.

---

## The Master Style Prompt (visual DNA — set ONCE for the entire film)

Before generating a single shot, lock the master style prompt. Every shot inherits this. From Gabe Michael's method: "Standardize one prompt that establishes the visual DNA of the entire project. Use it religiously on every generation."

**Our master style prompt for the WTF brand film:**

> *"Cinematic, intimate, documentary realism. Warm 1969 Kodachrome color palette with modern dynamic range — golden saturation, faded shadows, soft highlights. Shot on ARRI Alexa with 35mm lens. Subtle film grain. Shallow depth of field. Natural light, golden hour. Quiet, observational, emotionally honest. Cinematography inspired by Terrence Malick and Roger Deakins."*

This phrase (or a tightened variant) gets appended to every gen4.5 and gen4_aleph prompt. It sets the look once. We don't re-argue it per shot.

---

## The unified prompt anatomy

Every shot prompt has these slots, in this order. If a slot is empty, leave it empty — don't pad.

```
1. CAMERA MOTION  — what the camera is doing
2. SUBJECT + ACTION — who/what is in frame and what they do
3. ENVIRONMENT — where this is happening, time of day, weather
4. LIGHTING — direction, quality, color temperature
5. LENS + DEPTH — focal length, depth of field, framing
6. STYLE — film stock, color grade, director reference (or pull from master style)
7. EMOTION — explicit narrative tone in plain language
8. TIMING — sequence beats with timestamps if multi-action
```

**Runway's official formula** (use this for gen4.5 specifically):
> *"The camera [motion] as the subject [action]. [Additional descriptions]."*

That's the spine. Slots 3–8 fill in around it.

---

## Hard rules (non-negotiable)

These come up across all five sources. Break them and quality drops.

1. **Lead with camera motion.** Gen4.5 reads the first phrase as the priority. "Slow handheld pull-back as Mom holds the phone..." beats "Mom holds the phone while the camera pulls back."

2. **One camera move per shot. One action per subject.** Multiple simultaneous moves degrade output across every model tested. If the shot needs two moves, split it into two shots and edit them together.

3. **Positive phrasing only.** Never "no movement," "doesn't move," "avoid," "don't." Gen4.5 specifically does the opposite of what negative phrasing requests. Use "locked camera" for stationary, "still composition" for held frames.

4. **Don't restate the image.** When using image-to-video, the image already shows the model the subject. Words wasted re-describing the image are tokens stolen from the motion description.

5. **Strong action verbs, always.** Banned: moves, looks, goes, is, does, has. Required: lurches, trembles, gazes, pivots, reaches, glides, slips, cradles, slips. Verb specificity is the single biggest quality lever.

6. **Director or DP reference is mandatory.** "Deakins-inspired," "Malick tenderness," "Kubrick framing," "Lubezki natural light." This anchors the model to a known aesthetic faster than any descriptive language.

7. **Film stock specificity is mandatory.** 35mm, 16mm, Kodachrome, Portra 400, anamorphic, ARRI Alexa. Pick one and commit.

8. **Emotional anchor in plain language.** State it: "intimate tenderness," "quiet ache," "joyful disbelief," "psychological stillness." Don't make the model infer.

9. **Timing markers for any multi-beat shot.** Format: `[00:01] subject does X. [00:03] subject does Y. [00:05] camera completes pull-back.` Gen4.5 honors these reliably for clips up to 10 seconds.

10. **Generate 5–7 candidates per shot. Never one.** This is the iteration discipline that separates flawless from competent. A/B compare side by side. Pick the best. Re-roll the rejected with refined wording.

---

## Runway gen4.5 specifics

| Aspect | Guidance |
|---|---|
| **Cost** | ~60 credits per 5-second clip (observed in our tests). Aleph polish is ~5 cr/sec — much cheaper. |
| **Optimal duration** | 5–10 seconds. Beyond 10s, motion coherence degrades. |
| **Token sweet spot** | 150–300 tokens. Beyond 400, model loses focus. |
| **Image-to-video framing** | The image is the FIRST FRAME. Prompt should describe what happens AFTER frame 1. |
| **Multi-subject positional language** | "The subject on the left walks forward. The subject on the right remains still." Always anchor positions. |
| **Camera-move terminology that lands** | dolly in/out, push in, pull back, tracking shot, handheld with natural shake, gimbal, steadicam, orbit, arc, whip pan, crash zoom, rack focus, locked camera. |
| **Cinematic keywords confirmed working** | golden hour, backlit, rim light, lens flare, anamorphic, Kodachrome, 35mm, film grain, shallow depth, atmospheric haze, deep focus, soft focus, rack focus. |
| **Known weaknesses** | Multiple humans with distinct simultaneous actions, on-screen text, complex camera + fast action together, causal reasoning (effect-before-cause), counting, dialogue lip-sync (use act_two or character_performance instead). |

---

## Runway gen4_aleph specifics (cinematic polish pass)

Aleph is NOT generation. It is **transformation of existing video**. Use it as the final pass on every shot to unify look and atmosphere.

**Aleph formula:**
> *"[Action verb] the video [so/to] [specific transformation]."*

Action verbs: add, remove, change, replace, re-light, re-style, transform, restore, enhance.

**What Aleph does brilliantly:**
- Unify color grade across multi-source composites
- Add film grain consistently across all layers
- Re-light a finished composite to match a master frame
- Add atmospheric effects (dust, haze, light rays, lens flares)
- Remove unwanted UI artifacts, watermarks, or compositing edges
- Style transfer (cartoon → photoreal, modern → period, etc.)

**Preserve-what-you-have phrasing:**
- "keep the lighting the same"
- "the background stays unchanged"
- "preserve the subject's pose and expression"

**Reference-image phrasing:**
- "Re-light the video using the lighting from the image"
- "Apply the color grade from the reference image"
- "Restyle the video to match the aesthetic of the reference"

---

## The reusable template (paste into every shot prompt)

```
[CAMERA MOTION]: The camera [verb] [direction/path]
[SUBJECT + ACTION]: as [subject] [strong action verb] [object/manner]
[ENVIRONMENT]: in [location], [time of day], [weather/atmosphere]
[LIGHTING]: [direction] [quality] light, [color temperature]
[LENS]: [focal length] lens, [depth of field], [framing]
[STYLE]: [master style prompt — pasted in full]
[EMOTION]: [explicit narrative tone in plain language]
[TIMING]: [00:01] [beat]. [00:03] [beat]. [00:05] [beat].
```

---

## Iteration discipline

The flawless mandate is enforced by structured iteration, not by writing the perfect prompt on the first try.

**Per layer, every time:**

1. **Generate 5 candidates.** Same prompt, different seeds OR three prompt variants × two seeds each.
2. **A/B compare side-by-side at full screen.** Decide on a single best. Note WHY it won.
3. **Re-roll the bottom 3** with refined wording targeting the specific weakness (motion timing, lighting, character likeness).
4. **Lock the winner.**
5. **Run gen4_aleph polish pass** on the winner with the master style prompt.
6. **Compare locked-and-polished vs. locked alone.** Keep whichever is sharper.

**Time budget per layer:** 25–40 minutes. Six layers in the open shot at 30 min each = ~3 hours. That's a quarter of Friday's build window. Plan accordingly.

---

## Common failure modes (from the research synthesis)

1. **Prompt bloat.** Over-specifying details locks the model into rigidity. Cut adjectives until each one is load-bearing.
2. **Single-generation reliance.** "Maybe my prompt is wrong" usually means "I haven't generated enough seeds." Run 5+ before changing the prompt.
3. **Skipping the master style prompt.** Each shot drifts visually. Lock the master style FIRST, paste it into every prompt.
4. **Character morph across shots.** Build character reference sheets (front, side, back, close-up) before any video generation. Anchor to those refs.
5. **Treating Aleph as generation.** Aleph transforms existing video. If you ask it to generate, you'll fight it. Use gen4.5 for generation, Aleph for polish.
6. **Multi-character scenes in a single prompt.** Even gen4.5 struggles. Render each character separately; composite in post.
7. **Underestimating post.** Topaz upscale, DaVinci color correction, light film grain in Premiere. AI output is rarely truly final.

---

## Cross-model translation matrix

We're using Runway. But if a layer fails on Runway, here's where it goes:

| Need | Best non-Runway model | Why |
|---|---|---|
| Lip-sync dialogue | Veo 3.1 | Industry-leading lip accuracy. |
| Talking-head emotion | Kling 3.0 | Character expression mapping. |
| Multi-character distinct motion | Kling 2.6 | Stronger than gen4.5 here. |
| Large-scale environment physics | Sora 2 | Best at debris, weather, crowds. |
| UGC / authentic handheld | Minimax | Loose interpretation of minimal prompts. |
| Camera-driven cinematography | WAN 2.5 | Most responsive to camera commands. |

For our open shot, we stay 100% in Runway. The layers we build are all things gen4.5 + Aleph excel at: motion-stable image-to-video with strong lighting and character-anchored framing. Cross-model fallback is hackathon-day insurance, not the plan.

---

## Sources

- **Curious Refuge** — curiousrefuge.com (CCR method, lighting presets, model-jumping strategy)
- **LTX Studio** — ltx.studio (real cinematography language, 180-degree shutter trick, character element tags)
- **Gabe Michael's Cinematic AI Prompt Method** — creativepossible.substack.com (Master Style Prompt, 5W+H, Runway Gen:48 winner workflow)
- **Higgsfield** — higgsfield.ai (Cinema Studio gallery, multi-shot storyboard prompts, model-specific differences)
- **Runway official** — help.runwayml.com (gen4.5 + gen4_aleph official prompting guides)


---

# v2 UPDATE — Insights from ChatGPT triangulation (May 8, 2026)

ChatGPT's deep-dive (raw response saved at `docs/chatgpt_response_raw.md`) added five load-bearing refinements. These OVERRIDE the corresponding sections of v1 where they conflict.

## Critical refinement: bifurcate prompt length by tool

**This changes how we write every prompt.**

The v1 Master Style Prompt approach (paste full visual DNA into every prompt) is wrong for gen4.5 specifically. Runway's official guidance says image-to-video prompts that restate the input image in high detail REDUCE motion quality. The model treats both image AND text as the prompt; describing what's already in the image steals tokens from describing motion.

**Updated rule:**
- **gen4.5 prompts:** SHORT (40-80 tokens), motion-first, positive phrasing only. Do NOT paste the Master Style Prompt. Do NOT describe what's in the image. Describe ONLY what changes over time.
- **gen4_aleph prompts:** LONG (150-300 tokens), description-rich, full transformation language. Paste the Master Style Prompt here. Aleph is where the visual DNA gets enforced.
- **gen4_image prompts (text-to-image):** MEDIUM (80-150 tokens), description-rich because the image IS what we're describing. Paste the Master Style Prompt here.

## Critical insight: environmental motion is safer than human motion

ChatGPT's exact words: *"Environmental motion is safer than complex human motion. Wind, rain, smoke, fog, dust, reflections, and light movement usually generate better cinematic results."*

**Strategic implication for the open shot:**
- Layer 1 (kids splashing in water) = environmental motion = high success rate. Iterate 3-5 takes.
- Layer 4 (Mom over-the-shoulder holding phone) = complex human motion = HARDEST. Iterate 7-10 takes AND pose her STILL with environment moving around her.

**Updated Layer 4 strategy:** Mom does not move. The world moves around her — wind in her hair, kids splashing in soft-focus background, sunlight micro-shifting on her shoulder. The phone has subtle hand-held micro-tremor. That's it. We are prompting environmental motion around a still subject, not animating a complex human pose.

## The 2026 shift framing

> "Prompt motion, not image quality. Static image prompts describe what something looks like. Video prompts must describe what changes over time."

This becomes a sanity check on every gen4.5 prompt before we run it: does the prompt describe CHANGE OVER TIME, or does it describe the LOOK of the frame?

If it describes the look, rewrite it.

## Action beats with explicit counts

Augmenting our v1 timing markers ([00:01], [00:03]) with explicit beat counts:

> "She takes four steps, pauses, then turns her head in the final second."

This is more precise than timestamps alone because it ties beats to specific physical actions. Use both: timestamps for camera, beat counts for subject motion.

## Style-first placement

Our v1 says paste the master style prompt at the end. ChatGPT says LEAD with the style:

> "1970s handheld documentary footage of..." beats "A man walks into a room. Make it look like a 1970s documentary."

For gen4_aleph and gen4_image prompts, the master style prompt now goes FIRST (or its summary form does). For gen4.5, we don't paste it at all, so this rule doesn't apply there.

## Updated reusable templates

### gen4.5 motion prompt template (SHORT — 40-80 tokens)

```
[Subject in general terms — "the subject", "the woman", "the boy"] [strong verb 1], [strong verb 2], [optional verb 3].
The camera [single specific movement].
[Single environmental motion detail].
[00:01] [first beat]. [00:03] [second beat]. [00:05] [final beat].
```

### gen4_aleph polish prompt template (LONG — 150-300 tokens)

```
[Master Style Prompt pasted in full — visual DNA].
Apply [transformation 1], [transformation 2], [transformation 3].
Re-light [specific lighting direction].
Add [film grain / atmospheric effect / dust particles / lens flare].
Preserve [camera moves / subject performance / character likeness].
[Reference image instruction if applicable: "using the lighting from the reference image"].
```

### gen4_image still-frame prompt template (MEDIUM — 80-150 tokens)

```
[Master Style Prompt — full or summarized].
A [shot type] of [specific subject in 3-5 visual details] in [specific location].
[Lighting source + direction + quality].
Palette: [3-5 color anchors].
[Lens feel + depth of field].
Constraints: [positive constraints, no ambiguity].
```

## ChatGPT's master 11-slot scene breakdown (use as a pre-prompt brief)

Before writing any prompt, fill in these 11 slots first. Then convert to the appropriate template above.

```
1. Scene purpose: [emotional or commercial intent]
2. Shot: [wide / medium / close-up / macro / aerial / tracking / locked]
3. Subject: [focal point with 2-4 specific visual details]
4. Action: [one simple action in 2-3 physical beats]
5. Camera: [ONE camera movement only]
6. Location: [specific place with visible environmental details]
7. Lighting: [main light source, direction, quality, contrast]
8. Palette: [3-5 color anchors]
9. Texture: [35mm, 16mm, clean commercial, documentary, noir, etc.]
10. Audio: [diegetic sound, ambience, dialogue if needed]
11. Constraints: [no logos, no readable text, no extra characters, realistic motion, etc.]
```

## What ChatGPT did NOT contribute (so we keep these from v1)

- Gabe Michael 2x Gen:48 winner — still our highest-weighted source where alignments differ
- Master Style Prompt as a formalized project-wide discipline — keep, but apply only to Aleph and gen4_image, not to gen4.5
- Cross-model fallback matrix — still useful Friday insurance
