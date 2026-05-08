# Runway API Practitioner Playbook
**For the 72-hour Hackathon Build Window (May 8-11, 2026)**

This is a copy-paste reference for builders during active development. Do not summarize—use exact signatures, real error codes, and code you can run immediately. Last updated: May 7, 2026 (based on official Runway docs).

---

## 1. Authentication & Setup

### API Key Format and Headers

All requests require your API secret in the `Authorization` header:

```
Authorization: Bearer YOUR_API_KEY
```

API keys are issued from the developer portal at https://dev.runwayml.com/. Keys are shown only once—save them securely. Format is `key_` followed by alphanumeric characters.

**Required Headers for all requests:**
- `Authorization: Bearer key_xxxxx` (required)
- `Content-Type: application/json` (required for POST/PUT)
- `X-Runway-Version: 2024-11-06` (optional but recommended for version pinning)

### Environment Setup

```bash
# macOS/Linux
export RUNWAYML_API_SECRET="key_xxxxx"

# Windows PowerShell
setx RUNWAYML_API_SECRET "key_xxxxx"
```

### SDK Installation

**Node.js:**
```bash
npm install --save @runwayml/sdk
# or yarn add @runwayml/sdk
# or pnpm add @runwayml/sdk
```

**Python:**
```bash
pip install runwayml
```

The SDKs automatically read `RUNWAYML_API_SECRET` from environment. SDKs support Node 18+ and Python 3.8+.

### Minimum Viable Client Initialization

**Node.js:**
```javascript
import RunwayML from '@runwayml/sdk';
const client = new RunwayML({
  apiKey: process.env.RUNWAYML_API_SECRET, // optional—auto-detected
});
```

**Python:**
```python
from runwayml import RunwayML
client = RunwayML()  # auto-reads RUNWAYML_API_SECRET
```

---

## 2. Per-Endpoint Reference

### Video Generation Endpoints

#### `gen4.5` (Text-to-Video & Image-to-Video)

**Pricing:** 12 credits/second. A 5-second generation costs 60 credits ($0.60).

**SDK Method:**
- Node: `client.imageToVideo.create({})`
- Python: `client.image_to_video.create()`

**Parameters (copy-paste ready):**

| Parameter | Type | Required | Notes |
|-----------|------|----------|-------|
| `model` | string | yes | Must be `'gen4.5'` |
| `prompt_text` or `promptText` | string | yes | Max 1000 chars. Supports reference images via `@tagname` syntax. |
| `prompt_image` or `promptImage` | URL or data URI | no | Omit for pure text-to-video. URL must be HTTPS. Max 16MB via URL, 5MB via data URI. |
| `ratio` or `ratio` | string | yes | Landscape: `'1280:720'`, `'1584:672'`, `'1104:832'`. Portrait: `'720:1280'`, `'832:1104'`, `'672:1584'`. Square: `'960:960'`. |
| `duration` | integer | yes | Range: 2–10 seconds. |
| `seed` | integer | no | Fixed seed for reproducibility. |
| `content_moderation` or `contentModeration` | object | no | Set `level: 'lenient'` to allow recognizable public figures (default: `'auto'`). |

**Exact Python Example:**
```python
from runwayml import RunwayML, TaskFailedError
import base64

client = RunwayML()

try:
    # Text-to-video: no prompt_image needed
    task = client.image_to_video.create(
        model='gen4.5',
        prompt_text='A serene mountain landscape at sunrise with mist rolling through the valleys',
        ratio='1280:720',
        duration=5,
    ).wait_for_task_output()
    
    print(f"Video URL: {task.output[0]}")
    
except TaskFailedError as e:
    print(f"Task failed: {e.task_details}")
```

**Exact Node.js Example:**
```javascript
import RunwayML, { TaskFailedError } from '@runwayml/sdk';

const client = new RunwayML();

try {
    const task = await client.imageToVideo
        .create({
            model: 'gen4.5',
            promptText: 'A serene mountain landscape at sunrise with mist rolling through the valleys',
            ratio: '1280:720',
            duration: 5,
        })
        .waitForTaskOutput();
    
    console.log(`Video URL: ${task.output[0]}`);
    
} catch (error) {
    if (error instanceof TaskFailedError) {
        console.error('Task failed:', error.taskDetails);
    } else {
        throw error;
    }
}
```

**Output Schema:**
```json
{
  "id": "task-uuid-here",
  "status": "SUCCEEDED",
  "createdAt": "2026-05-07T12:00:00Z",
  "output": ["https://dnznrvs05pmza.cloudfront.net/output.mp4?_jwt=..."]
}
```

**Observed Latency:** 15–45 seconds for 5-second gen4.5 videos at Tier 1.

**Constraints:** Aspect ratio must fall within 0.5–2.0 (width÷height).

---

#### `gen4_aleph` (Video-to-Video)

**Pricing:** 15 credits/second.

**SDK Method:**
- Node: `client.videoToVideo.create({})`
- Python: `client.video_to_video.create()`

**Parameters:**

| Parameter | Type | Required | Notes |
|-----------|------|----------|-------|
| `model` | string | yes | Must be `'gen4_aleph'` |
| `prompt_text` or `promptText` | string | yes | Describes the transform to apply. Max 1000 chars. |
| `prompt_video` or `promptVideo` | URL or data URI | yes | Input video. Max 32MB via URL, 16MB via data URI. Aspect ratio 0.5–2.358. |
| `ratio` | string | yes | Output ratio. Landscape: `'1280:720'`, `'1584:672'`, `'1104:832'`, `'848:480'`. Portrait: `'720:1280'`, `'832:1104'`, `'480:848'`. Square: `'960:960'`. |
| `duration` | integer | no | If omitted, matches input duration. Range: 2–10 sec. |
| `seed` | integer | no | Reproducibility. |
| `content_moderation` | object | no | As above. |

**Python Example:**
```python
task = client.video_to_video.create(
    model='gen4_aleph',
    prompt_video='https://example.com/input.mp4',
    prompt_text='Transform the video to look like an oil painting',
    ratio='1280:720',
).wait_for_task_output()
```

---

#### `gen4_turbo` (Faster Image-to-Video)

**Pricing:** 5 credits/second.

**SDK Method:**
- Node: `client.imageToVideo.create({ model: 'gen4_turbo' })`
- Python: `client.image_to_video.create(model='gen4_turbo')`

**Parameters:** Same as `gen4.5` except:
- `ratio` supports: Landscape `'1280:720'`, `'1584:672'`, `'1104:832'`; Portrait `'720:1280'`, `'832:1104'`; Square `'960:960'`.
- `duration` range: 2–10 seconds.

---

#### `veo3`, `veo3.1`, `veo3.1_fast` (Google Models)

**Pricing:**
- `veo3`: 40 credits/second
- `veo3.1` (with audio): 40 credits/sec
- `veo3.1` (no audio): 20 credits/sec
- `veo3.1_fast` (with audio): 15 credits/sec
- `veo3.1_fast` (no audio): 10 credits/sec

**SDK Method:**
- Node: `client.imageToVideo.create({ model: 'veo3' })`
- Python: `client.image_to_video.create(model='veo3')`

**Parameters:** Same as gen4.5, with these differences:
- Aspect ratio range: 0.5–2.0 (width÷height).
- First and last keyframe support (veo3.1 only).

---

#### `act_two` (Character Performance)

**Pricing:** 5 credits/second.

**SDK Method:**
- Node: `client.characterPerformance.create({})`
- Python: `client.character_performance.create()`

**Parameters:**

