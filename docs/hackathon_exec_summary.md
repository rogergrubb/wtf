# Runway Hackathon: 60-Second Playbook

**May 8–11, 2026. $25K prizes. 200K API credits per team.**

---

## MODELS YOU HAVE (Ranked by Hackathon Viability)

### Tier 1: Highest Novelty (Use These)

**Runway Characters (GWM-1)** — Real-time interactive video agents
- Audio-driven avatar performance; zero-shot character transfer from image
- Launched March 2026; judges will reward novel uses
- Cost: Unknown but included in 200K allocation
- **Build:** Interactive customer service bots, streaming avatars, conversational AI

**Act-Two** — Motion capture to character animation
- Actor performance → character animation (no mocap suit needed)
- Unique in industry; competitors don't have this API
- Cost: Unknown
- **Build:** Creator tools ("I act, AI animates"), accessibility features

### Tier 2: Proven & Stable (Safe Bet)

**Gen-4.5** — High-fidelity text-to-video & image-to-video
- 5–10 second generations; real-time 1080p preview
- Native audio (dialogue + SFX + music)
- Cost: 12 credits/second → $1.20 per 10-second clip
- **Build:** Product video automation, short-form content, marketing

**Aleph** — Professional cinematic editing
- Edit footage (e.g., change lighting, style, subjects)
- Add motion to static images
- Cost: ~12 credits/second (slower than Gen-4.5)
- **Build:** Professional video editing, VFX-free workflows

### Tier 3: Complementary (Nice-to-Have)

- **Image generation (gen4_image):** 5 credits/image; up to 3 reference images
- **ElevenLabs audio:** 29-language dubbing, voice isolation, custom voices
- **Inpaint, upscale, remove background:** Editing utilities

---

## THE MATH

| Metric | Value |
|---|---|
| **Budget** | 200K credits |
| **Cost per 10s Gen-4.5** | 120 credits ($1.20) |
| **Generations possible** | ~1,667 full videos |
| **Recommended split** | 40% Gen-4.5, 30% Gen-3 Turbo, 20% Characters/Act-Two, 10% contingency |

---

## CRITICAL CONSTRAINTS

1. **Duration:** Max 10 seconds per generation; can extend 3x to ~40 seconds total
2. **Latency:** Gen-4.5 = 30–60 sec; Characters = real-time (in API, but network adds overhead); Aleph = 60–120 sec
3. **Content moderation:** Auto-blocks violence, nudity, public figures, artist styles; too many rejections = account suspension
4. **API model:** Async polling (no streaming); submit task → wait for completion
5. **No real-time streaming:** Can't build live-video products; batch/queue instead

---

## WINNING FORMULA

✓ Heavy use of **Characters** (newest; judges want to see it)  
✓ At least one demo with **Act-Two** (unique; no competitors have this)  
✓ **Interactive** elements (not just batch processing)  
✓ **Modal integration** for scalability (webhook-based pipeline)  
✓ **End-to-end product** (something creators would actually use)  

✗ "Just another Gen-4.5 demo" (judges have seen this already)  
✗ Relying on public figures without content moderation config  
✗ Building for real-time latency you can't deliver  
✗ Running out of credits mid-pitch  

---

## MODAL PRICING (Infrastructure Cost)

If you build custom post-processing on Modal:

| GPU | Hourly Cost | Hackathon Risk |
|---|---|---|
| H100 | $3.95 (base); up to $14.81 (production US) | Expensive; avoid unless real-time required |
| A100 40GB | $2.10 (base); up to $7.87 (production US) | Reasonable for batch jobs |

**Free tier:** 10 concurrent GPUs (Starter plan); sufficient for hackathon.

---

## CONTENT MODERATION: DON'T GET SUSPENDED

**These trigger auto-block (configurable, but risky):**
- Recognizable public figures
- Living artist styles
- Violence, gore, nudity

**These = indefinite suspension (non-negotiable):**
- Child sexual abuse material
- Sexualization of minors

**Best practice:** Pre-filter inputs in your app before sending to Runway.

---

## BEFORE YOU SHIP

- [ ] Test Gen-4.5, Characters, Act-Two under load (10 parallel requests)
- [ ] Verify content moderation on edge cases (faces, styles, text)
- [ ] Measure end-to-end latency (API call → output)
- [ ] Calculate true cost per user at scale
- [ ] Implement credit tracking (stop when near limit)
- [ ] Document prompt engineering tuning (quality will vary)

---

## JUDGE SCORING (My Estimate)

| Category | Weight | Win By |
|---|---|---|
| **Novelty** | 30% | Heavy Characters + Act-Two use |
| **Execution** | 25% | Demo works without crashes; latency is realistic |
| **Idea** | 25% | Solves real creator/business problem |
| **Pitch** | 20% | Clear story + impressive visuals |

**Tiebreaker:** Interactive demo beats batch processing.

---

## SOURCES

- [Runway API Docs](https://docs.dev.runwayml.com/)
- [Runway Developer Portal](https://dev.runwayml.com/)
- [Modal Docs](https://modal.com/docs)
- [GitHub: runwayml/skills](https://github.com/runwayml/skills)

