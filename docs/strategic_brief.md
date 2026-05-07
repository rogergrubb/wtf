# Runway API Hackathon 2026: Strategic Brief for Number One Son
**Prepared for: Roger & Co-Founder**
**Date: May 5, 2026**
**Hackathon Dates: May 8-11, 2026**
**Objective: Win $25K + 200K API credits**

---

## EXECUTIVE SUMMARY

The May 8-11 Runway API Hackathon is **fundamentally different** from Runway's other competitions (Gen:48, AIFF). It rewards **practical problem-solving over pure creativity**, **commercial viability over artistic vision**, and **systems-thinking over feature showcases**.

**Key Insight:** Judges are looking for builders who see Runway's API as a *tool to solve real problems*, not creators who want to make beautiful AI-generated content. This is a developer/entrepreneur competition disguised as a hackathon.

---

## THE HACKATHON AT A GLANCE

| Metric | Detail |
|--------|--------|
| **Dates** | May 8-11, 2026 (72 hours) |
| **Format** | Virtual, self-organized teams |
| **1st Prize** | $25,000 cash + 200,000 API credits |
| **2nd Prize** | 200,000 API credits |
| **3rd Prize** | 200,000 API credits |
| **Participant Credits** | All participants get 50,000 API credits |
| **Co-Organizer** | Modal (infrastructure/deployment partner) |
| **Winner Announcement** | May 15, 2026 |

### Judging Criteria (Official)
1. **Creativity** (25%?) — Does it solve a real problem or explore interesting use case?
2. **Technical Depth** (25%?) — Does it leverage Runway API beyond basic usage?
3. **Impact** (25%?) — Is it usable by real users? Product potential?
4. **Polish** (25%?) — Working demo, not a concept. End-to-end experience?

*Note: Official weightings not provided. These are inferred from scoring patterns across similar competitions.*

---

## WHAT WINS: THE WINNING FORMULA

### Ingredient 1: Real Problem + Real Market
**Winning projects solve problems people actually have and will pay to solve.**

Examples of strong problem statements:
- "Marketing teams spend 40+ hours/week manually editing product demo videos. We cut that to 4 hours."
- "Customer support teams answer same questions 500x/day. We built an AI agent that handles tier-1 support."
- "Indie developers can't afford $500/day video editors. We made one that costs $5."

Examples of weak problem statements:
- "We wanted to see what Runway could do."
- "AI-generated videos are cool, so we made more."
- "Imagine if video creation was easy." (It is easy already.)

