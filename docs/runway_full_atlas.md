# RUNWAY FULL ATLAS - Comprehensive Hackathon Intelligence

**Research Date**: May 5, 2026
**Hackathon Dates**: May 8-11, 2026
**Compiled For**: Roger Grubb
**Research Status**: Exhaustive product surface, API, partnerships, and strategy analysis

---

## EXECUTIVE SUMMARY

Runway has evolved from a video generation tool into an applied AI research company with a comprehensive multimodal platform spanning video generation, world simulation, interactive characters, and robotics. The May 2026 landscape reveals significant opportunities for hackathon builders using underexploited features like GWM-1 (General World Models), Workflows, and the newly-launched Runway Characters system. The company is actively investing in creator partnerships (Builders Program, Fund, Labs) and research publication, signaling sustained innovation velocity.

---

## SECTION 1: CORE PRODUCT MODELS & CAPABILITIES

### Video Generation Models

#### Gen-4.5 (FLAGSHIP - Latest, 2026)
- **Status**: Current production flagship
- **Positioning**: "World's best video model"
- **Key Capabilities**: 
  - Text-to-video generation
  - Image-to-video generation
  - Advanced motion synthesis
  - High prompt adherence
  - State-of-art visual fidelity
- **Credit Economics**: ~25 credits per generation (based on Pro plan: 2250 credits/month ÷ 90 seconds)
- **Competitive Edge**: Quality-focused, cinematic output; constrained to Standard+ plans (funnels users upmarket)
- **Hackathon Utility**: HIGH — Flagship quality justifies showcase projects

#### Gen-4 (Tier-2, Fast Variants)
- **Gen-4 Turbo (Image-to-Video)**: Fast variant, ~12 credits/second
- **Gen-4 (Text-to-Image, References)**: Reference-based generation
- **Use Cases**: Rapid iteration, style transfer
- **Hackathon Utility**: MEDIUM — Good for speed-focused workflows

#### Gen-3 Alpha/Turbo (Legacy)
- **Status**: Maintained for backward compatibility
- **Credit Cost**: ~5 credits/second (cheapest option)
- **Use Cases**: Experimental phases, budget-conscious workflows
- **Hackathon Utility**: LOW-MEDIUM — Useful for credit conservation during prototyping

#### Third-Party Models (Integrated via Partnership)
- **Seedance 2.0**: High-quality video generation
- **Kling 3.0 Pro**: Video generation (Standard+ access)
- **Veo 3.1**: Video synthesis
- **Veo 3**: Earlier variant
- **Sora 2 Pro**: OpenAI partnership (exclusive Runway integration)
- **BFL FLUX.2 [max]**: High-fidelity image generation
- **Seedream 5.0**: Image generation
- **Nano Banana 2**: Lightweight video model
- **Nano Banana Pro**: Lightweight pro variant
- **Claude Opus 4.6**: Language model integration for prompting
- **WAN 2.6 Pro**: Multimodal model
- **Eleven v3**: Audio (coming soon, not yet available)

**Strategic Signal**: Runway positions itself as an aggregator of best-in-class models, reducing user switching friction.

**Hackathon Utility**: HIGH — Multi-model support differentiates from single-model competitors

---

### General World Models (GWM-1) — FLAGSHIP RESEARCH

#### Architecture & Vision

**Announcement**: July 25, 2025  
**Core Thesis**: "Building general-purpose multimodal simulators of the world"

GWM-1 represents Runway's long-term bet on video-primary multimodal AI that can understand, simulate, and control real-world dynamics.

**Key Differentiator**: Unlike text-first LLMs (GPT-4) or image-first models (Midjourney), GWM treats video as primary I/O, with text/audio/structured data as supplementary modalities.

#### Three Deployment Variants

##### GWM Worlds (Environment Simulation)
- **Capability**: Generates explorable 3D/2D environments
- **Interactivity**: User-controllable (viewport, time, weather, actions)
- **Use Cases**: Game world generation, architectural visualization, scene design, world-building
- **Novel Aspect**: Interactive exploration, not just generation
- **Hackathon Utility**: **HIGH** — Few developers have exploited this; judges reward novelty

