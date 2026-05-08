# characters_integration

Building your integration | Runway API
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
- Architecture overview 
- Installation 
- Server setup 
- Client integration 
- Simple: AvatarCall 
- Webcam and screen sharing 
- Fully custom: hooks 
- Browser support 

## On this page

- Overview 
- Architecture overview 
- Installation 
- Server setup 
- Client integration 
- Simple: AvatarCall 
- Webcam and screen sharing 
- Fully custom: hooks 
- Browser support 

## Building your integration

This guide walks through building a complete Avatar integration using Next.js App Router. The same patterns apply to other React frameworks.

Keep your API key secure
Your RUNWAYML_API_SECRET must never be exposed to the client. Always create Sessions server-side. If your key is compromised, rotate it immediately in the Developer Portal.

## Architecture overview

Section titled “Architecture overview”

Avatar Sessions require a server component to keep your API key secure. The client never sees your Runway API secret.

- 
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐│ Client │ │ Your Server │ │ Runway API ││ (React App) │ │ (Next.js) │ │ │└────────┬────────┘ └────────┬────────┘ └────────┬────────┘ │ │ │ │ 1. Request Session │ │ │ POST /api/avatar/session │ │ │ ─────────────────────────►│ │ │ │ │ │ │ 2. Create Session │ │ │ POST /v1/realtime_sessions │ │ ─────────────────────────►│ │ │ │ │ │ 3. Poll until ready │ │ │ GET /v1/realtime_sessions/:id │ │ ─────────────────────────►│ │ │ │ │ │ 4. Consume credentials │ │ │ POST /v1/realtime_sessions/:id/consume │ │ ─────────────────────────►│ │ │ │ │ 5. Return credentials │◄───────────────────────── │ │◄───────────────────────── │ │ │ │ │ │ 6. WebRTC connection │ │ │ ─────────────────────────────────────────────────────►│ │ │ │

## Installation

Section titled “Installation”

Install both the server SDK and React components:
Terminal window
npm install @runwayml/sdk @runwayml/avatars-react

## Server setup

Section titled “Server setup”

Create an API route that handles Session creation. This endpoint receives an Avatar ID from the client, creates a Session with Runway, polls until it’s ready, consumes the credentials, and returns them to the client.

The client can also pass optional personality and startScript fields to override the Avatar’s defaults for this session — useful for injecting user-specific context like the caller’s name.

