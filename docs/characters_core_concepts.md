# characters_core_concepts

Core Concepts | Runway API
- 
- 
- 
- 

- 
- 

- Skip to content Runway API 
 Search CtrlK Cancel 

 Copy Page 
 Open in Cursor 
 Open in ChatGPT 
 Open in Claude Docs API Reference 
Dev Portal

 Docs API Reference 
- Get Started 

- Create your account 
- Using the API 
- Models 
- Pricing 
- Go-live checklist 
- Playground ↗ 
- Characters 

- Overview 
- Quickstart 
- Custom Avatars 
- Core Concepts 
- Building Your Integration 
- Embedded Widget 
- Knowledge Base 
- Custom Voices 
- Tool calling 

- Overview 
- Client tools 
- Server tools 
- Best practices 
- Reference 
- Video Meeting 
- Camera and Screen Sharing 
- LiveKit Agents 
- Troubleshooting 
- React SDK ↗ 
- API details 

- SDKs 
- Inputs 
- Outputs 
- Uploads 
- Content moderation 
- Usage & Billing 

- Autobilling 
- Usage tiers 
- Attribution 
- Organizations and roles 
- Sample Apps 

- Web app: Hair makeover 
- Chrome extension: Generate video from any image 
- Chrome extension: Virtual try on 
- Figma plugin: Image and Video Generator 
- Errors 

- HTTP Errors 
- Task failures 
- Troubleshooting 
- API versions 

- Changelog 
- Overview 
- Version 2024-11-06 Theme Selector 

 Dark modeLight modeSystem default 
 On this page

- Overview 
- Avatars and Sessions 
- Session lifecycle 
- Creating a Character 
- Developer Portal 
- API 
- Per-call overrides 
- Reference image guidelines 
- Voice configuration 
- Conversation transcripts and recordings 

## On this page

- Overview 
- Avatars and Sessions 
- Session lifecycle 
- Creating a Character 
- Developer Portal 
- API 
- Per-call overrides 
- Reference image guidelines 
- Voice configuration 
- Conversation transcripts and recordings 

## Core Concepts

## Avatars and Sessions

Section titled “Avatars and Sessions”

Understanding the distinction between Avatars and Sessions is fundamental to building with the Characters API.

Avatars are persistent personas with a defined appearance, voice, and personality. Define your Avatar with a single reference image—any visual style works, from photorealistic humans to animated mascots to stylized brand characters. Configure voice, personality, knowledge base, and conversational actions.

Sessions are live WebRTC connections for real-time conversation. Each Session connects a user to an Avatar for a single interaction. Sessions have a maximum duration of 5 minutes.

## Session lifecycle

Section titled “Session lifecycle”

Sessions progress through a defined set of states:

- 
 ┌───────────┐ ┌──────────┤ NOT_READY ├──────────┐ │ └─────┬─────┘ │ │ │ │ ▼ ▼ ▼ CANCELLED READY FAILED ┌──┴──┐ │ │ ▼ ▼ RUNNING FAILED ┌──┴──┐ │ │ ▼ ▼ COMPLETED CANCELLED

StatusDescriptionNOT_READYSession is being provisioned. Poll until ready.READYSession is ready to connect. The sessionKey is available.RUNNINGWebRTC connection is active. The conversation is in progress.COMPLETEDSession ended normally after the conversation finished.FAILEDSession encountered an error. Check the failure field for details.CANCELLEDSession was explicitly cancelled before completion.

One-time consume
Session credentials can only be retrieved once. If the WebRTC connection fails after credentials are consumed, you must create a new Session.

## Creating a Character

Section titled “Creating a Character”

## Developer Portal

Section titled “Developer Portal”

The Developer Portal provides a visual interface for managing Characters:

- Go to the Characters tab

- Click Create a Character

- Define your Character with a single reference image

- Configure voice, personality, knowledge base, and conversational actions

- Preview and test before deploying

The portal also lets you preview available voices and access session recordings.

Portal = API
Everything you see in the Developer Portal can be done via the API. The portal is built on the same public API available to you.

## API

Section titled “API”

Create and manage Avatars programmatically for automated workflows or dynamic Avatar generation:

- Node 
- Python 
- 
import RunwayML from '@runwayml/sdk';
const client = new RunwayML();
const avatar = await client.avatars.create({ name: 'Support Agent', referenceImage: 'https://example.com/avatar.png', voice: { type: 'runway-live-preset', presetId: 'clara', }, personality: 'You are a helpful customer support agent...',}); 
from runwayml import RunwayML
client = RunwayML()
avatar = client.avatars.create( name='Support Agent', reference_image='https://example.com/avatar.png', voice={ 'type': 'runway-live-preset', 'preset_id': 'clara', }, personality='You are a helpful customer support agent...',) 

