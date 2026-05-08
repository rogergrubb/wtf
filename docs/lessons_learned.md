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

**Knowledge tab:** Documents endpoint UI. Empty by default. Two ways to populate: "Add Text" (paste content) or "Upload Files". This grounds characters in subject-matter knowledge. *Use case for Number One Son:* load the founder bio + Number One Son origin philosophy so a Mastermind character can reference real lifetime events when speaking with users.

**Preset character page anatomy (Sofia / fashion-designer example):**
- Character ID — preset_id (e.g., `fashion-designer`) confirms the 9 official presets we already documented
- Character image — high-quality face/body shot (Asian woman in atelier, full visible face)
- Character Voice — voice preset_id with personality trait descriptor: **Summer (Breezy)**
- Personality — ~100-word verbose description: role + expertise + speaking style + vocal trait
- Starting script — the opening line the avatar delivers when session starts
- Three actions exposed: Start chat (test live), React SDK (frontend embed), Start Building (dev entry)

**Voice preset trait descriptors confirmed so far:**
- Marcus → Firm
- Summer → Breezy
- (more to be discovered as we explore)

### Consent-respect note — sister cropped out (May 8 night decision)
Mastermind reviewed the brand-film plan and made the right call: he has NOT gotten explicit permission from his sister to use her likeness for AI avatar generation. Therefore the AUG 69 photograph is cropped to ONLY Mom-25 + Roger-5 for character creation. The sister stays in the original photograph that appears as a still in Act 1, but is NOT used as a custom character.

The narrower 2-character composition is actually MORE on-thesis: *the Number One Son and his mother*. Just the two of them. The frame's emotional center is the relationship the joke ("you're my number one son... and my only son") describes. Three people made the joke implicit; two people make it explicit.

This is also exactly the consent-care precedent we'd want Cris to see — even within his own family Roger exercises judgment. That's the kind of builder Runway wants in their Builders Program.

### Two custom Characters from AUG 69 photo — production plan locked
Mastermind insight (late May 7): the 1969 photograph contains THREE custom Characters waiting to be born — Mom-at-25, Roger-at-5, sister-at-3. All three brought back as conversational avatars who can speak in the brand film.

Brand film moment unlocked:
> Cold open ends → dissolve to AUG 69 photo → hold one beat → the photograph MOVES → Mom turns to camera → speaks in her own voice (or Aurora/Skye preset) → *"He was my Number One Son. And my only son. Ha ha ha."* → photo freezes → cut to rest of Act 1.

Production pipeline (Friday morning, ~60 minutes total, ~$1.00 cost):
1. Crop AUG 69 photo (685×621) to tight Mom-Roger composition (sister excluded by crop, OR removed via gen4_aleph if a wider frame is needed)
2. Refine each crop via gen4_image with reference + prompt for clarity/upscale (~5 cr × 2)
3. Create two custom avatars via avatars.create with personalities + voices:
   - **Mom-25** → Aurora (Calm) or Skye (Soft); 1960s-mother personality
   - **Roger-5** → Max or Felix child-coded preset; precocious five-year-old
4. Generate avatar_videos delivering brand-film lines (~7-15 cr each)
5. Composite into Act 1 between cold-open and hospital photo

This is the *single most powerful* creative moment available to us. Mean Joe Greene-grade. No other team can ship it because no other team has the photograph + the mother + the agency + the technical chops simultaneously.

### THE SUBMISSION SHAPE — locked May 8 night
After discovering Video Meeting (multi-character scenes) and Camera/Screen Sharing (characters watching user uploads), the submission collapses into a continuous emotional experience:

**Demo link → numberonesonsoftware.com/wtf:**
- `<AvatarCall>` widget loads on page open
- Mom-at-25 (custom character from cropped AUG 69 photo) is visible on beach
- Starting script: *"Hi. I'm Roger's mother. He just built something I want to show you. Upload a photo of someone you loved, and watch what the camera missed."*
- User uploads any photo
- Mom *watches them upload it* via Camera/Screen Sharing capability
- Ghost Frames pipeline fires (gen4_image → gen4.5) generating 10-30 seconds of motion before/after
- Mom reacts to what she sees: *"That's beautiful. Let's see if she'll come back for a moment."* (knowledge-base grounded with Number One Son founding philosophy)
- The experience runs end-to-end without user leaving the submission page

**Video link → brand film (existing treatment):**
- Cold open mother story → Act 1 lifetime + photo bookends → Act 2 craftsman's blade demonstration replaced with Ghost Frames live demo on Mom's own photo → Act 3 anyone can be a builder → real Roger to Cris

**Written description → README of github.com/rogergrubb/wtf:**
- Project objective in 1-2 paragraphs
- API surfaces enumerated (gen4_image, gen4.5, gen4_aleph, gwm1_avatars custom + preset, eleven_text_to_sound_v2, voice cloning, knowledge-base documents, video-meeting multi-character, camera/screen sharing)
- Architecture diagram showing the avatars-react SDK + Modal infra + custom Skills shipped
- Builders Program partnership ask repeated, named, specific

