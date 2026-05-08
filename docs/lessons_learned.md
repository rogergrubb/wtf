# WTF — Lessons Learned (Live Log)

Permanent record of what we hit, what we learned, what we changed. Updated continuously through the build. Friday morning's pre-flight will pull from this file.

---

## Tuesday May 5, 2026 — Day 1

### Strategic
- **Cofounder rule:** account-binding fields ("email associated with X account") get a spoken verification before the form is touched. Submitted hackathon registration twice — once with `roger@grubb.net`, once with `rogergrubbrealestate@gmail.com` — only the second matched the Runway dev account. Recovery cost: cleanup email to `events@runwayml.com`.
- **Build pivot:** dropped DirectorOS single-product framing in favor of Number One Son agentic clone-army platform. The thesis "we built the platform that builds the platform" is stronger than "we built one good product."
- **Magnum Opus = Origin Documentary.** The film is itself produced by the system it documents. Recursive structure unlocks the WTF reveal in Act 4.

### Production / Visual
- **Voice and avatar gender must match.** Closing segment used cooking-teacher avatar (apparent male presentation) with Georgia voice (female). Mismatch broke immersion. Going forward: explicit gender-pairing review before every `avatar_videos.create` call. Default safe pairings:
  - Apparent-male avatars → marcus, vincent, drew, felix, adrian, blake, david, nathan, sam, adam, zach, roman, jasper, leo
  - Apparent-female avatars → aurora, mia, clara, skye, summer, ruby, nina, emma, maya, georgia, petra, violet, luna
- **Tool-tray highlight needs more visual weight.** Current orange outline + dim fill is too subtle in busy compositions. Friday version: bright gold halo ring with pulsing brightness modulation, thicker outlines, and active-state inner glow.
- **Sergeant grouping titles (VIDEO, IMAGE, WORLD, etc.) must also highlight** when any of their soldiers fires. Helps the audience read the categorization in real time.
- **Avatar segments arrive at different scales and crops** — some fill the frame, some sit small in the middle. Friday pipeline must pre-process each avatar video to consistent crop + scale before compositing into the viewport.

### Tooling / API
1. API keys must start with `key_` — non-`key_` prefix fails before validation.
2. `gen4_image_turbo` requires `referenceImages` array — NOT pure text-to-image. Use `gen4_image` for prompt-only.
3. `TextToImageCreateResponse` has only `id` field — must immediately call `c.tasks.retrieve(task.id)` to get status.
4. **Always persist `task.id` to disk on submit** — if your script crashes between create and poll, the in-flight credits are spent and the task is unreachable.
5. Output URLs are JWT-signed CloudFront — short-lived, download immediately on `SUCCEEDED`.
6. Auth failures return clean 401 with `error` + `docUrl` JSON body.
7. SDK has no direct `text_to_speech` namespace — use `avatar_videos` for text→speech-with-avatar or `realtime_sessions` for live.
8. `sound_effect.create()` uses `prompt_text` (not `prompt`).
9. `avatars.list()` requires `limit` keyword arg.
10. `avatars.create()` is heavy — requires name, personality, reference_image (URL), voice. Multi-step Characters setup: portrait → avatar → wait READY → avatar_video. ~30s of avatar processing.
11. `avatars.create()` voice param: `type: 'runway-live-preset'` — different literal value from `avatar_videos.create()` speech.voice param: `type: 'preset'`. Same 30 voices, different `type` discriminator. Easy mistake.
12. **Nine official Avatar presets** ready without `avatars.create()`: game-character, music-superstar, game-character-man, cat-character, influencer, tennis-coach, human-resource, fashion-designer, cooking-teacher. Use `{preset_id, type: 'runway-preset'}`.
13. **Thirty preset voices**: victoria, vincent, clara, drew, skye, max, morgan, felix, mia, marcus, summer, ruby, aurora, jasper, leo, adrian, nina, emma, blake, david, maya, nathan, sam, georgia, petra, adam, zach, violet, roman, luna.
14. Aleph lives in `c.video_to_video` (not `c.image_to_video`). Separate namespace.
15. Avatar status lifecycle: `PROCESSING` → `READY`. Must poll `c.avatars.retrieve(id).status` before using.
16. Task status set: `PENDING`, `RUNNING`, `THROTTLED` (queued), `SUCCEEDED`, `FAILED`, `CANCELLED`. The undocumented one is `THROTTLED`.
17. `gwm1_avatars` concurrency: `max_concurrent_generations=1, max_daily_generations=50`. Submitting 9 in parallel = 1 runs, 8 throttle in queue.
18. Credits are charged on submit, not on completion.
19. Tier ceiling: `max_monthly_credit_spend=10000` ($100/month) on free tier.
20. **Public model list (23):** gen4.5, gen4_turbo, gen3a_turbo, seedance2, veo3, veo3.1, veo3.1_fast, gen4_aleph, gen4_image, gen4_image_turbo, gemini_2.5_flash, gemini_image3_pro, gpt_image_2, gwm1_avatars, gwm1_avatar_async_audio_to_video, gwm1_avatar_async_text_to_video, act_two, voice_processing, eleven_multilingual_v2, eleven_voice_isolation, eleven_voice_dubbing, eleven_multilingual_sts_v2, eleven_text_to_sound_v2.
21. `gpt_image_2` and `gemini_image3_pro` are bundled image models we didn't have on the original 51-roster — adds 2 to the count.
22. GWM-1 Worlds and GWM-1 Robotics are NOT in the public API — research only. Confirmed.
23. The classic editing primitives (Inpainting, Frame Interpolation, 4K Upscale, Super-Res, Remove BG) appear to live INSIDE Aleph (`gen4_aleph`) — no separate endpoints in the public API.
24. `c.video_to_video.create` accepts `video_uri` parameter (URL of source video) for Aleph editing.