- app/api/avatar/session/route.ts
import RunwayML from '@runwayml/sdk';
const client = new RunwayML();
export async function POST(request: Request) { const { avatarId, personality, startScript } = await request.json();
 // 1. Create session // To add tool calling, pass a tools array here — see /characters/tools const { id: sessionId } = await client.realtimeSessions.create({ model: 'gwm1_avatars', avatar: { type: 'custom', avatarId }, personality, startScript, });
 // 2. Poll until ready let sessionKey: string | undefined; for (let i = 0; i &#x3C; 60; i++) { const session = await client.realtimeSessions.retrieve(sessionId);
 if (session.status === 'READY') { sessionKey = session.sessionKey; break; } if (session.status === 'FAILED') { return Response.json({ error: session.failure }, { status: 500 }); } await new Promise(r => setTimeout(r, 1000)); }
 if (!sessionKey) { return Response.json({ error: 'Session timed out' }, { status: 504 }); }
 // 3. Consume session to get connection credentials const consumeResponse = await fetch( `${client.baseURL}/v1/realtime_sessions/${sessionId}/consume`, { method: 'POST', headers: { Authorization: `Bearer ${sessionKey}`, 'X-Runway-Version': '2024-11-06', }, } ); const credentials = await consumeResponse.json();
 return Response.json({ sessionId, serverUrl: credentials.url, token: credentials.token, roomName: credentials.roomName, });} setTimeout(r, 1000)); } if (!sessionKey) { return Response.json({ error: &#x27;Session timed out&#x27; }, { status: 504 }); } // 3. Consume session to get connection credentials const consumeResponse = await fetch( &#x60;${client.baseURL}/v1/realtime_sessions/${sessionId}/consume&#x60;, { method: &#x27;POST&#x27;, headers: { Authorization: &#x60;Bearer ${sessionKey}&#x60;, &#x27;X-Runway-Version&#x27;: &#x27;2024-11-06&#x27;, }, } ); const credentials = await consumeResponse.json(); return Response.json({ sessionId, serverUrl: credentials.url, token: credentials.token, roomName: credentials.roomName, });}">

Save the session ID
The sessionId returned from client.realtimeSessions.create() is also the conversationId for that call. Persist it with your own call record if you want to later fetch transcript or recordingUrl from GET /v1/avatars/{id}/conversations/{conversationId}.

Set your API key as an environment variable:
.env.local
RUNWAYML_API_SECRET=your_api_key_here

## Client integration

Section titled “Client integration”

## Simple: AvatarCall

Section titled “Simple: AvatarCall”

The simplest way to add an Avatar is with the AvatarCall component. It handles WebRTC connection and renders a default UI.
app/page.tsx
'use client';
import { AvatarCall } from '@runwayml/avatars-react';import '@runwayml/avatars-react/styles.css';
export default function Home() { return ( &#x3C;AvatarCall avatarId="customer-service" connectUrl="/api/avatar/session" onEnd={() => console.log('Call ended')} onError={(error) => console.error('Error:', error)} /> );} console.log(&#x27;Call ended&#x27;)} onError={(error) => console.error(&#x27;Error:&#x27;, error)} /> );}">

To use a custom Avatar created in the Developer Portal, replace "customer-service" with your Avatar ID.

## Webcam and screen sharing

Section titled “Webcam and screen sharing”

During a call, the Avatar can use your webcam and/or your screen as visual context—for example walkthroughs, slides, or showing something in frame. Enable that with @runwayml/avatars-react; webcam and screen share are part of the same realtime Session as audio (the usual WebRTC call).

Custom voice
Custom Avatars that use a custom voice do not support webcam or screen sharing.

Minimal example with the default control bar and screen sharing enabled:

// app/page.tsx — webcam (default) + optional screen share UI'use client';
import { AvatarCall, AvatarVideo, ControlBar, ScreenShareVideo,} from '@runwayml/avatars-react';import '@runwayml/avatars-react/styles.css';
export default function Home() { return ( &#x3C;AvatarCall avatarId="customer-service" connectUrl="/api/avatar/session"> &#x3C;AvatarVideo /> &#x3C;ScreenShareVideo /> &#x3C;ControlBar showScreenShare /> &#x3C;/AvatarCall> );}     );}">

## Fully custom: hooks

Section titled “Fully custom: hooks”

For complete control over the UI, use AvatarSession with hooks. This example shows how to build a custom interface with useAvatarSession for Session state and useLocalMedia for mic and webcam controls:
components/CustomAvatarUI.tsx
'use client';
import { AvatarSession, AvatarVideo, UserVideo, useAvatarSession, useLocalMedia,} from '@runwayml/avatars-react';import type { SessionCredentials } from '@runwayml/avatars-react';
function CallUI() { const { state, end } = useAvatarSession(); const { isMicEnabled, toggleMic } = useLocalMedia();
 return ( &#x3C;div className="relative w-full h-screen"> &#x3C;AvatarVideo className="w-full h-full object-cover" /> &#x3C;UserVideo className="absolute bottom-4 right-4 w-48 rounded-lg" />
 &#x3C;div className="absolute bottom-4 left-4 flex gap-2"> &#x3C;button onClick={toggleMic}> {isMicEnabled ? 'Mute' : 'Unmute'} &#x3C;/button> &#x3C;button onClick={end}>End&#x3C;/button> &#x3C;/div>
 {state === 'connecting' &#x26;&#x26; &#x3C;div>Connecting...&#x3C;/div>} &#x3C;/div> );}
export function CustomAvatar({ credentials }: { credentials: SessionCredentials }) { return ( &#x3C;AvatarSession credentials={credentials} audio video> &#x3C;CallUI /> &#x3C;/AvatarSession> );}     {isMicEnabled ? &#x27;Mute&#x27; : &#x27;Unmute&#x27;}  End  {state === &#x27;connecting&#x27; &#x26;&#x26; Connecting...}  );}export function CustomAvatar({ credentials }: { credentials: SessionCredentials }) { return (    );}">

For more components, hooks, and examples—including the full Webcam &#x26; Screen Sharing section—see the React SDK README. For client tools (UI tool calls) and server tools (server-side tools with return values), see Tool calling.

## Browser support

Section titled “Browser support”

The Avatars SDK uses WebRTC for real-time communication:

BrowserMinimum VersionChrome74+Firefox78+Safari14.1+Edge79+

Users must grant microphone permissions when prompted. Webcam access is required if the user’s video is enabled. 
 Core Concepts 
 Embedded Widget