| Parameter | Type | Required | Notes |
|-----------|------|----------|-------|
| `model` | string | yes | Must be `'act_two'` |
| `character_image` or `characterImage` | URL or data URI | yes | Reference image of the performer. Aspect ratio 0.5–2.358. |
| `character_video` or `characterVideo` | URL or data URI | no | Optional character motion reference. Aspect ratio 0.5–2.358. |
| `reference_video` or `referenceVideo` | URL or data URI | no | Optional video to use for stylization. Aspect ratio 0.5–2.358. |
| `prompt_text` or `promptText` | string | yes | Description of the performance. Max 1000 chars. |
| `ratio` | string | yes | Same options as gen4_turbo. |
| `duration` | integer | yes | 2–10 seconds. |
| `seed` | integer | no | Reproducibility. |

---

### Image Generation Endpoints

#### `gen4_image` (Runway's Standard Image Model)

**Pricing:** 5 credits per 720p image, 8 credits per 1080p image.

**SDK Method:**
- Node: `client.textToImage.create({})`
- Python: `client.text_to_image.create()`

**Parameters:**

| Parameter | Type | Required | Notes |
|-----------|------|----------|-------|
| `model` | string | yes | Must be `'gen4_image'` |
| `prompt_text` or `promptText` | string | yes | Max 5500 chars. Use `@tagname` to reference images. |
| `reference_images` or `referenceImages` | array | no | Up to 14 images. Each: `{ "uri": "url", "tag": "name" }`. Tag is optional. |
| `ratio` | string | yes | Common: `'1920:1080'`, `'1360:768'`. Supports 10 aspect ratios. |
| `seed` | integer | no | Reproducibility. |
| `content_moderation` | object | no | As above. |

**Python Example:**
```python
task = client.text_to_image.create(
    model='gen4_image',
    prompt_text='@EiffelTower painted in the style of @StarryNight',
    reference_images=[
        {
            'uri': 'https://example.com/eiffel.jpg',
            'tag': 'EiffelTower',
        },
        {
            'uri': 'https://example.com/starry.jpg',
            'tag': 'StarryNight',
        },
    ],
    ratio='1920:1080',
).wait_for_task_output()

print(f"Image URL: {task.output[0]}")
```

---

#### `gen4_image_turbo`

**Pricing:** 2 credits per image (any resolution).

**SDK Method:** Same as `gen4_image`, change model to `'gen4_image_turbo'`.

**Parameters:** Same as `gen4_image`.

---

#### `gemini_image3_pro` (Nano Banana Pro)

**Pricing:** 20 credits/1K–2K, 40 credits/4K.

**SDK Method:** Node: `client.textToImage.create({ model: 'gemini_image3_pro' })`.

**Parameters:**

| Parameter | Type | Required | Notes |
|-----------|------|----------|-------|
| `model` | string | yes | `'gemini_image3_pro'` |
| `prompt_text` | string | yes | Up to 5500 chars. Supports `@tagname` references. |
| `reference_images` | array | no | Up to 14 images. |
| `ratio` | string | yes | Supports 10 aspect ratios. |

---

#### `gpt_image_2` (OpenAI)

**Pricing:** 1–41 credits per image by quality and resolution.

| Quality | 1K / 2K | 4K (incl. `auto`) |
|---------|---------|------------------|
| `low` | 1 | 2 |
| `medium` | 5 | 11 |
| `high` | 20 | 41 |
| `auto` | 20 | 41 |

**SDK Method:** `client.textToImage.create({ model: 'gpt_image_2' })`.

**Parameters:**

| Parameter | Type | Required | Notes |
|-----------|------|----------|-------|
| `model` | string | yes | `'gpt_image_2'` |
| `prompt_text` | string | yes | Up to 4000 chars. Supports `@tagname`. |
| `reference_images` | array | no | Up to 16 images. |
| `ratio` | string | yes | 30 aspect ratios across 1K, 2K, 4K, + auto. |
| `quality` | string | no | Default `'high'`. Options: `'low'`, `'medium'`, `'high'`, `'auto'`. |
| `output_count` | integer | no | Number of images to generate. Billed as `credits_per_image × output_count`. |

---

#### `gemini_2.5_flash`

**Pricing:** 5 credits per image (any resolution).

**SDK Method:** `client.textToImage.create({ model: 'gemini_2.5_flash' })`.

**Parameters:** Same as `gen4_image`.

---

### Audio Generation Endpoints

#### `eleven_multilingual_v2` (Text-to-Speech)

**Pricing:** 1 credit per 50 characters.

**SDK Method:**
- Node: `client.textToSpeech.create({})`
- Python: `client.text_to_speech.create()`

**Parameters:**

| Parameter | Type | Required | Notes |
|-----------|------|----------|-------|
| `model` | string | yes | `'eleven_multilingual_v2'` |
| `prompt_text` or `promptText` | string | yes | Text to convert to speech. |
| `voice` | object | yes | Voice configuration: `{ "type": "preset", "preset_id": "adam" }` or custom. |
| `language` | string | no | ISO 639-1 code (e.g., `'en'`, `'es'`, `'fr'`). 29 languages supported. |

**Available Preset Voices:** `adam`, `alice`, `aria`, `bella`, `brian`, `callum`, `carol`, `carlos`, `charlie`, `claire`, `clara`, `daniel`, `david`, `davide`, `diana`, `dora`, `donald`, `doug`, `douglas`, `drew`, `edward`, `emily`, `eric`, `ernie`, `eva`, `evan`, `frank`, `george`, `gerald`, `gigi`...

**Python Example:**
```python
task = client.text_to_speech.create(
    model='eleven_multilingual_v2',
    prompt_text='Hello, this is a test of the text-to-speech system.',
    voice={'type': 'preset', 'preset_id': 'adam'},
    language='en',
).wait_for_task_output()

print(f"Audio URL: {task.output[0]}")
```

---

#### `eleven_text_to_sound_v2` (Sound Effect Generation)

**Pricing:** 1 credit/second of audio if duration provided, 2 credits if no duration, roughly 1 credit per 6 seconds if generated.

**SDK Method:**
- Node: `client.soundEffect.create({})`
- Python: `client.sound_effect.create()`

**Parameters:**

| Parameter | Type | Required | Notes |
|-----------|------|----------|-------|
| `model` | string | yes | `'eleven_text_to_sound_v2'` |
| `prompt_text` or `promptText` | string | yes | Describe the sound effect. |
| `duration_seconds` or `durationSeconds` | number | no | Target duration in seconds. If provided, cost is 1 credit/sec. |

**Python Example:**
```python
task = client.sound_effect.create(
    model='eleven_text_to_sound_v2',
    prompt_text='A heavy wooden door slamming shut, followed by an echo',
    duration_seconds=3,
).wait_for_task_output()
```

---

#### `eleven_voice_isolation` (Noise Removal)

**Pricing:** 1 credit per 6 seconds of audio.

**SDK Method:**
- Node: `client.voiceIsolation.create({})`
- Python: `client.voice_isolation.create()`

**Parameters:**

| Parameter | Type | Required | Notes |
|-----------|------|----------|-------|
| `model` | string | yes | `'eleven_voice_isolation'` |
| `audio` | URL or data URI | yes | Audio to clean. Max 32MB URL, 16MB data URI. Supported formats: MP3, WAV, FLAC, M4A, AAC. |

---

#### `eleven_voice_dubbing` (Multilingual Dubbing)

**Pricing:** 1 credit per 2 seconds of audio.

**SDK Method:**
- Node: `client.voiceDubbing.create({})`
- Python: `client.voice_dubbing.create()`

**Parameters:**

