# Runway API Hackathon: Complete Capability Map (May 2026)

**Context:** Runway API Hackathon May 8–11, 2026. $25K prize pool. 200K free API credits to participants. Modal provides infrastructure backbone.

**Status Date:** April 20, 2026.

---

## 1. RUNWAY API ENDPOINTS & MODELS

### 1.1 Video Generation

#### **Gen-4.5** (Latest, launched Feb 10, 2026)
- **What it does:** High-fidelity video generation from text or image inputs
- **Input modes:** 
  - Text-to-video: describe a scene and generate with dynamic motion
  - Image-to-video: animate static images into photorealistic sequences
- **Duration:** 5 or 10 seconds base generation; extendable via chaining
- **Cost:** 12 credits/second of video
  - 5-second generation: 60 credits ($0.60)
  - 10-second generation: 120 credits ($1.20)
- **Latency:** Real-time 1080p preview generation now available; full-res (up to 4K) takes longer
- **Max output resolution:** 4K upscale available (2 credits/second additional)
- **Constraints:**
  - Maximum 10 seconds per single generation
  - Cannot extend beyond ~40 seconds total (via 3 successive extend operations)
  - Content moderation auto-triggers on policy violations
- **What this enables:** Rapid video prototyping, cinematic stock footage generation, automated short-form content, product demos

#### **Gen-4 / Gen-3 Alpha & Turbo** (Legacy, still available)
- **Cost:** 
  - Gen-3 Alpha Turbo: 5 credits/second
  - Gen-3 Alpha (High Quality): 10 credits/second
  - Gen-4: 10–12 credits/second
- **Duration:** Up to 40 seconds (Gen-3 Alpha) or 34 seconds (Gen-3 Alpha Turbo) with extensions
- **Status:** Maintained; Gen-4.5 is the recommended bleeding edge
- **What this enables:** Cost-effective lower-quality proofs-of-concept; bulk content generation where quality tradeoff is acceptable

#### **GWM-1 (Generative World Model)** — Runway Characters, launched March 9, 2026
- **What it does:** Real-time interactive video agent API for conversational digital characters
- **Variants:**
  - GWM Worlds: explorable environments
  - GWM Avatars: conversational characters (the main hackathon draw)
  - GWM Robotics: robotic manipulation (experimental)
- **Input:** 
  - Character reference: single photorealistic or stylized image
  - Audio: spoken dialogue (audio-driven performance capture)
  - Optional motion control: camera pose, actions, interactive commands
- **Output:** Real-time video with natural motion, facial expressions, eye tracking, lip-sync
- **Key feature:** No fine-tuning required; zero-shot character transfer from image
- **Latency:** Real-time (low enough for interactive conversation)
- **Infrastructure:** Powered by Modal for multi-node GPU clusters with RDMA networking across regions
- **What this enables:** 
  - Interactive AI avatar systems (customer service, tutoring, entertainment)
  - Real-time video conversation agents
  - Zero-shot character animation from images
  - **Hackathon wildcard:** judges will weight novelty; Runway literally launched this March 9, 2026

### 1.2 Image Generation

#### **gen4_image**
- **What it does:** Multimodal image-generation model for prompted generation + visual references
- **Input:** 
  - Text prompt
  - Up to 3 reference images (to preserve identity, style, or location)
  - Reference syntax: at-mention in text (e.g., `@ref_image_1`)
- **Output:** High-quality controllable images with consistent style/identity
- **Cost:** 5 credits per image
- **Conditioning:** Text and reference embeddings fused in multimodal backbone; optional control signals (pose, depth, mask) supported
- **What this enables:** Style-locked character asset generation, batch portrait upscaling, concept art workflows

### 1.3 Advanced Editing & Manipulation

#### **Aleph** (in-context video model)
- **What it does:** High-fidelity cinematic video editing/generation (new as of 2025)
- **Capabilities:**
  - Edit specific subjects/objects/environments in footage
  - Add simple animations over static images (motion description → dynamic scene)
  - Visual style transformation (lighting, tone, texture, artistic style matching)
  - Scene angle and composition generation
