# tool_calling_reference

Reference | Runway API
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
- Limits 
- Reading tool call history 
- Troubleshooting 

## On this page

- Overview 
- Limits 
- Reading tool call history 
- Troubleshooting 

## Reference

## Limits

Section titled “Limits”

ResourceLimitTools per session20Parameters per tool20Tool name length1–64 charactersTool name pattern^[a-zA-Z_][a-zA-Z0-9_]*$Tool namesMust be unique within a sessionDescription length1–1024 charactersEnum values per string parameter20Enum value length64 charactersNested properties per object20Backend RPC timeout1–8 seconds (default 4)Backend RPC handlers per session1

## Reading tool call history

Section titled “Reading tool call history”

After a session ends, you can read back tool call history from the Conversations API.

The list endpoint includes a hasTools flag on each conversation:

- Terminal window
curl https://api.dev.runwayml.com/v1/avatar_conversations \ -H "Authorization: Bearer $RUNWAYML_API_SECRET" \ -H "X-Runway-Version: 2024-11-06"

The detail endpoint includes the full transcript with tool calls and results:
Terminal window
curl https://api.dev.runwayml.com/v1/avatar_conversations/conv_123 \ -H "Authorization: Bearer $RUNWAYML_API_SECRET" \ -H "X-Runway-Version: 2024-11-06"

The response includes:

- tools — the tools that were configured for the session (type, name, description)

- transcript — each entry can include:

- toolCalls — tool invocations on assistant turns: { id, name, arguments }

- toolResults — results returned: { id, name, result, error, durationMs }

- content — can be null for tool-only turns where the Character didn’t speak

Example transcript entry with a tool call:

{ "role": "assistant", "content": null, "timestamp": "2025-01-15T10:30:00Z", "toolCalls": [ { "id": "call_abc123", "name": "check_order_status", "arguments": { "order_id": "ORD-12345" } } ], "toolResults": [ { "id": "call_abc123", "name": "check_order_status", "result": { "status": "shipped", "eta": "2025-01-17" }, "error": null, "durationMs": 230 } ]}

## Troubleshooting

Section titled “Troubleshooting”
Tool not being invoked
Make descriptions specific about the trigger (“when the user asks about…”). You can also add guidance in the Character’s personality field about when to use each tool.
Backend RPC timing out
The default timeout is 4 seconds. Increase timeoutSeconds (max 8) if your handler makes external API calls. If it consistently takes longer, consider pre-fetching or caching.
Backend handler not connecting
Verify RUNWAYML_API_SECRET is set correctly. The session must be in READY or RUNNING status before the handler can connect. Only one backend handler can connect per session.
Client tool events not arriving
Make sure you’re subscribing inside an AvatarCall, AvatarProvider, or AvatarSession component. Check the browser console for WebRTC data channel errors.
Unexpected arguments
Use Standard Schema (Zod) validation with clientTool to catch malformed args at runtime. For backend RPC, validate args in your handler and throw descriptive errors. 
 Best practices 
 Video Meeting
