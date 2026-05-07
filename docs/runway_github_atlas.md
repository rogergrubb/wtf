# Runway GitHub Organization Audit
## Complete Hackathon Intelligence Report

**Date:** 2026-05-05  
**Scope:** github.com/runwayml (61 repositories)  
**Focus:** Hackathon edge — models, SDKs, agent patterns, skills framework, and external adoption

---

## Executive Summary

Runway's GitHub organization reveals a tightly-focused API-first strategy centered on **three pillars**:

1. **Skills Framework** — Agent-native code patterns for media generation and integration
2. **SDKs** — Lightweight, well-maintained libraries for Python and Node.js
3. **Real-Time Avatars** — GWM-1 characters with embedded React components and LiveKit integration

**Hackathon Opportunity:** The `skills` repository is the endorsed developer pattern. It ships with runnable generation scripts, integration templates, and explicitly targets Claude Code, Cursor, and other AI agents. **This is your primary edge.**

---

## Repository Inventory (61 Total)

### Tier 1: High Stars & Recent Activity (Hackathon Priority)

| Repo | Language | Stars | Last Commit | Status | Purpose |
|------|----------|-------|-------------|--------|---------|
| **guided-inpainting** | Python | 243 | 2026-02-22 | Active Research | Keyframe propagation / video editing research — high quality but archived |
| **RunwayML-for-Photoshop** | TypeScript | 159 | 2026-04-25 | Active | Official Photoshop plugin using Runway API — clean, maintained integration pattern |
| **RunwayML-for-Unity** | C# | 196 | 2025-12-09 | Maintained | Game engine integration — reference for modal/callback patterns |
| **ofxRunway** | Makefile | 103 | 2025-09-13 | Archived | openFrameworks integration |
| **p5js** | JavaScript | 102 | 2026-02-23 | Archived | p5.js creative coding library integration |
| **javascript** | JavaScript | 101 | 2026-05-04 | Active | RunwayML + JavaScript (no README — likely starter template) |
| **learn** | Documentation | 141 | 2025-09-20 | Reference | Official learning resources & tutorials |
| **model-sdk** | Python | 106 | 2025-09-20 | Legacy | Port custom ML models to Runway (deprecated in favor of new API) |

### Tier 2: SDK & Integration Core (Critical for Hackathon)

| Repo | Language | Stars | Last Commit | Status | Purpose |
|------|----------|-------|-------------|--------|---------|
| **skills** | Python | 30 | 2026-05-02 | **ACTIVE** | **Agent-native skills framework** — generation + integration patterns |
| **sdk-python** | Python | 26 | 2026-05-03 | **ACTIVE** | Official Python SDK — v4.13.0, async support, type-safe |
| **sdk-node** | TypeScript | 18 | 2026-05-03 | **ACTIVE** | Official Node.js SDK — v3.20.0, full TypeScript types |
| **avatars-sdk-react** | TypeScript | 17 | 2026-04-24 | **ACTIVE** | React component for GWM-1 avatars — v0.14.0 |
| **runway-api-mcp-server** | TypeScript | 17 | 2026-04-23 | Active | MCP server wrapper for Runway API — Claude integration |
| **confingy** | Python | 27 | 2026-04-21 | Active | Implicit configuration system — used by skills framework |
| **try-on-chrome-extension** | JavaScript | 45 | 2026-04-21 | Active | Virtual try-on demo — image processing example |
| **hair-makeover-api-demo** | TypeScript | 33 | 2026-01-17 | Active | Image-based makeover demo — reference for image generation |

### Tier 3: Agent & Real-Time Frameworks (Emerging)

| Repo | Language | Stars | Last Commit | Status | Purpose |
|------|----------|-------|-------------|--------|---------|
| **runway-agents-js** | TypeScript | 0 | 2026-05-01 | **NEW** | Node.js agents framework — multimodal AI agents, real-time WebRTC |
| **livekit-agents** | Python | 0 | 2026-05-01 | **NEW** | Voice AI agents framework (Python, part of LiveKit) — STT/TTS/LLM plugins |
| **avatars-node-rpc** | TypeScript | 0 | 2026-04-15 | New | RPC handler for avatar backend tool calls — server-side event handling |
| **runway-pipecat** | (metadata only) | 0 | 2026-04-14 | New | Pipecat framework integration (voice/multimodal conversational AI) |
| **runway-studio-skills** | Python | 0 | 2026-04-20 | New | Runway Studio skills (internal tool integration) |

### Tier 4: Character & Avatar Integrations

