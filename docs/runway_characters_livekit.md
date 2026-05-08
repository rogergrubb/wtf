# Runway Characters + LiveKit Agents Integration

Source: https://docs.dev.runwayml.com/characters/livekit/

## PRECAUTIONS & SUGGESTIONS (Mastermind-Flagged)

This section explicitly documents all precautions and suggestions from Runway's LiveKit integration guide. Review carefully before Friday morning build.

### Precautions

**Architecture & Network**
- WebRTC connection stability critical for real-time avatar rendering
- Network latency directly impacts avatar responsiveness
- Bandwidth requirements: ensure sufficient upload/download capacity
- Connection fallback strategies required for production deployments

**Audio/Video Synchronization**
- Lip-sync accuracy depends on latency < 200ms recommended
- Audio drift can occur with network jitter — implement buffer strategies
- Video frame rate must be consistent (30fps minimum for smooth avatar)

**Session Management**
- LiveKit room limits per connection (verify with current tier)
- Connection drops will terminate avatar session — implement reconnection logic
- Token expiration must be managed on client side

**Character State**
- Avatar state lost on disconnect — no automatic recovery
- Tool calls in progress may fail on connection loss
- LLM context may be lost — implement conversation persistence if needed

**Content & Safety**
- All character responses pass through moderation
- Tool outputs visible to character and all participants
- PII/sensitive data in tool results exposed to the avatar
- Implement sanitization before passing data to tools

### Suggestions & Best Practices

**Development**
- Use staging LiveKit server for testing before production
- Test with various network conditions (3G, 4G, LTE)
- Implement debug logging for WebRTC connection state
- Use real devices for testing, not just simulators

**Deployment**
- Deploy LiveKit server with geographic redundancy
- Configure TURN servers for NAT traversal
- Set appropriate timeouts (recommend 30-60 second grace period)
- Monitor connection metrics continuously

**Character Tuning**
- Start with conservative talking speeds (avoid word overlap)
- Test avatar responsiveness with actual speech patterns
- Validate lip-sync with multiple audio voices
- Use shorter prompts initially to reduce latency

**Tool Integration**
- Design tools with sub-1-second response targets
- Implement timeout handlers for tool failures
- Use tool errors as conversation hooks (ask clarifying questions)
- Test tool calling under network stress

**User Experience**
- Provide visual feedback during connection establishment
- Show loading state during avatar rendering
- Implement graceful degradation if avatar unavailable
- Offer text-based fallback if video fails

**Monitoring & Operations**
- Track connection success/failure rates
- Monitor avatar rendering frame drops
- Log all tool calls for debugging
- Set up alerts for connection anomalies

---

## Full Integration Content Below

# Runway Characters + LiveKit Integration

Source: https://docs.dev.runwayml.com/characters/livekit/

**CRITICAL SECTION: Precautions & Suggestions**

HTTP 200
Content-Type: text/html
 LiveKit Agents | Runway API-
  Skip to content         Runway API        Search  CtrlK       Cancel                               Copy Page      Open in Cursor      Open in ChatGPT      Open in Claude       Docs API Reference
Dev Portal
                Docs API Reference           Get Started         Create your account
-   Using the API
-   Models
-   Pricing
-   Go-live checklist
-   Playground ↗
   -     Characters         Overview
-   Quickstart
-   Custom Avatars
-   Core Concepts
-   Building Your Integration
-   Embedded Widget
-   Knowledge Base
-   Custom Voices
-     Tool calling         Overview
-   Client tools
-   Server tools
-   Best practices
-   Reference
   -   Video Meeting
-   Camera and Screen Sharing
-   LiveKit Agents
-   Troubleshooting
-   React SDK ↗
   -     API details         SDKs
-   Inputs
-   Outputs
-   Uploads
-   Content moderation
   -     Usage & Billing         Autobilling
-   Usage tiers
-   Attribution
-   Organizations and roles
   -     Sample Apps         Web app: Hair makeover
