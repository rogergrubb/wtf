# Open Shot — Friday-Ready Prompts

**The keystone shot of the WTF brand film.** Over-the-shoulder cell phone reveal: young Roger on Johnson's Beach 1969 inside a phone screen, camera pulls back, Mom's shoulder enters frame, full reveal of her holding the phone, kids playing in water behind. ~5–7 seconds total. Eight Runway endpoints stacked into seven seconds. The flawless mandate applies.

**Built using:** the Cinematic Prompt Playbook at `/docs/cinematic_prompt_playbook.md`. Read that first if you haven't.

**Master Style Prompt (paste into every prompt below):**
> *"Cinematic, intimate, documentary realism. Warm 1969 Kodachrome color palette with modern dynamic range — golden saturation, faded shadows, soft highlights. Shot on ARRI Alexa with 35mm lens. Subtle film grain. Shallow depth of field. Natural light, golden hour. Quiet, observational, emotionally honest. Cinematography inspired by Terrence Malick and Roger Deakins."*

---

## Layer 1 — Background plate: Russian River with kids splashing

**Tool:** gen4_image (3-5 candidates) → gen4.5 image-to-video on the winner (3 motion candidates)

**Reference inputs:** None required for plate; gen4.5 takes winning still as first frame.

### gen4_image candidate prompts (generate 5)

**Variant A — wide environmental anchor**

> A 1969 photograph of Johnson's Beach on the Russian River, late August golden hour. Three children in vintage swimsuits splash in shallow water mid-frame, soft silhouettes backlit by warm sun. A scattering of beach umbrellas and beach blankets in the middle distance. Low riverbank with pebbles in the foreground, blurred. Tall trees on the far bank, hazy with summer atmosphere. Shot on Kodachrome, 35mm, golden saturation, soft highlights, faded shadows. Cinematic, observational, intimate. Inspired by Terrence Malick.

**Variant B — tighter framing on kids**

> Late afternoon golden hour at the Russian River, August 1969. Three small children, ages 4–7, mid-splash in shallow water — caught mid-motion, droplets backlit by the low sun creating bokeh sparkles. The water surface is glassy and warm-toned. A vintage striped beach umbrella visible in the soft-focus background. Shot on Kodachrome 35mm, shallow depth of field, golden saturation, intimate observational documentary framing. Inspired by Roger Deakins.

**Variant C — atmospheric lower-key**

> Russian River shoreline, August 1969, hazy late-afternoon light filtered through summer atmosphere. Three children in mid-frame, knee-deep in shallow water, energetic movement softened by motion blur and bokeh. Backlit silhouettes, rim-lit edges, warm dust particles drifting through frame. Shot on Kodachrome 35mm, atmospheric haze, soft golden palette. Cinematic, dreamy, observational. Inspired by Malick.

**Variant D — composition with negative space for compositing**

> A 1969 Kodachrome photograph: Russian River shoreline in late August golden hour, with the lower-left third of the frame intentionally clean and uncluttered (for compositing). Three small children playing in shallow water occupy the right two-thirds, mid-splash, backlit by warm sun. Shallow depth of field, soft focus on background trees. 35mm lens. Inspired by Deakins.

**Variant E — wider safety**

> Wide establishing shot of Johnson's Beach on the Russian River, August 1969 golden hour. Children playing in shallow water, families on blankets in middle distance, vintage striped umbrellas dotting the shoreline. Atmospheric haze, warm Kodachrome saturation, soft natural lighting. 35mm, shallow depth, observational documentary feel. Inspired by Malick.

### gen4.5 motion prompt (run on the winning still)

> The camera glides slowly to the right in a soft handheld pan as the children mid-frame splash and laugh, water droplets catching golden hour light, beach umbrellas in soft-focus background gently shifting in summer breeze. Bokeh in foreground.
> 
> [Master Style Prompt pasted here in full.]
> 
> [00:00] Children mid-splash, water droplets suspended. [00:02] Slow pan right continues, droplets land. [00:05] Pan settles, children laugh, ambient breeze.

---

## Layer 2 — Phone bezel + screen frame

**Tool:** gen4_image (3 candidates). Static asset, no motion needed at this layer.

### gen4_image candidate prompts (generate 3)

**Variant A — anonymous-modern primary**

> A modern smartphone in landscape orientation, photographed in studio. Anonymous, generic design — black bezel, no manufacturer logo, no recognizable Apple or Samsung styling. Bezel approximately 4mm. Screen surface clean and reflective. Phone is held at a slight three-quarter angle. Soft studio lighting, neutral background. Photorealistic, product-quality detail. Designed to feel like "a phone" rather than a specific product.

**Variant B — shadow detail variation**

