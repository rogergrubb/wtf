# RUNWAY API & TECHNICAL SPECIFICATIONS

**Reference**: For Hackathon Build Planning (May 8-11, 2026)

---

## API ACCESS & AUTHENTICATION

### Getting Started
- **Platform**: https://dev.runwayml.com
- **Plan**: API Build (free tier) for hackathon
- **Requirements**: 
  - Runway account
  - API key generation
  - Credit allocation (free tier or purchased)

### Authentication
- API key-based (REST)
- Bearer token in Authorization header
- Rate limiting: TBD (check docs)

---

## CORE API ENDPOINTS (Inferred from Product)

### Video Generation

#### Text-to-Video
```
POST /api/v1/generate/text-to-video
{
  "prompt": "A dog running in a park",
  "model": "gen-4-5", 
  "duration": 5,
  "resolution": "1080p"
}
```
**Response**: Video ID, status, URL when ready

#### Image-to-Video
```
POST /api/v1/generate/image-to-video
{
  "image": "<base64 or URL>",
  "prompt": "describe motion",
  "model": "gen-4-5"
}
```

### Processing

#### Upscale
```
POST /api/v1/process/upscale
{
  "video_id": "<video_id>",
  "target_resolution": "4K"
}
```

#### Remove from Video
```
POST /api/v1/process/remove
{
  "video_id": "<video_id>",
  "prompt": "remove person"
}
```

#### Add Dialogue
```
POST /api/v1/process/add-dialogue
{
  "video_id": "<video_id>",
  "text": "What a beautiful day",
  "voice_model": "default" // or custom voice ID
}
```

### World Models (Likely Endpoints, TBD)

#### GWM Worlds
```
POST /api/v1/gwm/worlds
{
  "prompt": "A futuristic city",
  "interactive": true,
  "duration": 30
}
```

#### GWM Avatars
```
POST /api/v1/gwm/avatars
{
  "character_description": "...",
  "voice": "...",
  "dialogue": "Hello, how can I help?"
}
```

#### GWM Robotics (Likely)
```
POST /api/v1/gwm/robotics
{
  "task": "pick and place",
  "environment": "tabletop"
}
```

### Workflows

#### Create Workflow
```
POST /api/v1/workflows
{
  "name": "My Pipeline",
  "nodes": [
    {"type": "text-to-video", "model": "gen-4-5", "prompt_source": "user"},
    {"type": "upscale", "target": "4K"},
    {"type": "add-dialogue", "voice_model": "custom"}
  ],
  "edges": [[0, 1], [1, 2]]
}
```

#### Execute Workflow
```
POST /api/v1/workflows/{workflow_id}/execute
{
  "inputs": {"user_prompt": "A cat"}
}
```

---

## EXPECTED LATENCIES & CONSTRAINTS

| Operation | Expected Latency | Credits | Notes |
|-----------|-----------------|---------|-------|
| Gen-4.5 (5s video) | 30-60s | 25 | Depends on queue |
| Gen-4 Turbo (4s) | 10-20s | 12 | Faster, acceptable quality |
| Gen-3 Alpha Turbo (8s) | 5-10s | 5 | Fast prototyping |
| Upscale | 10-30s | Bundled | Processing only |
| Remove from Video | 15-40s | Bundled | Dependent on scene |
| Add Dialogue | 5-15s | Bundled | Simple speech synthesis |
| GWM Worlds | 20-60s | TBD | Likely higher latency (complex) |
| GWM Avatars | 10-40s | TBD | Likely moderate latency |

**Hackathon Strategy**: Use Gen-3 for real-time interactivity; Gen-4.5 for final demo.

---

## CREDIT COST CALCULATOR

### Monthly Plan Credits to Cost Mapping

**Standard Plan (625 credits/month)**:
- 625 credits ÷ 52 seconds of Gen-4 = ~12 credits per second of Gen-4
- 625 credits ÷ 25 seconds of Gen-4.5 = 25 credits per second of Gen-4.5
- 625 credits ÷ 125 seconds of Gen-3 = 5 credits per second of Gen-3

### Hackathon Budget Example (Assume 50 credits free)

