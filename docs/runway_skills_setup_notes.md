# Runway Skills — Friday Setup Notes

Live data captured May 7, 2026 night, from cloning `github.com/runwayml/skills` to `/tmp/runwayml_skills`.

## 17 official skills (CHANGELOG v2.1.0)

Generation (runnable directly):
- `rw-generate-video` — text/image/video to video
- `rw-generate-image` — text to image
- `rw-generate-audio` — TTS, dubbing, voice ops

Integration (server-side patterns):
- `rw-integrate-video`, `rw-integrate-image`, `rw-integrate-audio`
- `rw-integrate-uploads` — file upload pattern
- `rw-integrate-characters` — Characters/avatar lifecycle
- `rw-integrate-character-embed` — React SDK embedding
- `rw-integrate-documents` — knowledge base for grounded characters

Setup & utility:
- `rw-recipe-full-setup` — full setup walkthrough
- `rw-setup-api-key` — auth setup
- `rw-check-compatibility` — analyze project stack
- `rw-check-org-details` — org tier and balance
- `rw-api-reference` — full reference cached
- `rw-fetch-api-reference` — live fetch
- `use-runway-api` — direct API access without SDK

## Install (Friday 0901 ET, after build window opens)

```bash
# Claude Code path:
claude plugin marketplace add anthropics/claude-plugins-community
claude plugin install runway-api-skills@claude-community

# Universal path:
npx skills add runwayml/skills
```

## v2.1.0 critical updates
- `use-runway-api` runtime script now ships *with* the skill (was previously at repo root)
- `rw-api-reference` added Request Body Reference section with minimal POST bodies for every generation endpoint
- New env var: `RUNWAY_SKILLS_DIR` for custom install paths

## Friday usage pattern

For our pipeline, we'll lean on:
- `rw-generate-video` for craftsman's-blade five-pass demos (gen4.5)
- `rw-generate-image` for Mom-25/Roger-5/sister-3 portrait refinement
- `rw-integrate-characters` + `rw-integrate-character-embed` for avatars-react frontend integration
- `rw-integrate-documents` for grounding the Mastermind character with Number One Son founding story

## Custom Skills we'll author and ship as part of submission

Three new skills published to `github.com/rogergrubb/wtf/skills/` Friday — judges who built the Skills repo will pattern-match positively when they see them:
- `nos-shot-planner` — orchestrate brand-film shot lists with cost estimates
- `nos-judge-loop` — LLM-as-judge regeneration for prompt-adherence scoring
- `nos-ghost-frames` — the Ghost Frames pipeline as a reusable skill (NEW addition based on tonight's pivot)