> Modern anonymous smartphone in landscape orientation, held at a slight angle. Generic black bezel, no logos, no recognizable brand styling. Studio lighting from upper left creates a soft shadow on the right edge. Screen surface clean and slightly reflective with subtle ambient reflection. Photorealistic detail, clean compositing-ready edges.

**Variant C — slightly futuristic**

> A near-future generic smartphone in landscape orientation, slim profile, anonymous design with no logos or brand markers. Edge-to-edge screen with minimal black bezel (~2mm). Subtle metallic gunmetal frame. Photorealistic, studio lit, neutral background, clean compositing edges. Feels timeless rather than dated.

**Compositing note:** in post, the screen rectangle gets masked transparent so Layer 3 (Roger inside the phone) renders inside it.

---

## Layer 3 — Roger-5 inside the phone screen

**Tool:** avatars.create (Roger-5 Character from cropped AUG 69 photo) → avatar_videos.create (3-5 takes) → optional character_performance polish

**Reference inputs:** Cropped AUG 69 photo isolating young Roger.

### avatars.create personality prompt

> A five-year-old boy in 1969, on Johnson's Beach at the Russian River. Wears a white short-sleeve shirt. Light brown hair, slight squint from the afternoon sun. Personality: curious, content, easily delighted. He has just heard his mother call him her Number One Son and is starting to giggle. He doesn't fully understand what the words mean, but he remembers them. He is unselfconscious, present, and warm.

**Voice preset:** felix (young masculine) — confirm Friday morning by listening to 2-3 alternates.

### avatar_videos.create motion prompts (generate 4 takes)

**Take 1 — pure delight**

> The camera holds steady in a soft close-up as the boy giggles, eyes squinting from the sun, head tilted slightly upward toward an unseen mother just off-frame. He scrunches his nose in joy.
> 
> [Master Style Prompt.]
> 
> [00:00] Eyes upward, mouth softening into smile. [00:01] Begins to giggle, shoulders shake slightly. [00:03] Squints from sun, beams. [00:04] Eyes drift down, content.

**Take 2 — quieter beat**

> The camera holds steady in a soft close-up as the boy looks up at his mother off-frame, breaks into a quiet smile, and lets out a small laugh, blinking against the bright afternoon sun.
> 
> [Master Style Prompt.]
> 
> [00:00] Looks up. [00:01] Recognition, eyes brighten. [00:02] Slight smile begins. [00:04] Laughs softly.

**Take 3 — looks at us (the phone)**

> The camera holds steady as the boy looks directly toward the camera (toward the phone screen), face brightening into a wide, unguarded smile. He squints slightly, then giggles softly. The river background is softly out of focus behind him.
> 
> [Master Style Prompt.]
> 
> [00:00] Looking off-frame. [00:01] Eyes meet camera. [00:02] Smile widens. [00:04] Soft giggle.

**Take 4 — playful**

> The camera holds steady on the boy, who is mid-laugh, looking up and slightly to the right at his mother. He brings one hand up briefly toward his face in joyful embarrassment, then drops it. Wind moves his hair.
> 
> [Master Style Prompt.]
> 
> [00:00] Mid-laugh. [00:01] Hand begins to rise. [00:02] Hand near face, peeks. [00:03] Hand drops, big grin. [00:05] Settles, smiling.

---

## Layer 4 — Mom-25 over-the-shoulder holding the phone

**Tool:** avatars.create (Mom-25 Character from cropped AUG 69 photo) → avatar_videos.create (5-7 takes — this is the hardest layer)

**Reference inputs:** Cropped AUG 69 photo isolating Mom in striped swimsuit.

### avatars.create personality prompt

> A 25-year-old woman in 1969, on Johnson's Beach at the Russian River. Wears a striped two-piece swimsuit, hair pinned back, light tan from a summer outdoors. Personality: warm, attentive, mother of a five-year-old boy she calls her Number One Son. She is thoroughly present in this moment — watching him, photographing him, savoring it. She is alive at 82 in 2026, and the woman we render is the woman she was. Knowledge: the words "Number One Son" and the boy in front of her are inseparable in her memory. The river behind her is loud with kids and breeze.

**Voice preset:** Friday huddle decision — aurora / clara / cloned-Mom-at-82.

### avatar_videos.create motion prompts (generate 5–7 takes)

The hardest layer because she is back-to-camera holding a 2026 phone in 1969. Iteration is mandatory.

**Take 1 — straight reveal pose**

