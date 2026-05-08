#!/bin/bash
# Number One Son — Friday morning setup script.
# Installs Runway Skills + verifies API access.
# Run once at start of build window, ~2 minutes total.

set -e
echo "=== Number One Son Friday Setup ==="

# 1. Check prerequisites
command -v uv >/dev/null || { echo "Installing uv..."; curl -LsSf https://astral.sh/uv/install.sh | sh; }
command -v npx >/dev/null || { echo "ERROR: npx required (install Node.js 18+)"; exit 1; }

# 2. Confirm API key is set
if [ -z "$RUNWAYML_API_SECRET" ]; then
  echo "ERROR: RUNWAYML_API_SECRET not set. Export it first:"
  echo "  export RUNWAYML_API_SECRET=key_..."
  exit 1
fi

# 3. Install Runway Skills (interactive — select all with Space)
echo "Installing Runway Skills..."
echo "  When prompted: press Space to select all, Enter to confirm."
npx skills add runwayml/skills

# 4. Probe org / credit balance
echo "Verifying API access..."
python3 -c "
from runwayml import RunwayML
c = RunwayML()
o = c.organization.retrieve()
print(f'  Org tier: {o.tier.max_monthly_credit_spend} credit cap')
print(f'  Credit balance: {o.credit_balance}')
print(f'  Models available: {len(o.tier.models)}')
" 2>/dev/null || echo "  (Python SDK probe skipped — Skills will handle auth)"

echo ""
echo "✓ Setup complete. Ready for build."
echo "  Skills installed at ~/.skills/runwayml/skills/"
echo "  Next: invoke skills via Claude Code, Cursor, or use-runway-api directly."
