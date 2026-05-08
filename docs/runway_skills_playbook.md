# Runway Skills Library: Practitioner Playbook
**For the Runway API Hackathon (May 8-11, 2026)**

*A comprehensive guide to the Runway Skills framework, official skill catalog, custom skill authoring, and hackathon submission patterns.*

---

## Table of Contents
1. [What Skills Are](#what-skills-are)
2. [Skills Repo Structure](#skills-repo-structure)
3. [Complete Skill Catalog](#complete-skill-catalog)
4. [How to Install & Use](#how-to-install--use)
5. [Authoring Custom Skills](#authoring-custom-skills)
6. [Three Custom Skills Proposed](#three-custom-skills-proposed)
7. [Patterns for Hackathon Success](#patterns-for-hackathon-success)
8. [Integration with Broader Runway Stack](#integration-with-broader-runway-stack)
9. [Recent Activity & Roadmap Signals](#recent-activity--roadmap-signals)

---

## What Skills Are

### Purpose & Philosophy

Runway Skills are **standardized agent task definitions** that allow Claude Code, Cursor, and other compatible agents to invoke Runway API functionality with **zero boilerplate**.

A Skill is fundamentally:
- **A contract** — describes what the agent should do (description, triggers, use cases)
- **A wrapper** — encapsulates CLI scripts, SDK calls, or pure logic that implements that contract
- **A discovery mechanism** — agents learn what you can do via `SKILL.md` metadata without reading source code

Skills differ from raw API calls because:
- **Pre-validated** — scripts handle auth, retry logic, error messages
- **Agent-optimized** — descriptions are written to trigger on agent intent, not specific keywords
- **Framework-agnostic** — works across Claude Code, Cursor, GitHub Copilot, and any Agent Skills-compatible tool
- **Opinionated** — embed best practices (security, cost awareness, output formatting) by design

### How Agents Load & Use Skills

When you invoke a skill, the agent:

1. **Discovers** — reads your project's `SKILL.md` files or plugin manifests
2. **Matches intent** — finds the skill whose description best fits the user's request
3. **Invokes** — calls the skill's script with parsed arguments
4. **Handles output** — interprets results and presents to the user

Example: A user says *"Generate a video of a sunset over the ocean"*. The agent:
- Searches skill descriptions for "video" + "generate" → matches `rw-generate-video`
- Parses the user's input → `prompt="sunset over the ocean"`, `filename="sunset.mp4"`, `model="gen4.5"` (default)
- Runs `uv run scripts/generate_video.py --prompt "..." --filename "..." --model gen4.5`
- Captures output → signed URL + local file path
- Presents result → lead with model + cost, embed image in Markdown, offer to save locally

The agent never sees the implementation — only the `SKILL.md` contract.

---

## Skills Repo Structure

### Folder Layout

```
runwayml/skills/
├── .claude-plugin/              # Claude Code plugin manifest
│   ├── plugin.json
│   └── skills/
│       ├── rw-generate-video/
│       ├── rw-integrate-video/
│       └── ...
├── .cursor-plugin/              # Cursor plugin manifest
│   ├── plugin.json
│   └── skills/
│       └── ...
├── scripts/                     # Shared scripts (deprecated, moved to skills/)
│   ├── generate_video.py
│   ├── generate_image.py
│   ├── generate_audio.py
│   ├── get_task.py
│   ├── list_models.py
│   └── runway_helpers.py
├── skills/                      # Official skill directories
│   ├── rw-generate-video/
│   │   ├── SKILL.md            # Skill contract
│   │   ├── scripts/            # Runnable code
│   │   │   └── generate_video.py
│   │   └── references/         # Documentation
│   ├── rw-generate-image/
│   ├── rw-generate-audio/
│   ├── rw-integrate-video/
│   ├── rw-integrate-image/
│   ├── rw-integrate-audio/
│   ├── rw-integrate-uploads/
│   ├── rw-integrate-characters/
│   ├── rw-integrate-character-embed/
│   ├── rw-integrate-documents/
│   ├── rw-check-compatibility/
│   ├── rw-setup-api-key/
│   ├── rw-check-org-details/
│   ├── rw-recipe-full-setup/
│   ├── rw-api-reference/
│   ├── rw-fetch-api-reference/
│   └── use-runway-api/
├── assets/                      # Brand assets, icons, examples
├── README.md                    # Installation + quick start
├── CHANGELOG.md                 # Version history
└── LICENSE                      # MIT
```

### SKILL.md Structure

Every skill directory contains a `SKILL.md` file. The frontmatter defines the contract:

```markdown
---
name: rw-generate-video
description: "Generate videos directly using the Runway API via runnable scripts. Supports text-to-video, image-to-video, and video-to-video with seedance2, gen4.5, veo3, and more."
user-invocable: true
allowed-tools: Read, Grep, Glob, Edit, Write, Bash(uv run *), Bash(command -v uv)
---

# Generate Video

[Body content: usage, parameters, examples, security notes]
```

**Frontmatter fields:**

| Field | Type | Purpose | Example |
|-------|------|---------|---------|
| `name` | string | Kebab-case identifier | `rw-generate-video` |
| `description` | string | What it does, for agent matching | `"Generate videos directly..."` |
| `user-invocable` | boolean | Can user call directly (vs. prerequisite) | `true` |
| `allowed-tools` | array | Which tools the skill uses | `Read, Bash(uv run *), ...` |

**Description optimization for agent triggering:**
- Lead with the **action** (generate, integrate, check, setup)
- Include **data types** (video, image, audio, avatar)
- Mention **models** if brand-new (gen4.5, veo3, seedance2)
- Use **concrete examples** in the body, not the description itself

### scripts/ vs references/

- **scripts/** — Runnable code the agent executes: Python/JavaScript files, shell commands
- **references/** — Documentation for humans: guides, security notes, FAQ
- **SKILL.md body** — The practical guide agents read before executing

### Naming Conventions

**Skills that get loaded automatically:**
- Prefix: `rw-` (Runway) for official skills
- Format: `rw-<action>-<object>` or `rw-<object>`
- Examples: `rw-generate-video`, `rw-integrate-uploads`, `rw-check-compatibility`

**Custom skills for your submission:**
- Prefix: `nos-` (Number One Son) to avoid conflicts
- Format: `nos-<facet>` or `nos-<verb>-<noun>`
- Examples: `nos-shot-planner`, `nos-judge-loop`, `nos-multilang-export`

---

## Complete Skill Catalog

### Generation Skills (User-Invocable, Run Directly)

These skills run Python scripts via `uv run`. No SDK setup required.

**rw-generate-video** — Generate videos (text-to-video, image-to-video, video-to-video)
- **When:** User says "Generate a 10-second video", "Create a product ad", "Animate this image"
- **Required inputs:** `--prompt`, `--filename`, optional: `--model`, `--ratio`, `--duration`, `--image-url`, `--video-url`
- **Models:** seedance2, gen4.5, gen4_turbo, gen4_aleph, veo3, veo3.1, veo3.1_fast
- **Cost:** 36 credits/sec (seedance2), 12/sec (gen4.5), 40/sec (veo3), 5-15/sec (others)
- **Example:**
```bash
uv run scripts/generate_video.py --prompt "A serene mountain sunrise" --filename "sunset.mp4" --model seedance2 --ratio 1280:720 --duration 5
```

**rw-generate-image** — Generate images (text-to-image with optional reference images)
- **When:** "Create an image of...", "Design a product photo"
- **Required inputs:** `--prompt`, `--filename`, optional: `--model`, `--ratio`, `--reference-images`
- **Models:** gen4_image (5-8 credits), gen4_image_turbo (2 credits), gemini_2.5_flash (5 credits)
- **Example:**
```bash
uv run scripts/generate_image.py --prompt "Japanese garden at sunset" --filename "garden.png" --model gen4_image
```

**rw-generate-audio** — Generate audio (TTS, SFX, voice isolation, dubbing, voice conversion)
- **When:** "Create a voiceover", "Generate a sound effect", "Dub this to Spanish"
- **Required inputs:** `--type` (tts|sfx|isolate|dub|sts), `--filename`, plus type-specific args
- **Cost:** 1 credit per 50 chars (TTS), 1-2 (SFX), 1/6sec (isolate), 1/2sec (dub), 1/3sec (voice conversion)
- **Example:**
```bash
uv run scripts/generate_audio.py --type tts --text "Welcome to our product" --filename "voice.mp3" --voice-id Noah
```

---

### Integration Skills (Guide Code Writing)

These skills generate framework-specific code for server-side projects.

**rw-integrate-video** — Add video generation to projects (Next.js, Express, FastAPI, Django)
**rw-integrate-image** — Add image generation with reference image support
**rw-integrate-audio** — Add TTS, sound effects, voice processing
**rw-integrate-uploads** — Upload local files to get `runway://` URIs
**rw-integrate-characters** — Create GWM-1 avatars and real-time WebRTC sessions
**rw-integrate-character-embed** — Embed avatar UI in React via `@runwayml/avatars-react`
**rw-integrate-documents** — Add knowledge base documents to avatars

---

### Setup Skills

**rw-check-compatibility** — Analyze project for server-side API capability
**rw-setup-api-key** — Guide through account creation, SDK install, env var setup
**rw-check-org-details** — Query credit balance, rate limits, usage tier
**rw-recipe-full-setup** — End-to-end orchestration (compatibility → key → SDK → code → test)

---

### Utility Skills

**use-runway-api** — Call any public API endpoint (GET/POST/PATCH/DELETE)
**rw-api-reference** — Complete reference (models, costs, endpoints, limits, schemas)
**rw-fetch-api-reference** — Fetch latest docs from docs.dev.runwayml.com

---

## How to Install & Use

### Claude Code

```bash
claude plugin install runway-api-skills@claude-community
claude plugin reload
```

### Other Agents (npx skills)

```bash
npx skills add runwayml/skills
# Select skills via checkbox menu
```

### Verify Installation

```bash
ls ~/.claude/skills/  # or ~/.agents/skills/
# Should see: rw-generate-video/, rw-integrate-video/, etc.
```

### Invoke a Skill

```
+rw-generate-video

User: "Generate a 10-second sunset video"

Agent runs: uv run scripts/generate_video.py --prompt "A sunset..." --filename "sunset.mp4" --model gen4.5
```

---

## Authoring Custom Skills

### SKILL.md Frontmatter

```markdown
---
name: nos-shot-planner
description: "Orchestrate a shot list for a brand film. Plan camera angles, performer actions, and Runway API calls for each shot. Estimates cost and duration."
user-invocable: true
allowed-tools: Read, Grep, Glob, Edit, Write
---
```

**Best practices:**
- **name**: Kebab-case, unique, project-prefixed (e.g., `nos-` for Number One Son)
- **description**: Lead with action verb + data type + key models/concepts
- **user-invocable**: `true` for user-facing skills, `false` for helper skills
- **allowed-tools**: List what the skill can do (Read files, Write files, run Bash, etc.)

### How Claude Code Discovers Skills

1. Scans `.claude/skills/` folder (or installed via plugin)
2. Reads every `SKILL.md` frontmatter
3. Matches user intent against skill descriptions
4. Invokes highest-scoring skill
5. Captures output and presents to user

### Description Optimization

Good: *"Orchestrate a multishot brand film using Runway API generation, LLM scene planning, and character performance."*

Poor: *"Runnable script for video composition with agent scaffolding."*

---

## Three Custom Skills Proposed

### 1. nos-shot-planner

**Purpose:** Break a film treatment into shots, specify camera/performer/API actions per shot, estimate cost + duration.

**Output:**
```
| Shot | Description | Camera | Endpoint | Model | Duration | Cost |
|------|-------------|--------|----------|-------|----------|------|
| 1 | Mastermind speaks | Dolly-in | /v1/character_performance | gwm1_avatars | 6s | 30 |
| 2 | Office reveal | Pan right | /v1/image_to_video | seedance2 | 5s | 180 |
| 3 | Clone army | Zoom-out | /v1/text_to_video | seedance2 | 8s | 288 |

Total: ~22 seconds, ~500 credits
```

---

### 2. nos-judge-loop

**Purpose:** Evaluate a generated shot against its prompt. Output a score (0-100) and decision: ACCEPT, ITERATE, or ESCALATE.

**Output:**
```json
{
  "score": 78,
  "decision": "ITERATE",
  "semantic_match": 85,
  "technical_quality": 72,
  "artistic_fit": 76,
  "performance": 65,
  "issues": [
    "Avatar lip-sync is off",
    "Background is too dark"
  ],
  "suggested_iteration": {
    "model": "seedance2",
    "new_prompt": "Mountain sunrise with golden mist...",
    "reason": "Seedance2 handles lighting better"
  }
}
```

---

### 3. nos-multilang-export

**Purpose:** Dub a video to multiple languages using ElevenLabs. Output localized MP4 files + manifest.

**Output:**
```
generated/
├── brand-film-es.mp4
├── brand-film-fr.mp4
├── brand-film-de.mp4
├── brand-film-ja.mp4
├── brand-film-zh.mp4
└── manifest.json
```

Cost: ~1 credit per 2 seconds of audio per language

---

## Patterns for Hackathon Success

### 1. Concept Clarity

Show mastery of Runway's platform:
- All major models (seedance2, gen4.5, veo3, gwm1_avatars)
- When to use which (seedance2 for animation, gen4.5 for general, gwm1 for real-time)
- Cost/tradeoff reasoning
- Multi-skill composition (generate → judge → iterate → dub)

### 2. Craft & Execution

- Real API calls with correct parameters
- Task polling (PENDING → RUNNING → SUCCEEDED)
- Error handling + retry logic
- Security best practices (env vars, URL validation, no hardcoded secrets)

### 3. Emotional Impact

Your brand film should:
- Tell a story (origin, character arc, emotional payoff)
- Use Runway authentically (real generation, no Midjourney/DALL-E)
- Demonstrate scale (50+ clones, multi-shot orchestration)
- Show iteration (judge + regenerate → final polish)

### 4. Adherence to Runway

- Runway-native models ONLY
- Real credits (show invoice/dashboard proof)
- Skills-first workflow (not raw SDK calls)
- No external generative tools

### 5. Novel Contribution

- Custom skills that extend Runway's offerings
- New patterns (judge loop for quality feedback)
- Multi-domain integration (music, dubbing, subtitles)
- Agentic autonomy (skills make decisions without user each time)

---

## Integration with Broader Runway Stack

### avatars-react SDK

Embed avatar call UI in web apps:

```typescript
import { AvatarCall } from '@runwayml/avatars-react';

<AvatarCall
  avatarId="your-avatar-id"
  connectUrl="/api/avatar/session"
  onEnd={() => console.log('Call ended')}
/>
```

Skills: `rw-integrate-characters` + `rw-integrate-character-embed`

### livekit-agents (Upcoming)

Runway's production agent framework for multi-turn avatar conversations.

Skills anticipating this: `rw-integrate-characters`, `rw-integrate-documents`, `use-runway-api`

---

## Recent Activity & Roadmap Signals

### Recent Commits (Feb 10 - Apr 21, 2026)

**v2.1.0 (Apr 17)** — Runtime improvements
- `use-runway-api` script moved into skill directory
- Added output presentation best practices
- Fixed env var names, added Request Body Reference

**v2.0.0 (Apr 16)** — Agent-first generation
- New `rw-generate-*` skills (direct `uv run`, no SDK setup)
- All skills support seedance2
- Plugins bumped to v2.0.0

**v1.1.0 (Mar 2026)** — Skills renamed with `rw-` prefix
**v1.0.0 (Feb 10)** — Initial release

### Actively Committed

- `rw-generate-*` skills (hero skills)
- Seedance2 support (high priority)
- Security hardening (Snyk audits)

### Drifting Toward Stability

- Character embed (mature)
- Check compatibility (maintenance)
- API reference (docs.dev.runwayml.com is source of truth)

### Roadmap Signals

Runway is prioritizing:
1. Agent-first generation (skip SDK setup)
2. Security hardening
3. Multi-language support (dubbing)
4. Real-time avatars (WebRTC)
5. Cost transparency

---

## Quick Reference: Model Costs

| Type | Model | Cost | Best For |
|------|-------|------|----------|
| Video | seedance2 | 36/sec | Long, high quality |
| Video | gen4.5 | 12/sec | General purpose |
| Video | veo3 | 40/sec | Premium |
| Image | gen4_image | 5-8 | Highest quality |
| Image | gen4_image_turbo | 2 | Fast + cheap |
| Audio TTS | eleven_multilingual_v2 | 1/50 chars | Voiceover |
| Audio Dub | eleven_voice_dubbing | 1/2 sec | Multi-language |
| Avatar | gwm1_avatars | 5/sec | Real-time |

---

**Document version:** 1.0 (May 2026)  
**Source:** runwayml/skills GitHub, docs.dev.runwayml.com  
**Prepared for:** Number One Son submission, Runway API Hackathon 2026