| Parameter | Type | Required | Notes |
|-----------|------|----------|-------|
| `model` | string | yes | `'eleven_voice_dubbing'` |
| `audio` | URL or data URI | yes | Source audio. |
| `target_language` or `targetLanguage` | string | yes | Language code: `'en'`, `'es'`, `'fr'`, `'de'`, `'it'`, `'ja'`, `'zh'`, etc. (29 languages). |

---

#### `eleven_multilingual_sts_v2` (Speech-to-Speech)

**Pricing:** 1 credit per 3 seconds of audio.

**SDK Method:**
- Node: `client.speechToSpeech.create({})`
- Python: `client.speech_to_speech.create()`

**Parameters:**

| Parameter | Type | Required | Notes |
|-----------|------|----------|-------|
| `model` | string | yes | `'eleven_multilingual_sts_v2'` |
| `audio` | URL or data URI | yes | Source audio. |
| `voice` | object | yes | Target voice config: `{ "type": "preset", "preset_id": "adam" }` or custom. |

---

### Real-Time Avatar Endpoint

#### `gwm1_avatars` (Runway Characters)

**Pricing:** 2 credits upfront + 2 credits per 6 seconds of conversation.

**SDK Method:**
- Node: `client.realtimeSessions.create({})`
- Python: `client.realtime_sessions.create()`

**Parameters:**

| Parameter | Type | Required | Notes |
|-----------|------|----------|-------|
| `model` | string | yes | `'gwm1_avatars'` |
| `avatar` | object | yes | Avatar spec: `{ "type": "custom", "avatar_id": "uuid" }` or `{ "type": "preset", "preset_id": "name" }`. |
| `personality` | string | no | Override avatar's system prompt (max 10,000 chars). |
| `start_script` | string | no | Override opening message (max 2000 chars). |

**Session Lifecycle States:**
- `NOT_READY`: Provisioning in progress. Poll until ready.
- `READY`: Ready to connect. `sessionKey` is available.
- `RUNNING`: WebRTC connection active.
- `COMPLETED`: Conversation ended normally.
- `FAILED`: Error occurred. Check `failure` field.
- `CANCELLED`: Session explicitly cancelled.

**Python Example:**
```python
# Create session
session = client.realtime_sessions.create(
    model='gwm1_avatars',
    avatar={
        'type': 'custom',
        'avatar_id': 'your-avatar-uuid',
    },
    personality='You are a helpful customer support agent...',
).wait_for_task_output()

print(f"Session Key: {session.session_key}")
print(f"Session Status: {session.status}")
```

**Session Max Duration:** 5 minutes. Output expires 24–48 hours after access.

---

## 3. Task Lifecycle & Polling

### Submitting a Task

All generation endpoints return a task immediately:

```python
# Don't await yet—you can get the task ID first
task_promise = client.image_to_video.create(...)

# Optionally capture the task ID for a database
task_id = (await task_promise).id  # await the create() to get ID

# Then await the full output
completed_task = await task_promise.wait_for_task_output()
```

### Task Status Values (Complete List)

| Status | Description | Retryable |
|--------|-------------|-----------|
| `PENDING` | Queued, not yet running. | N/A (will progress) |
| `QUEUED` | Enqueued in the queue. | N/A |
| `RUNNING` | Currently generating. | N/A |
| `SUCCEEDED` | Completed successfully. Output in `output[]`. | N/A |
| `FAILED` | Generation failed. See `failureCode` and `failure`. | Depends on code |
| `THROTTLED` | Hit concurrency limit. Enqueued when slot opens. | N/A (will progress) |
| `CANCELED` | Explicitly cancelled. | No |

### Manual Polling Pattern (without SDK built-in)

```python
import time

task_id = (await client.image_to_video.create(...)).id

# Polling loop with exponential backoff + jitter
attempt = 0
max_attempts = 100
while attempt < max_attempts:
    task = client.tasks.retrieve(task_id)
    
    if task.status == 'SUCCEEDED':
        print(f"Done: {task.output[0]}")
        break
    elif task.status == 'FAILED':
        print(f"Failed: {task.failure_code}")
        break
    elif task.status in ['THROTTLED', 'PENDING', 'QUEUED', 'RUNNING']:
        # Exponential backoff: 2^attempt seconds, capped at 30s
        wait_time = min(2 ** attempt + (random.random() * 2 ** attempt), 30)
        print(f"Status: {task.status}, waiting {wait_time:.1f}s...")
        time.sleep(wait_time)
        attempt += 1
    else:
        print(f"Unexpected status: {task.status}")
        break

if attempt >= max_attempts:
    print("Polling timeout after 100 attempts")
```

### Recommended Polling Interval

- Start with 5 seconds between polls.
- Use exponential backoff with jitter: `min(2^n + random(0, 2^n), 30)` seconds.
- Max wait between polls: 30 seconds.
- Timeout: 10 minutes (SDKs default), but set explicitly for hackathon: 5–15 minutes.

### SDK Built-In Polling (Preferred)

```python
from runwayml import RunwayML, TaskFailedError, TaskTimeoutError

client = RunwayML()

try:
    task = client.image_to_video.create(...).wait_for_task_output(
        timeout=5 * 60  # 5 minutes
    )
    print(f"Output: {task.output[0]}")
except TaskFailedError as e:
    print(f"Task failed: {e.task_details.failure_code}")
except TaskTimeoutError:
    print("Task timed out after 5 minutes")
```

---

## 4. Async vs. Sync Patterns

### Fire-and-Forget (Async)

Store task IDs and poll later or via webhook:

```python
# Submit many tasks immediately
task_ids = []
for i in range(10):
    task_id = (await client.image_to_video.create({
        model='gen4.5',
        prompt_text=f'Prompt {i}',
        ratio='1280:720',
        duration=5,
    })).id
    task_ids.append(task_id)

# Poll later (e.g., in a separate job queue)
for task_id in task_ids:
    task = client.tasks.retrieve(task_id)
    if task.status == 'SUCCEEDED':
        print(f"Task {task_id} done: {task.output[0]}")
```

### Polling via Webhook (Svix Integration)

Runway does not natively provide webhook support via the API, but you can:
1. Use a third-party service like Svix to manage webhook subscriptions.
2. Set up your own webhook endpoint on your server.
3. When creating a task, do NOT wait; store the task ID.
4. In your webhook, poll the Runway API for task status and process the output.

**Hackathon Strategy:** For 72 hours, polling with exponential backoff is simpler than setting up webhooks. Use polling.

### Concurrency Limits by Tier

| Tier | Max Concurrent (per model) | Max Gens/Day | Max Monthly Spend |
|------|---------------------------|-------------|------------------|
| 1 | 1 video, 2 image, 1 real-time | 50 / 200 / 50 | $100 |
| 2 | 3 / 3 / 3 | 500 / 1,000 / 500 | $500 |
| 3 | 5 / 5 / 5 | 1,000 / 2,000 / 1,000 | $2,000 |
| 4 | 10 / 10 / 10 | 5,000 / 10,000 / 5,000 | $20,000 |
| 5 | 20 / 20 / 20 | 25,000 / 30,000 / 25,000 | $100,000 |

**Key:** All video models share concurrency limits. Submit all tasks at once; Runway queues them automatically. No rate-limit retries needed—the API queues beyond your concurrency slot.

---

## 5. Output URLs & Expiry

### Output URL Format

```json
{
  "id": "task-uuid",
  "status": "SUCCEEDED",
  "output": ["https://dnznrvs05pmza.cloudfront.net/output.mp4?_jwt=eyJhbGc..."]
}
```

The URL includes a JWT token in the query string for authentication.

### Expiry & Download Strategy

- **Expiry window:** 24–48 hours after first access.
- **Strategy:** Download immediately after task succeeds. Do not rely on keeping URLs around.
- **Error on expiry:** 401 Unauthorized or 403 Forbidden.

