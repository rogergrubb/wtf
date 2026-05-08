# tool_calling_server_tools

Server tools | Runway API
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
- Timeout 
- Error handling 
- Combining with client events 
- Next steps 

## On this page

- Overview 
- Guide 
- Timeout 
- Error handling 
- Combining with client events 
- Next steps 

## Server tools

Connect your Character to external data and systems. Server tools let the Character fetch live data, call APIs, and query databases — with results that feed back into the conversation so it can speak from real information.

Unlike client tools, server tools return results to the LLM. Use them when you need server-side auth, database lookups, or any data that shapes what the Character says next.

## Guide

Section titled “Guide”

- 

Declare tools at session creation

On your server, declare backend_rpc tools when creating the Session:

- 
import RunwayML from '@runwayml/sdk';
const client = new RunwayML();
const { id: sessionId } = await client.realtimeSessions.create({ model: 'gwm1_avatars', avatar: { type: 'custom', avatarId: 'your-avatar-id' }, tools: [ { type: 'backend_rpc', name: 'check_order_status', description: 'Look up a customer order by ID and return the current shipping status', timeoutSeconds: 6, parameters: [ { type: 'string', name: 'order_id', description: 'The order ID, e.g. ORD-12345', }, ], }, ],});

- 

Set up the RPC handler

Connect the RPC handler using @runwayml/avatars-node-rpc. Pass your API key and session ID — the package calls /connect_backend and joins the room automatically:

import { createRpcHandler } from '@runwayml/avatars-node-rpc';
const handler = await createRpcHandler({ apiKey: process.env.RUNWAYML_API_SECRET!, sessionId, tools: { check_order_status: async (args) => { const order = await db.orders.find(String(args.order_id)); return { status: order.status, eta: order.eta }; }, }, onConnected: () => console.log('Connected to session'), onDisconnected: () => console.log('Session ended'), onError: (err) => console.error('RPC error:', err),}); { const order = await db.orders.find(String(args.order_id)); return { status: order.status, eta: order.eta }; }, }, onConnected: () => console.log(&#x27;Connected to session&#x27;), onDisconnected: () => console.log(&#x27;Session ended&#x27;), onError: (err) => console.error(&#x27;RPC error:&#x27;, err),});">

If you’ve already called /connect_backend yourself, pass pre-fetched credentials instead:

const handler = await createRpcHandler({ credentials: { url: 'wss://livekit.example.com', token: '&#x3C;jwt>', roomName: '&#x3C;room-name>', }, tools: { check_order_status: async (args) => { const order = await db.orders.find(String(args.order_id)); return { status: order.status, eta: order.eta }; }, },});&#x27;, roomName: &#x27;&#x27;, }, tools: { check_order_status: async (args) => { const order = await db.orders.find(String(args.order_id)); return { status: order.status, eta: order.eta }; }, },});">

- 

Test it

Start a conversation and ask something like “What’s the status of my order 12345?” Your handler should fire, and the Character will respond with the returned data: “Your order has shipped! It should arrive by May 7th.”

For the full list of handler options, see the @runwayml/avatars-node-rpc README.

## Timeout

Section titled “Timeout”

Server tools accept a timeoutSeconds field that controls how long the Character waits for your handler to respond.

SettingValueDefault4 secondsMinimum1 secondMaximum8 seconds

If your handler doesn’t respond within the timeout, the tool call is treated as failed and the Character continues the conversation without the result.

Choose a timeout that covers your expected handler latency with a small buffer. If your backend needs to make external API calls, consider increasing from the default:

{ type: 'backend_rpc', name: 'fetch_weather', description: 'Get current weather for a city', timeoutSeconds: 8, parameters: [ { type: 'string', name: 'city', description: 'City name' }, ],}

## Error handling

Section titled “Error handling”

If a tool handler throws an error, the error message is sent back to the worker so the model can acknowledge the failure instead of hanging until timeout:

tools: { check_order_status: async (args) => { const order = await db.orders.find(String(args.order_id)); if (!order) { throw new Error('Order not found'); } return { status: order.status, eta: order.eta }; },}, { const order = await db.orders.find(String(args.order_id)); if (!order) { throw new Error(&#x27;Order not found&#x27;); } return { status: order.status, eta: order.eta }; },},">

Other things to know:

- One handler per session — the API enforces a single backend RPC connection per Session. Attempting a second /connect_backend call will be rejected.

- Disconnect handling — if the handler disconnects mid-session, pending RPC calls will time out. Use the onDisconnected callback to detect this.

## Combining with client events

Section titled “Combining with client events”

You can use both server tools and client tools in the same Session. Declare both tool types in the tools array:

import { openModalTool } from '@/lib/tools';
await client.realtimeSessions.create({ model: 'gwm1_avatars', avatar: { type: 'custom', avatarId }, tools: [ openModalTool, { type: 'backend_rpc', name: 'check_order_status', description: 'Look up a customer order', parameters: [ { type: 'string', name: 'order_id', description: 'The order ID' }, ], }, ],});

On the client, subscribe to client events as usual. On the server, connect the RPC handler for the backend tools.

## Next steps

Section titled “Next steps”
 Client tools Fire-and-forget tools that drive your UI — modals, navigation, and Page Actions. 
 Best practices Parameter schemas, limits, and prompting tips for reliable tool calls. 
 Example: RPC weather Weather assistant using backend RPC tools. 
 SDK reference Complete documentation for the Node RPC handler. 

 Client tools 
 Best practices
