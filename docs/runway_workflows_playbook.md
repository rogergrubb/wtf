# Runway Workflows Playbook (May 8, 2026)

**Synthesized from 4 parallel research streams during the hackathon kickoff. Read this before deciding whether to build with Workflows.**

---

## TL;DR — The cofounder verdict

**For our hackathon FILM production: YES, use Workflows.** The visual node builder lets us iterate the central Mom-25 + Roger-5 scene faster than custom Python orchestration. We don't need to publish it — it's just a build tool.

**For Ghost Frames SAAS backend: HYBRID.** Publish a Workflow as a v1 endpoint to ship the demo Sunday. Build Modal backend in parallel for production traffic post-hackathon. Workflows accept runtime inputs but lack conditional branching, retries, and caching — you outgrow them at scale.

**For character reference sheets: USE NANO BANANA PRO** (not GPT-Image-2). Better identity preservation across 14 reference images, native 4K, ~$0.067/image with batch discount. Critical for our Mom-25 and Roger-5 character sheets generated from the cropped 1969 photo.

**For our 22-second dialogue scene: STICK WITH gen4.5 + character_performance** as primary. Use Seedance 2.0 as a known fallback. Seedance is newer and less battle-tested for tender multi-character emotional dialogue.

---

## 1. What Runway Workflows IS

A node-based visual pipeline builder inside the main Runway app. Launched October 2025. Available on **Standard plan ($12/mo) and above** — NOT free tier.

URL pattern: `app.runwayml.com/video-tools/teams/[workspace]/ai-tools/workflows/[id]/edit`

**Prerequisite (verified live May 8 kickoff):** App account and Dev account MUST be linked at **runwayml.com/building-tools** before published Workflows are callable via API. Without this link, Publish creates an internal asset only. Do this BEFORE any other Workflow work.


Four node categories:

| Category | Examples |
|---|---|
| **Input nodes** | Text, Image, Video |
| **Media model nodes** | gen4.5, gen4_aleph, Seedance 2.0, Kling 3.0, Veo 3.1, Nano Banana Pro, GPT-Image-2 |
| **LLM nodes** | Gemini 2.5 Flash, Claude Sonnet 4.5, Claude Opus 4.5 |
| **Utility nodes** | Stitch, Trim, Reverse, Extract Frame, Resize, JSON Parse — all FREE (no credits) |

9+ official templates available to fork: Image Style Generator, Storyboard Creator, Animatic Generator, Image Variations, Virtual Try-On, Hair Salon, Style Blend, Custom Instructions Workshop, Image to Text.

---

## 2. Publishing — what happens when you click Publish

Two paths:

**Path A: Publish as API Endpoint** ← THIS IS THE ONE WE CARE ABOUT
- Click Publish → Publish new endpoint
- Label inputs/outputs that callers will provide at runtime
- Toggle visibility (eye icon) on which inputs are exposed
- Result: live REST endpoint at `POST /v1/workflows/{id}`
- Callable via Python SDK, Node SDK, or raw HTTP

**Path B: Publish as App**
- Streamlined UI wrapper for non-technical users
- Workspace-internal only, NOT a public API
- Useful for sharing with team members but not for SaaS

---

## 3. Runtime parameterization — YES, this is real

Published Workflows accept dynamic user inputs at call time. This was the critical question.

```python
from runwayml import RunwayML

client = RunwayML()

task = client.workflows.create(
  workflow_id='ghost_frames_v1_workflow_id',
  inputs={
    'user_photo_uri': 'https://ghostframes.app/uploads/photo.jpg',
    'user_story_text': 'My grandmother, in the kitchen, baking bread',
    'character_description': 'Woman in her 80s, white hair, warm smile'
  }
)

output = task.wait_for_task_output(timeout=600)
print(output.output)  # video URL
```

**For Ghost Frames:** publish a workflow exposing photo + story + character description as inputs. Frontend POSTs to it, gets back a video URL.

---

## 4. Pricing — sum of node credits, no workflow tax

Workflow runs cost = sum of individual node credits. No per-execution fee.

Utility nodes (Stitch, Trim, Reverse, etc.) are FREE.

Example for a Ghost Frames v1 video:
- Nano Banana Pro character sheet (1K, batch): ~10 credits
- gen4.5 image-to-video (10s): ~120 credits
- gen4_aleph polish: ~50 credits
- Stitch + trim: 0 credits
- **Total: ~180 credits per user video = ~$1.80**

Free tier doesn't have Workflows. Standard at $12/mo gives 625 credits = ~3.5 user videos/month free, then pay per call from Developer Portal at $0.01/credit.

---

## 5. Limitations and gotchas

- **Concurrency:** ~5 concurrent workflow runs on Standard plan, higher on Pro/Enterprise
- **No conditional branching:** can't say "if quality score < 0.8, regenerate." Pipeline structure is locked at design time
- **No automatic retries on node failure:** failed node = workflow fails, must rerun
- **No caching:** identical inputs run from scratch every time
- **Versioning is implicit:** publishing a new version replaces the old endpoint immediately, no rollback. Existing API consumers see new version with no warning
- **Default poll timeout:** 10 minutes via SDK's `wait_for_task_output()`
- **Webhook support:** Enterprise+ tier only

---

## 6. Seedance 2.0 — model deep dive

ByteDance video model integrated into Runway as of April 16, 2026. Model ID: `bytedance/seedance-2-0`.

**Strengths:**
- Native multi-character dialogue with lip-sync
- Up to 9 reference images + 3 reference audio files supports our character + voice workflow
- 5-15 second duration sweet spot
- Director-level control via @Image1, @Audio1 syntax in prompt
- Cinematic quality, smooth physics-realistic motion