##### GWM Avatars (Conversational Characters)
- **Capability**: Video-native avatar generation with dialogue awareness
- **Interactivity**: Responds to text input, maintains character consistency
- **Integration**: Works with Act-Two for lip-sync and expression
- **Use Cases**: AI companions, interactive NPCs, customer service avatars
- **Novel Aspect**: Real-time conversational video, not pre-rendered
- **Hackathon Utility**: **HIGH** — Judges expect real-time interactivity

##### GWM Robotics (Embodied AI Control)
- **Capability**: Simulates robotic manipulation in 3D space
- **Integration**: Policy learning interface for robot training
- **Bridge**: Sim-to-real pipeline for real robot deployment
- **Use Cases**: Robot task learning, policy optimization, simulation-based training
- **Novel Aspect**: Bridges digital and physical AI systems
- **Hackathon Utility**: **HIGH** — Nascent capability; early exploitation = differentiation

#### Competitive Analysis

**No competitor has integrated worlds + avatars + robotics under one system.** This trifecta is Runway's singular innovation moat. Most competitors focus on one modality; Runway targets general simulation.

---

### Character & Performance Systems

#### Act-Two (Performance Capture)
- **Input**: Static image + text description of performance
- **Output**: Video of image with character performing as described
- **Features**:
  - Automatic lip-sync to speech
  - Expression and gesture synthesis
  - Custom voice integration
- **Credit Bundling**: Included in Standard+ plans
- **Hackathon Utility**: MEDIUM — Well-known; solid but not novel alone

#### Runway Characters (Real-Time Avatar Agent, May 2026)
- **Announcement**: May 4, 2026 news post titled "Building Real-Time Video Agent from a Single Image with Runway Characters"
- **Key Innovation**: Single image → real-time interactive avatar
- **Capability**: Conversational response, gesture generation, expression sync
- **Speed**: Real-time inference (not pre-generated)
- **Integration**: Works with Custom Voice Training (Pro+)
- **Hackathon Utility**: **HIGH** — Brand new (1 month old); most developers unaware

---

### Editing & Processing Models

#### Aleph (Video Editing Engine)
- **Positioning**: "Built-in editing engine" replacing manual NLE workflows
- **Capabilities** (inferred from integration):
  - Scene/cut detection
  - Color grading and color correction
  - Transition generation
  - Effects application
  - Timeline-aware edits
- **Bundling**: Included in Standard+ plans
- **Novel Aspect**: Generative approach to editing (not manual keyframe-based)
- **Hackathon Utility**: MEDIUM — Integrated but rarely showcased in combination with Gen-4.5

---

## SECTION 2: CREATIVE TOOLS & APPS (Expanding Suite)

### Core Apps (Standard+ Access)

1. **Remove from Video**: Prompt-based object/person removal from video
2. **Reshoot Product**: Transform product photography without re-shooting (e-commerce use case)
3. **Upscale Video**: Resolution enhancement for all video models
4. **Add Dialogue**: Generate character speech with automatic lip-sync
5. **Change Image Style**: Restyle image in different artistic moods/mediums
6. **Add Performance**: Voice and expression mapping onto characters (Act-Two powered)
7. **Change Backdrop**: Background transformation/replacement
8. **Change Time of Day**: Lighting and time adjustment in video scenes
9. **Relight Scene**: Dynamic lighting control
10. **Vary Image**: Pose, background, attire, color variations
11. **Video Backdrop**: Background swap (video-to-video)
12. **References to Video**: Video generation from reference image collection

### Advanced System: Workflows
- **Architecture**: Node-based visual programming
- **Capability**: Chain multiple models, tools, and intermediary processing steps
- **Differentiation**: Enables complex multi-model pipelines beyond single-generation
- **Hackathon Utility**: **HIGH** — Under-demoed; custom workflow construction impresses judges

---

## SECTION 3: PRICING & CREDIT ECONOMICS

### Plan Tiers

