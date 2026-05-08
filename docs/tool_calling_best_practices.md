# tool_calling_best_practices

Best practices | Runway API
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
- Writing effective descriptions 
- Use personality to guide invocation 
- Parameter schema reference 
- Basic types 
- String with enum 
- Array 
- Object 
- Complete example 
- Related 

## On this page

- Overview 
- Writing effective descriptions 
- Use personality to guide invocation 
- Parameter schema reference 
- Basic types 
- String with enum 
- Array 
- Object 
- Complete example 
- Related 

## Best practices

Tips for writing reliable tool definitions, staying within limits, and debugging when things go wrong.

## Writing effective descriptions

Section titled “Writing effective descriptions”

The description field on both tools and parameters is how the model decides when to invoke a tool and what arguments to pass. Vague descriptions lead to missed or incorrect invocations.

Be specific about when the tool should be used:

- 
// ✅ Good — the model knows exactly when to call this{ name: 'check_order_status', description: 'Look up a customer order by ID when the user asks about delivery, tracking, or order updates. Returns the current status and estimated arrival date.',}
// ❌ Bad — too vague for reliable invocation{ name: 'check_order_status', description: 'Checks orders',}

Be specific about parameter formats:

// ✅ Good — tells the model what to extract from conversation{ type: 'string', name: 'order_id', description: 'The order ID mentioned by the user, typically in the format ORD-12345',}
// ❌ Bad — leaves the model guessing{ type: 'string', name: 'id', description: 'The ID',}

## Use personality to guide invocation

Section titled “Use personality to guide invocation”

Your Character’s personality field can include instructions about when and how to use tools. This is especially useful when the Character has multiple tools and you want predictable behavior:

await client.realtimeSessions.create({ model: 'gwm1_avatars', avatar: { type: 'custom', avatarId }, personality: `You are a helpful shopping assistant.
When the user asks about an order, use check_order_status to look up the details before answering.When the user asks about products, use search_catalog to find relevant items.Always confirm the order ID before looking it up.`, tools: [/* ... */],});

## Parameter schema reference

Section titled “Parameter schema reference”

Tools accept a parameters array where each entry describes one argument. Six types are supported:

## Basic types

Section titled “Basic types”

TypeDescriptionExample valuestringText value"ORD-12345"integerWhole number42numberDecimal number3.14booleanTrue/falsetrue

Each parameter requires a type, name, and description. Set required: false to make a parameter optional (defaults to true). See the API reference for the full schema.

## String with enum

Section titled “String with enum”

String parameters can include an enum to restrict values:

{ type: 'string', name: 'priority', description: 'Urgency level for the support ticket', enum: ['low', 'medium', 'high', 'critical'],}

## Array

Section titled “Array”

Array parameters specify the type of each element:

{ type: 'array', name: 'tags', description: 'Keywords to tag the support ticket with', items: { type: 'string' },}

Array items can be string, integer, number, or boolean.

## Object

Section titled “Object”

Object parameters define nested properties — each one follows the same schema as a top-level parameter:

{ type: 'object', name: 'address', description: 'Shipping address for the order', properties: [ { type: 'string', name: 'street', description: 'Street address' }, { type: 'string', name: 'city', description: 'City name' }, { type: 'string', name: 'zip', description: 'ZIP or postal code' }, ],}

## Complete example

Section titled “Complete example”

Here’s a tool with a mix of parameter types:

{ type: 'backend_rpc', name: 'create_support_ticket', description: 'Create a support ticket when the user reports a problem. Collect the issue details and priority before calling.', timeoutSeconds: 6, parameters: [ { type: 'string', name: 'subject', description: 'A short summary of the issue', }, { type: 'string', name: 'priority', description: 'Urgency level', enum: ['low', 'medium', 'high'], }, { type: 'array', name: 'tags', description: 'Keywords to categorize the ticket', items: { type: 'string' }, }, { type: 'boolean', name: 'notify_customer', description: 'Whether to send a confirmation email to the user', required: false, }, ],}

## Related

Section titled “Related”
 Client tools Fire-and-forget tools that drive your UI — modals, navigation, and Page Actions. 
 Server tools Tools executed on your server whose results feed back into the conversation. 

 Server tools 
 Reference