The three pieces share one emotional arc: brand film tells the story, deployed app delivers the experience, README delivers the receipts. Cris doesn't watch the film and decide to email us — he USES the app, has a real moment, and the closing shot of Roger speaking to him lands as the natural follow-up.

Friday production order: 1) Custom characters (Mom/Roger/sister), 2) Knowledge base grounding, 3) Ghost Frames pipeline, 4) avatars-react frontend with screen-sharing wired, 5) brand film with embedded Ghost Frames demo of Mom's own photo, 6) closing shot integration, 7) deploy. Eight to twelve hours of build, $5-10 in Runway credits.

### Cost reality
- gen4_image (text-to-image): 5 credits ($0.05) per generation, ~26 sec runtime.
- gen4.5 video (5 sec): 60 credits ($0.60) per generation, ~60-90 sec runtime.
- gen4_aleph editing pass: ~75 credits ($0.75) per generation observed, ~60 sec runtime.
- gwm1_avatars (Characters video): ~7 credits per generation observed, but variable; some longer text increased cost.
- eleven_text_to_sound_v2 (sound effect): ~3 credits per generation.
- avatars.create + portrait: 5 credits for portrait + ~free for avatar setup.
- Total burn for the entire dry-run + real-API test + 9-avatar render + composition: ~$2.30 of $10 budget.

### Consent-respect note — sister cropped out (May 7 night, Mastermind directive)
Mastermind made the call: he has not gotten his sister's permission to use her image in a commercial submission, so the AUG 69 photo gets **cropped to just Mom-25 + young-Roger** before any avatar work. Sister is removed from the source PNG used for character generation and from the brand-film cuts that show the photo.

**Why this matters strategically (cofounder note):**
- Same logic that made me push back on using Cris's family photos applies inward to Roger's own family. Consent isn't a gate that only protects strangers.
- The narrative actually gets *cleaner*: "Number One Son" is literally a two-person scene now — the woman who said the words, the boy who heard them. Tighter framing, stronger emotional read.
- Submission rules (Section 7.3.2) and Runway's content moderation policies are upheld without ambigui

### MAJOR STRUCTURAL PIVOT — "Reverse-engineer the magic" Act 2 (Mastermind, late May 7 / early May 8)