| Repo | Language | Stars | Last Commit | Purpose |
|------|----------|-------|-------------|---------|
| **runway-characters-meet** | HTML | 3 | 2026-04-28 | Character video meeting demo |
| **runway-characters-meeting-skill** | Python | 0 | 2026-04-05 | Skill for multi-character interactions |
| **openclaw-skills** | TypeScript | 2 | 2026-04-28 | OpenClaw agent skill framework |
| **openclaw-skill-send-video-message** | Python | 0 | 2026-03-26 | Video message skill for agents |

### Tier 5: Creative Tool Plugins (Reference Only)

Processing, Max/MSP, Grasshopper, Pure Data, Arduino, OpenRNDR, Touch Designer — all **archived or minimally maintained**. Useful for understanding Runway's plugin architecture but not active development.

### Tier 6: Infrastructure & Utilities (Not Relevant for Hackathon)

Kubernetes adapters, Terraform modules, AWS utilities, AWS Secrets, CI/CD helpers. Skip these.

---

## Deep Dive: The Skills Framework (Your Primary Edge)

**Location:** `github.com/runwayml/skills`  
**Latest commit:** 2026-05-02 (3 days ago)  
**Recent work:**
- Security fixes (Snyk W007/W011 in video/image skills)
- Runnable scripts for media generation at scale
- Seedance2 model integration
- Agent-centric improvements

### Available Skills (18 Total)

**Generation Skills (Runnable, Single-Step):**
- `rw-generate-video` — Text/image/video-to-video with seedance2, gen4.5, veo3, veo3.1, gen4_turbo, gen4_aleph
- `rw-generate-image` — Text-to-image with gen4_image, gen4_image_turbo, gemini_2.5_flash
- `rw-generate-audio` — TTS, sound effects, voice isolation, dubbing, voice conversion (ElevenLabs models)

**Integration Skills (Add to Backend):**
- `rw-integrate-video` — Server-side video generation endpoints (Express, FastAPI examples)
- `rw-integrate-image` — Server-side image generation
- `rw-integrate-audio` — Server-side audio generation
- `rw-integrate-uploads` — Local file upload to Runway's ephemeral storage
- `rw-integrate-characters` — GWM-1 avatar creation and real-time session management
- `rw-integrate-character-embed` — React SDK embedding for avatar calls
- `rw-integrate-documents` — Knowledge base / domain-specific context for avatars

**Setup & Utility Skills:**
- `rw-recipe-full-setup` — Complete integration guide (compatibility → API key → implementation)
- `rw-setup-api-key` — Account creation and SDK configuration
- `rw-check-compatibility` — Analyze project stack for API compatibility (requires server-side)
- `rw-check-org-details` — Query credit balance, rate limits, usage tier
- `rw-api-reference` — Complete API reference (models, endpoints, costs, limits)
- `rw-fetch-api-reference` — Live API reference fetcher
- `use-runway-api` — Direct API access from agent (no SDK needed)

### Code Patterns

**Generation Script Pattern (Python):**
```python
# From rw-generate-video skill
import os
from runwayml import RunwayML

client = RunwayML(api_key=os.environ.get("RUNWAYML_API_SECRET"))

task = client.image_to_video.create(
    model="gen4_turbo",
    prompt_image="https://example.com/image.jpg",
    ratio="1280:720",
    prompt_text="Description of motion",
)
print(f"Task ID: {task.id}")
# Poll task.retrieve() until completed
```

**Integration Pattern (Node.js, Next.js):**
```typescript
// Server-side route
import RunwayML from '@runwayml/sdk';

const client = new RunwayML({
  apiKey: process.env.RUNWAYML_API_SECRET
});

export async function POST(req: Request) {
  const { prompt, model } = await req.json();
  const task = await client.imageToVideo.create({
    model,
    promptText: prompt,
    ratio: '1280:720',
  });
  return Response.json({ taskId: task.id });
}
```

**Avatar Pattern (React):**
```tsx
import { AvatarCall } from '@runwayml/avatars-react';

export default function AvatarPage() {
  return (
    <AvatarCall
      avatarId="music-superstar"
      connectUrl="/api/avatar/connect"
    />
  );
}
```

### Critical Findings for Hackathon

1. **Skills are agent-first** — Explicitly designed for Claude Code, Cursor, and compatible agents
2. **Runnable scripts** — You can generate media directly without building an app first
3. **Server-side requirement** — All API calls must come from your backend (not browser)
4. **Billing required** — Must prepay $10 minimum (1,000 credits) before any generation works
5. **Task-based async pattern** — All generations are async; you submit, poll for completion, download result
6. **Model ecosystem** — 7 video models (seedance2, gen4.5, veo3, veo3.1, etc.), 3 image models, 5 audio models