**Weaknesses for OUR scene:**
- Newer = less battle-tested for tender emotional dialogue
- Multi-shot continuity weaker than gen4.5 + character_performance
- Emotion subtlety not quite at the level of purpose-built character tools

**For our 22-second Mom + Roger scene:**
- **Primary:** gen4.5 + character_performance (proven, purpose-built for dialogue)
- **Fallback:** Seedance 2.0 if character_performance struggles with our specific scene

**Pricing:** ~12 credits/sec at 720p. 22-second scene = ~264 credits = $2.64. Very affordable.

---

## 7. Nano Banana Pro vs GPT-Image-2 — the verdict

Both are now available in Runway as of late April 2026.

| Dimension | Nano Banana Pro | GPT-Image-2 |
|---|---|---|
| Provider | Google (Gemini 3 Pro Image) | OpenAI |
| Character consistency | 95%+ across infinite variations | Strong within single batch only |
| Reference images | Up to 14 | Up to 16 (but identity drifts between calls) |
| Native resolution | 4K | 2K (4K beta) |
| Speed | 10-15s | 3s |
| Aspect ratios | 10 | 30 |
| Pricing | $0.134/img, $0.067 with batch | $0.211/img |
| Text rendering | Strong | Best (~99% accuracy) |
| Watermarking | SynthID + C2PA | C2PA only |
| Best for | **Character reference sheets** | Text-heavy assets, format variety |

**For our Mom-25 + Roger-5 character sheets: NANO BANANA PRO.** Higher character consistency across multiple poses + native 4K + cheaper at batch + softer output (fewer artifacts when handed off to gen4.5 image-to-video).

Runway model ID: `gemini_image3_pro`

---

## 8. Build path recommendations

### Path A — Hackathon demo (ship Sunday)

```
Frontend (Next.js)
    ↓
Calls published Runway Workflow via API
    ↓
Workflow:
  user_photo + story → Nano Banana Pro character sheet
    → gen4.5 image-to-video (with char refs)
      → gen4_aleph polish
        → output: video URL
    ↓
Frontend displays video, user downloads
```

Build time: 4-8 hours for the workflow + 4-6 hours for the frontend.

### Path B — Production SaaS (week 2 onwards)

```
Frontend (Next.js)
    ↓
Modal Python backend
  - validates inputs
  - photo hash → cache check (return existing video if seen)
  - rate limit per user (3 free/day)
  - calls Runway endpoints individually
    - gen4_image / Nano Banana Pro for character refs
    - gen4.5 for motion (with retry on quality fail)
    - gen4_aleph for polish
    - eleven_text_to_sound_v2 for ambient
  - composites with ffmpeg
  - stores result in S3/R2
  - returns CDN URL
    ↓
Frontend
```

Build time: 20-30 hours including caching, retry, rate limiting, error handling.

---

## 9. The film production decision (separate from SaaS)

**For the v3 brand film itself:** Use Workflows internally as a build tool. We don't need to publish — we just use the visual node graph to iterate the central Mom + Roger scene faster than scripting it via Python.

Build the workflow:
1. Text input: dialogue script
2. Two character refs (Mom-25 + Roger-5) generated by Nano Banana Pro from cropped AUG 69 photo
3. character_performance node OR Seedance 2.0 for the dialogue scene
4. gen4_aleph for color grade polish
5. Stitch with the photograph zoom-in/out transitions
6. Output: 22-second cinematic clip

Iterate within the workflow until the scene lands flawlessly. Then export the final clip and composite into the full film.

---

## 10. Sources

- https://help.runwayml.com/hc/en-us/articles/45763528999699-Introduction-to-Workflows
- https://help.runwayml.com/hc/en-us/articles/50085269258643-Publishing-a-Workflow-as-an-Endpoint
- https://help.runwayml.com/hc/en-us/articles/47865876793747-Publishing-Workflows-as-Apps
- https://help.runwayml.com/hc/en-us/articles/47184761711379-Using-Utility-Nodes-in-Workflows
- https://help.runwayml.com/hc/en-us/articles/50488490233363-Creating-with-Seedance-2-0
- https://help.runwayml.com/hc/en-us/articles/48649877897107-Available-Models-on-Runway
- https://docs.dev.runwayml.com/api/
- https://docs.dev.runwayml.com/api-details/sdks/
- https://runwayml.com/pricing
- https://runwayml.com/changelog
- https://github.com/runwayml/sdk-python
- https://academy.runwayml.com/tutorial/how-to-build-custom-workflows


---

## ADDENDUM (May 8, 9:45am — confirmed from live kickoff)

**The App↔Dev account link is the operational prerequisite.**

Confirmed from a live Publish UI demo at the kickoff: before any published Workflow becomes callable via API, the user's App account (where Workflows are built) must be linked to their Dev account (where API keys are issued). The link is configured at **runwayml.com/building-tools**.

Operational order:
1. **runwayml.com/building-tools** → link App ↔ Dev accounts
2. Build Workflow in App
3. Toggle eye-icon on user-supplied inputs in the Publish UI
4. Click Publish → Publish new endpoint
5. Note the workflow_id from the resulting URL: `app.runwayml.com/video-tools/teams/{ws}/ai-tools/workflows/{workflow-id}/publish-endpoint`
6. From client code: `client.workflows.create(workflow_id=..., inputs={...})`

The "Set user inputs" UI explicitly states: *"Users will be able to use their own prompts in the input fields below. Hide the fields that don't need to be shown to users."* Confirms the runtime parameterization model that this playbook anticipated.