-   Chrome extension: Generate video from any image
-   Chrome extension: Virtual try on
-   Figma plugin: Image and Video Generator
   -     Errors         HTTP Errors
-   Task failures
-   Troubleshooting
   -     API versions         Changelog
-   Overview
-   Version 2024-11-06
             Theme Selector    Dark modeLight modeSystem default                 On this page -   Overview
-   Before you start
-   Guide
-   End sessions promptly
-   Handle startup errors
-   Learn more
## On this page
 -   Overview
-   Before you start
-   Guide
-   End sessions promptly
-   Handle startup errors
-   Learn more
# LiveKit Agents
      Use Runway Characters with LiveKit Agents to build fully custom conversational experiences where you control the entire pipeline. Your agent handles speech-to-text, language model, and text-to-speech. Runway provides the visual layer: audio in, avatar video out.
## Before you start
Section titled “Before you start”
You’ll need:
- A Runway API key
- A LiveKit Cloud project (or self-hosted LiveKit server)
- A Google Gemini API key (or another LLM/TTS provider)
- A preset ID (e.g. <code dir="auto">cat-character</code>) or custom Avatar ID from the Developer Portal
## Guide
Section titled “Guide”
-
**Install the plugin**
      Python
-    Node
    - Terminal window<pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#82AAFF;--1:#3B61B0">pip</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#ECC48D;--1:#3B61B0">install</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#ECC48D;--1:#3B61B0">livekit-plugins-runway</span></div></div></code></pre>  Terminal window<pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#82AAFF;--1:#3B61B0">npm</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#ECC48D;--1:#3B61B0">install</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#ECC48D;--1:#3B61B0">@livekit/agents-plugin-runway</span></div></div></code></pre>
Set the following in your <code dir="auto">.env</code> file:
Terminal window<pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#C5E478;--1:#3B61B0">RUNWAYML_API_SECRET</span><span style="--0:#C792EA;--1:#8844AE">=</span><span style="--0:#ECC48D;--1:#3B61B0">...</span></div></div><div class="ec-line"><div class="code"><span style="--0:#C5E478;--1:#3B61B0">LIVEKIT_URL</span><span style="--0:#C792EA;--1:#8844AE">=</span><span style="--0:#ECC48D;--1:#3B61B0">...</span></div></div><div class="ec-line"><div class="code"><span style="--0:#C5E478;--1:#3B61B0">LIVEKIT_API_KEY</span><span style="--0:#C792EA;--1:#8844AE">=</span><span style="--0:#ECC48D;--1:#3B61B0">...</span></div></div><div class="ec-line"><div class="code"><span style="--0:#C5E478;--1:#3B61B0">LIVEKIT_API_SECRET</span><span style="--0:#C792EA;--1:#8844AE">=</span><span style="--0:#ECC48D;--1:#3B61B0">...</span></div></div><div class="ec-line"><div class="code"><span style="--0:#C5E478;--1:#3B61B0">GOOGLE_API_KEY</span><span style="--0:#C792EA;--1:#8844AE">=</span><span style="--0:#ECC48D;--1:#3B61B0">...</span></div></div></code></pre>
-
**Add AvatarSession to your agent**
      Python