---

## Core SDKs: Quality & Adoption

### Python SDK (runwayml)

**Latest:** v4.13.0 (2026-04-27)  
**Maturity:** Production-ready  
**Key features:**
- Synchronous and asynchronous clients (httpx + optional aiohttp)
- Full type hints (generated with Stainless)
- Supports all API endpoints: video, image, audio, uploads, characters, documents
- Auto-polling with `.wait_for_task_output()`
- Comprehensive error handling (BadRequestError, AuthenticationError, RateLimitError, etc.)

**Recent commits:**
```
feat: support setting headers via env
fix: use correct field name format for multipart file arrays
```

**Issues:**
- #202: licensing/copyright documentation needed
- #201: HTTP client reuse for storage uploads

### Node.js SDK (@runwayml/sdk)

**Latest:** v3.20.0 (2026-04-15)  
**Maturity:** Production-ready  
**Key features:**
- Full TypeScript support (no `any` types)
- Drop-in seedance2 support (2026-04-15 release)
- Request & response type definitions
- Error hierarchy (APIError, BadRequestError, etc.)
- NPM: https://npmjs.org/package/@runwayml/sdk

**Recent commits:**
```
feat(api): seedance2 model support
fix(api): remove spurious api param
```

### React SDK (@runwayml/avatars-react)

**Latest:** v0.14.0 (2026-04-24)  
**Maturity:** Active, feature-rich  
**Key features:**
- Drop-in AvatarCall component (handles WebRTC, session management)
- 10+ pre-built avatars (music-superstar, cat-character, fashion-designer, etc.)
- CSS variable theming
- Transcript hooks (`useTranscript`)
- Client event tools for interactive agents
- RPC support for backend communication
- 7 complete Next.js examples included

**Recent commits:**
```
feat(tools): accept Standard Schema v1 for client tool args
chore: use bun test runner (dropping vitest)
docs(agents): refine transcription from recent sessions
```

---

## Agent Frameworks (Emerging Edge)

### LiveKit Agents (Python & Node.js)

**Status:** Actively developed (commits 2026-05-01)  
**Purpose:** Voice & multimodal conversational AI framework  
**Key capabilities:**
- Real-time WebRTC agent framework
- Plugin ecosystem: OpenAI, Google, Deepgram, Cartesia, Neuphonic, Rime, Inworld, Silero, LiveKit, Anam, Bey, LemonSlice, LiveAvatar
- Semantic turn detection (transformer-based)
- RPC and Data API support
- Telephony integration (SIP)
- MCP (Model Context Protocol) support

**Hackathon angle:** If you're building voice agents, LiveKit Agents is the recommended runtime. Runway's character/avatar system can plug into this.

### Runway Agents JS (Node.js)

**Status:** NEW (2026-05-01 creation, but commits weekly)  
**Purpose:** Node.js distribution of LiveKit Agents for realtime AI agents  
**Features:**
- Realtime, multimodal participants (see, hear, understand)
- Flexible STT/LLM/TTS integrations
- Semantic turn detection
- WebRTC clients for all platforms

---

## Recent Commits & Active Work (Last 90 Days)

### Most Active Repos

1. **livekit-agents** — Weekly commits (STT/TTS plugins, interruption handling, SIP improvements)
2. **runway-agents-js** — Weekly commits (dependency updates, inference fixes)
3. **avatars-sdk-react** — Semi-weekly commits (tool args, transcription, testing)
4. **skills** — Every ~3 weeks (security fixes, runnable scripts, model additions)
5. **sdk-python** & **sdk-node** — Regular maintenance (new model support, bug fixes)

### Notable Commits

**Skills (agent framework):**
- "Media generation: runnable scripts for media generation at scale" (2026-04-16) — **Direct agent execution**
- "Make use-runway-api self-contained" (2026-04-17) — **No SDK dependency**
- "Address Snyk W007/W011 findings" (2026-04-21) — Security hardening

**SDKs:**
- "feat: seedance2" (sdk-node 2026-04-15) — New video model
- "feat: support setting headers via env" (sdk-python 2026-04-27) — More flexible auth
- "feat(tools): accept Standard Schema v1" (avatars-react 2026-04-22) — Modern schema validation

---

## External Projects Building on Runway

**Search results:** Community projects using Runway's SDKs