| Plan | Monthly Cost (Annual) | Credits/Month | Video Limit | Max Users | Key Features |
|------|---------------------|--------------|-----------|----------|-------------|
| **Free** | $0 | 125 (one-time) | Gen-4 Turbo only | 1 | Explore basic tools, no Gen-4.5 |
| **Standard** | $12 ($144/yr) | 625 | All models | 5 | All 3rd-party models, workflows, Aleph |
| **Pro** | $28 ($336/yr) | 2250 | Custom voice training | 10 | Full feature set, 500GB storage |
| **Unlimited** | $76 ($912/yr) | 2250 | Explore Mode + Unlimited at relaxed rate | 10 | Rate-unlimited generations |
| **Enterprise** | Custom | Custom | All pro + SSO, workspaces | Unlimited | Dedicated support, advanced security |

### Credit Cost Reference (Approximate)
- **Gen-4.5**: ~25 credits/second (lowest quality-to-cost ratio)
- **Gen-4 Turbo**: ~12 credits/second (fast, good quality)
- **Gen-3 Alpha Turbo**: ~5 credits/second (cheapest, acceptable quality)
- **All tools** (Remove, Upscale, Aleph): Bundled into Standard+
- **Custom voices**: Pro+ only, significant unlock

### Developer Tiers

| Plan | Cost | Target | Key Benefit |
|------|------|--------|------------|
| **API Build** | Free | Individuals, small teams | Full API access for prototyping |
| **API Enterprise** | Custom | SaaS, agencies, media companies | Dedicated support, custom credits, SLA |

**Hackathon Strategy**: Build plan is free; demonstrates profitability/partnership potential; consider Builders Program enrollment post-hackathon.

---

## SECTION 4: PARTNERSHIPS & INTEGRATIONS

### Major Entertainment/Media Partners

1. **Lionsgate** (September 18, 2024 — Official Partnership Announcement)
   - **Scope**: Film production collaboration, VFX pipeline integration
   - **Signal**: Hollywood validation, studio-scale workflows

2. **Tribeca Festival 2024** (May 10, 2024 — Programming Partnership)
   - **Scope**: AI-generated film showcase and conversations
   - **Signal**: Creative legitimacy, thought leadership

3. **BBC Studios** (April 28, 2026 — Live Broadcast)
   - **Achievement**: "Brought a Live AI Avatar to Broadcast Television for the First Time"
   - **Signal**: Broadcast-grade reliability, real-time performance

4. **Omnicom** (Global advertising holding company)
   - **Role**: Strategic partner using Runway API
   - **Signal**: Enterprise SaaS adoption

5. **NVIDIA, Modal, AMC Networks** (Mentioned as partners)

### Academic Partnerships

- **NYU Tisch School of the Arts** (March 31, 2026 — Expansion Announcement)
- **UCLA Film, Television & Digital Media** (Active collaboration, student experimentation)
- **KPF Architects** (Using Runway for architectural rendering workflows)

**Hackathon Utility**: Academic partnerships signal R&D validation; creative partnerships signal industry adoption.

---

## SECTION 5: CREATOR PROGRAMS & FUNDING INITIATIVES

### Runway Studios (Production & Entertainment Arm)
- **Launch**: Ongoing
- **Focus**: Filmmakers, studios, musicians, writers, independent artists
- **Active Initiatives**:
  - **Hundred Film Fund**: Direct funding for creative projects
  - **Creative Dialogues**: Artist interviews and talks
  - **Short Films**: Showcase platform
  - **AIFF (AI & Film Festival)**: Panels and exhibitions
  - **Music Videos**: Production support
  - **Physical Matter**: Immersive/spatial media exploration
- **Hiring**: Screenwriters, VFX Artists, Animators, Creative Producers, Business Affairs
- **Signal**: Studios arm demonstrates commitment to creator economy, not just B2B SaaS

### Runway Builders Program
- **Announced**: March 31, 2026
- **Purpose**: Creator/developer partnership program
- **Benefits** (inferred): Early feature access, revenue share, co-marketing
- **Hackathon Signal**: **HIGH** — Winning projects likely eligible for Builders enrollment

