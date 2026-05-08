# tool_calling_client_tools

Client tools | Runway API
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
- Guide 
- Page Actions 
- Server setup 
- Client setup 
- Available actions 
- Next steps 

## On this page

- Overview 
- Guide 
- Page Actions 
- Server setup 
- Client setup 
- Available actions 
- Next steps 

## Client tools

Enable your Character to trigger actions and control your application’s user interface — opening modals, updating state, navigating pages, and more. Great for info panels, trivia boards, highlights, game state, or any on-device effect that doesn’t need a server round trip.

Unlike server tools, client tools run entirely in the browser and don’t return results to the conversation. If you need the Character to speak from data your server provides, use server tools instead.

## Guide

Section titled “Guide”

- 

Define your tools

Use clientTool from @runwayml/avatars-react/api to define tools. Each tool needs a name, description, and a Standard Schema (like Zod) for its arguments.

- 
// lib/tools.ts — shared between server and clientimport { clientTool, type ClientEventsFrom } from '@runwayml/avatars-react/api';import { z } from 'zod';
export const openModalTool = clientTool('open_modal', { description: 'Open a modal dialog to display additional information', schema: z.object({ title: z.string(), content: z.string(), }),});
export const navigateToPageTool = clientTool('navigate_to_page', { description: 'Navigate the user to a specific page in the application', schema: z.object({ page: z.string() }),});
export const tools = [openModalTool, navigateToPageTool];export type AppEvents = ClientEventsFrom&#x3C;typeof tools>;;">

When you pass a schema, useClientEvent validates incoming args at runtime — malformed events are dropped instead of crashing your UI.

- 

Pass tools at session creation

On your server, pass the tools array when creating the Session:
app/api/avatar/session/route.ts
import RunwayML from '@runwayml/sdk';import { tools } from '@/lib/tools';
const client = new RunwayML();
export async function POST(request: Request) { const { avatarId } = await request.json();
 const { id: sessionId } = await client.realtimeSessions.create({ model: 'gwm1_avatars', avatar: { type: 'custom', avatarId }, tools, });
 // Poll and return credentials (see Building your integration) // ...}

- 

Handle events on the client

Inside an AvatarCall, AvatarProvider, or AvatarSession, use hooks to handle incoming tool calls.

Single tool — useClientEvent takes a tool definition and a callback:

import * as React from 'react';import { useClientEvent } from '@runwayml/avatars-react';import { openModalTool } from '@/lib/tools';
function ModalHandler() { const [modal, setModal] = React.useState&#x3C;{ title: string; content: string } | null>(null);
 const handleOpenModal = React.useCallback((args: { title: string; content: string }) => { setModal(args); }, []);
 useClientEvent(openModalTool, handleOpenModal);
 if (!modal) return null;
 return ( &#x3C;dialog open> &#x3C;h2>{modal.title}&#x3C;/h2> &#x3C;p>{modal.content}&#x3C;/p> &#x3C;/dialog> );}(null); const handleOpenModal = React.useCallback((args: { title: string; content: string }) => { setModal(args); }, []); useClientEvent(openModalTool, handleOpenModal); if (!modal) return null; return (  

## {modal.title}

 
{modal.content}  );}">

All tools — useClientEvents fires a callback for every tool call:

import { useClientEvents } from '@runwayml/avatars-react';import type { AppEvents } from '@/lib/tools';
function EventLogger() { useClientEvents&#x3C;AppEvents>((event) => { console.log('Tool called:', event.tool, event.args); }); return null;}((event) => { console.log(&#x27;Tool called:&#x27;, event.tool, event.args); }); return null;}">

- 

Test it

Start a conversation and say something like “Tell me more about the premium plan.” You should see a modal appear with the plan details while the Character continues speaking.

## Page Actions

Section titled “Page Actions”

The SDK ships with pre-built tools that let the Character interact with your page — clicking buttons, scrolling to sections, and highlighting elements. No custom tool definitions needed.

## Server setup

Section titled “Server setup”

Import pageActionTools and pass them when creating the Session:

import { pageActionTools } from '@runwayml/avatars-react/api';
const { id } = await client.realtimeSessions.create({ model: 'gwm1_avatars', avatar: { type: 'runway-preset', presetId: 'music-superstar' }, tools: pageActionTools,});

Combine with your own tools by spreading both arrays:

import { pageActionTools } from '@runwayml/avatars-react/api';import { tools as clientEventTools } from '@/lib/tools';
tools: [...pageActionTools, ...clientEventTools],

## Client setup

Section titled “Client setup”

Drop in the PageActions component inside your AvatarCall:

import { AvatarCall, AvatarVideo, ControlBar, PageActions } from '@runwayml/avatars-react';
function App() { return ( &#x3C;AvatarCall avatarId="music-superstar" connectUrl="/api/avatar/connect"> &#x3C;AvatarVideo /> &#x3C;ControlBar /> &#x3C;PageActions /> &#x3C;/AvatarCall> );}   
  );}">

The Character can now reference elements by id or by a data-avatar-target attribute:

- 
&#x3C;button id="signup">Sign Up&#x3C;/button>&#x3C;section data-avatar-target="pricing">...&#x3C;/section>Sign Up...">

## Available actions

Section titled “Available actions”

ActionWhat it doesclickCalls .click() on the target elementscroll_toScrolls the target into view with smooth scrollinghighlightPulses an outline around the target, then removes it

For styling, configuration, and advanced usage, see the PageActions documentation in the SDK repo.

## Next steps

Section titled “Next steps”
 Server tools Tools executed on your server whose results feed back into the conversation. 
 Best practices Parameter schemas, limits, and prompting tips for reliable tool calls. 
 Example: Client events Build a trivia game with client event tools. 
 SDK reference Complete SDK documentation for tool events and hooks. 

 Overview 
 Server tools