| Project | Stars | Language | Purpose |
|---------|-------|----------|---------|
| **mcp-video-gen** | 17 | TypeScript | MCP server for Luma + Runway video generation |
| **gimp-plugin-runway** | 13 | C | GIMP plugin integration |
| **runwayml-gazecapture** | 31 | Python | Eye tracking model ported to Runway |
| **Gen1 (Stable Diffusion inpainting)** | 26 | Python | Content-guided video synthesis |
| **cog-stable-diffusion-inpainting** | 19 | Python | SD inpainting on Runway |
| **openpifpaf** | 11 | Python | Pose estimation port |
| **runwayml-local-api** | 6 | Python | Local API wrapper |

**Pattern:** Most external projects are **model ports** (bringing academic research into Runway) or **tool integrations** (GIMP, MCP).

---

## Issues & Known Gotchas

### SDK Issues (Minor)

1. **sdk-python #201:** HTTP client not reused for multipart uploads — inefficient for batch operations
2. **sdk-python #202:** Licensing documentation incomplete
3. **sdk-node #156:** Release v3.20.1 pending (routine)
4. **avatars-react #27:** Client event tools fail with pt-BR accents instead of clear error

### No Critical Blockers

Skills repo has **zero open issues** — very clean, well-maintained state.

---

## Model Ecosystem & Cost Structure

### Video Models (7 Options)

| Model | Input | Duration | Cost | Best For |
|-------|-------|----------|------|----------|
| **seedance2** | Text/Image/Video | 2-15s | 36 cr/sec | Long, reference-based |
| **gen4.5** | Text/Image | 2-5s | 12 cr/sec | General purpose, quality |
| **gen4_turbo** | Image required | 2-5s | 5 cr/sec | Fast, cheap |
| **veo3** | Text/Image | 2-15s | 40 cr/sec | Highest quality |
| **veo3.1** | Text/Image | 2-15s | 20-40 cr/sec | High quality, balanced |
| **veo3.1_fast** | Text/Image | 2-15s | 10-15 cr/sec | Fast Google model |
| **gen4_aleph** | Video + Text/Image | 2-5s | 15 cr/sec | Video editing/transformation |

**Hackathon strategy:** gen4.5 is the safe default (12 cr/sec, good quality). seedance2 if you need reference images or long duration. veo3.1_fast for budget-conscious iterations.

### Image Models (3 Options)

| Model | Cost | Speed | Best For |
|-------|------|-------|----------|
| **gen4_image** | 5-8 cr | Standard | Highest quality |
| **gen4_image_turbo** | 2 cr | Fast | Requires 1-3 reference images |
| **gemini_2.5_flash** | 5 cr | Standard | Google model option |

### Audio Models (ElevenLabs)

| Model | Cost | Purpose |
|-------|------|---------|
| **eleven_multilingual_v2** | 1 cr/50 chars | Text-to-speech |
| **eleven_text_to_sound_v2** | 1-2 cr | Sound effects |
| **eleven_voice_isolation** | 1 cr/6 sec | Isolate voice from audio |
| **eleven_voice_dubbing** | 1 cr/2 sec | Dub to other languages |
| **eleven_multilingual_sts_v2** | 1 cr/3 sec | Voice conversion |

---

## Hackathon Build Recommendations

### Option 1: Skills-Based Agent (Fast Track)

**Use:** `runwayml/skills` directly  
**How:** Install via `npx skills add runwayml/skills` in Claude Code or Cursor  
**Advantage:** Zero integration work, direct generation scripting, agent-native  
**Cost:** ~$10 for 1,000 credits covers ~28 gen4.5 videos @ 5s each  
**Timeline:** 15 minutes to setup, immediate generation

### Option 2: Full Backend Integration

**Use:** `@runwayml/sdk` (Node.js or Python)  
**How:** Build a Next.js app with `/api/generate` endpoints  
**Advantage:** Web UI, better UX, production-ready patterns  
**Examples:** 7 complete Next.js examples in avatars-react repo  
**Cost:** Same as above  
**Timeline:** 1-2 hours with examples

### Option 3: Voice Agent with Avatars

**Use:** `livekit-agents` + `@runwayml/avatars-react`  
**How:** LiveKit framework + Runway characters  
**Advantage:** Real-time conversational AI, embedded avatars, multimodal  
**Cost:** LiveKit infrastructure (free tier available) + Runway credits  
**Timeline:** 2-3 hours for complete pipeline

### Option 4: Existing Research (Fast Integration)