- **Input:** Text prompts, reference images, source video clips
- **Cost:** Not separately disclosed; bundled under video generation tier
- **Constraint:** Intended for cinematic/professional work; slower than Gen-4.5
- **What this enables:** Professional video editing automation, visual style transfer, scene regeneration, VFX-free cinematic work

#### **Act-Two** (Motion Capture & Character Animation) — NEW, launched ~Feb 2026
- **What it does:** Performance capture model converting actor performance to character animation
- **Input:**
  - Driving performance: short video (webcam/phone) of someone acting a scene
  - Character reference: image or video of target character
- **Output:** Animated character with transferred body motion, facial expressions, hand gestures
- **Features:**
  - Full-body motion tracking (head, hands, torso)
  - Facial expression capture (eyes, mouth, micro-expressions)
  - Audio-visual sync (lip-sync) automatic
  - Works without fine-tuning
- **Latency:** "Seconds" (not specified; likely slower than Gen-4.5)
- **Cost:** Not separately disclosed
- **Constraint:** Requires driving video as input (not generative from text alone)
- **What this enables:**
  - Avatar animation pipelines (streamer-to-character transfer)
  - Accessible character animation without mocap suits
  - Accessibility features (act-by-proxy)
  - **Hackathon advantage:** Novel model; judges reward differentiation

#### **Remove Background**
- **What it does:** Automated background separation
- **Status:** Available (help articles exist); API endpoint accessible
- **Cost:** Likely bundled/minimal; exact credit cost not disclosed in API docs
- **What this enables:** Asset preparation, portrait isolation, compositing workflows

#### **Inpainting & Interpolation**
- **What it does:** 
  - Inpainting: remove/regenerate masked regions of images/video
  - Frame interpolation: smooth low-FPS footage or create slow-motion
- **Cost:** Likely bundled under image/video tier
- **Status:** Available in web app; API support varies by endpoint
- **What this enables:** Defect removal, slow-motion creation, content repair

#### **Super-Resolution & Upscaling**
- **What it does:** Increase resolution/quality of images and video
- **Cost:** 2 credits/second for 4K upscale (video); 5 credits per image (image upscale)
- **Constraint:** Cannot upscale beyond source content detail
- **What this enables:** Legacy content refresh, archive restoration, quality enhancement

### 1.4 Audio & Voice

#### **ElevenLabs Multilingual v2 Text-to-Speech** (via Runway, available Sept 25, 2025)
- **What it does:** Text → natural, emotionally-aware speech (29 languages)
- **Features:** Maintains consistent voice quality and personality across utterances
- **Cost:** Integrated into Runway credits (exact per-character cost not disclosed; likely proportional)
- **What this enables:** Global multilingual narration, accessible video content, voice-over automation

#### **ElevenLabs Voice Isolation**
- **What it does:** Strips background noise, isolates speech
- **Cost:** Bundled in Runway
- **What this enables:** Audio preprocessing, podcast/interview cleanup

#### **ElevenLabs Dubbing** (29 languages)
- **What it does:** Translate video to target language + AI voice maintains original speaker characteristics
- **Cost:** Integrated
- **What this enables:** Global content distribution without revoicing actors

#### **Custom Voice Training**
- **What it does:** Train a custom voice from a sample
- **Input:** 2–5 minute voice sample
- **Cost:** 300 credits per custom voice
- **What this enables:** Brand-specific narration, celebrity voice clones (within policy), consistent AI presenters

#### **Gen-4.5 Native Audio**
- **What it does:** Generate novel video WITH audio (dialogue, sound effects, background music)
- **Also:** Native audio editing for existing videos
- **Cost:** Included in Gen-4.5 generation cost (12 credits/second)
- **What this enables:** End-to-end video production (visual + audio) in single API call, audio-reactive animations

#### **Seedance 2.0 Audio Support** (via Runway, Feb 2026)
- **Status:** Integration announced; direct API not yet public (ByteDance disputes ongoing)
- **What it enables:** Keyframe control + audio conditioning for video (if integrated)

### 1.5 Experimental / Emerging

