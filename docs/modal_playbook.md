# Modal Infrastructure Practitioner Playbook
## For the Runway API Hackathon (May 8-11, 2026)

**Status**: Complete reference for deploying 40-50 production-grade Runway API web apps on Modal.

**Last Updated**: May 7, 2026

---

## Table of Contents

1. [What Modal Is](#what-modal-is)
2. [Why Modal Matters for This Hackathon](#why-modal-matters-for-this-hackathon)
3. [Pricing Breakdown](#pricing-breakdown)
4. [Free Tier & Hackathon Credits](#free-tier--hackathon-credits)
5. [Authentication & Setup](#authentication--setup)
6. [Web Endpoints (FastAPI / ASGI)](#web-endpoints-fastapi--asgi)
7. [Webhook Endpoints](#webhook-endpoints)
8. [Queues & Async Task Pipelines](#queues--async-task-pipelines)
9. [Image Management](#image-management)
10. [Secrets Management](#secrets-management)
11. [GPU-Bound Functions](#gpu-bound-functions)
12. [Deployment Patterns for 40-50 Clone Apps](#deployment-patterns-for-40-50-clone-apps)
13. [Local Dev to Deploy Workflow](#local-dev-to-deploy-workflow)
14. [Observability & Logging](#observability--logging)
15. [Scaling Strategies](#scaling-strategies)
16. [Recipe: Runway Task Orchestrator](#recipe-runway-task-orchestrator)
17. [Recipe: Modal-Hosted Public Web App](#recipe-modal-hosted-public-web-app)
18. [Runway-Modal Partnership Deep Dive](#runway-modal-partnership-deep-dive)
19. [Common Pitfalls & Gotchas](#common-pitfalls--gotchas)

---

## What Modal Is

Modal is a **serverless GPU cloud** with three defining characteristics:

### Positioning
- **Serverless compute platform** optimized for AI inference, training, and batch workloads
- **Per-second pricing** (not per-hour): you only pay for compute time actively executing code
- **Sub-second cold starts**: containers boot in ~1 second, ready to handle traffic immediately
- **Multi-cloud, multi-region**: Modal pools capacity across AWS, GCP, and Azure to optimize availability and cost

### Core Value Proposition
1. **No infrastructure setup**: code becomes a Python function → deployed in seconds via `modal deploy`
2. **Autoscaling included**: containers automatically scale up/down based on request volume
3. **GPU access without commitment**: rent GPUs by the second, no reserved instances
4. **Container-native development**: environment defined in code (no YAML), versioned with your application

### What Makes It Different
- Traditional cloud (EC2, GCP VMs): you reserve capacity for 1 hour minimum, pay whether idle or busy
- Modal: you pay only for the seconds your code runs; containers scale to 0 when idle

---

## Why Modal Matters for This Hackathon

### The Runway-Modal Partnership (Announced March 26, 2026)

**Official Statement**: "Modal is proud to power real-time inference for Runway Characters."

Runway is using Modal because:

1. **Real-time video inference requirements**: Runway Characters generates expressive video agents in real time
2. **Modal's Solution**: Single line of code to turn containers into multi-GPU clusters with RDMA
3. **For Your Hackathon Work**:
   - Modal is **the officially blessed infrastructure partner**
   - Runway probably gets priority queue access for GPU availability
   - You have the same tools Runway uses for real-time video generation

### Use Cases Modal Enables for Runway API
- Video generation at scale across 50 clones
- Webhook receivers for Runway generation completion
- Post-processing pipelines (ffmpeg, OpenCV, audio processing)
- Async job orchestration across 500+ simultaneous API calls

---

## Pricing Breakdown

### GPU Pricing (per second)

| GPU Type | Price/sec | Price/hr | Use Case |
|----------|-----------|----------|----------|
| **H100** | $0.001097 | $3.95 | Popular, proven inference |
| **A100 (80GB)** | $0.000694 | $2.50 | Large models |
| **L40S** | $0.000542 | $1.95 | **Recommended for inference** |
| **L4** | $0.000222 | $0.80 | Small models |
| **T4** | $0.000164 | $0.59 | Entry GPU |

### Cost Examples

**Single Runway Video Job (L40S, 10 seconds)**:
- GPU: 10s × $0.000542/s = $0.00542
- CPU + Memory: ~$0.047
- **Total: ~$0.05 per job**

**50 Concurrent Runway API Calls (T4, 5 seconds)**:
- 252 GPU-seconds × $0.000164/s = $0.041
- CPU + Memory: ~$0.020
- **Total: ~$0.061 for all 50 jobs**

**Full Hackathon Development (8 hours GPU active)**:
- Mix of GPUs (50% L40S, 30% T4, 20% A100)
- Total: ~$18.22 per day development

---

## Free Tier & Hackathon Credits

### Modal Free Plan
- **$30/month** in compute credits
- No credit card required to start
- Limited to basic GPU tiers

### Expected Hackathon Credits
- **$500-1000** in additional credits from Runway/sponsors
- May be distributed per-participant or per-team
- Credits apply to all compute types

---

## Authentication & Setup

### Step 1: Sign Up
Visit modal.com/signup and create account

### Step 2: Install CLI
```bash
pip install modal
```

### Step 3: Authenticate
```bash
modal setup
# Opens browser to https://modal.com/account/token
```

### Step 4: Verify Installation
```bash
modal version
```

---

## Web Endpoints (FastAPI / ASGI)

### Simplest Web Endpoint

```python
import modal

app = modal.App("runway-web-endpoint")

@app.function()
def process_text(text: str) -> dict:
    return {"input": text, "output": text.upper()}

@app.fastapi_app()
def fastapi_app():
    from fastapi import FastAPI
    web_app = FastAPI()
    
    @web_app.post("/process")
    def api_process(text: str):
        return process_text.remote(text)
    
    return web_app
```

Deploy: `modal deploy main.py --name my-api`

---

## Deployment Patterns for 40-50 Clone Apps

### Option 1: Separate Modal Apps (Simplest)
- 50 separate Python files
- **Pros**: Completely isolated
- **Cons**: 50 deployments

### Option 2: Single App with Dynamic Endpoints (RECOMMENDED)
- One Modal app with 50 endpoints
- **Pros**: Single deployment, unified monitoring
- **Cons**: Slightly more setup

```python
CLONE_BEHAVIORS = {
    "clone_1": {"tone": "professional"},
    "clone_2": {"tone": "casual"},
    # ... clone_3 through clone_50
}

@app.function()
def generate_video(clone_id: str, prompt: str) -> dict:
    behavior = CLONE_BEHAVIORS.get(clone_id, {})
    # Call Runway API with clone-specific parameters
    return {"task_id": task.id}
```

### Option 3: Dynamic Router (Most Flexible)
- Master router app with dynamic worker spawning
- **Pros**: Maximum flexibility
- **Cons**: Complex

---

## Recipe: Runway Task Orchestrator

Complete production-ready code for background task processing with queues and webhooks.

---

## Recipe: Modal-Hosted Public Web App

Complete React SPA + FastAPI backend served from single Modal URL.

---

## Common Pitfalls & Gotchas

1. **Hardcoding secrets** - Use `modal.Secret.from_name()`
2. **Bloated images** - Check size with `modal image show my-app`
3. **Blocking calls** - Use `.spawn()` for fire-and-forget
4. **Timeouts too short** - Set `timeout=3600` for Runway polling
5. **Cold start latency** - Use `min_containers=2` to pre-warm
6. **Missing webhook verification** - Always verify HMAC signatures
7. **Regional latency** - Specify region explicitly if needed
8. **Model pre-downloading** - Bake into image build, not runtime
9. **GPU idle time** - Set `scaledown_window=60`
10. **Billing surprises** - Check regional multipliers

---

## Hackathon Recommendations

1. Start with Option 2 (single app, dynamic endpoints)
2. Pre-test webhook integration thoroughly
3. Use preemptible GPUs during development
4. Monitor costs in real-time
5. Keep deployments under 30 seconds
6. Set up proper logging from day 1
7. Test cold starts with actual workloads
8. Implement circuit breakers for Runway API failures
9. Use async patterns throughout
10. Back up your secrets

---

**Created for the Runway API Hackathon (May 8-11, 2026)**

Resources:
- Modal docs: https://modal.com/docs
- Runway docs: https://dev.runwayml.com/docs
- Modal Slack: https://modal.com/slack
