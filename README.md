# WTF — Whiskey Tango Foxtrot

> *A craftsman's blade in the agentic era.*

**Number One Son Software Development's submission to the Runway API Hackathon, May 8–11, 2026.**

This is the public working repo for the brand film, the build scripts, the verified Runway API outputs, and the lessons learned during the build. The internal codename — *Whiskey Tango Foxtrot* — is the punchline. The external brand is **Number One Son**.

---

## What this is

A solo founder (Roger Grubb, journeyman carpenter, 62) builds a brand film about himself entering the Runway API Hackathon — using Runway's API. The film is recursive: the tools we describe are the tools we used to make the film. The closing shot is real Roger looking at the camera and saying seven words to Cris Valenzuela.

**Elevator pitch for the company being built here:**
> Number One Son is a clone army that teaches companies how to build clone armies.

**The hook of the brand film:**
> A son still trying to live up to what his mother saw in him — even now, in the age of artificial intelligence.

**The closing shot:**
> *"Cris, we're here for you. Let's talk."*

---

## Repo structure

```
wtf/
├── docs/                          Strategic + research markdown
│   ├── brand_film_script.md       LOCKED v1 shooting script (the master doc)
│   ├── lessons_learned.md         Live build log — every Friday-prep note, every pivot
│   ├── runway_capability_map.md   Full Runway API surface (23 endpoints documented)
│   ├── runway_full_atlas.md       Runway product surface scan
│   ├── runway_github_atlas.md     github.com/runwayml org audit (61 repos)
│   ├── research_report.md         SOTA agentic-media-pipeline survey
│   ├── leadership_values.md       Cris/Yining/Anastasis public values mining
│   ├── strategic_brief.md         Hackathon strategic brief
│   ├── quick_reference.md         5-minute project overview
│   └── ...
│
├── scripts/                       All build pipelines
│   ├── wtf_dress_build.py         Static frame generation (PIL)
│   ├── wtf_dress_assemble.py      Final video composition (ffmpeg)
│   ├── wtf_dry_run.py             First structural mockup
│   ├── wtf_real_run.py            51-facet visualized version
│   ├── wtf_tooltray_compose.py    Tool-tray HUD compositor
│   ├── wtf_9avatar_doc.py         9-avatar narration generator
│   └── ...
│
├── assets/
│   ├── photos/                    Mastermind's real photos (mother bookend etc.)
│   ├── runway_outputs/            Real Runway API output verified during dry runs
│   │   ├── phase1c_real_runway_image.png    gen4_image
│   │   ├── phase2_real_runway_video.mp4     gen4.5
│   │   ├── phase3_real_runway_sfx.mp3       eleven_text_to_sound_v2
│   │   ├── phase6c_preset_avatar.mp4        gwm1_avatars (preset)
│   │   ├── phase7_custom_avatar.mp4         gwm1_avatars (custom)
│   │   └── phase8_aleph_color_grade.mp4     gen4_aleph
│   └── dry_runs/                  Iteration archive of every test cut
│
└── outputs/                       Submission-ready deliverables
    ├── DRESS_REHEARSAL.mp4        Current latest assembly (placeholders for closing shot)
    ├── Runway_Hackathon_Battle_Plan.docx
    └── battle_plan_database.xlsx
```

---

## The film at a glance

**Total runtime target:** 100–125 seconds.

**Cold open (10s):** Black + white text. *"My mother used to call me her Number One Son. And that gave me something to live up to."*

**Act 1 — The lifetime (24s):** Seven real photographs spanning sixty years. Roger's mother bookends Act 1: she's 25 in the AUG 69 beach photo and ~75 in the hospital three-generation photo.

**Act 2 — The craftsman's passes (45s):** Live demonstration of a single shot getting better with each Runway tool applied. *Rough → Clarity → The cut → The voice → The soul.* Same craftsman, sharper blade with every tool in his hands.

**Act 3 — The thesis (10s):** *"Anyone can be a builder. Here's one."*

**Climax — The closing shot (6s):** AI dissolves. Real Roger on camera. *"Cris, we're here for you. Let's talk."*

**End card (4s):** Number One Son. Powered by Runway. Builders Program — let us talk.

See [`docs/brand_film_script.md`](docs/brand_film_script.md) for the full locked shooting script with timing, narration, and per-scene asset map.

---

## What's verified working (real Runway API endpoints)

Eight endpoints tested end-to-end with real output, all in `assets/runway_outputs/`:

| Endpoint | Purpose | Cost observed |
|---|---|---|
| `gen4_image` | Text-to-image | 5 cr / image |
| `gen4.5` | Text-to-video (5s) | 60 cr / clip |
| `gen4_aleph` | Cinematic editing pass | ~75 cr |
| `gwm1_avatars` (preset) | Characters preset video | ~7 cr |
| `gwm1_avatars` (custom) | Characters custom avatar | ~10 cr |
| `eleven_text_to_sound_v2` | Sound effects | ~3 cr |
| `avatars.create` | Multi-step avatar setup | ~5 cr |
| Tasks API | Submit/poll/retrieve | free |

See [`docs/lessons_learned.md`](docs/lessons_learned.md) for the full set of Friday-prep notes — every undocumented param, every type discriminator gotcha, every async-vs-sync surprise we encountered.

---

## License

MIT. See [`LICENSE`](LICENSE).

---

*"The negotiations were short."*