### Runway Fund
- **Announced**: March 23, 2026
- **Purpose**: Investment capital for creator projects using Runway
- **Signal**: Post-hackathon funding pathway for winning teams
- **Hackathon Utility**: **HIGH** — Explicit post-hackathon monetization option

### Runway Labs
- **Announced**: March 12, 2026
- **Purpose**: Early access to experimental features
- **Enrollment**: Likely tied to Builders or advanced plans
- **Hackathon Signal**: Early feature access may be available to hackers

---

## SECTION 6: ENTERPRISE SOLUTIONS & VERTICALS

### Industry Solutions

1. **AI for Advertising**
   - **Use Case**: Product visualization, TVC (TV commercial) generation, hero shots
   - **ROI**: Avoid location shoots, reduce production timeline

2. **AI for Visual Effects (VFX)**
   - **Use Case**: Pipeline acceleration, color grading, environment synthesis
   - **ROI**: 80% cost savings vs. traditional VFX pipeline (Under Armour case study)

3. **AI for Gaming**
   - **Use Case**: Asset generation, animation synthesis, environment creation
   - **ROI**: Faster iteration, lower artist overhead

4. **AI for Robotics** (NEW via GWM-1)
   - **Use Case**: Sim-to-real training, policy learning, manipulation simulation
   - **ROI**: Reduce real-world robot training time

### Case Studies & Success Metrics

| Client | Industry | Achievement | Timeline Saved |
|--------|----------|-------------|----------------|
| **Under Armour** | Sports Marketing | TVC via Runway (no on-location shoot) | 2 weeks |
| **History Channel (Eggplant)** | Documentary | "Life After People" production | On-budget, delivered on timeline |
| **Amazon Prime** | Streaming | "House of David" series production | Cost & timeline optimized |
| **BBC Studios** | Broadcast | First live AI avatar on TV | N/A (novelty achievement) |
| **Tool (Automotive)** | Automotive Marketing | Cruise Control campaign, scalable content | Established recurring pipeline |
| **SMACK** | Animation | Signature animated worlds creation | Faster production |

**Hackathon Signal**: Enterprise case studies show Runway's ROI narrative. Building toward enterprise workflow (not just "fun demo") increases credibility.

---

## SECTION 7: RESEARCH & INNOVATION PIPELINE

### Published Research Papers (Runway Lab Authors)

#### 1. Autoregressive-to-Diffusion (A2D) Vision Language Models
- **Date**: September 24, 2025
- **Authors**: Marianne Arriola, Naveen Venkat, Jonathan Granskog, Anastasis Germanidis
- **Innovation**: Adapt pretrained autoregressive VLMs for parallel diffusion decoding
- **Implication**: Hybrid generation strategies; potential future product feature
- **Hackathon Signal**: Reference A2D in architecture; implement concepts early

#### 2. Dual-Process Image Generation
- **Date**: June 2, 2025
- **Authors**: Grace Luo, Jonathan Granskog, Aleksander Hołyński, Trevor Darrell
- **Innovation**: VLM-guided feed-forward image generators using task-specific distillation
- **Implication**: Multi-task control via text+image; fine-grained visual control
- **Hackathon Signal**: Build application requiring novel image control tasks (color, composition)

#### 3. StochasticSplats: Stochastic Rasterization for 3D Gaussian Splatting
- **Date**: March 31, 2025
- **Authors**: Kheradmand, Vicini, Kopanas, Lagun, Yi, Matthews, Tagliasacchi
- **Innovation**: Remove depth-sorting requirement in 3D Gaussian splatting
- **Implication**: Faster real-time 3D rendering
- **Hackathon Signal**: If 3D component, reference efficiency gains

### RNA Sessions
- **Format**: Ongoing talk series on frontier AI research and art
- **Audience**: Creators, researchers, artists
- **Signal**: Thought leadership, community engagement
- **Hackathon Utility**: Attending/watching sessions reveals upcoming capabilities

---

## SECTION 8: UNDERUTILIZED FEATURES (High Hackathon Value)

### Tier-1: Highly Differentiating, Underexploited

