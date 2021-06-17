# actions-ftx-auto-stake

Automatically Re-stake your FTX Staking rewards using GitHub Actions

## Important notice

FTX restricts API access from US IP address. Since GitHub-hosted runner runs on US region, you need prepare your self-hosted runner which hosted on non-restricted region, to make it work.

## How to use

1. Fork this repository
2. Open secrets page and add following secrets. `https://github.com/[username]/actions-ftx-auto-stake/settings/secrets/actions`
   - `FTX_API_KEY` (Required)
   - `FTX_API_SECRET` (Required)
   - `FTX_STAKE_SYMBOLS` (Optional) ... comma-separated coin symbols which you want to automatically re-stake. Re-stake all available coins if not provided.
3. Done. It will automatiaclly re-stake every 10 minutes.