**Python Download Example:**
```python
import requests
from pathlib import Path

task = client.image_to_video.create(...).wait_for_task_output()

output_url = task.output[0]

# Download immediately
response = requests.get(output_url, stream=True)
response.raise_for_status()

output_path = Path('output.mp4')
with open(output_path, 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

print(f"Saved to {output_path}")
```

---

## 6. Reference Images & Video Inputs

### Supported Input Formats

**Images:**
- JPEG (`image/jpg` or `image/jpeg`)
- PNG (`image/png`)
- WebP (`image/webp`)
- NOT supported: GIF

**Videos:**
- MP4 (H.264, H.265, AV1) — `video/mp4`
- QuickTime MOV (H.264, H.265, ProRes) — `video/quicktime`
- Matroska MKV (H.264, H.265, VP8, VP9, AV1) — `video/x-matroska`
- WebM (VP8, VP9, AV1) — `video/webm`
- 3GPP (H.264) — `video/3gpp`
- Ogg (Theora) — `video/ogg`

**Audio:**
- MP3 — `audio/mpeg` or `audio/mp3`
- WAV (PCM) — `audio/wav`, `audio/wave`, `audio/x-wav`
- FLAC — `audio/flac`, `audio/x-flac`
- M4A (AAC, ALAC) — `audio/mp4`, `audio/x-m4a`
- AAC — `audio/aac`, `audio/x-aac`

### Size Limits

| Input | URL Limit | Data URI Limit | Ephemeral Upload |
|-------|-----------|----------------|------------------|
| Image | 16 MB | 5 MB | 200 MB |
| Video | 32 MB | 16 MB | 200 MB |
| Audio | 32 MB | 16 MB | 200 MB |

### URL Requirements

1. Must be HTTPS (not HTTP).
2. Must reference a domain name, not an IP address.
3. Server must respond with valid `Content-Type` and `Content-Length` headers.
4. No redirects (3XX responses fail).
5. Max URL length: 2048 chars.
6. Server must support HTTP `HEAD` requests.
7. User-Agent will be `RunwayML API/...`—allowlist if using WAF/anti-scrape.

### Data URI Format

```
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==
```

Base64-encoding increases size by ~33%. To fit in 5 MB limit, binary file must be ≤3.3 MB.

### Aspect Ratio Constraints

| Model | Input Type | Min Ratio | Max Ratio |
|-------|-----------|-----------|-----------|
| Gen-4.5 Image-to-Video | Prompt image | 0.5 | 2.0 |
| Gen-4 Turbo / Gen-4 | Image | 0.5 | 2.358 |
| Gen-4 Aleph | Video | 0.5 | 2.358 |
| Act-Two | Character image | 0.5 | 2.358 |
| Veo 3 / 3.1 / 3.1 Fast | Image | 0.5 | 2.0 |
| Gemini 2.5 Flash | Reference | 0.25 | 4.0 |

**Example:** A 1920×1080 image has ratio 1.778 (1920÷1080). For Gen-4.5, this falls within 0.5–2.0. ✓

### Using Reference Images in Prompts

Tag a reference image and mention it in the prompt:

```python
task = client.text_to_image.create(
    model='gen4_image',
    prompt_text='@EiffelTower in the style of @StarryNight',
    reference_images=[
        {
            'uri': 'https://example.com/eiffel.jpg',
            'tag': 'EiffelTower',
        },
        {
            'uri': 'https://example.com/starry.jpg',
            'tag': 'StarryNight',
        },
    ],
    ratio='1920:1080',
).wait_for_task_output()
```

---

## 7. Avatars CRUD Lifecycle

### Create an Avatar

**SDK Method:**
- Node: `client.avatars.create({})`
- Python: `client.avatars.create()`

**Parameters:**

| Parameter | Type | Required | Notes |
|-----------|------|----------|-------|
| `name` | string | yes | Avatar name (max 100 chars). |
| `reference_image` or `referenceImage` | URL or data URI | yes | Single image of the avatar. Aspect ratio recommended 1088×704. |
| `voice` | object | yes | Voice config (see below). |
| `personality` | string | yes | System prompt for the avatar (max 10,000 chars). |
| `start_script` or `startScript` | string | no | Opening message (max 2000 chars). |
| `document_ids` or `documentIds` | array | no | Knowledge base documents to attach. |

**Voice Configuration:**

**Preset voice:**
```python
voice={
    'type': 'runway-live-preset',
    'preset_id': 'clara',  # or: victoria, vincent, etc.
}
```

**Custom voice:**
```python
voice={
    'type': 'custom',
    'id': 'voice-uuid',  # from client.voices.create()
}
```

**Python Example:**
```python
avatar = client.avatars.create(
    name='Support Agent',
    reference_image='https://example.com/agent.png',
    voice={
        'type': 'runway-live-preset',
        'preset_id': 'clara',
    },
    personality='You are a helpful customer support agent for Acme Corp. Answer questions clearly and professionally.',
    start_script='Hello! How can I help you today?',
)

print(f"Avatar ID: {avatar.id}")
print(f"Avatar Status: {avatar.status}")
```

### Avatar Status Lifecycle

| Status | Description |
|--------|-------------|
| `PROCESSING` | Avatar image is being processed. Poll until `READY`. |
| `READY` | Avatar is ready to use. |
| `FAILED` | Avatar creation failed. Check `failure_reason`. |

### Retrieve an Avatar

```python
avatar = client.avatars.retrieve(avatar_id='uuid-here')
print(avatar.name, avatar.status)
```

### Update an Avatar

```python
client.avatars.update(
    avatar_id='uuid-here',
    name='Updated Name',
    personality='New system prompt...',
    voice={
        'type': 'runway-live-preset',
        'preset_id': 'victoria',
    },
)
```

### List Avatars

```python
for avatar in client.avatars.list():
    print(f"{avatar.name}: {avatar.status}")
```

### Delete an Avatar

```python
client.avatars.delete(avatar_id='uuid-here')
```

### Avatar Voice: 30+ Preset Options

| Preset ID | Name | Style |
|-----------|------|-------|
| `clara` | Clara | Soft, approachable |
| `victoria` | Victoria | Firm, professional |
| `vincent` | Vincent | Knowledgeable, authoritative |
| `adam` | Adam | Friendly, casual |
| (... 26 more presets) | | |

Cycle through in the Developer Portal to preview voices.

---

## 8. Custom Voices

### Create a Voice from Text Prompt

```python
voice = client.voices.create(
    name='Brand Ambassador',
    from_={
        'type': 'text',
        'prompt': 'A warm, friendly voice with a slight British accent. Speaks at a measured pace with a professional yet approachable tone.',
        'model': 'eleven_ttv_v3',  # or eleven_multilingual_ttv_v2
    },
)

print(f"Voice ID: {voice.id}")
print(f"Voice Status: {voice.status}")  # PROCESSING, READY, or FAILED
```

### Clone a Voice from Audio

```python
voice = client.voices.create(
    name='CEO Clone',
    from_={
        'type': 'audio',
        'audio': 'https://example.com/voice-sample.mp3',  # 10s–5m, max 10 MB
    },
)
```

Audio requirements:
- Duration: 10 seconds to 5 minutes
- Size: Max 10 MB
- Quality: Clear, minimal background noise, varied tone

### Poll for Voice Status

```python
voice = client.voices.retrieve(voice_id='uuid-here')

if voice.status == 'READY':
    print(f"Preview: {voice.preview_url}")
elif voice.status == 'PROCESSING':
    print("Still processing...")
elif voice.status == 'FAILED':
    print(f"Failed: {voice.failure_reason}")
```