#### **Frames** (mentioned in early hackathon docs; status unclear)
- **What it does:** Likely per-frame generation or manipulation
- **Maturity:** Unknown; may not be stable API
- **Hackathon note:** If available, explore but with caution

---

## 2. RUNWAY API MECHANICS

### 2.1 Request/Response Model

- **Async task-based workflow (no streaming):**
  - Submit generation request → get back Task ID
  - Poll `/v1/tasks/{id}` for status (recommended: ≥5 second intervals with exponential backoff + jitter)
  - Status returns: `pending`, `in_progress`, `succeeded`, `failed`
  - On `succeeded`, extract output URL(s)
  - Default timeout: 10 minutes (can be customized per SDK)

- **Why no streaming:** Video/image generation requires significant compute; not progressively deliverable like text

### 2.2 Rate Limits & Quotas

- **No hard RPM limit** (unlike OpenAI), but:
  - Bounded by daily credit budget
  - 429 (Too Many Requests) returned if daily generation limit exceeded
  - Requests should tolerate 429 + exponential backoff
- **Polling safety:** Don't poll faster than 5-second intervals; adds jitter to avoid thundering herd

### 2.3 Webhooks

- **Available for Enterprise tiers and above** (not clear if hackathon participants get this)
- **Pattern:** Register endpoint URL + select event types
- **Implementation partner:** Svix (managed webhook delivery, retry logic, signature verification)
- **Example use case:** CI/CD trigger (release completed → GitHub Actions)
- **What this enables:** Async pipeline automation without polling overhead

### 2.4 Input Handling

#### **Reference Images**
- Supported as base64 data URIs or HTTPS URLs
- Up to 3 per generation (on supported models like gen4_image)
- At-mention syntax in prompts

#### **Video Inputs**
- Supported for image-to-video, video-to-video, inpainting
- Formats: likely MP4, MOV, WebM (check docs for exact list)
- Max duration: varies by endpoint (typically matches output max)

#### **Audio Inputs**
- Supported for Characters (GWM-1)
- Required for Act-Two (driving performance)
- Format: likely MP3, WAV, M4A

### 2.5 Output Formats

- **Video:** MP4 (H.264 encoded); downloadable URL returned
- **Images:** JPEG or PNG (format varies by model)
- **Metadata:** All outputs include generation metadata (seed, model version, etc.) for reproducibility

### 2.6 SDKs & Libraries

- **Official SDKs:** Python, JavaScript/Node.js
- **Package manager:** npm (JavaScript), pip (Python)
- **Language bindings:** Community bindings exist (e.g., Go, Rust)
- **Sample code:** Available in dev portal quickstart

---

## 3. PRICING & CREDITS

### 3.1 Credit System

- **Rate:** $0.01 per credit
- **Minimum purchase:** $10 (1,000 credits)
- **Purchase method:** Dev portal billing tab
- **Separate pools:** Web app credits ≠ API credits (keep them segregated)

### 3.2 Cost Breakdown (Per-Generation)

| Model/Task | Cost | Notes |
|---|---|---|
| Gen-4.5 base (5 sec) | 60 credits | $0.60 |
| Gen-4.5 base (10 sec) | 120 credits | $1.20 |
| Gen-4.5 upscale to 4K | 2 credits/sec | Add $0.10–0.20 per generation |
| gen4_image | 5 credits | Single image |
| Aleph (cinematic) | ~12 credits/sec | Estimated; not confirmed |
| Act-Two | Unknown | Estimate $1–3/generation |
| ElevenLabs voice | ~0.5 credits/100 chars | Estimate |
| Custom voice training | 300 credits | One-time per voice |
| Inpaint/Interpolate | 2–5 credits | Varies |
| Remove background | <5 credits | Bundled; minimal |

### 3.3 Hackathon Credits