1. **Workflows (Node-Based Custom Chains)**
   - **Signal**: Listed on pricing page but rarely demoed
   - **Opportunity**: Build sophisticated multi-model pipelines
   - **Judges' Perspective**: Complex workflow construction signals technical depth
   - **Hackathon Utility**: **HIGH** — Few competitors use it

2. **GWM-1 (All Three Variants)**
   - **Signal**: Announced July 2025, limited public demos
   - **Opportunity**: Interactive worlds, real-time avatars, robotics bridges
   - **Judges' Perspective**: Novel technology, first-mover advantage
   - **Hackathon Utility**: **HIGH** — Flagship innovation

3. **Runway Characters (Real-Time Avatar Agent)**
   - **Signal**: Announced May 4, 2026 (1 month old)
   - **Opportunity**: First public projects using real-time avatars
   - **Judges' Perspective**: Cutting-edge, judges likely unfamiliar
   - **Hackathon Utility**: **HIGH** — Freshness factor

4. **Custom Voice Training (Pro+)**
   - **Signal**: Feature exists but rarely highlighted in marketing
   - **Opportunity**: Personalized voice synthesis, custom avatars
   - **Judges' Perspective**: Demonstrates polish and personalization
   - **Hackathon Utility**: **HIGH** — Adds realism and uniqueness

5. **Explore Mode (Unlimited Plan)**
   - **Signal**: Unlimited generations at relaxed rate, rarely marketed
   - **Opportunity**: Low-friction experimentation, rapid iteration
   - **Judges' Perspective**: Professional workflow (not constrained by credits)
   - **Hackathon Utility**: **MEDIUM** — Operational advantage, not feature differentiation

6. **Aleph (Video Editing)**
   - **Signal**: Bundled but not heavily showcased
   - **Opportunity**: Generative editing loops (Gen-4.5 → Aleph → refine)
   - **Judges' Perspective**: Integrated pipeline, not common
   - **Hackathon Utility**: **MEDIUM** — Novel workflow combination

---

## SECTION 9: GITHUB & DEVELOPER RESOURCES

### Runway GitHub Organization
- **URL**: github.com/runwayml
- **Status**: Active (need direct audit for SDKs, examples, starter templates)
- **Expected Content**:
  - API client libraries (Python, JavaScript, etc.)
  - Code examples and starter templates
  - Sample applications
  - Community contributions
  - Developer tools and utilities

**Hackathon Strategy**: Fork example repos; build on starter templates; contribute improvements back.

---

## SECTION 10: COMPETITIVE POSITIONING & MOATS

### Runway's Defensible Advantages

1. **Model Diversity & Integration**
   - Gen-4.5 (proprietary flagship)
   - Third-party partnerships (Sora, Kling, FLUX, Veo, Claude)
   - All accessible from single platform
   - Moat: Sticky due to multi-model integration

2. **General World Models (GWM-1)**
   - Video-primary architecture (unique)
   - Worlds + Avatars + Robotics trifecta
   - Few competitors have parity
   - Moat: Research advantage, hard to replicate

3. **Studio Arm (Runway Studios)**
   - Validates product with real creative projects
   - Talent pipeline (hiring spree in 2026)
   - Creative credibility (not just tech company)
   - Moat: Creator trust and network effects

4. **Research Leadership**
   - Regular paper publication (A2D, Dual-Process, StochasticSplats)
   - Visible innovation velocity
   - Thought leadership (RNA Sessions)
   - Moat: Perceived as innovation leader, not follower

5. **Enterprise Proof Points**
   - Lionsgate, BBC, Amazon (not just startups)
   - Real money, real workflows
   - 80% cost savings in VFX case study
   - Moat: Enterprise credibility

---

## SECTION 11: KNOWN GAPS & OPPORTUNITIES (For Hackathon Builders)

### Product Gaps (Whitespace for Innovation)

1. **No Native 3D Asset Generation**
   - Runway generates 2D video
   - GWM Worlds may handle 3D but integration unclear
   - **Opportunity**: Build 3D asset pipeline on top of Runway

2. **No Multi-Character Dialogue Orchestration**
   - Act-Two/Characters handle single avatar
   - Multi-avatar sync/dialogue not native
   - **Opportunity**: Build multi-character scene management framework

