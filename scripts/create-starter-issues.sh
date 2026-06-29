#!/usr/bin/env bash
# Create labels and starter issues for sevendyne_hrms contributor funnel.
# Prerequisites: gh auth login
set -euo pipefail

REPO="sevendyne/sevendyne_hrms"

echo "▶ Creating labels (ignore errors if they already exist)..."
for spec in \
  "good-first-issue:0e8a16:Good for newcomers" \
  "candidate-challenge:1d76db:Skills evaluation task" \
  "documentation:0075ca:Docs improvements" \
  "tests:fbca04:Test coverage" \
  "enhancement:a2eeef:New feature or improvement" \
  "bug:d73a4a:Something is broken" \
  "attendance:f9d0c4:Attendance module"; do
  IFS=':' read -r name color desc <<< "$spec"
  gh label create "$name" --repo "$REPO" --color "$color" --description "$desc" 2>/dev/null || true
done

create_issue() {
  local title="$1"
  local body="$2"
  shift 2
  local labels=("$@")
  local label_args=()
  for l in "${labels[@]}"; do
    label_args+=(--label "$l")
  done
  # Skip if issue with same title already open
  if gh issue list --repo "$REPO" --state open --search "in:title \"$title\"" --json title --jq '.[].title' 2>/dev/null | grep -Fxq "$title"; then
    echo "  ⏭  Already exists: $title"
    return 0
  fi
  gh issue create --repo "$REPO" --title "$title" --body "$body" "${label_args[@]}"
  echo "  ✓ Created: $title"
}

echo "▶ Creating starter issues..."

create_issue "docs: add dashboard screenshot to README" \
"## Task
Capture the admin dashboard after \`docker compose up\`, save to \`docs/images/dashboard.png\`, and add it to the README below the hero badges.

## Acceptance criteria
- [ ] Screenshot saved at \`docs/images/dashboard.png\`
- [ ] README updated with the image
- [ ] Image is reasonably sized (compress if > 500KB)

## How to run locally
\`\`\`bash
docker compose up --build
# Login: admin / admin → http://localhost:8000/app/login/
\`\`\`

Good first issue for contributors new to the repo." \
  good-first-issue documentation

create_issue "feat: export monthly attendance register as CSV" \
"## Task
Add a download action on the attendance list view in \`apps/employee\` to export the monthly attendance register as CSV.

## Acceptance criteria
- [ ] Export button/action on attendance list UI
- [ ] CSV includes employee, date, and status columns
- [ ] \`pytest-django\` tests for the export view
- [ ] CI passes (flake8, black, pytest)

## Module
\`apps/employee\` — see \`AttendanceRegister\` model.

Candidate challenge — slightly harder than a docs-only task." \
  candidate-challenge enhancement attendance

create_issue "feat: add /health/ endpoint for Docker orchestration" \
"## Task
Add a simple \`/health/\` endpoint that returns HTTP 200 and reports database connectivity status. Useful for Docker/Kubernetes health checks.

## Acceptance criteria
- [ ] \`GET /health/\` returns JSON with \`status\` and \`database\` fields
- [ ] Returns 503 if database is unreachable
- [ ] Documented in \`docs/DOCKER.md\`
- [ ] Optional: pytest for healthy response

## Example response
\`\`\`json
{\"status\": \"ok\", \"database\": \"connected\"}
\`\`\`" \
  good-first-issue enhancement

create_issue "ui: add GitHub star link on login page footer" \
"## Task
Add a small footer on the login page (\`templates/authentication/login.html\`) linking to the GitHub repo with a star CTA and MIT license note.

## Acceptance criteria
- [ ] Link to https://github.com/sevendyne/sevendyne_hrms
- [ ] Mentions MIT license / open source
- [ ] Matches existing login page styling

## File
\`templates/authentication/login.html\`" \
  good-first-issue documentation

create_issue "test: add tests for seed_demo_data management command" \
"## Task
Add \`pytest-django\` tests for the \`seed_demo_data\` management command in \`apps/main/management/commands/seed_demo_data.py\`.

## Acceptance criteria
- [ ] Test verifies admin user is created (\`admin\` / \`admin\`)
- [ ] Test verifies HRMS client (\`hrmsclient1\`) with \`hrms_clients\` group
- [ ] Test verifies employee (\`employee1\`) with \`employee_group\` group
- [ ] Tests are idempotent (running seed twice does not break)
- [ ] CI passes

## Run tests
\`\`\`bash
pytest apps/main/ -k seed -v
\`\`\`" \
  good-first-issue tests

echo ""
echo "✅ Done. Pin 2–3 issues at: https://github.com/$REPO/issues"
gh issue list --repo "$REPO" --state open --limit 10
