# characters_quickstart

Quickstart | Runway API
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
- 1. Create a developer account 
- 2. Create a new API key 
- 3. Add credits 
- 4. Download the React app template 
- 5. Install packages 
- 6. Set your API key 
- 7. Run the app 
- Troubleshooting 
- Next steps 

## On this page

- Overview 
- 1. Create a developer account 
- 2. Create a new API key 
- 3. Add credits 
- 4. Download the React app template 
- 5. Install packages 
- 6. Set your API key 
- 7. Run the app 
- Troubleshooting 
- Next steps 

## Quickstart

In this tutorial, we will build a React web app that video calls a Runway character — in under 5 minutes.

Helpful links:

- Runway developer account

- Runway avatar SDK template

## 1. Create a developer account

Section titled “1. Create a developer account”

Create an account at dev.runwayml.com.

Once you log in, you will see an “Characters” tab at the top bar, and there are a few preset characters. We are going to video call the character called “Tooth”.

## 2. Create a new API key

Section titled “2. Create a new API key”

Go to the Manage tab in the top bar, then click the New API key button in the top-right corner.

Give your key a name and copy it to a safe location. Once you close the pop-up, the key value is not available again. You can always create a new key if needed.

## 3. Add credits

Section titled “3. Add credits”

Click on Billing in the left sidebar under the Manage tab, and add some credits to the account.

## 4. Download the React app template

Section titled “4. Download the React app template”

In your terminal, run this command to copy the template into your local directory:

- Terminal window
npx degit runwayml/avatars-sdk-react/examples/nextjs-simple my-avatar-appcd my-avatar-app

## 5. Install packages

Section titled “5. Install packages”

Make sure you are using Node.js 18+, then install dependencies:
Terminal window
npm install

## 6. Set your API key

Section titled “6. Set your API key”

Copy the .env.example file as .env, and paste your API key:

RUNWAYML_API_SECRET=your_api_key_here

## 7. Run the app

Section titled “7. Run the app”
Terminal window
npm run dev

The server starts at http://localhost:3000. Click on the Mina character to start a conversation.

## Troubleshooting

Section titled “Troubleshooting”

- API key errors:

- Make sure you copy the entire API key correctly. The key begins with key_ followed by 128 hex characters.

- Make sure the key is currently active. Deactivated keys will be rejected.

- No credits: Make sure the developer account has credits before starting a call.

## Next steps

Section titled “Next steps”
 Create Your Own Characters Create your own character from a single image — no training required. 

 Overview 
 Custom Avatars