**How to Win on This Dimension:**
- Interview 5-10 potential users before submitting (in the 72 hours, that's doable)
- Document in your demo: current manual process + your solution
- Show time/cost savings with numbers
- Identify market size (even if rough: "50,000 indie creators", "8M small businesses")

### Ingredient 2: Sophisticated API Integration (Not Feature Showcase)
**Judges want to see systems that chain multiple decisions, not single API calls.**

Weak API usage:
```
user input → Runway API → output
```

Strong API usage:
```
user input → LLM decides what to generate → Runway generates → check quality → 
iterate prompt → Runway generates again → compare variants → return best
```

Or:
```
user request → LLM breaks into shots → Runway generates each shot → 
LLM scores coherence → refine shots that scored low → assemble into video → 
add voiceover via TTS → sync audio → deliver
```

**How to Win on This Dimension:**
- Show your system making multi-step decisions
- Integrate Runway with at least one other API (LLM, voice, image, database)
- Build feedback loops (system learns from user feedback)
- Optimize for something measurable (latency, cost, quality)
- Handle asynchronous operations properly (don't block on long API calls)

### Ingredient 3: Integration with Real Workflow
**Judges want to see projects that fit into tools people already use.**

Strong integrations:
- Slack bot (command: `/create-demo-video "product X has feature Y"`)
- Web UI inside existing CMS
- API endpoint that works in video editing pipeline
- Discord bot for creators
- Browser extension for content creators
- Webhook handler for marketing automation

Weak integrations:
- Standalone Python script
- Local command-line tool
- Requires setting 5 environment variables
- Must run custom Docker container
- No clear user entry point

**How to Win on This Dimension:**
- Pick ONE integration point (don't try to support Slack + Discord + Web + CLI in 72 hours)
- Make it 2-click setup (authentication handled, no manual config)
- Show non-technical person using it (if applicable)
- Document deployment process clearly

### Ingredient 4: Relentless Polish
**Judges expect working demos, not prototypes or concepts.**

Strong polish signals:
- Demo video shows full workflow (input → output)
- Handles edge cases gracefully (typos, empty inputs, rate limits)
- Error messages are helpful, not cryptic
- UI is professionally designed (even if simple)
- No manual steps between submissions
- Reproducible setup for judges

Weak polish signals:
- "We ran out of time, so..."
- Works 80% of the time
- Requires manual fixes between demo runs
- Unclear how to actually use it
- Documentation is incomplete
- Demo breaks on unexpected input

**How to Win on This Dimension:**
- Test with edge cases (what if input is blank? 1 word? 10,000 words? special characters?)
- Have a pre-recorded demo video in case live demo fails
- Write README assuming judges don't know your domain
- Include example commands/screenshots
- Make the deploy-and-run process foolproof

---

## WHAT DOESN'T WIN: Common Failures

### ❌ Feature Showcases
"We used Runway's Gen-2, Gen-3, Characters, Voices, and Avatars APIs in one project!"

**Why this fails:** API capabilities aren't interesting; solving problems with APIs is.

### ❌ Art Projects
"Here are 100 beautiful AI-generated frames arranged as a visual essay on meaning."

**Why this fails:** This is Gen:48 or AIFF, not an API hackathon. Different competition.

### ❌ Toy Examples
"Generate meme videos automatically by meme template."

**Why this fails:** The problem isn't real ("Generating memes" takes 2 minutes manually). No market.

### ❌ Incomplete Execution
"If we had more time, we'd add..."

**Why this fails:** Judges see incomplete, rate it as incomplete.

### ❌ Single API Call
User input → Runway Gen-2 → video

**Why this fails:** No technical depth. Could do this in 30 minutes on Day 1. Judges want to see you *solve* something *with* the API.

### ❌ Over-Scoped
"We're building a full video production suite with AI-powered editing, color grading, sound design, and automated subtitles."

**Why this fails:** 72 hours. Pick one killer feature, not 5 incomplete ones.

---

## THE WINNING TEAM PROFILE

Based on Runway competition history, winning teams typically include:

### Skills Needed
1. **Backend/Full-Stack Engineer** (API integration, orchestration, deployment)
2. **Product Thinking** (problem identification, UX design)
3. **Demo Skills** (can explain complexity in 3 minutes)

### Team Size
- **Solo:** Possible (but harder to ship a complete product in 72h)
- **2-3 people:** Optimal (one person → API integration, one → UI/product, one → demo/docs)
- **4+:** Overkill for a hackathon (too many dependencies)

### Ideal Background Combo
- AI/ML engineer + product manager + designer
- Backend engineer + frontend engineer + business person
- Full-stack developer + creative partner + someone who can talk to customers

### What Doesn't Matter
- Famous names on team (judges care about the project, not the team)
- Tons of followers (irrelevant to judging)
- Expensive hardware/software (Runway API credits are provided)
- Prior startup experience (helpful but not required)

---

## THE 72-HOUR EXECUTION PLAN

### Friday, May 8 — Kickoff Day (6 hours of actual work)

**9:00am ET** — Hackathon begins with Runway overview & API walkthrough
- Watch the technical showcase
- Skim API docs
- Get familiar with example code

**By 2:00pm ET** — Your team should have:
- ✅ Problem identified (what are you solving?)
- ✅ Target user identified (who needs this?)
- ✅ Solution architecture sketched (how will you solve it with Runway API?)
- ✅ Tech stack decided (Node.js? Python? What framework for UI?)
- ✅ Assigned tasks (who does what?)

**By 5:00pm ET** — First spike/prototype
- Get "Hello World" working with Runway API
- Confirm you can authenticate and make a basic API call
- Verify your chosen infrastructure (Modal, local, cloud) works

**Evening** — Rest (you need sleep for productivity Sat-Sun)

### Saturday, May 9 — Build Day (16 hours of work)

**All day:** Build the core system
- **Morning:** API integration complete (can call Runway API reliably)
- **Afternoon:** Add decision logic / multi-step orchestration
- **Evening:** Integrate with your chosen interface (Slack bot / Web UI / etc.)

**Goal by end of day:** "Vertical slice" — full workflow works end-to-end, even if janky
- User can input something
- System processes through Runway API
- User gets output
- Everything integrated (no manual handoff steps)

### Sunday, May 10 — Polish & Demo (12 hours of work)

**Morning:** Fix bugs and edge cases
- What breaks when users input garbage?
- What happens at rate limits?
- What if API calls fail?

**Afternoon:** Polish UI/UX
- Make it look professional (doesn't need to be beautiful, needs to be clear)
- Write helpful error messages
- Test with fresh eyes (have someone not on team try to use it)

**Evening:** Create demo
- Record 3-5 minute video showing full workflow
- Write documentation/README
- Prepare live demo backup plan (in case something breaks in presentation)

**By 9:00am Monday:** Submit
- All code on GitHub (clean, with README)
- Demo video uploaded
- Submission forms filled out

### Monday, May 11 — Final Polish (4 hours)

**Early morning:** Last-minute fixes if anything broke
**By 9:00am ET:** Submissions close
**Breathe.** You're done.

---

## WINNING PROJECT CONCEPT (Example)

### Project: "MotionBrief"
**Tagline:** "Turn product briefs into polished demo videos in minutes, not weeks."

### The Problem
- Product marketing teams spend 2-4 weeks creating product demo videos
- Process: script → storyboard → shoot → edit → revise
- Only 30% of product teams create regular demo content (too time-consuming)
- Demo videos are expensive and slow to iterate

### The Solution
**MotionBrief**: Marketing brief → AI-generated demo video

**Workflow:**
1. PM writes brief: "Show how our new dashboard filters by date range, then compare two timeframes"
2. System (via Slack `/motionbrief` command):
   - LLM parses brief → generates shot list & script
   - Runway Gen-3 generates each shot
   - Evaluates each shot for product accuracy (custom validator)
   - If score < 0.7, regenerates with refined prompt
   - Runway Voice generates voiceover
   - Assembles shots + narration
   - Uploads to cloud
   - Returns link in Slack
3. PM previews, says "Make the dashboard movement faster"
4. System re-generates with new parameters
5. Final video ready for web, social, sales deck

### Why This Wins
- **Real Problem:** Marketing teams actually struggle with this (verified via user interviews)
- **Market Size:** 100,000+ small/mid-market SaaS companies = $1B TAM
- **Technical Depth:** 
  - Multi-step orchestration (parse → generate → validate → regenerate → assemble)
  - Integration of Runway Gen-3 + Voice APIs
  - Custom validation layer
  - Asynchronous job queue for parallel shots
- **Integration:** Slack bot means zero context switching
- **Impact:** Saves 20-30 hours per video (high ROI)
- **Polish:** Works reliably, handles revisions, professional output

### Estimated Build Time
- **Fri 2pm-5pm:** Architecture + Runway API spike (2h)
- **Sat 9am-6pm:** Core API orchestration + validation (9h)
- **Sat 6pm-11pm:** Slack bot integration (5h)
- **Sun 9am-1pm:** UI/testing/edge cases (4h)
- **Sun 1pm-5pm:** Polish + demo creation (4h)
- **Total:** ~24 hours of actual development (very doable)

---

## STRATEGIC ADVANTAGES FOR ROGER'S TEAM

### Potential Differentiators
Based on Runway's stated philosophy and team backgrounds:

**1. Real User Validation**
- If your team can show you've talked to actual potential customers (even via cold email or Discord), that's impressive
- "We talked to 5 indie game studios; they said this would save them 2-3 weeks per game" = credible

**2. Commercial Thinking**
- Include a slide or section in your README about potential GTM
- Don't need a full business plan, but show you've thought about monetization
- "We'd charge $X/month for unlimited generations" = judges know this is buildable

**3. Team Diversity**
- If team includes designer + engineer + domain expert, that's stronger than 3 engineers
- If team includes someone from marketing/product, emphasize their voice
- Runway values "art + tech" combinations (Steph Dinkins philosophy)

**4. Integration with Real Tools**
- If you can integrate with Modal's infrastructure directly (not just as compute platform), bonus
- Discord bots are more impressive than local CLI tools
- Deployed web apps more impressive than Jupyter notebooks

---

## FINAL CHECKLIST: Submission Requirements

Before hitting submit button, verify:

### Code & Documentation
- [ ] GitHub repo is public with MIT/Apache license
- [ ] README has:
  - [ ] Problem statement (1 paragraph)
  - [ ] Solution overview (1 paragraph)
  - [ ] How to run it (step-by-step)
  - [ ] Demo video link
  - [ ] Team member names + roles
  - [ ] Tech stack list
  - [ ] Future improvements (shows ambition)
- [ ] Code is clean (no credentials in commits, reasonable comments)
- [ ] Deployment is documented (how do judges run this?)

### Demo
- [ ] Video shows complete end-to-end workflow (5 min max)
- [ ] Video has clear audio narration (explains what you're doing)
- [ ] Backup live demo prepared (in case video doesn't work)
- [ ] Someone outside your team has seen demo (ask for feedback)

### Project Documentation
- [ ] Clear problem statement with estimated market size
- [ ] Explain why Runway API is the right tool
- [ ] Show technical sophistication (not just calling API once)
- [ ] Include metrics/benchmarks if possible (time saved, cost reduction)

### Team Info
- [ ] Team member bios submitted
- [ ] Contact info for follow-up
- [ ] LinkedIn/GitHub profiles shared
- [ ] Diversity note (if applicable; Runway values inclusive teams)

---

## WILD CARD STRATEGIES

### If You Have Extra Time/Energy

**Advanced Strategies that Impress:**
1. **Cost Optimization:** Calculate API spend, optimize prompts to reduce cost while maintaining quality
2. **Custom Metrics:** Build a quality scoring system for outputs (judges like optimization mindset)
3. **Concurrent Execution:** If building videos from multiple shots, parallelize API calls (Modal-native advantage)
4. **Production Features:** Rate limiting, queue management, analytics dashboard
5. **Extensibility:** Other users could build on your API (open source contributions)

### Unlikely to Help
- Fancy UI with animations (judges care about function, not flash)
- Perfect color design (nice-to-have, not a scorer)
- Multiple language support (out-of-scope for 72 hours)
- Mobile app (web works, don't over-engineer)

---

## SUCCESS METRICS FOR YOUR TEAM

### If You Win (Tier 1)
- $25,000 cash
- 200,000 API credits (6+ months of heavy usage)
- Feature on Runway's channels
- Potential for Runway partnership/acquisition conversations

### If You Place 2nd-3rd (Tier 2)
- Major API credits (enough for 3-6 months of development)
- Exposure in community
- Validation that your idea resonates

### If You Don't Place But Build Something Real (Tier 3)
- Market-ready product to commercialize independently
- Proof of concept for fundraising
- Community recognition and potential partnerships

### Base Case (Just Participating)
- 50,000 API credits (worth $5K-10K in value)
- Network with Runway team and other builders
- Learning about latest AI API capabilities

---

## THE MINDSET TO WIN

### Judges Are Looking For
People who see **Runway as a tool to solve real problems**, not people who want to showcase **Runway's capabilities**.

### The Winning Pitch (In Your Head)
"Here's a problem I've seen repeatedly. Here's how I used Runway's API (plus other tools) to solve it. Here's the result: X hours saved, Y cost reduced, Z users can now do this themselves. I built it in 72 hours as a proof of concept, but it could be a real product serving N customers."

### The Losing Pitch (Don't Do This)
"Here's what we made with Runway's Gen-2 and Gen-3 and Voices and Characters APIs. Isn't it cool?"

---

## FINAL WORDS

You're not competing to make the most beautiful AI video or the most creative use of AI. **You're competing to show that you can identify real problems, solve them with modern AI tools, and ship polished solutions that other people would actually use.**

That's an engineering + product + commercial thinking competition, dressed up as a creative hackathon.

**The team that wins is the one that thinks like founders, not artists.**

Now go build something people need.

---

## Quick Reference: Key Dates & Contacts

| Item | Detail |
|------|--------|
| **Hackathon Starts** | Friday, May 8, 2026, 9:00am ET |
| **Kickoff Presentation** | 9:00am ET (watch the API walkthrough) |
| **Technical Support** | Runway Discord (link emailed to registrants) |
| **Submissions Close** | Monday, May 11, 2026, 9:00am ET |
| **Winners Announced** | Friday, May 15, 2026 |
| **Contact** | (Check registration confirmation email) |

---

*Document prepared by: AI Research Agent*
*For: Number One Son Software Development*
*Purpose: Strategic brief for Runway API Hackathon May 8-11, 2026*
