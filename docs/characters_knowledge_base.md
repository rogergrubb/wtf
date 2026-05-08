# characters_knowledge_base

Knowledge base | Runway API
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
- Why use a knowledge base 
- Supported content 
- Adding knowledge to an Avatar 
- 1. Create a Document 
- 2. Update a Document 
- 3. Link the Document to your Avatar 
- 4. Start a Session 

## On this page

- Overview 
- Why use a knowledge base 
- Supported content 
- Adding knowledge to an Avatar 
- 1. Create a Document 
- 2. Update a Document 
- 3. Link the Document to your Avatar 
- 4. Start a Session 

## Knowledge base

The Documents API lets you give Avatars access to domain-specific knowledge. Upload content that your Avatar can reference during conversations to provide accurate, contextual responses.

Token limit
Each Avatar supports up to 50,000 tokens of knowledge. We plan to increase this limit in the future.

## Why use a knowledge base

Section titled “Why use a knowledge base”

A knowledge base helps your Avatar stay on topic and provide accurate information. Common use cases:

- Customer support: FAQs, product information, company policies

- Quizzes and games: Question banks, correct answers, scoring rules

- Education: Course material, reference content, learning objectives

- Brand experiences: Brand guidelines, messaging, product details

## Supported content

Section titled “Supported content”

FormatDescriptionPlain textUnformatted text contentMarkdownStructured content with headings and formatting

More formats are planned for future releases.

## Adding knowledge to an Avatar

Section titled “Adding knowledge to an Avatar”

The flow is: create a Document, then link it to your Avatar.

## 1. Create a Document

Section titled “1. Create a Document”

- Node 
- Python 
- 
import RunwayML from '@runwayml/sdk';
const client = new RunwayML();
const document = await client.documents.create({ name: 'Product FAQ', content: '# Product FAQ\n\n## What is your return policy?\n\nWe offer a 30-day return policy...',});
console.log('Document created:', document.id); 
from runwayml import RunwayML
client = RunwayML()
document = client.documents.create( name='Product FAQ', content='# Product FAQ\n\n## What is your return policy?\n\nWe offer a 30-day return policy...',)
print('Document created:', document.id) 

## 2. Update a Document

Section titled “2. Update a Document”

You can update a Document’s name, content, or both using the update method.

- Node 
- Python 
await client.documents.update(document.id, { name: 'Updated Product FAQ', content: '# Product FAQ\n\n## What is your return policy?\n\nWe now offer a 60-day return policy...',}); 
client.documents.update( id=document.id, name='Updated Product FAQ', content='# Product FAQ\n\n## What is your return policy?\n\nWe now offer a 60-day return policy...',) 

Both fields are optional — provide only the fields you want to change.

## 3. Link the Document to your Avatar

Section titled “3. Link the Document to your Avatar”

Update your Avatar to attach the Document. This replaces any existing Document attachments.

- Node 
- Python 
await client.avatars.update(avatarId, { documentIds: [document.id],}); 
client.avatars.update( avatar_id, document_ids=[document.id],) 

## 4. Start a Session

Section titled “4. Start a Session”

The Avatar now has access to the knowledge during conversations. Start a Session as usual:

- Node 
- Python 
const session = await client.realtimeSessions.create({ model: 'gwm1_avatars', avatar: { type: 'custom', avatarId: avatarId, },}); 
session = client.realtime_sessions.create( model='gwm1_avatars', avatar={ 'type': 'custom', 'avatar_id': avatar_id, },) 

You can also manage Documents through the Developer Portal. See the API reference for all available endpoints. 
 Embedded Widget 
 Custom Voices