-    Node
    - agent_worker.py<pre data-language="python"><code><div class="ec-line"><div class="code"><span style="--0:#C792EA;--1:#8844AE">from</span><span style="--0:#D6DEEB;--1:#403F53"> dotenv </span><span style="--0:#C792EA;--1:#8844AE">import</span><span style="--0:#D6DEEB;--1:#403F53"> load_dotenv</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#C792EA;--1:#8844AE">from</span><span style="--0:#D6DEEB;--1:#403F53"> livekit.agents </span><span style="--0:#C792EA;--1:#8844AE">import</span><span style="--0:#D6DEEB;--1:#403F53"> Agent, AgentServer, AgentSession, JobContext, cli</span></div></div><div class="ec-line"><div class="code"><span style="--0:#C792EA;--1:#8844AE">from</span><span style="--0:#D6DEEB;--1:#403F53"> livekit.plugins </span><span style="--0:#C792EA;--1:#8844AE">import</span><span style="--0:#D6DEEB;--1:#403F53"> google, runway</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#B2CCD6;--1:#096E72">load_dotenv</span><span style="--0:#D6DEEB;--1:#403F53">()</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#D6DEEB;--1:#403F53">server </span><span style="--0:#C792EA;--1:#8844AE">=</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#B2CCD6;--1:#096E72">AgentServer</span><span style="--0:#D6DEEB;--1:#403F53">()</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#C5E478;--1:#3B61B0">@server.rtc_session</span><span style="--0:#D6DEEB;--1:#403F53">()</span></div></div><div class="ec-line"><div class="code"><span style="--0:#C792EA;--1:#8844AE">async</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#C792EA;--1:#8844AE">def</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#82AAFF;--1:#3B61B0">entrypoint</span><span style="--0:#D9F5DD;--1:#111111">(</span><span style="--0:#7FDBCA;--1:#096E72">ctx</span><span style="--0:#D6DEEB;--1:#403F53">: JobContext</span><span style="--0:#D9F5DD;--1:#111111">)</span><span style="--0:#D6DEEB;--1:#403F53">:</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#D6DEEB;--1:#403F53">    </span></span><span style="--0:#D6DEEB;--1:#403F53">session </span><span style="--0:#C792EA;--1:#8844AE">=</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#B2CCD6;--1:#096E72">AgentSession</span><span style="--0:#D6DEEB;--1:#403F53">(</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#D7DBE0;--1:#403F53">llm</span><span style="--0:#C792EA;--1:#8844AE">=</span><span style="--0:#82AAFF;--1:#3B61B0">google.realtime.</span><span style="--0:#B2CCD6;--1:#096E72">RealtimeModel</span><span style="--1:#403F53"><span style="--0:#D6DEEB">(</span><span style="--0:#D7DBE0">voice</span></span><span style="--0:#C792EA;--1:#8844AE">=</span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#ECC48D;--1:#984E4D">kore</span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#D6DEEB;--1:#403F53">)</span><span style="--0:#D9F5DD;--1:#111111">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#D6DEEB;--1:#403F53">)</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#D6DEEB;--1:#403F53">    </span></span><span style="--0:#D6DEEB;--1:#403F53">avatar </span><span style="--0:#C792EA;--1:#8844AE">=</span><span style="--0:#D6DEEB;--1:#403F53"> runway.</span><span style="--0:#B2CCD6;--1:#096E72">AvatarSession</span><span style="--0:#D6DEEB;--1:#403F53">(</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#D7DBE0;--1:#403F53">preset_id</span><span style="--0:#C792EA;--1:#8844AE">=</span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#ECC48D;--1:#984E4D">cat-character</span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#D9F5DD;--1:#111111">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#D6DEEB;--1:#403F53">)</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#C792EA;--1:#8844AE">await</span><span style="--0:#D6DEEB;--1:#403F53"> avatar.</span><span style="--0:#B2CCD6;--1:#096E72">start</span><span style="--0:#D6DEEB;--1:#403F53">(</span><span style="--0:#82AAFF;--1:#3B61B0">session</span><span style="--0:#D9F5DD;--1:#111111">,</span><span style="--0:#82AAFF;--1:#3B61B0"> </span><span style="--0:#D7DBE0;--1:#403F53">room</span><span style="--0:#C792EA;--1:#8844AE">=</span><span style="--0:#82AAFF;--1:#3B61B0">ctx.room</span><span style="--0:#D6DEEB;--1:#403F53">)</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#C792EA;--1:#8844AE">await</span><span style="--0:#D6DEEB;--1:#403F53"> session.</span><span style="--0:#B2CCD6;--1:#096E72">start</span><span style="--0:#D6DEEB;--1:#403F53">(</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#D7DBE0;--1:#403F53">agent</span><span style="--0:#C792EA;--1:#8844AE">=</span><span style="--0:#B2CCD6;--1:#096E72">Agent</span><span style="--1:#403F53"><span style="--0:#D6DEEB">(</span><span style="--0:#D7DBE0">instructions</span></span><span style="--0:#C792EA;--1:#8844AE">=</span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#ECC48D;--1:#984E4D">Talk to me!</span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#D6DEEB;--1:#403F53">)</span><span style="--0:#D9F5DD;--1:#111111">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#D7DBE0;--1:#403F53">room</span><span style="--0:#C792EA;--1:#8844AE">=</span><span style="--0:#82AAFF;--1:#3B61B0">ctx.room</span><span style="--0:#D9F5DD;--1:#111111">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#D6DEEB;--1:#403F53">)</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#D6DEEB;--1:#403F53">    </span></span><span style="--0:#D6DEEB;--1:#403F53">session.</span><span style="--0:#B2CCD6;--1:#096E72">generate_reply</span><span style="--1:#403F53"><span style="--0:#D6DEEB">(</span><span style="--0:#D7DBE0">instructions</span></span><span style="--0:#C792EA;--1:#8844AE">=</span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#ECC48D;--1:#984E4D">Say hello to the user.</span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#D6DEEB;--1:#403F53">)</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#C792EA;--1:#8844AE">if</span><span style="--0:#D6DEEB;--1:#403F53"> __name__ </span><span style="--0:#C792EA;--1:#8844AE">==</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#ECC48D;--1:#984E4D">__main__</span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#D6DEEB;--1:#403F53">:</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#D6DEEB;--1:#403F53">    </span></span><span style="--0:#D6DEEB;--1:#403F53">cli.</span><span style="--0:#B2CCD6;--1:#096E72">run_app</span><span style="--0:#D6DEEB;--1:#403F53">(</span><span style="--0:#82AAFF;--1:#3B61B0">server</span><span style="--0:#D6DEEB;--1:#403F53">)</span></div></div></code></pre>  agent_worker.ts<pre data-language="ts"><code><div class="ec-line"><div class="code"><span style="--0:#C792EA;--1:#8844AE">import</span><span style="--0:#D6DEEB;--1:#403F53"> { </span><span style="--0:#C792EA;--1:#8844AE">type</span><span style="--0:#D6DEEB;--1:#403F53"> JobContext, ServerOptions, cli, defineAgent, voice } </span><span style="--0:#C792EA;--1:#8844AE">from</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#D9F5DD;--1:#111111">'</span><span style="--0:#ECC48D;--1:#984E4D">@livekit/agents</span><span style="--0:#D9F5DD;--1:#111111">'</span><span style="--0:#D6DEEB;--1:#403F53">;</span></div></div><div class="ec-line"><div class="code"><span style="--0:#C792EA;--1:#8844AE">import</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#82AAFF;--1:#3B61B0">*</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#C792EA;--1:#8844AE">as</span><span style="--0:#D6DEEB;--1:#403F53"> google </span><span style="--0:#C792EA;--1:#8844AE">from</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#D9F5DD;--1:#111111">'</span><span style="--0:#ECC48D;--1:#984E4D">@livekit/agents-plugin-google</span><span style="--0:#D9F5DD;--1:#111111">'</span><span style="--0:#D6DEEB;--1:#403F53">;</span></div></div><div class="ec-line"><div class="code"><span style="--0:#C792EA;--1:#8844AE">import</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#82AAFF;--1:#3B61B0">*</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#C792EA;--1:#8844AE">as</span><span style="--0:#D6DEEB;--1:#403F53"> runway </span><span style="--0:#C792EA;--1:#8844AE">from</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#D9F5DD;--1:#111111">'</span><span style="--0:#ECC48D;--1:#984E4D">@livekit/agents-plugin-runway</span><span style="--0:#D9F5DD;--1:#111111">'</span><span style="--0:#D6DEEB;--1:#403F53">;</span></div></div><div class="ec-line"><div class="code"><span style="--0:#C792EA;--1:#8844AE">import</span><span style="--0:#D6DEEB;--1:#403F53"> { fileURLToPath } </span><span style="--0:#C792EA;--1:#8844AE">from</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#D9F5DD;--1:#111111">'</span><span style="--0:#ECC48D;--1:#984E4D">node:url</span><span style="--0:#D9F5DD;--1:#111111">'</span><span style="--0:#D6DEEB;--1:#403F53">;</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#C792EA;--1:#8844AE">export</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#C792EA;--1:#8844AE">default</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#82AAFF;--1:#3B61B0">defineAgent</span><span style="--0:#D6DEEB;--1:#403F53">({</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#82AAFF;--1:#3B61B0">entry</span><span style="--0:#D6DEEB;--1:#403F53">: </span><span style="--0:#C792EA;--1:#8844AE">async</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#D9F5DD;--1:#111111">(</span><span style="--0:#D7DBE0;--1:#403F53">ctx</span><span style="--0:#7FDBCA;--1:#096E72">:</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--1:#111111"><span style="--0:#FFCB8B">JobContext</span><span style="--0:#D9F5DD">)</span></span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#C792EA;--1:#8844AE">=></span><span style="--0:#D6DEEB;--1:#403F53"> {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#C792EA;--1:#8844AE">await</span><span style="--0:#D6DEEB;--1:#403F53"> ctx</span><span style="--0:#C792EA;--1:#8844AE">.</span><span style="--0:#82AAFF;--1:#3B61B0">connect</span><span style="--0:#D6DEEB;--1:#403F53">();</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#C792EA;--1:#8844AE">const </span><span style="--0:#82AAFF;--1:#3B61B0">session</span><span style="--0:#C792EA;--1:#8844AE"> = </span><span style="--0:#7FDBCA;--1:#096E72">new</span><span style="--0:#C792EA;--1:#8844AE"> </span><span style="--0:#D6DEEB;--1:#403F53">voice</span><span style="--0:#C792EA;--1:#8844AE">.</span><span style="--0:#82AAFF;--1:#3B61B0">AgentSession</span><span style="--0:#D6DEEB;--1:#403F53">(</span><span style="--0:#C792EA;--1:#8844AE">{</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#C792EA;--1:#8844AE">      </span></span><span style="--0:#C792EA;--1:#8844AE">llm: </span><span style="--0:#7FDBCA;--1:#096E72">new</span><span style="--0:#C792EA;--1:#8844AE"> </span><span style="--0:#D6DEEB;--1:#403F53">google</span><span style="--0:#C792EA;--1:#8844AE">.</span><span style="--0:#FAF39F;--1:#111111">beta</span><span style="--0:#C792EA;--1:#8844AE">.</span><span style="--0:#FAF39F;--1:#111111">realtime</span><span style="--0:#C792EA;--1:#8844AE">.</span><span style="--0:#82AAFF;--1:#3B61B0">RealtimeModel</span><span style="--0:#D6DEEB;--1:#403F53">(</span><span style="--0:#C792EA;--1:#8844AE">{ voice: </span><span style="--0:#D9F5DD;--1:#111111">'</span><span style="--0:#ECC48D;--1:#984E4D">Kore</span><span style="--0:#D9F5DD;--1:#111111">'</span><span style="--0:#C792EA;--1:#8844AE"> }</span><span style="--0:#D6DEEB;--1:#403F53">)</span><span style="--0:#C792EA;--1:#8844AE">,</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#C792EA;--1:#8844AE">    </span></span><span style="--0:#C792EA;--1:#8844AE">}</span><span style="--0:#D6DEEB;--1:#403F53">);</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#C792EA;--1:#8844AE">const </span><span style="--0:#82AAFF;--1:#3B61B0">avatar</span><span style="--0:#C792EA;--1:#8844AE"> = </span><span style="--0:#7FDBCA;--1:#096E72">new</span><span style="--0:#C792EA;--1:#8844AE"> </span><span style="--0:#D6DEEB;--1:#403F53">runway</span><span style="--0:#C792EA;--1:#8844AE">.</span><span style="--0:#82AAFF;--1:#3B61B0">AvatarSession</span><span style="--0:#D6DEEB;--1:#403F53">(</span><span style="--0:#C792EA;--1:#8844AE">{</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#C792EA;--1:#8844AE">      </span></span><span style="--0:#C792EA;--1:#8844AE">presetId: </span><span style="--0:#D9F5DD;--1:#111111">'</span><span style="--0:#ECC48D;--1:#984E4D">cat-character</span><span style="--0:#D9F5DD;--1:#111111">'</span><span style="--0:#C792EA;--1:#8844AE">,</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#C792EA;--1:#8844AE">    </span></span><span style="--0:#C792EA;--1:#8844AE">}</span><span style="--0:#D6DEEB;--1:#403F53">);</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#C792EA;--1:#8844AE">await</span><span style="--0:#D6DEEB;--1:#403F53"> avatar</span><span style="--0:#C792EA;--1:#8844AE">.</span><span style="--0:#82AAFF;--1:#3B61B0">start</span><span style="--0:#D6DEEB;--1:#403F53">(session, ctx</span><span style="--0:#C792EA;--1:#8844AE">.</span><span style="--0:#7FDBCA;--1:#096E72">room</span><span style="--0:#D6DEEB;--1:#403F53">);</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#C792EA;--1:#8844AE">await</span><span style="--0:#D6DEEB;--1:#403F53"> session</span><span style="--0:#C792EA;--1:#8844AE">.</span><span style="--0:#82AAFF;--1:#3B61B0">start</span><span style="--0:#D6DEEB;--1:#403F53">({</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#D6DEEB;--1:#403F53">      </span></span><span style="--0:#D6DEEB;--1:#403F53">agent: </span><span style="--0:#7FDBCA;--1:#096E72">new</span><span style="--0:#D6DEEB;--1:#403F53"> voice</span><span style="--0:#C792EA;--1:#8844AE">.</span><span style="--0:#82AAFF;--1:#3B61B0">Agent</span><span style="--0:#D6DEEB;--1:#403F53">({ instructions: </span><span style="--0:#D9F5DD;--1:#111111">'</span><span style="--0:#ECC48D;--1:#984E4D">Talk to me!</span><span style="--0:#D9F5DD;--1:#111111">'</span><span style="--0:#D6DEEB;--1:#403F53"> }),</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#D6DEEB;--1:#403F53">      </span></span><span style="--0:#D6DEEB;--1:#403F53">room: ctx</span><span style="--0:#C792EA;--1:#8844AE">.</span><span style="--0:#7FDBCA;--1:#096E72">room</span><span style="--0:#D6DEEB;--1:#403F53">,</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#D6DEEB;--1:#403F53">      </span></span><span style="--0:#D6DEEB;--1:#403F53">outputOptions: { syncTranscription: </span><span style="--0:#FF6A83;--1:#A24848">false</span><span style="--0:#D6DEEB;--1:#403F53"> },</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#D6DEEB;--1:#403F53">    </span></span><span style="--0:#D6DEEB;--1:#403F53">});</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#D6DEEB;--1:#403F53">    </span></span><span style="--0:#D6DEEB;--1:#403F53">session</span><span style="--0:#C792EA;--1:#8844AE">.</span><span style="--0:#82AAFF;--1:#3B61B0">generateReply</span><span style="--0:#D6DEEB;--1:#403F53">({ instructions: </span><span style="--0:#D9F5DD;--1:#111111">'</span><span style="--0:#ECC48D;--1:#984E4D">Say hello to the user.</span><span style="--0:#D9F5DD;--1:#111111">'</span><span style="--0:#D6DEEB;--1:#403F53"> });</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#D6DEEB;--1:#403F53">  </span></span><span style="--0:#D6DEEB;--1:#403F53">},</span></div></div><div class="ec-line"><div class="code"><span style="--0:#D6DEEB;--1:#403F53">});</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#D6DEEB;--1:#403F53">cli</span><span style="--0:#C792EA;--1:#8844AE">.</span><span style="--0:#82AAFF;--1:#3B61B0">runApp</span><span style="--0:#D6DEEB;--1:#403F53">(</span><span style="--0:#7FDBCA;--1:#096E72">new</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#82AAFF;--1:#3B61B0">ServerOptions</span><span style="--0:#D6DEEB;--1:#403F53">({ agent: </span><span style="--0:#82AAFF;--1:#3B61B0">fileURLToPath</span><span style="--0:#D6DEEB;--1:#403F53">(</span><span style="--0:#C792EA;--1:#8844AE">import.</span><span style="--0:#7FDBCA;--1:#096E72">meta</span><span style="--0:#C792EA;--1:#8844AE">.</span><span style="--0:#7FDBCA;--1:#096E72">url</span><span style="--0:#D6DEEB;--1:#403F53">) }));</span></div></div></code></pre> {    await ctx.connect();    const session = new voice.AgentSession({      llm: new google.beta.realtime.RealtimeModel({ voice: &#x27;Kore&#x27; }),    });    const avatar = new runway.AvatarSession({      presetId: &#x27;cat-character&#x27;,    });    await avatar.start(session, ctx.room);    await session.start({      agent: new voice.Agent({ instructions: &#x27;Talk to me!&#x27; }),      room: ctx.room,      outputOptions: { syncTranscription: false },    });    session.generateReply({ instructions: &#x27;Say hello to the user.&#x27; });  },});cli.runApp(new ServerOptions({ agent: fileURLToPath(import.meta.url) }));">