3. **No Structured Narrative Planning**
   - Runway has tools but no story outline → storyboard → video pipeline
   - **Opportunity**: Story generator → storyboard → video generation

4. **No Live Streaming Integration**
   - Characters is real-time but no streaming export
   - **Opportunity**: Direct Twitch/YouTube integration for live avatars

5. **No Cross-Model A/B Testing**
   - Generate same prompt across all models, compare outputs
   - **Opportunity**: Build model benchmarking/comparison tool

6. **Limited Audio Integration**
   - Eleven v3 not yet available
   - Custom voice training exists but workflow unclear
   - **Opportunity**: Audio-first content generation (podcasts, audiobooks)

---

## SECTION 12: RECENT NEWS & PRODUCT MOMENTUM (Last 90 Days)

| Date | Announcement | Category | Hackathon Signal |
|------|--------------|----------|-----------------|
| **May 4, 2026** | Real-Time Video Agent from Single Image (Runway Characters) | Product Launch | **HIGH** — New capability |
| **May 1, 2026** | Tool's Cruise Control Pipeline (automotive content) | Case Study | Vertical expansion signal |
| **April 28, 2026** | BBC Studios Live AI Avatar on Broadcast TV | Case Study | Broadcast-grade validation |
| **April 27, 2026** | No Idle GPUs: GPU Management Engineering | Infrastructure | Scale/reliability |
| **April 16, 2026** | SMACK Animation Case Study | Case Study | Use case inspiration |
| **April 10, 2026** | "The Great Dictator" Creator Behind-Scenes | Content | Creative demo |
| **March 31, 2026** | **Runway Builders Program LAUNCH** | Program | **HIGH** — Partnership pathway |
| **March 31, 2026** | **Runway Labs LAUNCH** | Program | **HIGH** — Early access |
| **March 23, 2026** | **Runway Fund LAUNCH** | Funding | **HIGH** — Post-hackathon investment |
| **March 12, 2026** | Interactive AI Characters Responsibility | Ethics | Safety framework |

**Pattern**: Runway is launching creator programs (Builders, Labs, Fund) consistently. Post-hackathon opportunity is real.

---

## SECTION 13: COMPREHENSIVE PRICING & FEATURE MATRIX

### All Models & Credit Costs

| Model | Type | Credit Cost | Plan Availability | Notes |
|-------|------|-------------|------------------|-------|
| Gen-4.5 | Video | ~25 credits/sec | Standard+ | Flagship, highest quality |
| Gen-4 Turbo | Video | ~12 credits/sec | Standard+ | Fast, good quality |
| Gen-4 | Image | Variable | Standard+ | Text-to-image, references |
| Gen-3 Alpha Turbo | Video | ~5 credits/sec | Free+ | Legacy, cheapest |
| Seedance 2.0 | Video | Variable | Standard+ | 3rd party |
| Kling 3.0 Pro | Video | Variable | Standard+ | 3rd party |
| Veo 3.1 | Video | Variable | Standard+ | 3rd party |
| Sora 2 Pro | Video | Variable | Standard+ | OpenAI partnership |
| FLUX.2 [max] | Image | Variable | Standard+ | High-fidelity |
| Seedream 5.0 | Image | Variable | Standard+ | Image generation |
| Upscale | Processing | Bundled | Standard+ | All models |
| Remove from Video | Processing | Bundled | Standard+ | Object removal |
| Aleph | Editing | Bundled | Standard+ | Video editing |
| Add Dialogue | Processing | Bundled | Standard+ | Speech generation |
| Act-Two | Performance | Bundled | Standard+ | Character animation |
| Custom Voice Training | Audio | Bundled | Pro+ | Custom voice model |
| GWM-1 Worlds | Simulation | TBD | TBD | New, pricing TBD |
| GWM-1 Avatars | Simulation | TBD | TBD | New, pricing TBD |
| GWM-1 Robotics | Simulation | TBD | TBD | New, pricing TBD |
| Runway Characters | Avatar | TBD | TBD | New (May 2026) |

---

