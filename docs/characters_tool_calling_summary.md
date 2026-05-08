# Runway Characters & Tool Calling — Comprehensive Build Guide

**Hackathon Mission: Number One Son — Clone Army Platform**  
**Date Generated:** 2026-05-07  
**Target Deadline:** May 8-11, 2026  
**Status:** All 14 documentation pages fetched, extracted, and prioritized for Friday build sprint.

---

## TOP 20 ACTIONABLE FINDINGS (Ranked by Build-Day Impact)

### TIER 1: CRITICAL PATH — Do First (Blocking Dependencies)

#### 1. **Custom Avatars Creation from Single Image (CRITICAL FOR MOM-25/ROGER-5/SISTER-3)**
- **Source:** characters_custom_avatars.md
- **Action:** Use `/characters/create-your-own/` endpoint
- **Deliverable:** Convert single 1969 photograph → 3 distinct character models
- **Key Constraint:** Runway's "no fine-tuning required" model accepts ANY single image
- **Build Time Estimate:** 5-10 min per character = 15-30 min total for trio
- **Impact:** This is your Mother/Son/Sister visual foundation. Everything downstream depends on this working Friday morning.

#### 2. **Character Voice Configuration (Dual Path)**
- **Source:** characters_custom_voices.md
- **Path A (Faster):** Use pre-built voice library + TTS synthesis
- **Path B (Deeper):** Clone voice from audio sample (requires 30-60 sec reference audio)
- **Build Decision:** For hackathon, Path A is sufficient; Path B adds "authenticity layer"
- **Recommendation:** Record quick 30-sec Mastermind voice sample Thursday night as insurance

#### 3. **Knowledge Base Document Grounding (For Family Context)**
- **Source:** characters_knowledge_base.md
- **Mechanism:** Upload .txt/.pdf documents that Characters can reference during conversation
- **Use Case for You:** Upload Mastermind's life story, family timeline, personal context docs
- **Build Time:** ~5 min to prep docs + 2 min to upload per character
- **Impact:** Characters become context-aware rather than generic; judges notice the difference

#### 4. **Tool Calling Framework (Ghost Frames Pipeline Integration)**
- **Source:** tool_calling_overview.md + tool_calling_client_tools.md + tool_calling_server_tools.md
- **Your Use Case:** Characters invoke Ghost Frames generation mid-conversation
- **Architecture:** Client-side tool (UI feedback) + Server-side tool (call your Runway API endpoint)
- **Implementation Roadmap:**
  1. Client tool: `generate_ghost_frame` button/confirmation UI
  2. Server tool: HTTP POST to your Runway API with photo + prompt
  3. Character voice-narrates the generation as it happens
- **Build Time:** 30-45 min to wire up both tool types
- **Impact:** Judges see autonomous agent action → core judging rubric alignment

---

### TIER 2: MAJOR FEATURES — Do Second (Multiplicative Value)

#### 5. **Multi-Character Video Meeting (NEW Runway Capability)**
- **Source:** characters_video_meeting.md
- **What It Enables:** 3 characters (Mom-25, Roger-5, Sister-3) visible + audible simultaneously
- **Judges' Perspective:** Demonstrates clone-army coordination, family dialogue, narrative depth
- **Setup Complexity:** Moderate; requires session management for 3 parallel character instances
- **Build Time:** 20-30 min including UI layout
- **Killer Feature:** Judges rarely see this in hackathon submissions → distinctive

#### 6. **Embedded Widget for Public Demo (One-Line Drop-In)**
- **Source:** characters_embedded_widget.md
- **Mechanism:** `<script>` tag + single line of config
- **Use Case:** Your hackathon submission judges interact with live characters without leaving submission page
- **Build Time:** 5 min (literally a script tag)
- **Judging Impact:** Higher engagement = more memorable impression

#### 7. **Screen Sharing / Camera Input (NEW Runway Capability)**
- **Source:** characters_camera_screen_sharing.md
- **What It Enables:** Characters "see" your screen or your face via webcam
- **Potential for Number One Son:** Character reacts to family photos on screen, or "sees" you
- **Build Complexity:** Medium; adds real-time vision processing
- **Build Time:** 15-20 min
- **Judge Impact:** Novel interaction pattern; shows depth of Runway's capabilities

#### 8. **Server-Side Tool Implementation (Order Lookup Pattern)**
- **Source:** tool_calling_server_tools.md
- **Pattern You Should Copy:** Character asks for data → server fetch → model responds
- **Number One Son Example:** 
  - Character: "Tell me about Mom's childhood."
  - Tool call: Server retrieves from knowledge base / your backend
  - Character: Synthesizes response with actual facts
- **Implementation:** JSON schema definition + HTTP endpoint on your server
- **Build Time:** 15-20 min to stub; extends as you add more tools
- **Impact:** Grounds characters in live data vs. pure hallucination

---

### TIER 3: STABILITY & POLISH — Do Third (Polish, Not Blocking)