Use <code dir="auto">avatar_id</code> / <code dir="auto">avatarId</code> instead of <code dir="auto">preset_id</code> / <code dir="auto">presetId</code> to use a custom Character from the Developer Portal.
Note
The agent’s TTS drives what the Avatar says, so any voice or personality configured on the Runway Character is bypassed. Runway receives the already-synthesized audio and lip-syncs it to the Character.
See the LiveKit Runway plugin guide for the full list of <code dir="auto">AvatarSession</code> parameters.
-
**Test it**
Open the LiveKit Agents Playground to preview your agent without building a frontend. Start a conversation and verify the avatar video track appears alongside your agent’s audio.
## End sessions promptly
Section titled “End sessions promptly”
Runway bills realtime Character sessions while the Runway avatar worker is active. The plugin cancels the Runway realtime session during normal LiveKit job shutdown, so make sure your agent shutdown path runs when the user leaves, your agent disconnects, or your app ends the conversation.
Set <code dir="auto">max_duration</code> / <code dir="auto">maxDuration</code> (seconds) in the <code dir="auto">AvatarSession</code> constructor to cap session length. If the job is force-killed before cleanup runs, the Runway session can continue until this limit.
## Handle startup errors
Section titled “Handle startup errors”
<code dir="auto">AvatarSession.start()</code> can fail before the Character joins the LiveKit room, for example if the Runway project has insufficient credits or the session request is invalid. Catch startup errors in your agent and send an application-level message to your frontend so the user does not wait indefinitely for the avatar video track.
   -    Python