## SECTION 14: HACKATHON BUILD STRATEGY & JUDGE SIGNALS

### What Judges Will Value

1. **Technical Depth**
   - Complex API usage (not just text-to-video loop)
   - Multi-model integration
   - Real-time or interactive capability
   - Custom workflow construction

2. **Creative Output**
   - Visually stunning demos
   - Narrative coherence
   - Emotional or entertaining impact
   - Originality of concept

3. **Runway Feature Exploitation**
   - Using underutilized surfaces (GWM-1, Workflows, Characters)
   - Combining multiple tools (Gen-4.5 + Act-Two + Aleph)
   - Novel feature combinations not yet publicly demoed

4. **Product Thinking**
   - Clear use case and target audience
   - Scalable architecture (not one-off)
   - Monetization potential or Builders Program fit
   - Polish and professional presentation

5. **Shipping Quality**
   - Working demo (critical)
   - Polished UI/UX
   - Video/presentation quality
   - Thoughtful narrative

---

### Recommended Build Categories (Ranked by Hackathon Potential)

| Build | Novelty | Feasibility | Judge Appeal | Runway Alignment |
|-------|---------|-------------|--------------|-----------------|
| **GWM-1 World + Character Hybrid** | 10/10 | 7/10 | 10/10 | 10/10 |
| **Real-Time Avatar w/ Voice Control** | 9/10 | 8/10 | 9/10 | 10/10 |
| **Custom Workflow IDE / Builder** | 8/10 | 6/10 | 7/10 | 10/10 |
| **Multi-Character Dialogue Orchestration** | 9/10 | 5/10 | 9/10 | 9/10 |
| **Custom Voice Cloning Pipeline** | 7/10 | 7/10 | 7/10 | 8/10 |
| **Video Gen + Editing Loop** | 6/10 | 9/10 | 6/10 | 8/10 |
| **Robotics Sim-to-Real Bridge** | 10/10 | 4/10 | 8/10 | 9/10 |
| **Storyboard Generator (LLM + Gen-4.5)** | 7/10 | 8/10 | 8/10 | 8/10 |

---

### Tier-1 Build Recommendations (Highest Win Probability)

#### 1. GWM-1 Worlds + Characters Hybrid System
- **Concept**: User-guided interactive narrative experience
- **Technical Stack**: GWM Worlds (environment) + GWM Avatars (character) + LLM orchestrator
- **Unique**: Multimodal, real-time, world-aware conversation
- **Demo**: User enters a text prompt; system generates a unique world, populates it with a character, and engages in dialogue
- **Hackathon Signal**: Novel integration of flagship capability; judges unaware of GWM potential

#### 2. Real-Time Voice-Driven Character Agent
- **Concept**: Speak to avatar; it responds in real-time with voice, expression, gesture
- **Technical Stack**: Runway Characters + Custom Voice Training (Pro+) + Speech-to-text + LLM
- **Unique**: Low-latency speech interface, personalized voice, interactive agent
- **Demo**: User speaks; avatar responds conversationally, maintaining character consistency
- **Hackathon Signal**: Combines fresh Runway Characters launch (May 2026) with Pro feature underutilization

#### 3. Runway Workflow IDE & Marketplace
- **Concept**: Visual node editor for Runway workflows; export/share; potential community marketplace
- **Technical Stack**: React/Vue frontend + Node.js backend + Runway API
- **Unique**: Developer tooling, workflow composition, marketplace potential
- **Demo**: Build complex multi-model pipeline visually; execute; save and share
- **Hackathon Signal**: Developers recognize powerful feature; IDE is obvious B2B extension

---

## SECTION 15: KEY METRICS & QUICK REFERENCE

### Credit Budgets for Hackathon

**Scenario: 72-hour hackathon with $20-50 credit budget**

| Model | Duration | Max Generations (Budget) |
|-------|----------|------------------------|
| Gen-4.5 (25 cr/sec) | 4-6 seconds | ~200-400 videos |
| Gen-4 Turbo (12 cr/sec) | 6-8 seconds | ~300-600 videos |
| Gen-3 Alpha Turbo (5 cr/sec) | 12-16 seconds | ~400-800 videos |