### Strategic reframe (Mastermind's move — late Tuesday)
**Stop building a tech demo. Start building a brand film.**

The judges (Cris Valenzuela, Yining Shi, Anastasis Germanidis) are not evaluating startups by stack quality. They are looking for the *partner who shows them the future of Runway as a planet-scale brand* — the substrate of the next era of media, the way Coca-Cola is the substrate of "share a moment" or Nike is the substrate of "do the impossible."

Brand-film thesis (Mastermind authored):
- The Mastermind = relatable founder protagonist (Roger, Number One Son Software Development).
- The General = Number One Son the agent / the company.
- The Chief of Staff = Claude Cowork.
- The operational force = the clone army wielding Runway tools.
- This four-part structure is universal — *anyone* in the agentic era can map themselves into it. That's the scalable, brandable story.

What this means for the film:
- Show what *gets made*, not what's making it. (Nike doesn't show factories.)
- One narrator: the Mastermind, cloned voice. One perspective. One character.
- 51-facet thesis present as visual flourish, not a roll call.
- Recursive structure preserved — film is still made by the system it documents — but as a second-viewing rabbit hole, not the punchline.
- Builders Program close stays explicit. That's the partnership ask.

What we let go:
- Literal tool tray with badge numbers (becomes a companion artifact — one-page receipts page on the site).
- 9-avatar narrator cycling.
- Sergeant-cascade trickle-down sequences (becomes "making of" companion).

What we keep:
- WTF codename (internal punchline, for Runway leadership's closed-door discussion).
- 51 deployed clone URLs as proof gallery (separate from the hero film).
- 8 verified Runway endpoints driving every shot.

Pinned: pausing visual iteration. Reframe first, then re-architect Friday's production around the brand-film deliverable.

### The Number One Son founding story (the brand's emotional anchor)
Roger's mother called him her **Number One Son**. Every single time, she'd follow with the joke: **"and you're my only son. Ha ha ha."**

The joke was funny. The joke was also a lesson — two lessons, in two lines:
- *"You're my Number One Son"* → believe in yourself. Ambition without ceiling.
- *"And you're my only son"* → stay grounded. Take yourself seriously, never too seriously.

This duality is the entire Number One Son brand DNA. It's the ethos of the agentic-era founder: do thousand-person work AND remember you're a person whose mother loves you. Real. Unfaked. Untaught. Sitting in family history for forty years until it became the soul of a software company.

Roger's arc: a kid told there's no limit to what human creativity can dream up → today's founder standing inside *the smartest AI we've ever experienced*. The film's job is to walk that arc in 100 seconds and end on real Roger speaking to Cris.

Founder's stated mission (Roger's words): **"We're here to show it off right now and be part of the solution."** That's the peer-offer that defines the partnership ask.

### The iconic-commercial standard (Mastermind's frame)
The brand film must hit the emotional weight of Mean Joe Greene's Coke, Apple's *1984*, Nike's *Just Do It*, Subaru's *Dog Tested*, Tony the Tiger. **Pattern across all of them: one hook, one moment, one image you cannot unsee.**

**Our one hook:** *A son still trying to live up to what his mother saw in him — even now, in the age of artificial intelligence.* Universal. Every viewer with a parent feels it. Every viewer without feels the absence. The agentic era doesn't release Roger from his mother's standard; it raises the bar.

