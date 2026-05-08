# characters_custom_voices

Custom voices | Runway API
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
- Voice design 
- Voice cloning 
- Voice status 
- Assigning a custom voice to an Avatar 
- Listing voices 

## On this page

- Overview 
- Voice design 
- Voice cloning 
- Voice status 
- Assigning a custom voice to an Avatar 
- Listing voices 

## Custom voices

The Voices API lets you create custom voices for your Characters. Design an entirely new voice from a text prompt, or clone a voice from an audio sample. Once created, assign the voice to any Avatar.

## Voice design

Section titled “Voice design”

Create a voice by describing the characteristics you want. The prompt should include details like tone, accent, pacing, and personality.

- Node 
- Python 
- 
import RunwayML from '@runwayml/sdk';
const client = new RunwayML();
const voice = await client.voices.create({ name: 'Brand Ambassador', from: { type: 'text', prompt: 'A warm, friendly voice with a slight British accent. Speaks at a measured pace with a professional yet approachable tone.', model: 'eleven_ttv_v3', },});
console.log('Voice created:', voice.id); 
from runwayml import RunwayML
client = RunwayML()
voice = client.voices.create( name='Brand Ambassador', from_={ 'type': 'text', 'prompt': 'A warm, friendly voice with a slight British accent. Speaks at a measured pace with a professional yet approachable tone.', 'model': 'eleven_ttv_v3', },)
print('Voice created:', voice.id) 

ParameterTypeDescriptionnamestringA name for the voice (max 100 characters).from.type"text"Indicates voice design from a text prompt.from.promptstringA description of the desired voice characteristics. Must be at least 20 characters.from.modelstringThe voice design model. Use eleven_ttv_v3 (latest) or eleven_multilingual_ttv_v2.

## Voice cloning

Section titled “Voice cloning”

Clone a voice from an audio sample. Provide a clear recording with minimal background noise and varied tone for best results.

- Node 
- Python 
const voice = await client.voices.create({ name: 'Cloned Narrator', from: { type: 'audio', audio: 'https://example.com/voice-sample.mp3', },});
console.log('Voice created:', voice.id); 
voice = client.voices.create( name='Cloned Narrator', from_={ 'type': 'audio', 'audio': 'https://example.com/voice-sample.mp3', },)
print('Voice created:', voice.id) 

The audio sample must be between 10 seconds and 5 minutes long, and at most 10 MB. You can pass a public HTTPS URL, a runway:// upload URI, or a data:audio/... data URI.

## Voice status

Section titled “Voice status”

Voice creation is asynchronous. After calling create, poll the voice until its status is READY.

- Node 
- Python 
const voice = await client.voices.retrieve(voiceId);
if (voice.status === 'READY') { console.log('Preview:', voice.previewUrl);} 
voice = client.voices.retrieve(id=voice_id)
if voice.status == 'READY': print('Preview:', voice.preview_url) 

StatusDescriptionPROCESSINGVoice is being generated. Poll until ready.READYVoice is ready. A previewUrl is available.FAILEDGeneration failed. Check failureReason.

## Assigning a custom voice to an Avatar

Section titled “Assigning a custom voice to an Avatar”

Once the voice is ready, assign it to an Avatar by setting the voice type to custom and providing the voice ID.

- Node 
- Python 
await client.avatars.update(avatarId, { voice: { type: 'custom', id: voice.id, },}); 
client.avatars.update( avatar_id, voice={ 'type': 'custom', 'id': voice.id, },) 

You can also create a new Avatar with a custom voice directly:

- Node 
- Python 
const avatar = await client.avatars.create({ name: 'Support Agent', referenceImage: 'https://example.com/avatar.png', voice: { type: 'custom', id: voice.id, }, personality: 'You are a helpful customer support agent...',}); 
avatar = client.avatars.create( name='Support Agent', reference_image='https://example.com/avatar.png', voice={ 'type': 'custom', 'id': voice.id, }, personality='You are a helpful customer support agent...',) 

## Listing voices

Section titled “Listing voices”

Retrieve all custom voices for your organization.

- Node 
- Python 
const voices = await client.voices.list();
for await (const voice of voices) { console.log(voice.name, voice.status);} 
for voice in client.voices.list(): print(voice.name, voice.status) 

You can also manage custom voices through the Developer Portal. See the API reference for all available endpoints. 
 Knowledge Base 
 Overview