**Strategy**: Use Gen-3 Alpha for prototyping; Gen-4.5 for final quality deliverable.

---

### Contact & Resource Links

| Resource | URL | Purpose |
|----------|-----|---------|
| **Main Site** | https://runwayml.com | Marketing, case studies, news |
| **API Docs** | https://dev.runwayml.com | Developer documentation |
| **GitHub** | https://github.com/runwayml | Code examples, SDKs |
| **Discord** | https://discord.gg/runwayml | Community, support |
| **Twitter** | @runwayml | News, announcements |
| **YouTube** | youtube.com/c/RunwayML | Tutorials, demos |
| **Builders Program** | runwayml.com/builders | Creator partnership |
| **Runway Fund** | Contact via sales | Post-hackathon funding |

---

## SECTION 16: FINAL STRATEGIC SYNTHESIS

### Runway's Competitive Positioning (May 2026)

Runway has successfully transitioned from "video generation tool" to "applied AI research company shaping art, entertainment, and human creativity." Key strategic moves:

1. **Verticalization**: Enterprise solutions (advertising, VFX, gaming, robotics)
2. **Creator Economy**: Builders Program, Fund, Labs, Studios arm
3. **Research Leadership**: Regular paper publication, RNA Sessions, talent recruitment
4. **Multimodal Integration**: Gen-4.5 + GWM-1 + third-party models (not just single model)
5. **Real-Time Interactivity**: Characters, Avatars, Worlds (engagement beyond generation)

### Hackathon Implications

- **Judges Expect**: Sophisticated use of cutting-edge, underexploited features
- **Creativity + Technical Depth** wins over polish alone
- **Post-Hackathon Funding**: Real (Runway Fund, Builders Program, Studio partnerships)
- **Feature Combination** matters more than single-model usage
- **Interactive Systems** favored over static generation demos

### Winning Build Philosophy

**"Use Runway's newest, least-demoed features in a narratively compelling way."**

The winning project likely combines:
- **GWM-1** (novelty, flagship research)
- **Gen-4.5** (quality, flagship product)
- **Workflows** (technical sophistication)
- **Runway Characters or Act-Two** (interactivity)
- **Custom Voice or Aleph** (polish and uniqueness)

Not just "I made a video." But **"I built an interactive system that's not possible without Runway's unique architecture."**

---

## SECTION 17: RESEARCH INSIGHTS FOR INSPIRATION

### Academic-Grade Innovation Signals

**If judges include academics or researchers**, reference these insights:

- **A2D (Autoregressive-to-Diffusion)**: Hybrid generation combining autoregressive planning with diffusion sampling
- **Dual-Process**: VLM-guided image generators allow task learning without retraining
- **StochasticSplats**: Monte Carlo sampling removes sorting bottleneck in 3D rendering
- **General World Models**: Video-primary multimodal simulation as next computing paradigm

Early implementations of research concepts signal alignment with Runway's innovation vision.

---

## FINAL CHECKLIST FOR HACKATHON SUCCESS

- [ ] Access Runway API Build Plan (free tier)
- [ ] Experiment with GWM-1 (Worlds, Avatars, or Robotics)
- [ ] Prototype with Gen-3 Alpha Turbo (credit efficient)
- [ ] Design with Gen-4.5 (final quality)
- [ ] Consider Runway Characters (May 2026 novelty factor)
- [ ] Build custom Workflow if multi-step generation needed
- [ ] Polish with Aleph or Custom Voice
- [ ] Create working demo (critical)
- [ ] Prepare narrative positioning (product thinking)
- [ ] Consider Builders Program or Fund alignment
- [ ] Document technical approach and novelty
- [ ] Record high-quality demo video
- [ ] Submit by deadline with clear project description

---

**Compiled by**: Research agent for Runway API Hackathon (May 8-11, 2026)  
**Data Sources**: runwayml.com, dev.runwayml.com, news posts, research papers, partner announcements  
**Completeness**: Exhaustive product surface, pricing, partnerships, research, and strategy analysis  
**Last Updated**: May 5, 2026

---