### Assign Custom Voice to Avatar

```python
# Update existing avatar
client.avatars.update(
    avatar_id='avatar-uuid',
    voice={
        'type': 'custom',
        'id': 'voice-uuid',
    },
)

# Or create new avatar with custom voice
avatar = client.avatars.create(
    name='Custom Voice Agent',
    reference_image='https://example.com/agent.png',
    voice={
        'type': 'custom',
        'id': 'voice-uuid',
    },
    personality='You are an AI agent with a custom voice...',
)
```

### List Custom Voices

```python
for voice in client.voices.list():
    print(f"{voice.name}: {voice.status}")
```

---

## 9. Knowledge Base (Documents)

### Create a Document

```python
document = client.documents.create(
    name='Product FAQ',
    content="""# Product FAQ

## What is your return policy?
We offer a 30-day return policy on all items...

## How do I track my order?
You can track your order using the tracking number..."""
)

print(f"Document ID: {document.id}")
```

Supported formats: Plain text, Markdown.

### Update a Document

```python
client.documents.update(
    id=document_id,
    name='Updated Product FAQ',
    content='New content here...',
)
```

Both `name` and `content` are optional—update only what you need.

### Attach Document to Avatar

```python
client.avatars.update(
    avatar_id='avatar-uuid',
    document_ids=[document_id],  # Replaces existing documents
)
```

### List Documents

```python
for doc in client.documents.list():
    print(f"{doc.name}: {doc.id}")
```

### Delete a Document

```python
client.documents.delete(document_id)
```

---

## 10. Real-Time Sessions (Advanced)

### Session Lifecycle

1. **Create:** `client.realtime_sessions.create({})`
2. **Poll:** Check status until `READY`.
3. **Connect:** Use `sessionKey` to establish WebRTC.
4. **Converse:** Exchange audio/video over WebRTC.
5. **Disconnect:** Session auto-ends after 5 minutes or explicit close.

### Creating a Session

```python
session = client.realtime_sessions.create(
    model='gwm1_avatars',
    avatar={
        'type': 'custom',
        'avatar_id': 'avatar-uuid',
    },
    personality='Custom personality override (optional)',
    start_script='Custom opening (optional)',
).wait_for_task_output()

print(f"Session Key: {session.session_key}")
print(f"Session ID: {session.id}")
```

### Per-Call Overrides

Without modifying the avatar itself, customize each call:

```python
session = client.realtime_sessions.create(
    model='gwm1_avatars',
    avatar={'type': 'custom', 'avatar_id': 'avatar-uuid'},
    personality=f"""You are a customer support agent.
The customer's name is {user_name} and they are on the {user_plan} plan.
Address them by name.""",
    start_script=f"Hi {user_name}! How can I help?",
).wait_for_task_output()
```

### Session Status Polling

```python
import time

session_id = (await client.realtime_sessions.create(...)).id

while True:
    session = client.realtime_sessions.retrieve(session_id)
    
    if session.status == 'READY':
        print(f"Connect with: {session.session_key}")
        break
    elif session.status == 'FAILED':
        print(f"Failed: {session.failure}")
        break
    
    time.sleep(2)
```

### Max Duration

Sessions expire after **5 minutes** of conversation. Plan accordingly.

### Recording & Transcripts

After a session completes:

```python
conversation = client.avatars.conversations.retrieve(
    avatar_id='avatar-uuid',
    conversation_id=session_id,
)

print(f"Transcript: {conversation.transcript}")
print(f"Recording URL: {conversation.recording_url}")
```

The recording URL is temporary (expires quickly). Download immediately if needed.

---

## 11. Content Moderation System

### Moderation Approach

Runway flags requests that violate policy **before** generation. Default moderation is `'auto'`.

**Blocked categories:**
- Violent, graphic, or hateful content
- Sexual or adult content
- Child safety violations
- Illegal activities
- Non-consensual intimate imagery

### Customizing Moderation

By default, Runway blocks recognizable public figures. To relax this:

```python
task = client.text_to_image.create(
    model='gen4_image',
    prompt_text='A portrait of Albert Einstein',
    ratio='1920:1080',
    content_moderation={
        'level': 'lenient',  # Allow public figures
    },
).wait_for_task_output()
```

**Levels:**
- `'auto'` (default): Standard safety filtering.
- `'lenient'`: Allow recognizable public figures.

### Moderation Failures

If rejected, task status is `FAILED` with `failureCode` like:
- `SAFETY.INPUT.TEXT` — Text prompt rejected.
- `SAFETY.INPUT.IMAGE` — Image input rejected.
- `SAFETY.OUTPUT.*` — Output rejected by safety systems.

**Do not retry** safety failures—they'll fail again. Modify your prompt instead.

### Cost of Moderation

Moderated generations (rejected before running) are **free**—no credits charged.

### Account Suspension