- **Allocation:** 200K credits per team (estimated; unconfirmed in official rules)
- **Equivalent spend:** ~$2,000
- **Runway Builders Program:** Seed-to-Series-C startups get additional credits + higher rate limits
- **Eligibility:** Check official rules at [Runway API Hackathon Terms](https://runwayml.com/api-hackathon-terms)

### 3.4 Implications for Hackathon

- **Budget:** 200K credits = ~1,667 full Gen-4.5 10-second videos (120 credits each)
- **Strategy:** Prioritize Gen-4.5 for visual quality; use Gen-3 Turbo for bulk/iteration
- **Constraint:** Run-out of credits mid-hackathon = no generation; plan credit usage carefully

---

## 4. CONTENT MODERATION & LIMITATIONS

### 4.1 Automated Moderation

- **Scope:** Scans inputs AND outputs
- **System:** Hybrid (automated + human review for edge cases)
- **Response:** Requests rejected or output artifacts suppressed
- **False positive recovery:** Can add client-side moderation before API call to avoid suspension

### 4.2 Blocked Content Categories

- Nudity, obscenity, overly provocative imagery
- Violence, gore, blood, viscera
- Sexually explicit content
- Offensive subject matter
- **Public figures:** Recognizable faces of living public figures (configurable per request via `contentModeration` object)
- **Living artists:** Recognizable artistic style of living artists (can be overridden)
- **Child safety (absolute):** Any CSAM or sexualization of minors triggers:
  - Indefinite account suspension
  - Report to NCMEC + global law enforcement
  - **Non-negotiable.**

### 4.3 Account Suspension

- **Trigger:** Multiple rejected moderation requests from same account
- **Recovery:** Implement pre-filtering before calling API
- **Best practice:** Proactively filter user inputs in your app

### 4.4 Policy Configuration

- **Content moderation object:** Include in API requests to control strictness level (default: strict)
- **Use case:** If your app specifically targets documentaries or educational content, you can tune moderation parameters

### 4.5 Practical Constraints

- **Maximum video duration per generation:** 10 seconds (extendable via chaining; max ~40 sec total)
- **Video quality:** Runs lower on speed/quality tradeoff; if you need >10 sec at ultra-high quality, plan multiple chains
- **Audio generation:** Limited to natural dialogue + SFX + ambient; abstract/experimental audio not exposed
- **Image-to-video:** Requires visible character/subject in reference image; won't animate abstract patterns well

---

## 5. RUNWAY SKILLS FRAMEWORK

### 5.1 What It Is

- **Format:** Open-source framework for packaging reusable agent tasks
- **Repository:** [runwayml/skills on GitHub](https://github.com/runwayml/skills)
- **Purpose:** Enable agents (Claude, ChatGPT, etc.) to call Runway API without manual prompt engineering

### 5.2 Structure

Each skill is a folder containing:
- `SKILL.md` (required): Metadata (name, description) + instructions for agent
- Scripts: Executable code (Python/JavaScript) bundled in skill
- References: Documentation, examples, edge-case handlers
- Assets: Templates, prompts, style guides

### 5.3 How Agents Load & Use Skills

1. **Discovery:** Agent loads only skill name + description (lightweight)
2. **Activation:** When task matches description, agent reads full `SKILL.md` into context
3. **Execution:** Agent follows instructions, optionally executes bundled code or references files

### 5.4 Available Skills (Sampling)

The GitHub repo lists open-source skills for:
- Media generation at scale
- Multi-model orchestration (Gen-4.5, Act-Two, Aleph)
- Webhook setup & async handling
- Batch video processing
- Prompt engineering for cinematic quality

### 5.5 How to Use in Hackathon

- **Clone the repo:** `git clone https://github.com/runwayml/skills`
- **Read README:** Describes framework + available skills
- **Extend:** Add your own custom skills for your hackathon pipeline
- **Integration:** Your AI agent (or your code) loads skills to call Runway endpoints

### 5.6 Framework Requirements

- **Python:** 3.8+; run via `uv` (Python package runner)
- **Environment:** Set `RUNWAYML_API_SECRET` (your API key)
- **Backend (optional):** If adding server-side integration skills, need Node.js 18+ or Python framework

### 5.7 What This Enables

- **Agent-native workflows:** Describe "create a 30-second product video" to Claude; it uses skills to orchestrate Gen-4.5 + audio + webhooks
- **Reproducibility:** Skills version-controlled in Git; team collaboration
- **Modularity:** Swap components (e.g., Gen-4.5 → Act-Two) without rewriting agent prompts

---

## 6. MODAL: INFRASTRUCTURE FOR HACKATHON

### 6.1 What Modal Provides

- **Serverless GPU cloud:** Run code on A100, H100 GPUs on demand
- **Autoscaling:** Instant scale-up/down; pay per second (no idle charges)
- **Multi-region:** Deploy once, route requests globally (low latency)
- **Webhook support:** HTTP endpoints that trigger functions; queue-based for reliability
- **RDMA networking:** Low-latency inter-GPU communication (critical for Runway's Characters/GWM-1)

### 6.2 GPU Pricing (As of May 2026)

| GPU | Per-Second | Per-Hour | Notes |
|---|---|---|---|
| **H100** | $0.001097 | $3.95 | High-end; needed for real-time inference |
| **A100 80GB** | $0.000694 | $2.50 | Mid-range; good price-to-performance |
| **A100 40GB** | $0.000583 | $2.10 | Entry-level GPU; sufficient for batch jobs |

### 6.3 Production Multipliers

- **Regional multiplier:** 1.25x (US/EU/UK/AP) to 2.5x (other regions)
- **Non-preemptible multiplier:** Up to 1.5x (guaranteed availability)
- **Combined worst-case:** 3.75x (your $2.10/hour A100 becomes $7.87/hour in production US)
- **Implication:** Budget accordingly; test costs carefully

### 6.4 Concurrency Limits (Plan-Dependent)

| Plan | Monthly Cost | Max Concurrent GPUs | Max Containers |
|---|---|---|---|
| **Starter** | Free | 10 | 100 |
| **Team** | $250 | 50 | 1,000 |

- **Starter tier:** Sufficient for hackathon (single model inference)
- **Team tier:** Needed if running multiple inference servers or parallel batch jobs

### 6.5 Modal + Runway Integration (Runway Characters Case Study)

**Pattern:** Runway Characters (GWM-1) uses Modal under the hood:
- **What happens:**
  1. Your app calls Runway Characters API with audio + character image
  2. Runway routes request to Modal GPU cluster (nearest region)
  3. Modal spins up container, runs GWM-1 inference, streams output back
  4. Runway caches result, returns to your app
- **Why it matters:** Runway offloads infrastructure; your app only manages API calls
- **Hackathon implication:** You can either:
  - Use Runway API directly (Modal hidden; Runway manages cost)
  - Deploy your own Modal function to preprocess inputs or post-process outputs (you pay Modal directly)

### 6.6 Webhook/Queue Pattern for Hackathon

**Typical pipeline:**
```
User uploads video
  ↓
Your app → Modal HTTP endpoint (webhook)
  ↓
Modal function queues job to Runway API
  ↓
Polls Runway task status
  ↓
On completion, post-process result (crop, burn subtitles, etc.)
  ↓
Return to user
```

**Cost breakdown:**
- Runway API call: credits (your 200K allocation)
- Modal invocation: $0.20 per million requests + per-second GPU compute if you use GPU in post-processing
- Bandwidth: $0.12 per GB out (if streaming video to users; factor into cost model)

### 6.7 Modal Templates & Examples

- **Runway-specific starter:** Not officially published as of April 2026
- **Workaround:** Combine Modal's [web endpoints docs](https://modal.com/docs/guide/webhooks) + Runway SDK
- **Community:** Expect hackathon participants to share examples on GitHub

---

## 7. RECENT LAUNCHES & CUTTING-EDGE MODELS (Last 90 Days, as of April 2026)

### 7.1 February 10, 2026: Gen-4.5 Release

**Significance:** Main announcement of the hackathon period
- **Improvements over Gen-4:**
  - Native audio generation + editing (no separate ElevenLabs call needed)
  - Higher fidelity (especially faces, hands, lighting consistency)
  - 2–10 second durations (vs. previous Gen-4 limits)
  - Real-time 1080p preview (major UX shift)
- **Cost:** 12 credits/second (same as Gen-4; not cheaper, but better quality)
- **Integration:** Immediate availability via Runway API

### 7.2 March 9, 2026: Runway Characters (GWM-1)

**Significance:** NEWEST & HIGHEST NOVELTY for hackathon judges

- **Model class:** Generative World Model (autoregressive, real-time)
- **Capability shift:** From "generate any video" to "generate INTERACTIVE, CONTROLLABLE video agents"
- **Key differentiator:** Audio-driven + motion capture + interactive control (camera pose, actions)
- **Infrastructure:** Modal powers multi-region deployment with RDMA for low latency
- **Implications for hackathon:**
  - Judges explicitly want to see novel uses of Characters
  - Real-time interactive demos (vs. batch processing) = higher visual impact in pitch
  - Zero-shot character transfer from images is a game-changer for creators

### 7.3 ~Feb–Mar 2026: Act-Two API Release

**Significance:** Performance capture now available via API (was web-only)

- **Unique capability:** Only model that captures ACTOR PERFORMANCE and transfers to character
- **Differentiation:** No other major API (Veo, Kling, Seedance) offers this
- **Hackathon angle:** Build "instant influencer" tool or "accessible animation for creators"
- **Challenge:** Requires driving performance video input (not pure generative)

### 7.4 Sept 25, 2025 (But Still Fresh): ElevenLabs Integration

- **What's new:** ElevenLabs v2 + Voice Isolation + Dubbing now available via single Runway API call
- **Implication:** Multilingual, dubbing-capable video generation in single pipeline

### 7.5 NOT Available (But Rumored/Announced)

- **Seedance 2.0 official API:** ByteDance has not released; legal disputes ongoing
  - Third-party platforms integrated it (ModelsLab, etc.), but not through Runway API directly
  - Status: Not hackathon-ready
- **Sora 2:** OpenAI model; not available via Runway API
- **Kling 3.0:** Kuaishou model; not directly integrated (though third-party APIs offer it)

---

## 8. KNOWN GOTCHAS & LIMITATIONS

### 8.1 Duration & Extension Gotchas

- **Per-request max:** 10 seconds (Gen-4.5), 10 seconds (Gen-4)
- **Extension limit:** Max 3 successive extend operations → ~40 seconds total
- **Cost multiplier:** Each extension costs credits (e.g., 3x 10-second extends = 4x the base cost)
- **Implication:** Plan sequences carefully; 60-second video = 4–6 sequential generations + cost

### 8.2 Latency Reality Check

- **Gen-4.5 worst-case:** 30–60 seconds (depending on region, queue depth)
- **Characters real-time:** Marketed as real-time, but "real-time" means <500ms per frame in optimal conditions; network latency adds overhead
- **Aleph (cinematic):** Slower than Gen-4.5; estimate 60–120 seconds
- **Act-Two:** Unknown; estimate similar to Aleph

**Hackathon implication:** Don't build live-streaming products expecting <1-second latency; batch processing is more realistic

### 8.3 Content Moderation False Positives

- **Public figures:** Any recognizable face → auto-block (configurable, but risky)
- **Implication:** If your hackathon project involves celebrity avatars, you'll need explicit moderation configuration or face rejections
- **Account risk:** Too many rejections = suspension; test thoroughly with friendly content first

### 8.4 Credits Depletion

- **Hackathon allocation:** 200K credits
- **Default behavior:** When credits run out, all requests fail with 402 (Payment Required)
- **No free tier:** If you exceed, you either stop or buy more credits ($10 min)
- **Implication:** Implement credit tracking; warn users when approaching limit

### 8.5 Reference Image Quality

- **Best results:** High-res, well-lit, center-framed reference images
- **Failure cases:** Blurry references, extreme angles, artistic abstractions don't transfer well
- **Act-Two driving video:** Must have visible face + body; extreme angles/occlusion fail
- **Implication:** Pre-process user inputs; add quality checks

### 8.6 Audio Sync Issues

- **Characters + ElevenLabs audio:** Lip-sync is automatic, but can drift if input audio is heavily processed (pitch-shifted, time-stretched)
- **Gen-4.5 audio generation:** Novel dialogue generally works; background music/SFX quality varies
- **Implication:** Test audio + video sync in your pipeline before launch

### 8.7 Prompt Brittleness

- **Gen-4.5 & Aleph:** Quality heavily depends on prompt engineering (similar to image diffusion models)
- **No official prompting guide:** Must experiment; community examples inconsistent
- **Implication:** Budget 10–20% of hackathon time for prompt tuning

### 8.8 API Stability

- **Runway API:** Generally stable (used by thousands); occasional rate-limit surprises
- **GWM-1 (Characters):** New (March 2026); possible edge case bugs
- **Act-Two:** Very new; may have stability surprises
- **Implication:** Test all three major models under load before relying on them for final demo

---

## 9. DEVELOPER EXPERIENCE & ONBOARDING

### 9.1 Developer Portal (https://dev.runwayml.com)

- **Sign-up:** Email address + password; no credit card required immediately
- **Organization setup:** Create org → receive API key
- **Credentials:** API key is single-use (show once, copy to `.env`)
- **Billing:** Add payment method to org; set credit balance (minimum $10)

### 9.2 SDKs & Sample Code

- **Python SDK:** `pip install runway-python`
- **JavaScript SDK:** `npm install @runwayml/sdk`
- **Quickstart guides:** Available in developer portal
- **Code samples:** Gen-4.5, Characters, Act-Two examples provided

### 9.3 Documentation Quality

- **API Reference:** Comprehensive; endpoint parameters well-documented
- **Guides:** Setup, pricing, usage tiers, content moderation clearly explained
- **Changelog:** API changelog updated regularly; track new endpoints
- **Gaps:** Prompt engineering guide lacking; Act-Two docs sparse (model very new)

### 9.4 Community & Support

- **Discord/Slack:** Runway operates community channels
- **GitHub Issues:** runwayml/skills repo accepts issues
- **Email support:** For paid customers; response time ~24–48 hours
- **Hackathon-specific:** Expect live support channel during hackathon (check rules page)

---

## 10. STRATEGIC IMPLICATIONS FOR HACKATHON

### 10.1 Compete-to-Win Signals

**What judges will reward:**

1. **Use Cases for GWM-1 (Runway Characters):**
   - Interactive AI agents (customer service, tutoring, entertainment)
   - Real-time conversational video (streaming-ready)
   - Any demo showing <500ms latency or interactive control is high visual impact
   - **Why:** Model is brand-new; judges want to see creativity

2. **Act-Two Performance Capture:**
   - "Everyone can be a YouTuber" tools (act, animate, publish)
   - Accessibility features (dictation-to-performance)
   - Digital double creation for creators
   - **Why:** Unique differentiation; no other major API has this

3. **Gen-4.5 + Audio End-to-End:**
   - Script-to-video pipelines (prompt → video + narration in one call)
   - Multilingual content distribution (Dubbing)
   - Any product that ships to users with zero manual post-processing
   - **Why:** Demonstrates production-ready thinking

4. **Async/Batch Workflows:**
   - Bulk content generation (e.g., "personalize 1000 product videos in 1 hour")
   - Webhook-based pipelines (Runway → Modal → Your processor → User)
   - **Why:** Scalability + infrastructure maturity

5. **What NOT to do:**
   - "Yet another Gen-4.5 demo" (old news; judges have seen this)
   - Overreliance on fancy prompts without product value
   - Ignore content moderation (auto-suspension risk)

### 10.2 Credit Allocation Strategy

- **200K credits ÷ 120 (cost per 10-sec Gen-4.5) = ~1,667 clips**
- **Allocation recommendation:**
  - 40% (80K): Gen-4.5 for main product feature
  - 30% (60K): Gen-3 Turbo for rapid iteration + testing
  - 20% (40K): Characters + Act-Two experimentation
  - 10% (20K): Contingency + post-processing (upscale, inpaint, audio)

### 10.3 Technical Debt to Avoid

- **Don't build real-time UI expecting <1-second latency:** Use job queue + notifications instead
- **Don't rely on public figures without moderation config:** Risk auto-rejection + suspension
- **Don't skip content moderation testing:** One bad request = multiple rejections = account at risk
- **Don't run out of credits:** Track usage in real-time; warn users

### 10.4 Integration Checkpoints

Before final submission:
1. **Test all 3 major model paths:** Gen-4.5, Characters, Act-Two (if using)
2. **Load test:** Run 10 parallel requests; monitor for 429s or timeouts
3. **Content moderation:** Submit test inputs across edge cases (faces, violence, text); verify behavior
4. **Latency measurement:** Time full pipeline (API call → output); document in pitch
5. **Credits burned:** Calculate true cost of your product at scale (not just base cost)

---

## 11. SOURCES & REFERENCES

**Official Runway:**
- [Runway API Documentation](https://docs.dev.runwayml.com/)
- [Runway Developer Portal](https://dev.runwayml.com/)
- [API Pricing & Costs](https://docs.dev.runwayml.com/guides/pricing/)
- [API Changelog](https://docs.dev.runwayml.com/api-details/api_changelog/)
- [Content Moderation](https://docs.dev.runwayml.com/api-details/moderation/)

**Runway Announce:**
- [Runway API Hackathon](https://runwayml.com/api-hackathon)
- [Runway Characters News](https://runwayml.com/news/introducing-runway-characters)
- [Introducing GWM-1](https://runwayml.com/research/introducing-runway-gwm-1)
- [Introducing Act-Two](https://help.runwayml.com/hc/en-us/articles/42311337895827-Creating-with-Act-Two)

**Runway Skills:**
- [GitHub: runwayml/skills](https://github.com/runwayml/skills)

**Modal:**
- [Modal Homepage](https://modal.com/)
- [Modal Pricing](https://modal.com/pricing)
- [Modal GPU Docs](https://modal.com/docs/guide/gpu)
- [Modal Blog: Runway Characters](https://modal.com/blog/runway-chooses-modal-to-power-real-time-inference-for-runway-characters)

**WebSearch Articles:**
- [Runway Pricing in 2026](https://www.somake.ai/blog/runway-ai-pricing)
- [Gen-4.5 Guide](https://aitoolsdevpro.com/ai-tools/runway-guide/)
- [AI Video Generation Model Comparison 2026](https://resource.digen.ai/ai-video-generation-model-comparison-2026/)

---

## SUMMARY: What You Can Actually Build (May 8–11, 2026)

**In scope:**
- Interactive AI video agents (Characters; real-time; judges will love this)
- Performance capture → animation pipelines (Act-Two; unique; novel)
- Batch short-form content generation (Gen-4.5; scalable; production-ready)
- Multilingual video distribution (Gen-4.5 + ElevenLabs)
- Professional cinematic video editing (Aleph; slower but high-fidelity)
- Accessibility tools (Act-Two for motion, Characters for presence)

**Out of scope (infrastructure limitations):**
- Real-time 60+ second video (max ~40 sec via extensions; slow)
- Live-streaming (latency too high; 30–120 sec per generation)
- Sora/Kling/Seedance direct integration (not available via Runway API)
- Extreme personalization at <100ms latency (not possible; batch/queue instead)

**Competitive advantage (for judges):**
- **Heavy use of Characters + Act-Two** (newest models; highest novelty weight)
- **Interactive demo** (not just batch processing; shows real-time capabilities)
- **End-to-end product** (not just API showcase; something creators/businesses would use)
- **Thoughtful scaling story** (Modal + webhooks; shows production maturity)

**Timeline consideration:**
- Gen-4.5: Stable, proven, safe bet
- Characters: Brand-new (March 2026); some edge cases possible; worth the risk for novelty
- Act-Two: Very new; fewer examples; higher reward if you nail it

---

**Document prepared:** April 20, 2026  
**Hackathon dates:** May 8–11, 2026  
**Next step:** Review [official rules](https://runwayml.com/api-hackathon-terms) for exact credit allocation, submission format, and judging criteria.
