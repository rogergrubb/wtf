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