Too many moderation violations → account suspension. Can appeal via [help.runwayml.com](https://help.runwayml.com/hc/en-us/articles/21667383978003-How-can-I-appeal-my-account-s-suspension).

---

## 12. Tier Limits & Concurrency

### Concurrency Limits (per tier)

All video generation models (gen4.5, gen4_turbo, gen4_aleph, veo3, etc.) share the same concurrency limit. All image models share a separate limit.

**Example: Tier 1**
- Max 1 concurrent video generation (across all video models)
- Max 2 concurrent image generations (across all image models)
- Max 1 concurrent real-time session

**Example: Tier 3**
- Max 5 concurrent video generations
- Max 5 concurrent image generations
- Max 5 concurrent real-time sessions

### Daily Generation Limits

Separate limits for video, image, and character:

| Tier | Video / Day | Image / Day | Character / Day |
|------|------------|-----------|-----------------|
| 1 | 50 | 200 | 50 |
| 2 | 500 | 1,000 | 500 |
| 3 | 1,000 | 2,000 | 1,000 |
| 4 | 5,000 | 10,000 | 5,000 |
| 5 | 25,000 | 30,000 | 25,000 |

Limits reset on a **rolling 24-hour window** (not midnight UTC).

### Monthly Spend Cap

Once you hit the monthly cap, autobilling is prevented. You must manually add credits.

### No Rate-Limit for Submissions

There is **no maximum requests-per-minute limit**. Submit as many tasks as you want; they queue automatically within your concurrency slot.

---

## 13. Pricing Matrix & Cost Examples

### Video Model Costs

| Model | Cost | Example: 5s Video | Example: 10s Video |
|-------|------|-------------------|-------------------|
| gen4.5 | 12 credits/sec | 60 credits ($0.60) | 120 credits ($1.20) |
| gen4_turbo | 5 credits/sec | 25 credits ($0.25) | 50 credits ($0.50) |
| gen4_aleph | 15 credits/sec | 75 credits ($0.75) | 150 credits ($1.50) |
| veo3 | 40 credits/sec | 200 credits ($2.00) | 400 credits ($4.00) |
| veo3.1 (audio) | 40 credits/sec | 200 credits ($2.00) | 400 credits ($4.00) |
| veo3.1 (no audio) | 20 credits/sec | 100 credits ($1.00) | 200 credits ($2.00) |
| veo3.1_fast (audio) | 15 credits/sec | 75 credits ($0.75) | 150 credits ($1.50) |
| veo3.1_fast (no audio) | 10 credits/sec | 50 credits ($0.50) | 100 credits ($1.00) |

### Image Model Costs

| Model | Cost |
|-------|------|
| gen4_image | 5 credits (720p), 8 credits (1080p) |
| gen4_image_turbo | 2 credits (any resolution) |
| gemini_image3_pro | 20 credits (1K–2K), 40 credits (4K) |
| gpt_image_2 (low) | 1 credit (1K–2K), 2 credits (4K) |
| gpt_image_2 (medium) | 5 credits (1K–2K), 11 credits (4K) |
| gpt_image_2 (high) | 20 credits (1K–2K), 41 credits (4K) |
| gemini_2.5_flash | 5 credits (any resolution) |

### Audio Model Costs

| Model | Cost |
|-------|------|
| eleven_multilingual_v2 | 1 credit per 50 characters |
| eleven_text_to_sound_v2 | 1 credit per 6 seconds (if duration provided: 1 credit/sec) |
| eleven_voice_isolation | 1 credit per 6 seconds |
| eleven_voice_dubbing | 1 credit per 2 seconds |
| eleven_multilingual_sts_v2 | 1 credit per 3 seconds |

### Real-Time Avatar Costs

| Model | Cost |
|-------|------|
| gwm1_avatars | 2 credits upfront + 2 credits per 6 seconds |

**Example:** A 5-minute session = 2 + (2 × 50 frames @ 6s per credit) = ~35 credits ($0.35) approximately.

### Bulk Generation Example (Hackathon)

Scenario: Generate 10 images + 5 videos + 2 custom avatars in 72 hours.

```
10 × gen4_image_turbo @ 1080p      = 10 × 8 = 80 credits
5 × gen4.5 @ 5 sec                 = 5 × 60 = 300 credits
2 × gwm1_avatars (2 min each)      = 2 × (2 + 2 × 20) = 88 credits

Total: ~470 credits = $4.70

Budget: $100 buys 10,000 credits—plenty for hackathon.
```

---

## 14. Common Error Codes & Fixes

### HTTP Status Codes

| Code | Name | Cause | Retry? | Fix |
|------|------|-------|--------|-----|
| 400 | Bad Request | Invalid parameter | No | Check parameter names (snake_case vs camelCase), values, format. |
| 401 | Unauthorized | Invalid API key | No | Verify `RUNWAYML_API_SECRET` is set and correct. |
| 402 | Payment Required | Out of credits | No | Add credits in developer portal. Check monthly spend cap. |
| 404 | Not Found | Task/avatar/document ID doesn't exist | No | Verify ID is correct. Task may have been deleted. |
| 405 | Method Not Allowed | Wrong HTTP method | No | Use POST for creation, GET for retrieval, etc. |
| 429 | Too Many Requests | Rate limit or concurrency exceeded | Yes | Implement exponential backoff. Check tier concurrency limits. |
| 502 | Bad Gateway | Runway shedding load | Yes | Retry with exponential backoff + jitter. |
| 503 | Service Unavailable | Runway maintenance/overload | Yes | Retry. Wait up to 5 min. |
| 504 | Gateway Timeout | Request took too long | Yes | Retry. Runway may be saturated. |

### Task Failure Codes

| Code | Meaning | Retryable | Action |
|------|---------|-----------|--------|
| `SAFETY.INPUT.TEXT` | Prompt rejected | No | Modify prompt, resubmit. |
| `SAFETY.INPUT.IMAGE` | Image rejected | No | Use different image or modify prompt. |
| `SAFETY.OUTPUT.*` | Output failed moderation | No | Modify prompt. |
| `INPUT_PREPROCESSING.SAFETY.TEXT` | Text safety check failed | No | Same as SAFETY.INPUT.TEXT. |
| `INPUT_PREPROCESSING.INTERNAL` | Moderation service error | Yes | Retry with delay. |
| `ASSET.INVALID` | Image/video dimensions, duration, or format invalid | No | Resize image, trim video, check formats. |
| `INTERNAL.BAD_OUTPUT.01` | Quality/system error | Yes | Retry. Common: logos in input, text generation requests. |
| `INTERNAL` or null | Generic internal error | Yes | Retry with exponential backoff + jitter. |

### Retry Strategy (Exponential Backoff)

```python
import random
import time

def retry_task(task_fn, max_attempts=5):
    for attempt in range(max_attempts):
        try:
            return task_fn()
        except Exception as e:
            if attempt >= max_attempts - 1:
                raise
            
            # Exponential backoff: 2^attempt ± jitter
            wait = 2 ** attempt + random.uniform(0, 2 ** attempt)
            print(f"Attempt {attempt + 1} failed. Waiting {wait:.1f}s...")
            time.sleep(wait)
```

### Parameter Name Pitfalls

SDK methods use **snake_case**, but the **REST API uses camelCase**. The SDKs handle conversion.

**Python (snake_case):**
```python
client.image_to_video.create(
    prompt_text='...',
    prompt_image='...',
    duration_seconds=5,
)
```

**Node.js (camelCase):**
```javascript
client.imageToVideo.create({
    promptText: '...',
    promptImage: '...',
    durationSeconds: 5,
})
```

**REST API (camelCase):**
```bash
curl -X POST https://api.dev.runwayml.com/v1/image_to_video \
  -H "Authorization: Bearer key_xxx" \
  -d '{
    "promptText": "...",
    "promptImage": "...",
    "durationSeconds": 5
  }'
```

---

## 15. Hackathon Recipes

### Recipe 1: Multi-Shot Video Pipeline (Chained Generation + Aleph)

Goal: Generate image → image-to-video → video transform → final output.

```python
from runwayml import RunwayML

client = RunwayML()

# Step 1: Generate hero image
print("Step 1: Generating hero image...")
image_task = client.text_to_image.create(
    model='gen4_image',
    prompt_text='A cinematic establishing shot of a futuristic city at dawn',
    ratio='1920:1080',
).wait_for_task_output()

hero_image = image_task.output[0]
print(f"Hero image: {hero_image}")

# Step 2: Animate the image
print("Step 2: Animating image to video...")
video_task = client.image_to_video.create(
    model='gen4.5',
    prompt_image=hero_image,
    prompt_text='Camera slowly panning across the city skyline',
    ratio='1280:720',
    duration=5,
).wait_for_task_output()

base_video = video_task.output[0]
print(f"Base video: {base_video}")

# Step 3: Transform with Aleph
print("Step 3: Transforming video with Aleph...")
final_task = client.video_to_video.create(
    model='gen4_aleph',
    prompt_video=base_video,
    prompt_text='Apply a cinematic color grade with warm tones and film grain',
    ratio='1280:720',
).wait_for_task_output()

final_video = final_task.output[0]
print(f"Final video: {final_video}")

# Download all outputs
import requests
for i, url in enumerate([hero_image, base_video, final_video]):
    resp = requests.get(url)
    filename = ['hero.png', 'base.mp4', 'final.mp4'][i]
    with open(filename, 'wb') as f:
        f.write(resp.content)
    print(f"Downloaded {filename}")
```

**Cost:** ~$1.50 (image + 2 × video). **Time:** ~90 seconds.

---

### Recipe 2: Custom Avatar from Generated Portrait

Goal: Generate a portrait → Create avatar from portrait → Talk to avatar.

```python
# Step 1: Generate portrait
print("Generating avatar portrait...")
portrait_task = client.text_to_image.create(
    model='gen4_image_turbo',
    prompt_text='A professional headshot of a friendly woman with warm eyes, styled business casual',
    ratio='1920:1080',
).wait_for_task_output()

portrait_url = portrait_task.output[0]

# Step 2: Create avatar
print("Creating avatar...")
avatar = client.avatars.create(
    name='Generated Support Agent',
    reference_image=portrait_url,
    voice={
        'type': 'runway-live-preset',
        'preset_id': 'clara',
    },
    personality='You are a friendly and knowledgeable customer support representative. Always greet the user warmly and ask how you can help.',
    start_script='Hello! Welcome. I\'m here to assist you. What can I help you with today?',
)

print(f"Avatar created: {avatar.id}")
print(f"Avatar status: {avatar.status}")

# Step 3: Start a session
print("Starting realtime session...")
session = client.realtime_sessions.create(
    model='gwm1_avatars',
    avatar={'type': 'custom', 'avatar_id': avatar.id},
).wait_for_task_output()

print(f"Session key: {session.session_key}")
```

**Cost:** ~$2 (portrait + avatar setup). **Time:** ~2–3 minutes (avatar processing).

---

### Recipe 3: Voice Cloning + Multilingual Dubbing

Goal: Clone user's voice → dub a generated video into 3 languages.

```python
# Step 1: Clone voice from audio sample
print("Cloning voice...")
voice = client.voices.create(
    name='My Custom Voice',
    from_={
        'type': 'audio',
        'audio': 'https://example.com/my-voice-sample.mp3',  # 10s–5m
    },
).wait_for_task_output()

print(f"Voice ID: {voice.id}, Status: {voice.status}")

# Step 2: Generate a video with text
print("Generating video...")
video_task = client.image_to_video.create(
    model='gen4.5',
    prompt_text='A person speaking to the camera in a professional setting',
    ratio='1280:720',
    duration=10,
).wait_for_task_output()

video_url = video_task.output[0]

# Step 3: Create narration in original voice
print("Creating original narration...")
narration_task = client.text_to_speech.create(
    model='eleven_multilingual_v2',
    prompt_text='Welcome to our product. This revolutionary software will change how you work.',
    voice={'type': 'custom', 'id': voice.id},
    language='en',
).wait_for_task_output()

en_audio = narration_task.output[0]

# Step 4: Dub into Spanish and French
print("Dubbing into Spanish and French...")
es_dub_task = client.voice_dubbing.create(
    model='eleven_voice_dubbing',
    audio=en_audio,
    target_language='es',
).wait_for_task_output()

fr_dub_task = client.voice_dubbing.create(
    model='eleven_voice_dubbing',
    audio=en_audio,
    target_language='fr',
).wait_for_task_output()

print(f"English: {en_audio}")
print(f"Spanish: {es_dub_task.output[0]}")
print(f"French: {fr_dub_task.output[0]}")
```

**Cost:** ~$2–3. **Time:** ~2 minutes.

---

### Recipe 4: Real-Time Avatar with Knowledge Base

Goal: Create a support avatar trained on FAQs, then start a live session.

```python
# Step 1: Create knowledge base
print("Creating knowledge base...")
faq_doc = client.documents.create(
    name='Product FAQ',
    content="""# Our Product FAQ

## What is your pricing?
We offer three tiers: Starter ($9/mo), Professional ($29/mo), and Enterprise (custom).

## Do you offer refunds?
Yes, we offer a 30-day money-back guarantee.

## How can I contact support?
Email support@example.com or live chat on our website."""
)

print(f"Document created: {faq_doc.id}")

# Step 2: Create avatar
print("Creating avatar...")
avatar = client.avatars.create(
    name='Support Agent with Knowledge',
    reference_image='https://example.com/agent.png',
    voice={'type': 'runway-live-preset', 'preset_id': 'victoria'},
    personality='You are a knowledgeable and friendly support representative. Use your knowledge base to answer questions accurately. If you don\'t know the answer, offer to escalate.',
    start_script='Hello! I\'m your support agent. What can I help you with today?',
    document_ids=[faq_doc.id],
)

print(f"Avatar created: {avatar.id}")

# Step 3: Start realtime session
print("Starting session...")
session = client.realtime_sessions.create(
    model='gwm1_avatars',
    avatar={'type': 'custom', 'avatar_id': avatar.id},
).wait_for_task_output()

print(f"Session ready: {session.session_key}")
```

**Cost:** ~$2. **Time:** ~2–3 minutes.

---

### Recipe 5: Sound Design Layer (Audio Effects + Voice Processing)

Goal: Generate sound effects → add voice narration → isolate clean voice.

```python
# Step 1: Generate sound effects
print("Generating sound effects...")
sfx_task = client.sound_effect.create(
    model='eleven_text_to_sound_v2',
    prompt_text='A futuristic whoosh sound, like a spaceship passing by',
    duration_seconds=3,
).wait_for_task_output()

sfx_url = sfx_task.output[0]
print(f"SFX: {sfx_url}")

# Step 2: Generate narration
print("Generating narration...")
narration_task = client.text_to_speech.create(
    model='eleven_multilingual_v2',
    prompt_text='Welcome to the future of technology.',
    voice={'type': 'runway-live-preset', 'preset_id': 'brian'},
    language='en',
).wait_for_task_output()

narration_url = narration_task.output[0]
print(f"Narration: {narration_url}")

# Step 3: If you have a noisy recording, clean it
print("Isolating clean voice from noisy recording...")
isolation_task = client.voice_isolation.create(
    model='eleven_voice_isolation',
    audio='https://example.com/noisy-recording.mp3',
).wait_for_task_output()

clean_voice_url = isolation_task.output[0]
print(f"Clean voice: {clean_voice_url}")

# Now you have:
# - sfx_url: sound effects
# - narration_url: clean narration
# - clean_voice_url: processed voice
# Combine in your video editor or DAW
```

**Cost:** ~$1–2. **Time:** ~30 seconds.

---

## 16. Recent Changelog (Last 60 Days)

### Major Updates (May 2026–April 2026)

- **April 30, 2026:** Gemini 3 Pro Image (`gemini_image3_pro`) launched. Supports up to 5,500-char prompts, 14 reference images, 1K–4K resolutions.
- **April 23, 2026:** GPT Image 2 (`gpt_image_2`) launched. OpenAI's latest, supports 16 reference images, 30 aspect ratios, tiered pricing by quality/resolution.
- **February 10, 2026:** Gen-4.5 released. New SOTA video model, text-to-video and image-to-video, 2–10 second duration, better quality and control than gen4_turbo.

### Audio Updates

- **October 16, 2025:** ElevenLabs Voice Isolation and Voice Dubbing added to Runway API.
- **October 8, 2025:** ElevenLabs Text-to-Sound Effects (v2) launched.
- **September 25, 2025:** ElevenLabs Multilingual v2 Text-to-Speech integrated.

### Other Highlights

- **August 19, 2025:** Gen-4 Image Turbo launched (2–4x cheaper, 93.3% quality vs. standard).
- **August 1, 2025:** Aleph (gen4_aleph) video-to-video model released.
- **July 21, 2025:** Act-Two (act_two) motion capture model added.
- **June 13, 2025:** Runway MCP Server (for Claude AI) released on GitHub.
- **May 16, 2025:** Gen-4 Image added to Runway API.

---

## 17. Troubleshooting Checklist

### Before Submitting a Generation

- [ ] API key set in `RUNWAYML_API_SECRET` environment variable
- [ ] All URLs are HTTPS (not HTTP)
- [ ] Content-Type headers returned by your servers (if using URLs)
- [ ] Input image/video dimensions within supported aspect ratios
- [ ] Prompt text under 5500 chars (for image) or 1000 chars (for video)
- [ ] Model name correct: `'gen4.5'` not `'gen4'` or `'generation-4.5'`
- [ ] SDK method uses correct snake_case (Python) or camelCase (Node)
- [ ] Credits available in your account (Tier and daily limits)
- [ ] Concurrency slot available (check tier limits)

### If Task Fails

1. Check `failureCode`:
   - `SAFETY.*` → Modify prompt, don't retry
   - `INPUT_PREPROCESSING.INTERNAL` → Retry with delay
   - `ASSET.INVALID` → Fix dimensions/format
   - `INTERNAL.*` → Retry with exponential backoff
2. Verify inputs:
   - Image format is JPEG/PNG/WebP (not GIF)
   - Video codec is H.264/H.265/AV1
   - Aspect ratio within constraints
3. Check moderation:
   - Avoid recognizable public figures (unless `contentModeration.level: 'lenient'`)
   - Avoid violent/hateful content, etc.
4. If still failing, check the Runway status page for service issues.

### If Polling Stalls

- Task stuck in `PENDING` or `RUNNING` for >5 min: Check Runway status page.
- Task stuck in `THROTTLED`: You've hit concurrency limit. Wait for slots to free.
- 429 errors: Implement exponential backoff. Don't retry immediately.

### If API Key Fails

```
401 Unauthorized: The provided API key is not valid.
```

- Verify key format: `key_` prefix + alphanumerics
- Copy from developer portal again (only shown once)
- Check env var: `echo $RUNWAYML_API_SECRET` (macOS/Linux) or `echo %RUNWAYML_API_SECRET%` (Windows)

---

## 18. Quick Reference: SDK Method Mapping

| Operation | Endpoint | Python | Node |
|-----------|----------|--------|------|
| Text-to-Image | POST /v1/text_to_image | `client.text_to_image.create()` | `client.textToImage.create()` |
| Image-to-Video | POST /v1/image_to_video | `client.image_to_video.create()` | `client.imageToVideo.create()` |
| Video-to-Video | POST /v1/video_to_video | `client.video_to_video.create()` | `client.videoToVideo.create()` |
| Character Performance | POST /v1/character_performance | `client.character_performance.create()` | `client.characterPerformance.create()` |
| Text-to-Speech | POST /v1/text_to_speech | `client.text_to_speech.create()` | `client.textToSpeech.create()` |
| Sound Effect | POST /v1/sound_effect | `client.sound_effect.create()` | `client.soundEffect.create()` |
| Voice Isolation | POST /v1/voice_isolation | `client.voice_isolation.create()` | `client.voiceIsolation.create()` |
| Voice Dubbing | POST /v1/voice_dubbing | `client.voice_dubbing.create()` | `client.voiceDubbing.create()` |
| Speech-to-Speech | POST /v1/speech_to_speech | `client.speech_to_speech.create()` | `client.speechToSpeech.create()` |
| Get Task | GET /v1/tasks/{id} | `client.tasks.retrieve(id)` | `client.tasks.retrieve(id)` |
| Create Avatar | POST /v1/avatars | `client.avatars.create()` | `client.avatars.create()` |
| Get Avatar | GET /v1/avatars/{id} | `client.avatars.retrieve(id)` | `client.avatars.retrieve(id)` |
| Update Avatar | PUT /v1/avatars/{id} | `client.avatars.update(id, {})` | `client.avatars.update(id, {})` |
| List Avatars | GET /v1/avatars | `client.avatars.list()` | `client.avatars.list()` |
| Create Voice | POST /v1/voices | `client.voices.create()` | `client.voices.create()` |
| Get Voice | GET /v1/voices/{id} | `client.voices.retrieve(id)` | `client.voices.retrieve(id)` |
| Create Document | POST /v1/documents | `client.documents.create()` | `client.documents.create()` |
| Update Document | PUT /v1/documents/{id} | `client.documents.update(id, {})` | `client.documents.update(id, {})` |
| Create Realtime Session | POST /v1/realtime_sessions | `client.realtime_sessions.create()` | `client.realtimeSessions.create()` |
| Create Ephemeral Upload | POST /v1/uploads | `client.uploads.create_ephemeral(file)` | `client.uploads.createEphemeral(file)` |

---

## 19. Gotchas & Pro Tips

### Gotcha 1: Output URLs Expire in 24–48 Hours

**Problem:** You generate a video, save the URL, come back 3 days later to download it—404.

**Fix:** Download immediately after generation succeeds. Store the binary in your own cloud (S3, GCS, etc.), not just the URL.

### Gotcha 2: Reference Images Don't Use the `@tag` in URLs

**Problem:** You pass `{ 'uri': 'data:image/png;base64,...', 'tag': 'hero' }` but forget to use `@hero` in the prompt.

**Fix:** Always include `@tag` mentions in your prompt text if you want the model to reference the image.

### Gotcha 3: Parameter Names: Python Uses snake_case, Node Uses camelCase

**Problem:** You copy Node.js code and paste into Python without converting.

**Fix:** Python: `prompt_text`, `duration_seconds`. Node: `promptText`, `durationSeconds`. Rest API: camelCase.

### Gotcha 4: Video Aspect Ratio Auto-Crops

**Problem:** You pass a 2160×1440 image to gen4.5 with ratio `'1280:720'`. You expect the full image in the output.

**Fix:** Runway auto-crops from the center. Pre-crop your inputs or accept the crop.

### Gotcha 5: Moderation Failures Don't Refund Credits

**Problem:** You submit a prompt that gets rejected for safety. You check your balance—credits are gone.

**Fix:** Actually, moderation rejections are FREE. No credits charged if rejected before generation. Only pay if generation completes or is internally rejected (`INTERNAL.BAD_OUTPUT`).

### Gotcha 6: Task IDs Are Not Batch IDs

**Problem:** You submit 100 tasks in a loop. You store task IDs and expect to retrieve them as a batch later.

**Fix:** Task IDs are individual. You must poll each task separately or use a job queue. No batch retrieval endpoint.

### Pro Tip 1: Use `.wait_for_task_output()` in Python, `.waitForTaskOutput()` in Node

These built-in methods handle polling automatically. Don't write your own polling loop unless you need custom logic.

### Pro Tip 2: Concurrency Limits Are Per Organization, Not Per Model

If Tier 1 allows 1 concurrent video generation, you can't do gen4.5 + gen4_turbo simultaneously. Only 1 video model running at a time.

### Pro Tip 3: Seed for Reproducibility

Use the same `seed` value to reproduce an exact generation. Useful for testing or fine-tuning.

```python
task1 = client.image_to_video.create(
    model='gen4.5',
    prompt_text='A mountain sunrise',
    seed=42,
).wait_for_task_output()

# Exact same output
task2 = client.image_to_video.create(
    model='gen4.5',
    prompt_text='A mountain sunrise',
    seed=42,
).wait_for_task_output()

assert task1.output[0] == task2.output[0]  # Usually true
```

### Pro Tip 4: Pre-Filter Content Locally Before Sending

Don't rely on Runway's moderation for user inputs. Use your own content filter (e.g., OpenAI Moderation API) to reject bad input early and avoid account suspension.

---

## 20. Slack/Discord Help & Links

- **Developer Portal:** https://dev.runwayml.com/
- **API Docs (Full Reference):** https://docs.dev.runwayml.com/api
- **Help Center:** https://help.runwayml.com/
- **GitHub Skills & Examples:** https://github.com/runwayml/skills
- **Status Page:** Check for incidents before assuming your integration is broken

---

## Final Notes for Hackathon

- **72-hour window:** May 8–11, 2026. Use polling, not webhooks—simpler.
- **Tier 1 starting:** 1 concurrent video, 2 image, 50/day video, 200/day image. Upgrade if needed.
- **Cost discipline:** $100 buys 10,000 credits. A full brand film (image + 5 videos + 2 avatars + audio) costs ~$5–10. You're fine.
- **Error handling:** Implement exponential backoff for retries. Moderation rejections are free but will suspend your account if too many.
- **Download ASAP:** Output URLs expire. Download immediately after generation.

Good luck building.