| Strategy | Gen-3 Videos | Gen-4 Videos | Gen-4.5 Videos | Total | Quality |
|----------|-------------|------------|--------------|-------|---------|
| Prototype Heavy | 50 (400s) | 0 | 0 | 50 | Low-med |
| Balanced | 20 (160s) | 15 (120s) | 15 (60s) | 50 | Medium-high |
| Quality | 5 (40s) | 10 (80s) | 35 (140s) | 50 | High |

**Recommendation**: Balanced approach for iterative development + final quality.

---

## WORKFLOW COMPOSITION PATTERNS

### Simple Chain (Text → Video → Upscale)
```
Input: User text prompt
→ Gen-4.5 text-to-video
→ Upscale to 4K
→ Output: High-res video
Cost: 25 + bundled = 25 credits
```

### Complex Chain (Gen + Edit + Voice + Dialogue)
```
Input: Storyboard images
→ Image-to-video (4 images × Gen-4)
→ Add dialogue to each
→ Upscale
→ Output: Complete video
Cost: (12×4) + (bundled×4) + bundled = ~50 credits
```

### Interactive Loop (Real-Time Avatar)
```
Input: User speech
→ Speech-to-text
→ LLM dialogue generation
→ Runway Characters real-time avatar
→ TTS (Eleven v3, future)
→ Output: Video response
Cost: Variable (interactive, real-time)
```

---

## THIRD-PARTY INTEGRATIONS

### LLM Orchestration
- **Claude API**: Prompt generation, dialogue, planning
- **GPT-4**: Alternative language model
- **Llama 2**: Open-source option

**Hackathon Pattern**: Use Claude for scene generation, dialogue writing, workflow planning.

### Speech Processing
- **OpenAI Whisper**: Speech-to-text
- **Eleven Labs API**: Text-to-speech (integrated with Runway)
- **Custom Voice**: Train on user sample (Pro+ feature)

### Hosting & Deployment
- **Modal Labs**: Serverless compute (mentioned as Runway partner)
- **AWS Lambda**: Async job processing
- **Vercel/Netlify**: Frontend hosting

---

## SAMPLE CODE PATTERNS

### Python Pattern: Text-to-Video
```python
import runway

# Initialize client
client = runway.Client(api_key="your_api_key")

# Generate video
task = client.generate(
    model="gen-4-5",
    type="text-to-video",
    prompt="A futuristic city at sunset",
    duration=5
)

# Poll for completion
while task.status == "processing":
    time.sleep(2)
    task.reload()

# Retrieve result
video_url = task.output

print(f"Video ready: {video_url}")
```

### JavaScript Pattern: Workflow Execution
```javascript
const runway = require("runway-api");

const client = new runway.Client({
  apiKey: process.env.RUNWAY_API_KEY
});

async function executeWorkflow() {
  const workflow = await client.workflows.get("workflow_id");
  
  const execution = await workflow.execute({
    inputs: {
      user_prompt: "A dancing robot"
    }
  });

  console.log(`Workflow execution: ${execution.id}`);
  
  // Poll for completion
  let result = null;
  while (!result) {
    result = await execution.status();
    if (result.status === "completed") break;
    await new Promise(r => setTimeout(r, 2000));
  }

  console.log(`Result: ${result.outputs}`);
}

executeWorkflow();
```

---

## ERROR HANDLING & RESILIENCE

### Common Errors
- **Rate Limit (429)**: Implement exponential backoff
- **Insufficient Credits (402)**: Monitor balance; alert user
- **Timeout (408)**: Long-running tasks; implement polling
- **Invalid Prompt (400)**: Validate prompt length, content

### Retry Strategy
```
Attempt 1: Immediate
Attempt 2: 2s delay
Attempt 3: 4s delay
Attempt 4: 8s delay
Max 4 attempts
```

### Polling Pattern
```
Task submitted → ID returned
Poll every 2-5s
Check status: processing, completed, failed
Timeout after 5 minutes (or model-specific limit)
```

---

## PERFORMANCE TUNING