> The camera holds in a medium shot from behind the woman's left shoulder. She is steady, holding a phone in front of her at eye level in landscape orientation. Her right thumb hovers near the screen. The phone screen content is what we have been watching. Her hair shifts gently in the river breeze. The river and children are softly out of focus far behind her.
> 
> [Master Style Prompt.]
> 
> [00:00] Hovering, framing the shot. [00:02] Right thumb drifts toward shutter button. [00:04] Soft tap on screen, micro-tremor in hand. [00:05] Hand steady again.

**Take 2 — pull-back simulated through subject motion**

> The camera holds steady from behind the woman's left shoulder. She begins close in frame, holding a phone at eye level. Over five seconds her shoulders relax slightly and she shifts the phone a half-inch lower as if appraising the shot. The river background is softly out of focus.
> 
> [Master Style Prompt.]
> 
> [00:00] Phone at eye level, attentive. [00:02] Shoulders relax. [00:04] Phone shifts a half-inch lower. [00:05] Settled.

**Take 3 — shutter tap focus**

> The camera holds in a tight medium shot over her right shoulder. She holds the phone steady in landscape orientation. Her right thumb taps the shutter button on the screen at the 3-second mark. A subtle hand micro-tremor before and after the tap. Wind in her hair.
> 
> [Master Style Prompt.]
> 
> [00:00] Phone steady, framing. [00:02] Thumb begins drift to shutter. [00:03] Tap. [00:04] Thumb retracts. [00:05] Holds, looking at result.

**Take 4 — environmental anchor**

> Over-the-shoulder medium shot of the woman holding a phone at eye level. Beyond her shoulder and the phone, children play in shallow water in soft focus. Warm golden afternoon light catches the side of her arm and the phone's metallic edge. She holds steady, breathing in.
> 
> [Master Style Prompt.]
> 
> [00:00] Holding steady. [00:03] Slow inhale, shoulders subtle rise. [00:05] Settled, attentive.

**Take 5 — head tilt for connection**

> Camera holds over her left shoulder. She holds the phone at eye level, then tilts her head slightly toward the screen as if to better see her son. Her right hand grips the phone steadier. Soft afternoon light, river breeze.
> 
> [Master Style Prompt.]
> 
> [00:00] Holding straight. [00:01] Head tilts slightly toward screen. [00:03] Right hand re-grips. [00:05] Settled, attentive.

**Take 6 — micro-gesture warmth**

> Camera holds in a tight over-the-shoulder shot. She holds the phone steady. Her free left hand drifts up briefly to brush a strand of hair behind her ear, then settles back at her side. The phone never moves out of her right-hand grip. Soft golden light.
> 
> [Master Style Prompt.]
> 
> [00:00] Phone steady. [00:02] Left hand rises to ear. [00:03] Strand tucked. [00:04] Hand drops. [00:05] Settled.

**Take 7 — locked safety**

> Camera locked, over the woman's left shoulder. She holds the phone perfectly steady in landscape orientation at eye level. Wind moves her hair softly. Distant ambient motion in background (children, water). She does not move; only the world around her does.
> 
> [Master Style Prompt.]
> 
> Locked composition. World moves; subject still.

---

## Final composite — gen4_aleph polish pass

**Tool:** gen4_aleph on the layered composite of Layers 1–4.

**Prompt:**

> Apply a unified warm 1969 Kodachrome color grade across the entire video — golden saturation, soft faded shadows, gentle highlights. Add subtle film grain consistent with 35mm period photography. Re-light so the phone screen emits a warm nostalgic glow that falls on the woman's face, shoulder, and hand. Add atmospheric afternoon light rays and gentle dust particles. Keep all camera moves and subject performances unchanged. Preserve all character likenesses. Cinematography should feel inspired by Terrence Malick — quiet, observational, emotionally honest.

**Iteration:** run 3 Aleph passes, A/B compare, lock the strongest.

---

## Audio overlay (eleven_text_to_sound_v2)

Generate three layers, mix in post:

1. **Surf and water ambience** — *"Gentle river water lapping against pebbled shore, low frequency, stereo width, soft and continuous, 7 seconds"*
2. **Children laughing in distance** — *"Three or four small children laughing and splashing in mid-distance, soft and natural, slight reverb, no individual voices clear, 7 seconds"*
3. **Phone shutter click** — *"Single soft modern smartphone shutter click, mechanical and brief, 0.3 seconds, foreground"*

Mix: ambience -8dB, children -12dB, shutter at 5-second mark at -4dB.

**If Mom-at-82 voice clone is approved (Option C):** add her voice saying *"He was my Number One Son"* at the 5.5-second mark, just after the shutter click, at -2dB. Voice is layered on top of all three sound layers.

---

## Quality bar checklist for the open shot

The shot does not ship until each line is true.