**Our one image:** the closing shot. After ninety seconds of AI dissolving and re-forming, the AI gets out of the way and a real human face appears, looks Cris in the eye, and says seven words. That contrast IS the image. The Mean Joe jersey moment of our film.

### The strategic play (Mastermind authored): own the Builders Program category
Builders Program launched March 31, 2026 — 37 days old at hackathon time. NO canonical reference customer yet. The slot is empty. **Whoever fills it gets pointed at by Cris on stage at every conference for the next 12 months, cited in every funding deck, featured in every Builders blog post.** Not participation. Category ownership. The hackathon is the door; the film is the foot in the door; the closing shot is the handshake; the Builders Program is what we walk into together.

### Real photos as authenticity layer
For Coca-Cola-grade emotional weight, Act 1 needs REAL photos from Roger's life — even one or two. AI-generated journey imagery is good, but real photographs land emotionally in a way AI never can — the audience's brain registers them as TRUE. Mean Joe was a real football player; the Apple runner was a real woman. Authenticity is what makes iconic images iconic.

Photos to ask Roger for (when he has 20 minutes to dig):
- His mother (any era, especially when he was a child)
- Roger as a young carpenter on a job site
- A home or commercial building he built
- One of his published books (any of the 20+)
- A family moment

Filename pattern: `mastermind_real_*.jpg`. Layered into Act 1 alongside AI-generated extensions. The film becomes a hybrid — real artifacts of a real life, extended by AI used with intention. The pitch in microcosm.

### Roger's biography — the credibility anchor
Roger is **62 years old**. Journeyman carpenter. Built furniture, homes, commercial buildings, remodels. Published author of 20+ books, real-estate investor and realtor, world traveler. The craftsman metaphor is not adopted — it's biographical. This is the credibility anchor of the entire brand film. Show, don't declare.

**Roger's age is a FEATURE, not something to soften.** A 25-year-old saying "anyone can be a builder in the agentic era" is a tech founder talking to tech founders. A 62-year-old journeyman carpenter saying it is the entire industry hearing the message it actually needs to hear. Universality of the thesis depends on the person delivering it being NOT the typical demographic AI markets to.

### Roger's mother — alive at 82 (the emotional center of the film)
Roger's mother is 82 and still living. The film is therefore not a posthumous tribute — it is a son's **love letter to a mother who can still watch it**. Cris will see the film and realize "this man's mother might be watching this. He's going to send it to her. She's going to see what she meant." That is the emotional gravity that makes strangers cry and strangers send the film to their own mothers. That's the Mean Joe-viral mechanism.

Possible Act 1 on-screen text considerations:
- *"Eighty-two years between us. A lifetime each. And we're both still living up to it."*
- *"My mother is eighty-two. I am sixty-two. She's still right."*

Pick whichever lands stronger after Mastermind reviews.

### Photo inventory — DELIVERED (May 5)
Seven real photographs uploaded by Mastermind. Together they cover the full arc.

1. **AUG 69 beach photo** — Roger's MOTHER at 25, young Roger (~5) in the back, his only sister (~3) in front. The "and you're my only son" joke is witnessed in real form: the woman who said it, the year she said it, the boy who heard it, the daughter who was raised alongside the joke. Roger has ONE sister. Cold-open dissolve target.
2. **Teenage Roger in Norwegian sweater** — early adulthood, the bridge between child and man.
3. **Costume photo with partner in car** — joy, life, the "stay grounded" half of the joke.
4. **Roger at Golden Gate with HIS LITTLE BOY (his son, not grandchild)** — Roger is the father. The lineage opens forward: mother → only son → and now Roger's own son. The "Number One Son" name has a successor now. The film gains a future tense.
5. **Professional headshot** — present-day Roger, real-estate-professional poise.
6. **Roger holding toddler "flying" at the coast** — the *holding her hands so she can fly* image. Late Act 1 emotional setup for "anyone can be a builder."
7. **Three-generation hospital room photo — Mom + Roger + newborn** — Roger's mother (alive, ~75-78 in photo, 82 today) meeting her great-grandchild. Hospital wristband and name sticker visible — proof of unposed reality. Lands on the line *"I built a family"* in the Act 1 list.

### The Number One Son lineage — three generations
- **Roger's mother** called him *her Number One Son*. (Joke: "and you're my only son.") Mother is alive at 82.
- **Roger** is her only son. 62 years old. Now passes the name to his own son.
- **Roger's son** — the boy in the Golden Gate photo. Age TBC. The next Number One Son.