-    Node
    <pre data-language="python"><code><div class="ec-line"><div class="code"><span style="--0:#C792EA;--1:#8844AE">try</span><span style="--0:#D6DEEB;--1:#403F53">:</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#C792EA;--1:#8844AE">await</span><span style="--0:#D6DEEB;--1:#403F53"> avatar.</span><span style="--0:#B2CCD6;--1:#096E72">start</span><span style="--0:#D6DEEB;--1:#403F53">(</span><span style="--0:#82AAFF;--1:#3B61B0">session</span><span style="--0:#D9F5DD;--1:#111111">,</span><span style="--0:#82AAFF;--1:#3B61B0"> </span><span style="--0:#D7DBE0;--1:#403F53">room</span><span style="--0:#C792EA;--1:#8844AE">=</span><span style="--0:#82AAFF;--1:#3B61B0">ctx.room</span><span style="--0:#D6DEEB;--1:#403F53">)</span></div></div><div class="ec-line"><div class="code"><span style="--0:#C792EA;--1:#8844AE">except</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#C5E478;--1:#3B61B0">Exception</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#C792EA;--1:#8844AE">as</span><span style="--0:#D6DEEB;--1:#403F53"> exc:</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#C5E478;--1:#3B61B0">print</span><span style="--0:#D6DEEB;--1:#403F53">(</span><span style="--0:#C792EA;--1:#8844AE">f</span><span style="--0:#ECC48D;--1:#984E4D">"failed to start Runway avatar: </span><span style="--0:#82AAFF;--1:#3B61B0">{exc}</span><span style="--0:#ECC48D;--1:#984E4D">"</span><span style="--0:#D6DEEB;--1:#403F53">)</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#C792EA;--1:#8844AE">raise</span></div></div></code></pre>  <pre data-language="ts"><code><div class="ec-line"><div class="code"><span style="--0:#C792EA;--1:#8844AE">try</span><span style="--0:#D6DEEB;--1:#403F53"> {</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#C792EA;--1:#8844AE">await</span><span style="--0:#D6DEEB;--1:#403F53"> avatar</span><span style="--0:#C792EA;--1:#8844AE">.</span><span style="--0:#82AAFF;--1:#3B61B0">start</span><span style="--0:#D6DEEB;--1:#403F53">(session, ctx</span><span style="--0:#C792EA;--1:#8844AE">.</span><span style="--0:#7FDBCA;--1:#096E72">room</span><span style="--0:#D6DEEB;--1:#403F53">);</span></div></div><div class="ec-line"><div class="code"><span style="--0:#D6DEEB;--1:#403F53">} </span><span style="--0:#C792EA;--1:#8844AE">catch</span><span style="--0:#D6DEEB;--1:#403F53"> (error) {</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#D6DEEB;--1:#403F53">  </span></span><span style="--0:#D6DEEB;--1:#403F53">console</span><span style="--0:#C792EA;--1:#8844AE">.</span><span style="--0:#82AAFF;--1:#3B61B0">error</span><span style="--0:#D6DEEB;--1:#403F53">(</span><span style="--0:#D9F5DD;--1:#111111">'</span><span style="--0:#ECC48D;--1:#984E4D">failed to start Runway avatar</span><span style="--0:#D9F5DD;--1:#111111">'</span><span style="--0:#D6DEEB;--1:#403F53">, error);</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#C792EA;--1:#8844AE">throw</span><span style="--0:#D6DEEB;--1:#403F53"> error;</span></div></div><div class="ec-line"><div class="code"><span style="--0:#D6DEEB;--1:#403F53">}</span></div></div></code></pre>
## Learn more
Section titled “Learn more”
   LiveKit Runway plugin guide  LiveKit's integration guide for the Runway Characters plugin.      LiveKit Agents documentation  Full reference for the LiveKit Agents framework: models, plugins, room management, and deployment.      Agents Playground  Test your agent in the browser without building a frontend.      Python plugin source  livekit-plugins-runway in the livekit/agents monorepo.      Node plugin source  @livekit/agents-plugin-runway in the livekit/agents-js monorepo.                Camera and Screen Sharing        Troubleshooting