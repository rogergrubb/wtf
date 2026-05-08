# tool_calling_overview

## Tool calling overview

Tool calling lets the model decide when to invoke a named function during a realtime session. Your Character can trigger UI changes, look up live data, or click elements on the page — making it capable of taking actions, not just speaking.

## How it works

1. User speaks
"What's the status of my order 12345?"

2. Model analyzes intent
The LLM analyzes the request and determines it needs external information to respond accurately.

3. Tool invocation
The model selects the appropriate tool and generates a structured function call:

{
  "name": "check_order_status",
  "arguments": {
    "order_id": "12345"
  }
}

4. Tool execution
The system executes the tool based on its type:

- Client tools: your frontend handler runs (e.g. showing a UI overlay)
- Server tools: an HTTP-style request hits your server, which returns a result

5. Response integration
The tool result is returned to the model, which incorporates it into a natural response.

## Tool types

Runway Characters support two types of tools, each designed for different use cases. You can combine both in the same session.

### Client tools
Tools executed in the browser to drive your UI — overlays, navigation, and page interactions.

### Server tools
Tools executed on your server whose results feed back into the conversation.