- [ ] No AI tells in any face. No melted eyes, extra fingers, wrong number of teeth.
- [ ] Phone bezel reads as anonymous-modern. No Apple, no Samsung tells.
- [ ] Mom's hand has natural skin tone and micro-tremor.
- [ ] Color grade is unified across all layers (Aleph pass confirmed).
- [ ] Children in background move with natural physics — no floating limbs.
- [ ] Surf, kid laughter, and shutter click each readable in mix.
- [ ] Pull-back camera move (or simulated alternative) has organic ease-out.
- [ ] Frame settles before the shutter clicks.
- [ ] Watermark check: no Runway/Aleph/etc. visible artifacts.
- [ ] Real Roger watches the final and clears it himself.


---

# v2 UPDATE — Refined per ChatGPT triangulation (May 8, 2026)

After ChatGPT triangulation surfaced that Runway gen4.5 punishes long prompts that restate the input image, the gen4.5 motion prompts below SUPERSEDE the v1 versions for those specific layers. The gen4_image still-frame prompts and gen4_aleph polish prompt remain unchanged — those tools reward longer description.

## Layer 1 — REVISED gen4.5 motion prompt (SHORT, motion-first)

After the gen4_image winning still is selected, run this SHORT motion prompt on it:

```
The children mid-frame begin a fresh splash, droplets rising and 
catching golden light. The camera glides slowly to the right in a 
soft handheld pan. Beach umbrellas shift gently in summer breeze. 
[00:00] Splash begins. [00:02] Droplets at peak height. [00:04] 
Droplets land, pan settles. [00:05] Children turn back toward water.
```

Token count: ~55. Pure motion description. Master Style Prompt NOT pasted.

## Layer 4 — REVISED strategy: Mom is STILL, world moves around her

ChatGPT explicit guidance: environmental motion is safer than complex human motion. Mom over-the-shoulder is the hardest layer. The pose stays still; everything around her moves.

### Updated avatars.create personality prompt (unchanged from v1)

Keep as-is. Personality grounding is not affected by motion-prompt rules.

### REVISED avatar_videos.create motion prompts (generate 5 takes, all environment-first)

**Take 1 — wind + breath**

```
The subject holds steady, framing the shot. Her hair shifts in soft 
river breeze. Slow controlled inhale lifts her shoulders one millimeter. 
The camera holds locked over her left shoulder. [00:00] Steady. 
[00:02] Hair lifts. [00:04] Breath in. [00:05] Settled.
```

**Take 2 — shutter tap with environmental settle**

```
The subject holds the phone steady. At three seconds her right thumb 
taps the shutter and retracts. Wind moves her hair throughout. Camera 
locked. [00:00] Steady. [00:02] Thumb drift. [00:03] Tap. [00:04] 
Thumb retracts. [00:05] Settled, hair still moving.
```

**Take 3 — sunlight micro-shift**

```
The subject holds still. Golden afternoon sunlight micro-shifts across 
her shoulder and the phone's metallic edge. Camera locked over her 
left shoulder. Hair shifts gently in breeze. [00:00] Light steady. 
[00:02] Light begins shift. [00:05] Light settles warmer.
```

**Take 4 — background bokeh activates**

```
The subject holds steady. Behind her shoulder in soft focus, children 
splash in shallow water. Bokeh sparkles activate at three seconds. 
Camera locked. [00:00] Steady. [00:02] Background motion begins. 
[00:03] Bokeh sparkles peak. [00:05] Settle.
```

**Take 5 — micro-tremor on phone**

```
The subject holds the phone in steady grip with subtle hand micro-tremor. 
Wind in her hair. Camera locked over her left shoulder. [00:00] 
Steady. [00:02] Slight tremor. [00:04] Settles. [00:05] Steady again.
```

### Why this rewrite is stronger

- Mom is rendered as STILL POSE = high success rate.
- Environmental motion (hair, sunlight, bokeh, background splash) = ChatGPT's confirmed high-success category.
- Each take isolates ONE environmental motion variable for clean A/B comparison.
- Token count ~40-60 per prompt. Master Style Prompt NOT pasted. The image is the master style.

## Updated iteration loop for the open shot

For each layer, in order:
1. **gen4_image (still frame):** 3-5 candidates with FULL master style prompt + description.
2. **A/B select winning still.**
3. **gen4.5 (motion):** 5-7 candidates with SHORT motion-only prompts on the winning still. Master Style Prompt NOT included.
4. **A/B select winning clip.**
5. **gen4_aleph (polish):** 1-3 passes with FULL master style prompt + transformation language on the composite of all 4 layers.
6. **A/B compare polished vs raw composite.** Lock the strongest.

This is the correct workflow per Runway's own guidance, not an opinion.