### Latency Optimization
1. **Parallel Processing**: Submit multiple prompts simultaneously
2. **Credit Efficiency**: Use Gen-3 for iteration, Gen-4.5 only for final
3. **Caching**: Store intermediate results (upscaled videos, dialogue)
4. **Async Workflows**: Don't block on generation; queue and poll

### Quality Optimization
1. **Prompt Engineering**: Detailed, specific prompts yield better results
2. **Reference Images**: Provide style/quality examples
3. **Gen-4.5 for Finals**: Use flagship model for deliverables
4. **Upscaling**: 2x upscale often imperceptible; 4x risks artifacts

### Cost Optimization
1. **Gen-3 for Prototyping**: 5 credits/sec vs. 25 for Gen-4.5
2. **Batch Processing**: Amortize API overhead
3. **Workflow Reuse**: Save pipelines; don't regenerate
4. **Monitor Spend**: Alert at 80% credit usage

---

## TESTING STRATEGY (72-Hour Build)

### Phase 1: API Validation (6 hours)
- Test authentication
- Validate text-to-video endpoint
- Check credit deduction
- Confirm response format

### Phase 2: Feature Integration (24 hours)
- Build Gen-4.5 pipeline
- Integrate GWM-1 (if using)
- Test voice/dialogue
- Validate workflow execution

### Phase 3: Optimization & Polish (12 hours)
- Latency optimization (parallel requests)
- Credit efficiency tuning
- Error handling and retry logic
- Demo capture and refinement

### Phase 4: Final Testing (4 hours)
- End-to-end workflow test
- Edge case handling
- Demo video production
- Documentation

---

## DEPLOYMENT CHECKLIST

- [ ] API credentials configured (environment variables)
- [ ] Rate limiting implemented
- [ ] Error handling for all API calls
- [ ] Credit monitoring active
- [ ] Polling/async patterns working
- [ ] Output validation (video URLs valid, metadata correct)
- [ ] Workflow definitions tested
- [ ] LLM integration tested (if using Claude/GPT)
- [ ] Frontend UI responsive
- [ ] Demo capture clean and professional

---

## ADVANCED TECHNIQUES

### Multi-Model Composition
```
Step 1: Gen-4.5 generates hero shot (high quality)
Step 2: Gen-3 Alpha generates variations (fast iteration)
Step 3: Prompt engineering refinement
Step 4: Upscale top 3 candidates to 4K
Step 5: Human selection for final
```

### Workflow-as-Code Pattern
```
Define complex workflows in YAML/JSON
Version control workflow definitions
Support workflow marketplace (future)
Enable community sharing
```

### Real-Time Interactivity
```
WebSocket connection for live avatar interaction
Streaming video output (if supported)
Sub-100ms latency target for character response
Queue management for concurrent users
```

---

## MONITORING & OBSERVABILITY

### Metrics to Track
- API response latency (p50, p95, p99)
- Credit usage rate and budget remaining
- Error rate and error types
- Workflow execution success rate
- Video quality metrics (if available)

### Logging Pattern
```json
{
  "timestamp": "2026-05-08T10:30:00Z",
  "event": "video_generation",
  "model": "gen-4-5",
  "prompt": "...",
  "duration_seconds": 5,
  "credits_used": 25,
  "latency_ms": 45000,
  "status": "completed",
  "output_url": "..."
}
```

### Alerting
- Alert if error rate > 10%
- Alert if latency > 90 seconds
- Alert if credits < 10 remaining
- Alert if quota exceeded

---

## FINAL TECHNICAL RECOMMENDATIONS

1. **Use Python for scripting** (official SDK likely available)
2. **Use Node.js + React for frontend** (web-based interactive demo)
3. **Implement comprehensive error handling** (API is rate-limited)
4. **Cache intermediate results** (avoid regenerating same content)
5. **Monitor credits closely** (prevent unexpected overages)
6. **Test with Gen-3 first** (save Gen-4.5 budget for final)
7. **Profile latencies early** (plan demo around expected delays)
8. **Document workflows clearly** (judges want to understand architecture)

---

**Last Updated**: May 5, 2026  
**Source**: runwayml.com, dev.runwayml.com, inferred from API documentation

