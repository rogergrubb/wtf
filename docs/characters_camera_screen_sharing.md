# characters_camera_screen_sharing

Screen Sharing and Camera Feed | Runway API
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
- Webcam and screen sharing 
- Webcam 
- Screen sharing 
- Start sharing before the Session connects 
- Next steps 

## On this page

- Overview 
- Webcam and screen sharing 
- Webcam 
- Screen sharing 
- Start sharing before the Session connects 
- Next steps 

## Screen Sharing and Camera Feed

Runway Characters can take a live webcam or screen share from your app. The Character sees that feed over the Session, understands what is visible, and responds in real time through the Runway API — useful for demos, tutoring, games, and design feedback.

The overview below shows how Runway Characters work in real time, including seeing the user’s webcam and shared screen.

If you build with the React SDK (@runwayml/avatars-react), webcam and screen sharing are built into AvatarCall, ControlBar, and related components. For the full list of props, hooks (such as useLocalMedia), and edge cases, see Webcam &#x26; screen sharing in the React SDK README.

## Webcam and screen sharing

Section titled “Webcam and screen sharing”

Sharing video opens up visual workflows: identify objects on a desk, run trivia with physical cards (example), get guidance while you play (example), walk through slides, or ask for reactions to a layout in your design tool.

Compatibility
Webcam and screen sharing work for preset Characters and custom Characters that use a preset voice. Custom Characters with a custom voice do not support webcam or screen sharing.

## Webcam

Section titled “Webcam”

The webcam is on by default when you use the default UI. The video prop controls whether the camera starts when the Session connects; &#x3C;UserVideo> renders the local preview.

- Webcam enabled (default layout)
&#x3C;AvatarCall avatarId="music-superstar" connectUrl="/api/avatar/connect"> &#x3C;AvatarVideo /> &#x3C;UserVideo /> &#x3C;ControlBar />&#x3C;/AvatarCall>   ">

To join without sending camera video, set video={false}:
Disable webcam on connect
&#x3C;AvatarCall avatarId="music-superstar" connectUrl="/api/avatar/connect" video={false} />">

## Screen sharing

Section titled “Screen sharing”

Pass showScreenShare to ControlBar so users can start sharing from the built-in controls, and add &#x3C;ScreenShareVideo> to show the shared content in your layout.
Screen share control and preview
&#x3C;AvatarCall avatarId="music-superstar" connectUrl="/api/avatar/connect"> &#x3C;AvatarVideo /> &#x3C;ScreenShareVideo /> &#x3C;ControlBar showScreenShare />&#x3C;/AvatarCall>   ">

While sharing, the default ControlBar shows a banner with a quick Stop action.

## Start sharing before the Session connects

Section titled “Start sharing before the Session connects”

If you want the browser’s screen-share permission prompt before the call connects, capture a MediaStream first and pass it as initialScreenStream:
Pre-captured display media stream
import { useState } from 'react';import { AvatarCall, AvatarVideo, ControlBar, ScreenShareVideo } from '@runwayml/avatars-react';
function ScreenShareCall() { const [stream, setStream] = useState&#x3C;MediaStream | null>(null);
 async function startWithScreenShare() { const mediaStream = await navigator.mediaDevices.getDisplayMedia({ video: true }); setStream(mediaStream); }
 if (!stream) { return &#x3C;button onClick={startWithScreenShare}>Share screen and start call&#x3C;/button>; }
 return ( &#x3C;AvatarCall avatarId="music-superstar" connectUrl="/api/avatar/connect" initialScreenStream={stream} > &#x3C;AvatarVideo /> &#x3C;ScreenShareVideo /> &#x3C;ControlBar showScreenShare /> &#x3C;/AvatarCall> );}(null); async function startWithScreenShare() { const mediaStream = await navigator.mediaDevices.getDisplayMedia({ video: true }); setStream(mediaStream); } if (!stream) { return Share screen and start call; } return (      );}">

For programmatic toggles (camera, mic, screen share) inside a Session, use the useLocalMedia hook — documented in the same README section.

## Next steps

Section titled “Next steps”
 Building your integration Session creation, server routes, and wiring AvatarCall in a real app. 

 React SDK on GitHub Examples, hooks reference, and changelog for @runwayml/avatars-react. 

 Video Meeting 
 LiveKit Agents