**Use:** `guided-inpainting` (243 stars) or academic models  
**How:** Port model + use Runway API  
**Advantage:** Research-grade quality, novel output  
**Cost:** Higher per-generation (model-dependent)  
**Timeline:** 1-3 hours depending on model complexity

---

## Repository Hackathon Utility Matrix

### TIER A: Direct Hackathon Impact (HIGH)

| Repo | Utility | Why | Recommended Use |
|------|---------|-----|-----------------|
| **skills** | **HIGH** | Agent-native, runnable scripts, complete framework | Primary pattern — use directly |
| **sdk-python** | **HIGH** | Production API client, async support | Backend generation logic |
| **sdk-node** | **HIGH** | TypeScript, full types, Node.js ecosystem | Next.js / Express backends |
| **avatars-sdk-react** | **HIGH** | Drop-in component, 7 examples, production quality | Avatar UI integration |
| **livekit-agents** | **HIGH** | Voice agent framework, real-time capability | Voice AI pipeline |

### TIER B: Reference & Foundation (MEDIUM)

| Repo | Utility | Why | Recommended Use |
|------|---------|-----|-----------------|
| **runway-agents-js** | **MEDIUM** | Node.js agents framework (new, weekly commits) | Multimodal agent foundation |
| **runway-api-mcp-server** | **MEDIUM** | MCP integration (Claude compatible) | Use if Claude-to-Runway is key |
| **avatars-node-rpc** | **MEDIUM** | Backend RPC for avatar events | Server-side avatar logic |
| **RunwayML-for-Photoshop** | **MEDIUM** | Clean plugin architecture example | Pattern reference only |
| **hair-makeover-api-demo** | **MEDIUM** | Image generation example | Pattern reference |
| **guided-inpainting** | **MEDIUM** | Research-grade inpainting (243 stars) | If video editing is core |

### TIER C: Context Only (LOW)

| Repo | Utility | Why |
|------|---------|-----|
| Creative tool plugins (p5js, Max/MSP, Touch Designer, Processing, Arduino, etc.) | **LOW** | Archived, no active development |
| Infrastructure (Terraform, K8s adapters, AWS utilities) | **LOW** | Not relevant to hackathon code |
| Legacy models (model-sdk, alpha_models, etc.) | **LOW** | Deprecated in favor of public API |
| Design resources, CHANGELOG, documentation scaffolds | **LOW** | Reference only |

---

## Final Hackathon Strategy

### Recommended Path (3 Hours to Submission-Ready)

1. **Get a Runway API key** (https://dev.runwayml.com/)
   - Create organization, set up billing ($10 minimum)
   - Generate API key, store in `.env`

2. **Install skills framework** (5 minutes)
   ```bash
   npx skills add runwayml/skills
   # Or in Claude Code: /plugin install runway-api-skills
   ```

3. **Pick a generation pattern** (choose one):
   - **Direct scripting:** Use `rw-generate-video` skill to create videos immediately
   - **Web app:** Use next.js template from avatars-react examples
   - **Voice agent:** Use livekit-agents + character embedding

4. **Build hack** (2 hours)
   - Integrate Runway API calls
   - Use gen4.5 for reliable quality or seedance2 for reference control
   - Batch generations to maximize credit use

5. **Submit** — no additional setup needed if using skills framework

### Edge Advantages

- **Skills are agent-endorsed** — Claude Code, Cursor, and compatible agents have first-class support
- **Runnable scripts** — You don't need a full app; generation works from CLI
- **Character system** — GWM-1 avatars are hard to replicate elsewhere (high barrier to competition)
- **Recent model additions** — seedance2 (2026-04-14), veo3.1_fast (2026-04-15) are weeks old — cutting edge
- **Ecosystem momentum** — Active commits on livekit-agents and avatars indicate platform maturity

### What NOT to Do

- Don't use archived model repos (processing-library, etc.) — they won't work with current API
- Don't build on `model-sdk` — it's legacy; use public API instead
- Don't expose your API key to the browser — use backend routes only
- Don't expect free credits — you must prepay

---

## Conclusion

Runway's GitHub reveals a **highly cohesive, API-first platform** optimized for:
1. **Agent-native development** (skills framework)
2. **Real-time conversational AI** (avatars + LiveKit agents)
3. **Media generation at scale** (batch video/image/audio with async polling)

The **skills framework is your primary edge** — it's explicitly designed for AI agents like Claude Code and Cursor, ships with runnable examples, and requires minimal integration work.

**Estimated hackathon advantage:** Using skills + a core SDK gives you 2-3 hours of development time back compared to building from scratch. Pair that with character avatars for a "wow" factor and you have a competitive submission.