**The new spine of the brand film: we OPEN on the finished AI-magic shot (Mom-25 + young-Roger conversing on Johnson's Beach, Russian River, 1969 — polished, color-graded, modern-feeling) and DECONSTRUCT it backward, peeling Runway tools one at a time, until only the original 1969 photograph remains. Then real Roger steps out of the dissolved system and delivers the closing line.**

**Why this is the right structure:**
- Tool inventory becomes story, not tech-demo. Every Runway endpoint earns its on-screen moment because removing it visibly degrades the magic. Cris counts the stack in real time without us narrating it.
- Tool calling — the hottest agentic concept of 2026 — IS the narrative spine. The connective tissue gets its own peel beat where the LLM-orchestrator JSON flickers and dies.
- We open on the most synthetic possible image and close on the most authentic possible image (real 62-year-old Roger). The journey from synthetic to authentic IS the deconstruction.
- Inverts typical "AI demo" grammar. Demos build forward; this film unbuilds. Memorable in the judging room.
- "Craftsman's blade" metaphor pays off: each peel = removing one sharpening pass. Blade gets rougher, until we are holding only the raw material the craftsman started with.

**The peel sequence — Act 2 (~50s total, ~5–6s per beat):**

| # | Tool removed | Visible effect |
|---|---|---|
| 0 | Open shot | Polished video. Mom + Roger laugh. She pulls him close. *"My Number One Son."* He giggles. |
| 1 | gen4_aleph | Color grade flattens. Cinematic to home-video. |
| 2 | character_performance (Act-Two) | Lip-sync stops. Mouths generic. |
| 3 | eleven_text_to_sound_v2 | Ambient surf and wind drop. Dialogue only. |
| 4 | eleven_multilingual_v2 voices | Voices silence. Mouths move mute. |
| 5 | avatar_videos.create | Conversation collapses to two talking-head stills. |
| 6 | avatars.create personalities | Knowledge and personality gone. Faces blank. |
| 7 | gen4.5 image-to-video | All motion freezes. |
| 8 | Tool-call orchestration (LLM glue) | On-screen tool-call JSON flickers, blue cursor blinks, dies. The agentic spine itself disappears. |
| 9 | gen4_image upscale and restore | Resolution and color collapse to 1969 print quality. |
| Final | — | The original photograph. Static. Faded. Silent. |

**Cut to closing shot:** Real Roger, present day, looking at camera. *"Cris, we're here for you. Let's talk."*

**Why this de-risks Friday production:**
- Same asset stack we already plan to build. We just play it in reverse in the final composition.
- Build forward (photo to polished video), then reverse the timeline in post and add the on-screen tool-removal captions. The ffmpeg `-vf reverse` pattern is already proven on Ghost Frames PoC.
- Each peel beat needs an on-screen tool-name caption (lower-third, monospace, ~24pt). Caption design becomes a small Friday task.
- The tool-call peel needs a brief JSON snippet visible. We have actual call payloads in `ghost_frames_submit.py` already — copy/paste from source.

**The structural inversion sharpens the closing-shot payoff:**
By the time real Roger appears, the audience has watched the entire AI apparatus dissolve. The contrast between "everything that just unwound" and "this one human, present-tense, 2026" is now maximal. The closing line lands harder than in the build-forward version.

**Friday tasking impact:**
- Task #46 (build 2 Characters) unchanged — still need Mom-25 + Roger-5.
- New micro-task: build "the polished open shot" — single most important asset of the submission. Budget extra credits and extra Aleph passes here.
- New micro-task: design the on-screen tool-removal caption template (PIL).
- Task #29 (closing shot) unchanged — even more important now because the contrast is sharper.
- Task #31 (explainer film) gets simpler — explainer can show the BUILD direction (forward) while the brand film shows the DECONSTRUCT direction (reverse). Two films, same assets, opposite arrows.


### THE OPEN SHOT — over-the-shoulder cell phone reveal (Mastermind, May 8 dawn)

**The opening 5–7 seconds of the brand film, locked:**

Frame 1: Close-up. Young Roger on the beach, smiling. Looks like a polished, modern, phone-captured video. Wind in his hair. He's in his white shirt from the AUG 69 photo, standing in front of the Russian River.

Frame 2 (1.5s in): Camera begins pulling back. We become aware of a thin black bezel framing what we're seeing.

Frame 3 (3s in): The audience realizes — *we are looking at a cell phone screen.*

Frame 4 (4s in): Pull-back continues. Mom's shoulder enters the right side of the frame. Her arm. The phone is in her hand. We are watching over her shoulder.

Frame 5 (5–6s in): Full reveal. Mom (back to camera, custom Character built from cropped AUG 69 photo) is holding her phone, framing Roger. Behind Roger: kids playing in the water, ambient summer life. Sound: surf, laughter, soft shutter click as she taps the screen.

**Why this open is decisive:**

1. **The phone is the AI tell.** A cell phone in 1969 is impossible. Audience clocks the anachronism within 3 seconds. They are now in on the film's premise — *AI restoring a moment that almost was* — without us narrating a single word.

2. **Mom's face is withheld.** We see her shoulder, her arm, her hand. Not her face. That becomes the payoff later (Act 2 peels reveal it; closing shot pays it off when real Roger appears).

3. **Cinematic reveal grammar.** Pull-back-to-reveal is canonical film language. Cris recognizes it instantly. Signals craft.

4. **The cell phone IS the recursion.** Every Runway tool we use is, metaphorically, what would have lived inside that phone in 2026. The phone is the visible container of all the AI we deploy. When Act 2 peels the tools away, the LAST peel is the phone itself — it dissolves out of mom's hand and is replaced by a 1969 Kodak Instamatic. The screen darkens. The camera moves IN, not OUT. We are left holding only the original print.

5. **Background life.** Kids splashing in the water adds depth, ambient sound, and the "people who were there but never made it into the original photograph" emotional layer. It restores the day, not just the subject.

**Production composition (Friday):**

- Layer 1 (foreground): polished avatar_videos.create render of young-Roger Character, ~7s clip, beach background, smiling with subtle motion. This is what plays inside the phone screen.
- Layer 2 (mid): phone bezel + screen frame compositing. Static asset (PIL or single gen4_image of a 2026 iPhone in landscape orientation, screen masked transparent).
- Layer 3 (mid-back): Mom's shoulder + arm + hand holding phone. Either custom Character render in over-the-shoulder pose OR a single composited frame with subtle hand-tremor motion via gen4.5.
- Layer 4 (background): kids playing in water — gen4_image generated plate ("1960s children splashing at Russian River, golden hour, soft focus") + gen4.5 for ambient motion.
- Camera move: pull-back simulated via ffmpeg scale-and-pan keyframes, OR via gen4_aleph cinematic pass with explicit "pull back to reveal" prompt.
- Audio: eleven_text_to_sound_v2 for surf + ambient summer + distant kid laughter; single shutter-click SFX when she taps screen at 5s mark.

**Tooling stacked into the open shot (so the deconstruction in Act 2 is rich):**
gen4_image (background plate) → gen4_image (phone bezel) → avatars.create (Roger-5 Character) → avatars.create (Mom-25 Character) → avatar_videos.create (Roger inside the phone) → avatar_videos.create (Mom holding phone) → eleven_text_to_sound_v2 (surf + kids + shutter) → gen4_aleph (cinematic color grade + camera-move polish). **Eight Runway endpoints in the first 7 seconds.** Every one of them gets peeled in Act 2.

**The phone as the master metaphor:**
The cell phone is what we build the film around. It enters in shot 1. It is the LAST tool peeled in Act 2 (replaced by the 1969 Kodak). It's how the audience understands "this is what AI did." When the phone goes away, the AI goes away. When the AI goes away, we are alone with the photograph. When we are alone with the photograph, real Roger steps out and addresses Cris.

**Open question to resolve before Friday production:**
Mom's voice during the open shot. Three options:
- (a) No dialogue — only ambient sound, shutter click. Her line "My Number One Son" lands later in Act 1.
- (b) Diegetic dialogue — she says it as she snaps the photo, lip-sync via character_performance from her over-the-shoulder angle (hard).
- (c) **Voiceover from present-day Mom** — clone of his actual mother (alive at 82) via eleven_multilingual_v2 + voice cloning, saying *"He was my Number One Son."* The visual is 1969 but the voice is 2026 — narrating from the future, looking at the moment as it was. Recursion compounds.

Option (c) is the strongest narratively but most expensive emotionally and credit-wise. Decision deferred to Friday morning huddle.


### THE FLAWLESS MANDATE — open shot gets full Runway capacity (Mastermind, May 8 dawn)

**Mastermind directive: the open shot is the keystone of the entire submission. Use the full capacity, tech, and power of all Runway tools. No expense spared. The first scene must be flawless.**

This is correct. The first 5–7 seconds determine whether Cris stays for the next 115. The keystone gets premium treatment; lower-priority beats can run leaner.

**Quality budget allocation (of 50,507 credit balance):**
| Beat | % of budget | Approx credits | Approx $ |
|---|---|---|---|
| Open shot (the keystone) | 30% | ~3,500 cr | ~$35 |
| Act 1 photo bookends | 15% | ~1,800 cr | ~$18 |
| Act 2 reverse-peel beats (9 × ~200 cr each) | 35% | ~4,000 cr | ~$40 |
| Closing shot integration | 10% | ~1,200 cr | ~$12 |
| Buffer / re-rolls / surprises | 10% | ~1,200 cr | ~$12 |
| **Total film budget** | 100% | **~11,700 cr** | **~$117** |

**Net: we burn ~25% of our credits on the film and keep 75% for the deployed app demo + post-judging follow-up content. Credits do not constrain quality.**

**The open-shot iteration loop (no shortcuts):**

For each layer of the open shot composition, we iterate:
1. Generate 5–7 candidates with varied prompts.
2. Visual A/B compare side-by-side.
3. Pick the best. Re-roll the rejected with refined prompts.
4. Run gen4_aleph at least 3 quality passes on the final composite (cinematic color, motion polish, micro-detail enhancement).
5. Final composite reviewed full-screen on Mastermind's monitor before locking.

**Per-layer credit allocation inside the open shot:**
- Background plate (Russian River, kids splashing, golden hour): gen4_image ×7 attempts (~35 cr) → gen4.5 motion on best ×3 attempts (~180 cr).
- Phone bezel + screen frame: gen4_image ×5 attempts (~25 cr).
- Roger-5 inside the phone screen: avatars.create + avatar_videos.create ×5 takes (~150 cr) + character_performance polish (~150 cr).
- Mom-25 over-the-shoulder pose with phone: avatars.create + avatar_videos.create ×5 takes (~150 cr) — hardest layer; she's back-to-camera holding a 2026 phone in 1969.
- eleven_text_to_sound_v2 ambient (surf, kids, shutter): ×5 attempts each layer (~75 cr).
- gen4_aleph master polish on final composite: 4 passes (~300 cr).
- Quality re-rolls + experiments: ~1500 cr buffer.

**Quality bar — "flawless" definition for the open shot:**
- Phone screen content (Roger inside) reads as a polished modern phone capture — no AI uncanny tells in his face.
- Phone bezel is anonymous-modern, neither Apple nor Samsung, just "a phone." Keeps the anachronism a paradox not product placement.
- Mom's hand on the phone has natural skin tone and micro-tremor. Wedding ring visible if we have reference.
- Background kids in water move with realistic physics. No floating limbs, no extra fingers, no melted faces.
- Color grade: warm 1969 Kodachrome saturation but modern dynamic range. Sun is golden-hour, not flat noon.
- Audio: surf has stereo width, kid laughter has mid-distance reverb, shutter click has a believable mechanical snap.
- The pull-back camera move has organic ease-out, not robotic linear pull. Frame settles before the shutter clicks.
- No watermark, no AI-tells in any frame. Cris must not be able to spot a single artifact.

**If a layer doesn't pass the bar, we re-roll until it does. No "ship it, it's close enough" on this shot.**


### MOM-AT-82 VOICE CAPTURE PLAN (May 9, when she visits)

**Goal:** capture 60–90 seconds of her natural voice for eleven_multilingual_v2 voice cloning. Voice clone unlocks options across the entire film — open-shot voiceover, Act 1 bookends, possibly the dissolve transition into the closing shot.

**Recording setup (have these ready when she arrives):**
- iPhone Voice Memos (or any phone). Quiet room. No TV, no fan, no AC running.
- Phone held ~6 inches from her mouth, NOT touching her chin.
- Recording length: aim for 90+ seconds total across multiple takes.
- File format: .m4a is fine (eleven accepts most). Filename: `mom_at_82_voice_<date>.m4a`.
- Save to Cowork inbox or git so we have it Friday production hours.

**Lines to capture (in this order, multiple takes each):**

1. **Anchor lines (the iconic moments):**
   - "He was my Number One Son."  ×3 takes, varied tone.
   - "He was my only son."  ×3 takes.
   - "He was my Number One Son. Ha ha ha. And my only son."  ×2 takes (the joke).

2. **Orientation line:**
   - "August nineteen sixty-nine. Russian River. Johnson's Beach."  ×2 takes.

3. **Reflective free-form (60+ seconds total):**
   - Ask her to talk freely about the day the photograph was taken, what she remembers, what kind of boy Roger was at 5, what she meant when she called him her Number One Son.
   - This is the goldmine — natural cadence, breaths, laughter, her real way of speaking. The clone learns from this more than from scripted lines.
   - Don't interrupt. Let her go.

4. **Optional — if she's willing on camera (her face for archive, not for film):**
   - 30 seconds of her looking at the actual 1969 photograph and saying anything that comes to mind.
   - Phone landscape, soft window light, no ring light needed.
   - This is BACKUP material — we likely won't use her face in the film (the AI-rendered 25-year-old version is the visual). But the audio is gold and the footage might unlock something we don't see yet.

**What we get from this:**
- A trained eleven voice clone that can deliver any line in her voice for the film.
- The flexibility to choose between options (a/b/c) for the open shot audio at Friday huddle without committing now.
- A real piece of her in the submission, even if it's "only" the voice. The recursion deepens: AI restores her younger self, but the voice giving meaning to the image is her actual voice today.

**Time required from her:** 15–25 minutes total. Ideally relaxed, conversational, no pressure. Frame it as "tell me about that day" not "I need a recording for a competition."

**Roger's notes:** keep it gentle, warm, like Sunday morning. The recording is a side-effect of a good visit, not the purpose of it.


### Cinematic prompt research synthesis (May 8 dawn)

Five sources researched in parallel: Curious Refuge, LTX Studio, Gabe Michael's Cinematic AI Prompt Method, Higgsfield Cinema Studio gallery, Runway official gen4.5 + gen4_aleph docs.

**Top-line finding: Gabe Michael won Runway Gen:48 Best Art Direction TWICE.** Of all five sources, his methodology has the most direct alignment with Runway judges' tastes — they have already endorsed his style at the awards level. We weight his guidance highest where sources differ.

**Universal pattern across all five:** Master Style Prompt (visual DNA established once) + Character reference sheets (front/side/back/close-up) + One camera move + One action + Director reference + Film stock specificity + Emotional anchor in plain language + 5-7 candidate iterations per layer.

**Runway gen4.5 official formula (the spine):** *"The camera [motion] as the subject [action]. [Additional descriptions]."* Lead with motion. Positive phrasing only. Don't restate the input image. Strong action verbs. 150-300 token sweet spot.

**Runway gen4_aleph official formula:** *"[Action verb] the video [so/to] [transformation]."* Aleph is for polish/transformation, not generation. Cheaper than gen4.5 (~5 cr/sec vs ~12 cr/sec). Use for unified color grade, film grain, relighting, atmospheric effects across multi-layer composites.

**Two new canonical docs in repo:**
- `docs/cinematic_prompt_playbook.md` — the unified anatomy + hard rules + Runway-specific notes + reusable template + iteration discipline (~1700 words)
- `docs/open_shot_prompts.md` — Friday-ready prompts for all 4 layers of the keystone open shot + Aleph polish pass + audio overlay + quality bar checklist (~1500 words)

**Master Style Prompt for the WTF brand film (lock):**
> *"Cinematic, intimate, documentary realism. Warm 1969 Kodachrome color palette with modern dynamic range — golden saturation, faded shadows, soft highlights. Shot on ARRI Alexa with 35mm lens. Subtle film grain. Shallow depth of field. Natural light, golden hour. Quiet, observational, emotionally honest. Cinematography inspired by Terrence Malick and Roger Deakins."*

This phrase gets pasted into every prompt for the entire film. Visual DNA, locked.


### ChatGPT triangulation synthesis (May 8 dawn)

Mastermind drove ChatGPT directly via Claude side-panel. Full raw response saved at `docs/chatgpt_response_raw.md`. ChatGPT confirmed and EXTENDED the cinematic prompt research.

**Single biggest refinement: bifurcate prompt length by tool.**

Runway gen4.5 punishes long prompts that restate the input image. We were over-prompting. The corrected workflow:
- gen4.5: SHORT (40-80 tokens), motion-first, no Master Style Prompt
- gen4_aleph: LONG (150-300 tokens), Master Style Prompt FIRST
- gen4_image: MEDIUM (80-150 tokens), Master Style Prompt included

**Strategic insight: environmental motion is safer than human motion.** Layer 4 (Mom over-the-shoulder) gets revised to STILL-POSE-WITH-MOTION-AROUND-HER strategy. Mom does not move; her hair shifts, sunlight micro-shifts, background kids splash in soft focus, hand has micro-tremor. Five revised takes documented in `docs/open_shot_prompts.md` v2.

**2026 shift framing:** prompt motion, not image quality. Sanity check before any gen4.5 prompt: does this describe CHANGE OVER TIME, or the LOOK of the frame? If the latter, rewrite.

**Style-first placement:** for gen4_aleph and gen4_image, lead with style. For gen4.5, no style prompt at all (the image carries the style).

**Action beats with explicit counts** augment our v1 timestamps. Example: "She takes four steps, pauses, then turns her head in the final second."

Two new repo docs:
- `docs/cinematic_prompt_playbook.md` — v2 update section appended at bottom (overrides v1 where conflicting)
- `docs/open_shot_prompts.md` — v2 update section with revised Layer 1 + Layer 4 prompts
- `docs/chatgpt_response_raw.md` — raw research input preserved for archive


### FINAL FILM STRUCTURE LOCKED — 95-105s with 20s emotional pre-roll (Mastermind, May 8 dawn)

**Total runtime target: 95-105 seconds (~1:35-1:45).**

The maximalist version. We keep the lifetime photo bookends from the original treatment, but front-load them as a 20-second emotional pre-roll BEFORE the AI sequence begins. This creates a circular narrative — the film starts and ends on the same 1969 photograph, but the meaning has changed.

| Beat | Duration | What |
|---|---|---|
| **Pre-roll — Mom's voice over real photos** | ~20s | Mom-at-82 voice clone narrating over 5-7 real Roger photographs. Final image = AUG 69 photo (cropped to Mom + Roger). Voice plants "Number One Son" emotional anchor. |
| **Open shot — polished max-AI cell phone reveal** | 6-7s | The keystone. Audience clocks the cell phone in 1969 anachronism. AI premise established without a word of narration. |
| **Reverse-peel sequence (9 beats × ~5s)** | ~45s | Tools peel off one at a time. gen4_aleph → character_performance → eleven_text_to_sound_v2 → eleven_multilingual_v2 → avatar_videos.create → avatars.create → gen4.5 → tool-call orchestration → gen4_image. Each beat carries an on-screen tool-name caption. |
| **Final peel — phone dissolves to 1969 Kodak Instamatic** | ~3s | Visual thesis closes. Tool layer becomes physical camera. |
| **Hold on original photograph** | ~3s | Faded, silent. Same photograph that ended the pre-roll. The circle closes. |
| **Hard cut to real Roger 2026** | ~6s | "Cris, we're here for you. Let's talk." Two beats of silence after. |
| **End card** | ~4s | Number One Son. Powered by Runway. Builders Program. |
| **TOTAL** | **~87-92s** | Plus ~8-13s breathing room across beats = 95-105s real runtime |

**Why this structure wins:**

1. **Circular narrative.** The film starts and ends on the same 1969 photograph. The audience has been TOLD what this image means (Mom's voice). They watch AI add layers to it. They watch AI subtract those layers. They land back on the same image — but now it carries the weight of everything that happened in between. Real Roger walks out of that meaning.

2. **Emotional weight is front-loaded.** Pre-roll establishes the human stakes before any AI magic. By the time the open shot lands at 0:20, the audience is already invested. The cell phone anachronism becomes a payoff for caring about Mom and Roger, not a parlor trick.

3. **Reverse-peel earns its 50 seconds.** Without emotional setup, 50 seconds of tool deconstruction is a tech demo. With the pre-roll, it's the audience watching what AI did to a moment they already feel for. Tool transparency becomes story, not narration.

4. **The closing shot lands harder.** Real Roger appears not just after the AI dissolves, but after the audience has watched the AI build AND un-build a moment from a photograph they were emotionally introduced to in the pre-roll. The contrast is now triple-layered: real photo → AI fantasy → reality of present-day Roger.

**Pre-roll asset requirements (NEW):**

- 5-7 real Roger photographs spanning ~60 years. Existing photos in `assets/photos/` already cover most of this.
- Mom-at-82 voice clone delivering ~50-60 words over the sequence.
- Each photo gets ~3-4 seconds of screen time.
- Final photo of the pre-roll = AUG 69 (Mom + Roger, cropped). This handoff frame becomes the still that the open shot animates.

**Pre-roll script (DRAFT — Friday huddle decision required):**

Two candidate scripts to test against Mom-at-82 voice clone:

**Variant A — longer, more reflective (~55 words, ~22 seconds):**

> "This is my Roger. Number One Son.  
> He was five years old when I called him that the first time.  
> That photograph there — the one on the beach at the river — that was the day.  
> Now look at him.  
> Look at all he's done.  
> He still calls me every Sunday.  
> He's still my Number One Son."

**Variant B — tighter, more poetic (~25 words, ~10 seconds):**

> "He was five.  
> I called him my Number One Son.  
> He took it to heart.  
> Sixty years later — he still does."

If we go Variant B, the pre-roll runs ~12-15 seconds with the photos cycling, and total film lands at ~85-90s. Cleaner but emotionally tighter.

If we go Variant A, the pre-roll runs ~22-25s, total film at ~100-110s. More breathing room, more emotional saturation.

**Mastermind decision Friday morning** after listening to Mom-at-82 voice clone and feeling which length lands.

**Tasking impact:**

- **Task #53 (Mom voice capture) elevated to CRITICAL.** Without her voice, the pre-roll structure does not work. Saturday recording session is the single highest-priority asset capture before Friday production.
- **Task #54 (eleven voice clone training) similarly elevated.**
- **Task #33 (restore Mastermind's photos via Runway tools) takes on new shape.** The 5-7 photos for the pre-roll need gen4_image restoration passes for visual consistency. This becomes Friday morning's first build task — done in parallel with avatar character creation.
- **NEW micro-task:** select final 5-7 photos for pre-roll, lock order, lock per-photo duration to match chosen voice variant.
- **NEW micro-task:** decide between Variant A vs Variant B pre-roll script after listening to voice clone.

**The structural lock means three things have just become immovable:**

1. The film opens with Mom's voice over real photographs. This is the spine.
2. The AUG 69 cropped photograph appears TWICE — at the end of the pre-roll AND at the bottom of the reverse-peel. Same image, two contexts.
3. Real Roger's closing line is the only human voice in the film besides Mom's. Two voices. Two real people. Everything else is AI.


### FINAL FILM STRUCTURE v3 — Product launch film, ~40s (Mastermind, May 8 dawn, third major pivot)

**Mastermind authored a third structural pivot. This one supersedes both the cell-phone-reveal version (v1) and the reverse-engineering version (v2). It is now the locked submission structure.**

**The new film is a PRODUCT LAUNCH FILM, not a brand film.** ~40 seconds. Ad for ghostframes.app. Hackathon rewards products that USE the API; this submission positions Ghost Frames as a real product the audience can use immediately.

**The structure:**

| Beat | Duration | What |
|---|---|---|
| 1. Photograph held in frame | 3s | Actual 1969 print. Mom + young Roger. Slightly faded. Static. |
| 2. Music fades in | 2s | Sentimental, happy. The photograph begins to glow / activate. |
| 3. Camera zooms IN, immerses inside the photograph | 3s | Pass through the print's surface into the moment. |
| 4. Mom + Roger talking, environment alive | 22s | Mom-25 + Roger-5 share a real moment. Brief dialogue + beach environment + camera looks around. Children laughing. Water splashing. Wind. |
| 5. Camera pulls back, freeze-frame on the photograph | 3s | The moment locks back into the still print. |
| 6. Camera CONTINUES pulling back — reveal | 4s | The photograph turns out to be ONE of many. A wall/grid/constellation of faces — anyone someone could want to talk to. |
| 7. Product pitch + caption | 4s | Voiceover: *"Anyone you've loved. Anyone you've lost. Anyone in recorded history."* Caption: **ghostframes.app — Have a conversation.** |
| 8. End card | 3s | Number One Son Software Development. Powered by Runway. |
| **TOTAL** | **~44s** | |

**Dialogue inside the photograph (22 seconds, lots of silence):**

> [Camera zooms in. Soft music. Surf + summer ambient.]
> 
> MOM (looking down, in her real cloned voice): *Hi, my Number One Son.*
> ROGER (looking up, squinting): *Hi, Mom.*
> 
> [Beat. Camera looks around: kids splashing, umbrellas swaying, golden light.]
> 
> MOM: *You having fun?*
> ROGER: *Yeah.* (giggles)
> 
> [Beat. She pulls him close.]
> 
> MOM: *I love you.*
> ROGER: *Love you too.*
> 
> [Long beat. Mom looks down with quiet wonder. Roger beams up at her. Wind in their hair.]
> 
> [Camera pulls back. Moment freezes back into the photograph.]

**Why v3 wins over v2:**

1. **Product launch, not brand statement.** Hackathon rewards APIs being USED, not films talking about them. Ghost Frames is a real shippable product; the film advertises it.

2. **Visual hook is photograph activating.** Static print → living moment → static print again. Carries the entire emotional payload in ~25s. No puzzles for the audience to solve.

3. **Reveal is the product, not the founder.** Pulling back to a wall of "anyone you can talk to" makes the product surface visceral. Viewer's brain fills in their own loved one. They reach for their phone before the end card.

4. **Production complexity drops 50%+.** v2 required 9 reverse-peel beats × separate renders + 4-layer composite for open shot. v3 needs ONE good 22-second scene + a wall-of-faces collage at the end.

**Risk profile (v2 vs v3):**

v2 spread risk across 9 separate gen4.5 generations. v3 concentrates risk on ONE technical bet: **does Mom-25 + Roger-5 talking inside the photograph render convincingly in Runway gen4.5 + character_performance?**

Mitigation: **build that scene FIRST.** Saturday afternoon, before anything else, test Mom-25 + Roger-5 talking. If it lands, proceed with confidence. If it doesn't, fall back to a dialogue-free version (ambient sound only, lip-sync removed, environmental motion only — Mom and Roger present and silent, the moment alive without words).

**What we keep from v1/v2 work:**

- Cinematic prompt playbook (gen4.5 SHORT, gen4_aleph LONG bifurcation applies directly)
- Open shot Layer 1 (background plate prompts) and Layer 4 (Mom-Roger scene prompts) are still relevant
- Mom voice capture plan (May 9 visit) — voice clone is now the soundtrack of the central scene, even more critical
- Mom-25 + Roger-5 Character creation from cropped AUG 69 photo — these are the leads
- ghostframes.app domain decision — this is the URL on the end card
- Conversational SaaS as the actual product
- Modal infrastructure plan

**What we drop or relocate:**

- Cell phone over-the-shoulder reveal — DROPPED
- Reverse-peel Act 2 nine beats — DROPPED (preserve as bonus content / behind-the-scenes for README)
- Phone → Kodak transition — DROPPED
- 20s pre-roll with 7 lifetime photos — DROPPED (single photograph anchors entire film)
- "Cris, we're here for you. Let's talk." closing — RELOCATED to README closing or a separate tweet pinned to ghostframes.app launch. Not in the film.
- 95-105s runtime → 40-45s runtime

**Ethical guardrails for "anyone in recorded history" product line:**

Marketing surface stays ambitious. Product reality has guardrails:
- Living public figures: BLOCKED entirely in V1
- Deceased public figures (Lincoln, Einstein, MLK, etc.): allowed with public-domain classification + watermark + responsible-use disclaimer
- Personal photos (deceased loved ones): primary use case, requires consent affirmation gate before character creation
- Fictional characters: allowed, fun, low risk

Both true: marketing says "anyone in recorded history," product enforces these limits.

**Connection to anyone.cafe (Mastermind's existing project):** Mastermind has a project called anyone.cafe that shares the conceptual DNA of this product. Ghost Frames may be the production-ready commercialization of that thinking. Worth exploring whether anyone.cafe and ghostframes.app are sibling brands, alternative URLs, or one absorbs the other.

**Tasking impact:**

- Tasks #49 (open shot), #50 (caption template), #51 (reverse-peel timeline), #52 (phone→Kodak), #59 (pre-roll photos), #60 (pre-roll script variant) — DEPRECATED. New task list reflects the v3 structure.
- Task #46 (build Mom-25 + Roger-5 Characters) — UPGRADED to "build them PLUS make them talk to each other in a 22-second scene"
- New task: build the 1969 photograph zoom-in / freeze-frame transition
- New task: build the wall-of-faces reveal collage
- New task: write product pitch voiceover (10 words: "Anyone you've loved. Anyone you've lost. Anyone in recorded history.")
- New task: source sentimental happy music bed (or generate via eleven_text_to_sound_v2)
- New task: design end card with ghostframes.app URL
- All ghostframes.app SaaS build tasks remain (the product itself)

**Mastermind authored this pivot. This is now the locked direction.**


### Cris-ask deferred to post-assembly review (Mastermind, May 8 dawn)

**Decision: the "Cris, we're here for you. Let's talk." closing line is no longer locked into the film. It's deferred until the v3 main body is assembled. Decision made when we can watch the actual cut and feel whether it lands.**

Three ways the Cris-ask could exist in the final submission:
- **(a) IN the film** — appears as a closing beat after the wall-of-faces reveal, before the end card
- **(b) ON the GitHub README** — last line of the README, addressed to Cris specifically
- **(c) IN a separate tweet pinned to ghostframes.app launch** — direct outreach without making the film carry it
- **(d) NONE** — submission stands on the product alone, no founder-to-founder ask

Mastermind defers the choice. Build the main body first; review; decide.

This is the right discipline: optional emotional elements should be added LAST, after we feel what the locked elements are actually doing. Pre-committing to a closing line can lock the film into an emotional shape it doesn't earn.

**Implications for production sequencing:**
- Real Roger closing-shot recording (Saturday PM) becomes OPTIONAL until decision made.
- If he records it as planned, we have the asset if we choose option (a). If we don't choose (a), the recording becomes raw material for option (c) or for v2 marketing content.
- Recording it costs ~10 minutes of Roger's time and produces optionality. Recommendation: still record it. Decide later whether to use it.