The film honors all three generations. The closing line *"Anyone can be a builder. Here's one"* now widens silently — Roger AND his boy. Cris reads the future tense without us spelling it out.

### THE BOOKEND STRUCTURE — locked
**Roger's mother appears in BOTH the 1969 photo (age 25) and the hospital photo (age ~75).** Same woman, fifty years apart. She bookends Act 1. The film does in two photographs what most documentaries spend half an hour trying to do: the passage of a life made visible. Pixar's *Up* opening in less than 30 seconds.

- Cold open ends on dissolve to 1969 photo (Mom at 25, young Roger, his sister) — carries the line *"that gave me something to live up to"*
- Act 1's list plays over teenage / professional / partner / Golden Gate / coast photos
- Act 1 LAST beat lands on hospital photo (Mom at 75 with great-grandchild) — carries the line *"I built a family"*
- Then: *"and every time the world changed, I asked myself the same question. Am I still living up to it?"* — photo holds for one extra beat
- Transition: *"And then this happened."* Cut to today.

The photo set is COMPLETE. No further photos needed. Combined with the cloned-voice narration (recording pending) and the closing-line shot of real Roger (recording pending), we have everything the brand film requires.

### Photo restoration approach (Act 1 authenticity layer)
Old photos restored using Runway's own tools — recursion working for us. The medium IS the message: Act 1 *literally* uses AI to extend a real life's record. Tools: Super-Resolution for grain cleanup + sharpness, gen4_image with photo as reference for extension shots if needed, Aleph for gentle cinematic warmth on moving frames. Enhancement must be LIGHT — old photos have truth in their grain. Bring into focus, don't re-imagine.

Photos requested (3-5 strongest):
1. Mother (with young Roger preferred)
2. Young Roger on job site (real tools, real sawdust)
3. A home / building / furniture he built
4. Roger and mother together (any era — recent has extra weight)
5. Optional: one of his books

### MAJOR PIVOT — Drop "clone army" externally; replace with craftsman's blade metaphor (Mastermind authored)
**The clone-army metaphor is industrial-scale language. Cris's brand vocabulary is craft-coded — cinematic, world model, creative control, filmmaker. Star Wars clone troopers are faceless, interchangeable, ordered to fire — visually that IS the slop economy. The metaphor was working against our positioning.**

New external metaphor: **The blade sharpens with every pass.** Same craftsman. Same intent. Each Runway tool is one pass — first pass rough, second clarifies, third filters, fourth gains focus, fifth gains luminosity. Iterative refinement, not industrial replication.

The toolbox UI stays — but it's now a craftsman's workbench, not a military arsenal. Each tool drawn = the artisan reaching for the right instrument. The 51 facets stay; they're now *passes / instruments*, not soldiers.

**Externally banned vocabulary:**
- Clone army → craftsman's toolkit
- General → (drop entirely)
- Sergeants → tool families
- Soldiers → tools / instruments / passes
- Roll call → the passes
- "Army marches" → "blade sharpens"
- "Mastermind issues an order" → "the craftsman picks up the right tool"

**Internal WTF codename stays** — it's the punchline for Cris's closed-door discussion moment, lives in our chat / commits / private channels. Never spoken externally.

This pivot also resolves the slop tension automatically — a craftsman doing five passes on one shot is the *opposite* of a content farm. The metaphor argues for us without us having to defend.

### The slop thesis — anti-flood positioning (Mastermind authored)
The AI media landscape is sliding from "wonder" to "oh god, more of this." Cris reads X; he sees the flood; he is publicly pre-positioning Runway *above* the slop conversation ("world model," "cinematic," "creative control," "filmmaker"). He will not invest in proof points that increase the flood — he'll invest in proof points that *fight* it.

Our exponential-growth pitch must therefore sharpen into:

**"The clone army doesn't multiply noise. It multiplies one human's intention."**

Exponential growth = capability per founder, NOT volume of output. A solo founder with the right tools produces what a hundred-person studio used to produce, with the same care, same standards, same intentionality. The army serves the Mastermind's vision; it doesn't replace it; it doesn't dilute the work.

This is the anti-slop position. Runway tools elevated, not weaponized. We are the proof that intentional builders + Runway = quality at scale. Different argument from "more content faster" — and the argument Cris's communications team can actually use.

### The submission's three-artifact structure
1. **Brand film (~100s)** — emotional, mother story, lifelong arc, ends on Cris-direct close. For Cris's gut.
2. **Explainer film (~60-90s)** — AI-narrated, walks through exponential growth + anti-slop thesis, ends pointing at the brand film. For Cris's CFO and Builders Program team.
3. **Clone gallery (~46 deployed URLs)** — receipts, working products. For Cris's engineering team.