See the API reference for the complete list of Avatar management endpoints.

## Per-call overrides

Section titled “Per-call overrides”

The personality and startScript you set on an Avatar are defaults. When creating a Session, you can override either field to tailor the conversation for a specific caller — without modifying the Avatar itself.

If you omit these fields, the Avatar’s values are used as before. This is fully backward-compatible with existing integrations.

This is useful when you want to pass dynamic, user-specific context into each call. For example, a single support agent Avatar can greet every caller by name and adapt to their account details:

- Node 
- Python 
const session = await client.realtimeSessions.create({ model: 'gwm1_avatars', avatar: { type: 'custom', avatarId: 'your-avatar-id' }, personality: `You are a helpful support agent for Acme Corp.The customer's name is ${user.name} and they are on the ${user.plan} plan.Address them by name. Be aware of their plan limits when answering billing questions.`, startScript: `Hi ${user.name}! I'm your Acme support assistant. How can I help you today?`,}); 
session = client.realtime_sessions.create( model='gwm1_avatars', avatar={ 'type': 'custom', 'avatar_id': 'your-avatar-id' }, personality=f"""You are a helpful support agent for Acme Corp.The customer's name is {user['name']} and they are on the {user['plan']} plan.Address them by name. Be aware of their plan limits when answering billing questions.""", start_script=f"Hi {user['name']}! I'm your Acme support assistant. How can I help you today?",) 

FieldTypeDescriptionpersonalitystring (optional)Overrides the Avatar’s system prompt for this session. Max 10,000 characters.startScriptstring (optional)Overrides the Avatar’s opening message for this session. Max 2000 characters.

Provisioning time
Sessions created with personality or startScript overrides may take slightly longer to reach the READY state compared to sessions that use the Avatar’s defaults. Account for this in your polling logic.

## Reference image guidelines

Section titled “Reference image guidelines”

Generate expressive Avatars from a single image with zero fine-tuning required. For best results:

- Any visual style works: photorealistic humans, animated mascots, stylized brand characters

- Use high-quality images with good lighting

- Ensure the face is clearly visible and centered

- Avoid images with multiple people or obstructions

- Recommended aspect ratio: 1088×704

## Voice configuration

Section titled “Voice configuration”

Configure your Avatar’s voice using voice presets. Avatars support full conversational expressiveness including natural speech patterns and lip-syncing. Here are some examples:

Preset IDNameStyleclaraClaraSoft, approachablevictoriaVictoriaFirm, professionalvincentVincentKnowledgeable, authoritative

- Node 
- Python 
voice: { type: 'runway-live-preset', presetId: 'clara',} 
voice={ 'type': 'runway-live-preset', 'preset_id': 'clara',} 

Preview all available voices in the Developer Portal. You can also design a custom voice from a text prompt or clone one from an audio sample.

## Conversation transcripts and recordings

Section titled “Conversation transcripts and recordings”

After a conversation ends, you can review the transcript in the Developer Portal by opening your Character and browsing past conversations.

If you created the call with POST /v1/realtime_sessions, the returned session ID is also the conversation ID you use with the conversations API later. In other words, the sessionId from session creation becomes the conversationId for transcript and recording retrieval.

To retrieve or export transcripts programmatically, call the conversations endpoints on the public API (response shapes and SDK examples are in the API reference):

GET /v1/avatars/{id}/conversationsGET /v1/avatars/{id}/conversations/{conversationId}

Use the list endpoint to browse past sessions for a character. Use the conversation detail endpoint to fetch the full transcript and, when available, a recordingUrl for downloading the conversation recording.

- Node 
- Python 
import RunwayML from '@runwayml/sdk';
const client = new RunwayML();const avatarId = '550e8400-e29b-41d4-a716-446655440000';
const { id: sessionId } = await client.realtimeSessions.create({ model: 'gwm1_avatars', avatar: { type: 'custom', avatarId },});
const conversation = await client.avatars.conversations.retrieve( avatarId, sessionId);
console.log(conversation.transcript);console.log(conversation.recordingUrl); 
from runwayml import RunwayML
client = RunwayML()avatar_id = '550e8400-e29b-41d4-a716-446655440000'
session = client.realtime_sessions.create( model='gwm1_avatars', avatar={ 'type': 'custom', 'avatar_id': avatar_id },)
conversation = client.avatars.conversations.retrieve( avatar_id, session.id)
print(conversation.transcript)print(conversation.recording_url) 

The recordingUrl is temporary. If it has expired, fetch the conversation again to get a fresh download URL. 
 Custom Avatars 
 Building Your Integration
