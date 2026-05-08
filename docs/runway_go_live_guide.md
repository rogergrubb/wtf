# Runway Production Deployment Guide

Source: https://docs.dev.runwayml.com/guides/go-live/

HTTP 200
Content-Type: text/html
 Production Launch Checklist | Runway API-
  Skip to content         Runway API        Search  CtrlK       Cancel                               Copy Page      Open in Cursor      Open in ChatGPT      Open in Claude       Docs API Reference
Dev Portal
                Docs API Reference           Get Started         Create your account
-   Using the API
-   Models
-   Pricing
-   Go-live checklist
-   Playground ↗
   -     Characters         Overview
-   Quickstart
-   Custom Avatars
-   Core Concepts
-   Building Your Integration
-   Embedded Widget
-   Knowledge Base
-   Custom Voices
-     Tool calling         Overview
-   Client tools
-   Server tools
-   Best practices
-   Reference
   -   Video Meeting
-   Camera and Screen Sharing
-   LiveKit Agents
-   Troubleshooting
-   React SDK ↗
   -     API details         SDKs
-   Inputs
-   Outputs
-   Uploads
-   Content moderation
   -     Usage & Billing         Autobilling
-   Usage tiers
-   Attribution
-   Organizations and roles
   -     Sample Apps         Web app: Hair makeover
-   Chrome extension: Generate video from any image
-   Chrome extension: Virtual try on
-   Figma plugin: Image and Video Generator
   -     Errors         HTTP Errors
-   Task failures
-   Troubleshooting
   -     API versions         Changelog
-   Overview
-   Version 2024-11-06
             Theme Selector    Dark modeLight modeSystem default                 On this page -   Overview
-   1. Manage your usage     Tier up
-   Set up autobilling
  -   2. Test your integration     Check your integration’s validation
  -   3. Secure your integration     Ensure your key is stored securely
-   Stop sharing keys
  -   4. Monitor your integration     Ensure you’re receiving emails
-   Avoid account suspension
## On this page
 -   Overview
-   1. Manage your usage     Tier up
-   Set up autobilling
  -   2. Test your integration     Check your integration’s validation
  -   3. Secure your integration     Ensure your key is stored securely
-   Stop sharing keys
  -   4. Monitor your integration     Ensure you’re receiving emails
-   Avoid account suspension
# Production Launch Checklist
      Before going live, make sure that you’ve checked and double-checked that everything is
in order. This is a checklist of things that you might not think of.
## 1. Manage your usage
Section titled “1. Manage your usage”
### Tier up
Section titled “Tier up”
Limits on your organization are governed by tiers. If you haven’t done much
testing or haven’t added many credits to your organization, your tier may not allow enough
generations per day or enough concurrent generations to
satisfy your users’ demand.
Tiering up involves adding credits and waiting set intervals (predetermined by the tier).
If you have an estimate for how many generations you’ll be creating, you should tier up
to a tier that allows for that many generations per day.
### Set up autobilling
Section titled “Set up autobilling”
Make sure you have set up autobilling for your organization. Autobilling will ensure that
your integration doesn’t run out of credits unexpectedly. To set up autobilling, you’ll
set up a payment method to be charged. You’ll also provide a threshold below which your
credit balance will be recharged at, and the number of credits to add.
You can learn more about autobilling in the autobilling docs.
## 2. Test your integration
Section titled “2. Test your integration”
Make sure you’ve tested your integration thoroughly. You should be sure that your integration
can tolerate different kinds of failures, like <code dir="auto">429 Too Many Requests</code> errors (indicating your
integration has reached the rate limit) and <code dir="auto">503 Service Unavailable</code> errors (indicating a
service outage).
A full list of errors is documented on our errors page.
### Check your integration’s validation
Section titled “Check your integration’s validation”
Also be sure to check the API documentation to ensure inputs that you are passing
are validated. For example, passing a <code dir="auto">promptImage</code> referencing an image that’s too large
or an unsupported codec will result in a <code dir="auto">400 Bad Request</code> error. Test with a variety of
inputs to ensure you haven’t missed any edge cases.
All URLs that you pass should be sure to follow the guidance in the inputs
documentation.
## 3. Secure your integration
Section titled “3. Secure your integration”
Keeping your integration secure is important to make sure your key is not abused. There
are a few important steps to making sure your integration is built securely.
If you find that any key was stored insecurely, immediately disable the key. You can do this
from the API Keys tab in the developer portal.
### Ensure your key is stored securely
Section titled “Ensure your key is stored securely”
Your API key should never be hard-coded into your application. Instead, load your key from
secure storage (like a secrets manager), or from environment variables that are set securely.
Double check that your key is not stored in your codebase, as anyone with access to your
source code (or who obtains a copy of your source code) could abuse your key. You can easily
search for your key with <code dir="auto">git grep</code>:
- Terminal window<pre data-language="sh"><code><div class="ec-line"><div class="code"><span style="--0:#919F9F;--1:#5F636F"># Search a git repository for Runway API key prefixes</span></div></div><div class="ec-line"><div class="code"><span style="--0:#82AAFF;--1:#3B61B0">git</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#ECC48D;--1:#3B61B0">grep</span><span style="--0:#D6DEEB;--1:#403F53"> </span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#ECC48D;--1:#984E4D">key_</span><span style="--0:#D9F5DD;--1:#111111">"</span></div></div></code></pre>
Recommended key storage methods:
HashiCorp Vault
- AWS Secrets Manager
- Google Cloud Secret Manager
- Azure Key Vault
- Render environment variables
- Heroku config vars
### Stop sharing keys
Section titled “Stop sharing keys”
Create API keys liberally and revoke them when they are no longer needed. If you have a
staging environment, create a new API key for it that’s separate from your production API
key. If you create keys for developers to test with on their local machines, each developer
should have their own key.
Any keys that are shared between individuals or environments should be disabled and
replaced.
## 4. Monitor your integration
Section titled “4. Monitor your integration”
Knowing how your integration is behaving in production is important for diagnosing issues.
We recommend a few metrics for you to measure:
- **API error rate**: While some errors are expected (like <code dir="auto">404 Not Found</code> errors when
making idempotent task deletion requests), you should be sure that you are not receiving
errors in production. Errors like <code dir="auto">429 Too Many Requests</code> indicate that your integration
has been temporarily shut off after reaching a limit.
- **API request count**: You should know how many requests your integration is making
per day. This will help you understand how many credits you are using and how close you
are to your tier limits.
- **Throttled task count**: While it’s safe to treat tasks whose status is <code dir="auto">THROTTLED</code> as
though they are <code dir="auto">PENDING</code>, too many throttled tasks could be a sign that your integration
is approaching your generation limit.
### Ensure you’re receiving emails
Section titled “Ensure you’re receiving emails”
You’ll receive emails about your integration at the email address that you signed up for the
developer portal with. Make sure that this email address is monitored and that emails from
Runway are not being marked as spam. You’ll receive emails about autobilling charges and
charge failures: failing to receive these notices may cause your integration to run out of
credits.
### Avoid account suspension
Section titled “Avoid account suspension”
Runway will moderate unsafe requests. Too many moderated requests will lead to account suspension.
Ensure that the use case for your integration is not in our moderated categories.
If needed, ensure you have implemented content moderation before making requests to Runway.
             Pricing        Playground ↗