#### 9. **Tool Calling Best Practices (Gotchas Catalog)**
- **Source:** tool_calling_best_practices.md
- **Key Constraints You MUST Know:**
  - Tool invocation timeout: <1 second (your server must respond fast)
  - Tool argument validation happens client-side; schema is strict
  - Avoid ambiguous tool names (Runway disambiguates, but it slows response)
- **Build Time:** 10 min read + 5 min per tool to validate
- **Payoff:** Prevents submission failures Friday morning

#### 10. **API Reference (Parameter Tuning)**
- **Source:** tool_calling_reference.md
- **Use For:** Fine-tuning character behavior parameters (temperature, reasoning_budget, etc.)
- **Build Time:** Reference only; consult as needed
- **Impact:** Last-minute quality tweaks if characters are too zany or too robotic

---

### TIER 4: FOUNDATION & ARCHITECTURE — Reference Material

#### 11. **Quickstart (5-Minute Walkthrough)**
- **Source:** characters_quickstart.md
- **Purpose:** Baseline integration; shows minimal viable character session
- **When to Read:** Thursday evening to verify your dev environment is sane
- **Time:** 15 min (skimmable; mostly setup)

#### 12. **Core Concepts (Terminology & Mental Models)**
- **Source:** characters_core_concepts.md
- **Essential Definitions:**
  - Character vs. Avatar (visual representation of a conversational agent)
  - Session lifecycle (init → stream → close)
  - GWM-1 (Runway's General World Model; powers all Characters)
- **Build Time:** 20 min; read once, reference section 2-3 times
- **Payoff:** Prevents terminology confusion with judges

#### 13. **Integration Guide (High-Level Architecture)**
- **Source:** characters_integration.md
- **Covers:** SDK setup, authentication, session management, streaming
- **Number One Son Architecture Implications:**
  - You control the orchestration of 3 character sessions
  - Each character is a separate session instance
  - UI coordination happens on your frontend
- **Build Time:** 30 min deep read; reference for architecture decisions

#### 14. **Client-Side Tools (UI Interaction Pattern)**
- **Source:** tool_calling_client_tools.md
- **Pattern:** Character speaks → triggers JavaScript handler in browser
- **Example Implementation:** "Show me Ghost Frames" → button appears, user clicks, generation starts
- **Build Time:** 20 min to implement first tool; 5 min per additional
- **Payoff:** Snappy, responsive UI = judges feel the quality

---

## ESTIMATED BUILD TIMELINE FOR FRIDAY

### Phases 1-2: Thursday Evening (Prep, 2 hours)

- [ ] Read characters_quickstart.md (15 min)
- [ ] Read tool_calling_overview.md (10 min)
- [ ] Read tool_calling_best_practices.md (15 min)
- [ ] Prepare 1969 photograph for avatar creation (inspect, crop, validate) (20 min)
- [ ] Record 30-sec Mastermind voice sample (if using voice cloning) (15 min)
- [ ] Prepare knowledge base documents (life story, family context) (20 min)
- [ ] Set up dev environment, verify Runway API access (15 min)

### Phase 3: Friday Morning Execution (5 hours, 7am-12pm)

**Hour 1 (7-8am): Custom Characters**
- [ ] Create Mom-25 avatar from photo (10 min)
- [ ] Create Roger-5 avatar from photo (10 min)
- [ ] Create Sister-3 avatar from photo (10 min)
- [ ] Upload knowledge base docs to each character (15 min)
- [ ] Test individual character interaction (15 min)

**Hour 2 (8-9am): Tool Calling Infrastructure**
- [ ] Define tool schema for `generate_ghost_frame` (10 min)
- [ ] Implement client-side tool handler (UI button + callback) (20 min)
- [ ] Implement server-side tool handler (HTTP endpoint) (20 min)
- [ ] Test single tool invocation end-to-end (10 min)

**Hour 3 (9-10am): Multi-Character Scene**
- [ ] Set up video meeting session with 3 characters (15 min)
- [ ] Wire up UI layout (Mom top-left, Roger center, Sister top-right) (15 min)
- [ ] Test all 3 characters speaking simultaneously (10 min)
- [ ] Buffer/debug time (20 min)

**Hour 4 (10-11am): Embedded Widget + Polish**
- [ ] Create embedded widget script for judges (5 min)
- [ ] Add screen-sharing or camera interaction (optional; 15 min if time)
- [ ] Test all features end-to-end (20 min)
- [ ] Performance optimization + bug fixes (20 min)

**Hour 5 (11am-12pm): Final Prep**
- [ ] Write demo script for judges (10 min)
- [ ] Package submission + test deployment (10 min)
- [ ] Final walkthrough + confidence check (20 min)
- [ ] Catch any show-stopping bugs (20 min)

---

## URLS THAT RETURNED THIN CONTENT — Re-Fetch Candidates

**None.** All 14 pages extracted successfully with substantial content:
- Shortest: tool_calling_overview.md (1.3 KB; lightweight by design — overview page)
- Longest: characters_integration.md (10.7 KB)
- Average: ~6 KB per page

**Re-fetch strategy if issues arise Friday:**
1. Direct browser fetch of https://docs.dev.runwayml.com/characters/create-your-own/ if avatar creation fails
2. Direct fetch of tool-calling reference if tool invocation errors occur
3. Have Runway API playground (https://dev.runwayml.com/models) open as backup

---

## SPECIAL NOTES FOR CUSTOM AVATARS (MOM-25, ROGER-5, SISTER-3)

### Critical Success Factors

1. **Photo Quality:** Single 1969 photograph must be:
   - At least 500x500 pixels (higher is better)
   - Clear facial features (Runway's GWM-1 needs to see eyes, mouth)
   - Reasonable lighting (not backlit or heavily shadowed)

2. **Family Resemblance:** If using same photo → all 3 characters will resemble each other slightly (feature, not bug)
   - Judges will see the "clone family" theme embedded in visuals
   - Narrative strength: "This is what the family looks like when cloned"

3. **Voice Differentiation:** Don't use identical voice for all 3
   - Use voice cloning (Path B) to capture Mastermind's voice variations (Mom ≠ Roger ≠ Sister age/tone)
   - Or use TTS with different voice IDs (faster)

4. **Knowledge Base Personalization:** Each character should have role-specific context
   - Mom-25: Life story, motherhood, values
   - Roger-5: Childhood, innocent curiosity, family memories
   - Sister-3: Toddler perspective, wonder, playfulness

---

## GHOST FRAMES INTEGRATION CHECKLIST

For your Ghost Frames generation pipeline to work with tool calling:

- [ ] Create `/api/generate_ghost_frames` endpoint (or similar)
- [ ] Endpoint accepts: character_id, prompt, image_url, output_format
- [ ] Endpoint returns: task_id, status_url (for polling)
- [ ] Client tool definition includes tool schema matching this API
- [ ] Server tool definition makes HTTP call to your endpoint
- [ ] Character voice narrates generation: "Generating your frames now..."
- [ ] UI shows progress bar or spinning animation
- [ ] On completion, display generated frames in lightbox/modal

---

## JUDGING RUBRIC ALIGNMENT

Based on your earlier research (Concept/Craft/Emotional/Adherence):

| Judging Dimension | How These Docs Help |
|---|---|
| **Concept** | Docs show Runway's multi-character + tool-calling capabilities; judges see your understanding of the platform |
| **Craft** | Embedded widget, multi-character video meeting, screen sharing all demonstrate technical depth |
| **Emotional** | Knowledge base + voice cloning + character personalization = emotional authenticity |
| **Adherence** | Tool calling for Ghost Frames generation = direct use of hackathon theme (autonomous media gen) |

---

## DEPENDENCIES & CRITICAL PATHS

```
Photo (1969 family image)
    ↓
    ├→ Mom-25 Avatar (custom avatar endpoint)
    ├→ Roger-5 Avatar (custom avatar endpoint)
    └→ Sister-3 Avatar (custom avatar endpoint)
             ↓
        Knowledge Base Docs
             ↓
        Character Sessions (3 parallel)
             ↓
        Video Meeting UI Layout
             ↓
    Tool Calling Infrastructure
             ↓
        Ghost Frames Generation
             ↓
        Embedded Widget for Judges
```

**Critical Path Length:** ~5-6 hours of focused engineering  
**Slack Time:** 1-2 hours for debugging, polish, unexpected errors

---

## FILES SAVED TO OUTPUTS DIRECTORY

```
characters_quickstart.md (4.0 KB)
characters_custom_avatars.md (5.8 KB) ← CRITICAL
characters_core_concepts.md (9.9 KB)
characters_integration.md (10.7 KB)
characters_embedded_widget.md (5.8 KB)
characters_knowledge_base.md (4.9 KB)
characters_custom_voices.md (5.6 KB)
characters_video_meeting.md (7.3 KB)
characters_camera_screen_sharing.md (5.5 KB)
tool_calling_overview.md (1.3 KB)
tool_calling_client_tools.md (7.2 KB)
tool_calling_server_tools.md (7.1 KB)
tool_calling_best_practices.md (6.0 KB)
tool_calling_reference.md (4.3 KB)
───────────────────────────────────────
Total: ~104 KB of curated, extracted documentation
```

---

## SUCCESS CRITERIA FOR FRIDAY

By 12pm Friday (submission deadline):

- [ ] 3 custom avatars created from 1969 photo and interactive
- [ ] All 3 characters have personalized knowledge bases
- [ ] Tool calling works end-to-end (character → button click → Ghost Frames generation)
- [ ] Multi-character video meeting shows all 3 simultaneously
- [ ] Embedded widget allows judges to interact in real-time
- [ ] Demo script polished and timed to <3 minutes
- [ ] No unhandled errors or crashes in primary flow

**Confidence Target:** 90%+ that you can ship a compelling demo  
**Backup Plan:** If tool calling breaks, ship multi-character video + embedded widget (still strong)

---

**Good luck, Number One Son team. Mastermind is counting on you.**