Bridge: the explainer's last line points at the brand film — *"the founder is in another video, looking at you."* Forwarded together, they cover the full pitch surface across decision-makers.

### The product positioning — LOCKED ELEVATOR PITCH
**Number One Son is a clone army that teaches companies how to build clone armies.**

Recursive, scalable, defensible. We are what we sell. Produced by the Builders Program; produces more Builders.

We are produced *by* the Builders Program (canonical first graduate). We *produce* more Builders. Recursive scale. Cris invests in us not just as proof — he invests in us as an engine that proves his thesis at scale, founder by founder.

Partnership ask: *"Number One Son is the way every solo founder learns to build with Runway. Make us the canonical case study, and seed the engine that produces a thousand more like us."*

### The film treatment (locked)
~100 seconds.

- **Cold open (10s) — LOCKED Mastermind phrasing:** Black. *"My mother used to call me her Number One Son."* [beat] *"And that gave me something to live up to."*
- **Act 1 — The lifelong test (18-22s) — UPDATED with Mastermind's real biography:** Cloned-Roger VO over AI-generated journey imagery. *"So I lived. I worked. I built furniture. I built homes. I built commercial buildings. I built businesses. I built a family. And every time the world changed, I asked myself the same question. Am I still living up to it?"* [beat] *"And then this happened."* — cut to today.

**Why this list is non-negotiable:** Roger is a real journeyman carpenter who built furniture, homes, and commercial buildings. The craftsman metaphor isn't adopted; it's biographical. The film's emotional spine: *a man who built houses with his hands picks up a new set of tools — and keeps building.* AI is the latest hammer in his belt. The argument writes itself.
- **Act 2 — The Craftsman's Passes (40-50s):** *"The smartest AI we've ever experienced. And like every craftsman before me, I picked up the tools."* On screen: the workbench. Tool drawn → rough first pass. Tool drawn → clarity. Tool drawn → filter. Tool drawn → focus. Tool drawn → luminosity. Same shot, getting sharper each pass. Closing line: *"Same craftsman. Same intent. Sharper blade with every tool in his hands."* Cut to body of work — multiple finished shots, intentional, none of them slop.
- **Act 3 — The thesis (10-15s):** *"Anyone can be a builder. Here's one."* Silhouette assembled from clone-army badges resolves into real face.
- **Climax (5-8s):** AI dissolves. Real Roger, real face, real voice. *"Cris, we're here for you. Let's talk."*
- **End card:** Number One Son Software Development. Powered by Runway. Builders Program.

### The closing shot — locked (Boudica moment)
**Final 5–8 seconds of the film: real Roger, real face, real voice, looking dead at camera. Line: "Cris, we're here for you. Let's talk." (Cris = one S, Spanish nickname for Cristóbal — no H.)**

Why this is the entire film:
- The whole submission is AI-generated until this beat. The AI dissolves. The Mastermind reveals himself. The contrast IS the message.
- Cris cannot watch it without feeling personally addressed. There is no possible response except a human one.
- "We're here for you, let's talk" = peer to peer, founder to founder, equal to equal. That is how CEOs speak to CEOs.
- The "we" is doing colossal lifting: Roger + Claude + Number One Son + the army + Runway itself. The "we" includes Cris's own platform.
- Closes the recursion: the film about the system, made by the system, ends with the human stepping out of the system.

Production specs:
- Phone or recent laptop webcam, horizontal preferred, medium close-up shoulders up, eyes upper third, simple background.
- Soft front light from window or ring light.
- Wired earbuds with mic at collar OR AirPods. NOT phone built-in mic.
- 8–12 takes, varied tone. Two beats of silence after "let's talk" — don't cut.
- Optional 1-sec pre-roll where Roger looks at lens before speaking.
- Filename: `mastermind_closing_shot.mov`. Upload to Cowork by Thu EOD.

This shot is the North Star of the whole film. Every prior beat exists to build emotional tension that releases on these seven words.

### Runway dev portal Characters UI — recon (May 7 night)
The dev.runwayml.com Characters management page exposes 4 tabs: Characters, Explore, Knowledge, Usage.

**Characters tab:** lists custom characters created via avatars.create. Roger's `WTF Test Mastermind` (May 6) is still in the account, reusable Friday. Banner notice: *"Characters can now invoke tools during conversations"* — agentic tool-use is supported, characters can take actions not just speak.

**Knowledge tab:** Documents endpoint UI. Empty by default. Two ways to populate: "Add Text" (paste content) or "Upload Files". This grounds characters in subject-matter 