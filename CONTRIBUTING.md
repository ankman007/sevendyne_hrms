# Contributing to Sevendyne HRMS

We love community collaboration and use this repository to discover engineering talent for Sevendyne projects. **We built this system over one year with a small team of three in our local office** — and we want **collaborators to come forward**, use it, improve it, and grow with us. **More strong open projects from Sevendyne are on the way.**

If you are a candidate or contributor looking to collaborate, follow this workflow:

## The Evaluation Process

1. **Find an Issue:** Look at our GitHub Issues page labeled with `good-first-issue` or `candidate-challenge`.
2. **Fork & Branch:** Fork this repository and create a descriptive branch (e.g., `feature/attendance-api`).
3. **Follow Our Standards:**
   - Write automated tests for all new logic using `pytest-django`.
   - Ensure all code complies with PEP 8 standards (use `black` and `flake8`).
4. **Submit a Pull Request:** Open a PR against our `main` branch.

## Definition of Done for PRs

We treat engineering discipline with high priority. Your PR will only be reviewed if:

- The CI pipeline passes perfectly (0 linting errors, 100% test success).
- Database migrations are cleanly generated and optimized.
- Clear documentation is provided for any new APIs or methods.

## Local Development Setup

Any company or contributor should be able to spin this up in about one minute with Docker — no manual Python, PostgreSQL, or Redis setup required:

```bash
git clone https://github.com/sevendyne/sevendyne_hrms.git
cd sevendyne_hrms
docker compose up --build
```

Open http://localhost:8000 — demo users are seeded automatically.

Or install dependencies manually:

```bash
pip install -r requirements/local.txt
export DJANGO_SETTINGS_MODULE=config.settings.local
python manage.py migrate
python manage.py loaddata countries states
python manage.py seed_demo_data
python manage.py runserver
```

## Code Style

- Format with `black`
- Lint with `flake8`
- Run `pytest` before opening a PR

## What We're Looking For

- Engineers who read the codebase before changing it
- Clean migrations and tests with every feature
- Clear PR descriptions and documentation updates when behavior changes

## Questions?

Open a GitHub Discussion or reach out via the issue tracker. We review PRs regularly and are actively looking for people who want to work on **this project and upcoming Sevendyne repos**.
