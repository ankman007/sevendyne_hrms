# Sevendyne Enterprise HRMS

![Build Status](https://img.shields.io/badge/tests-passing-success)
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
![Django Version](https://img.shields.io/badge/django-5.0%20LTS-green)

A robust, enterprise-grade Human Resource Management System built with Python and Django. Designed for easy containerized deployment across any office infrastructure.

## Our Story

This HRMS was built over **one year** by a **small team of three engineers** working together in our **local office space** at Sevendyne. We designed it for real businesses — not as a tutorial project, but as production software we use and iterate on every day.

We are opening this repository so **collaborators can come forward**, run it locally, extend it, and grow with us. **More high-quality open projects from Sevendyne are coming soon** — this HRMS is the first of several we plan to share with the community.

If you want to build with us, start here: fork the repo, pick an issue, and open a PR. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Features

- **Authentication** — Custom user management, roles, and role-based dashboards
- **Attendance** — Check-in, check-out, and attendance register logic
- **Payroll** — Salary slips and fixed-point payroll calculation
- **Leave Tracker** — Leave types, requests, and approval workflows
- **Recruitment** — Candidate and job portal modules

## Project Structure

```
sevendyne_hrms/
├── .github/
│   └── workflows/          # CI/CD pipelines (pytest, linting)
├── config/                 # Root Django configuration
│   ├── settings/
│   │   ├── base.py         # Common settings
│   │   ├── local.py        # Local dev settings
│   │   └── production.py   # Production environment settings
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/                   # Clean separation of Django apps
│   ├── authentication/     # → apps/user (roles, login)
│   ├── attendance/         # → apps/employee
│   ├── payroll/
│   ├── leave_tracker/      # → apps/employee
│   ├── main/, hrms/, candidate/, client/, job/, asset/
├── compose/                # Production & local Docker files
│   ├── local/
│   └── production/
├── docs/                   # Full documentation
├── requirements/           # Split dependencies
│   ├── base.txt
│   ├── local.txt
│   └── production.txt
├── docker-compose.yml      # Local orchestration
├── README.md
└── CONTRIBUTING.md         # Guidelines for candidates/collaborators
```

Full technical documentation: [docs/](docs/)

## Getting Started

Ensure you have [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed.

```bash
# Clone the repository
git clone https://github.com/sevendyne/sevendyne_hrms.git
cd sevendyne_hrms

# Spin up the entire infrastructure (App, DB, Cache)
docker compose up --build

# Migrations and demo users run automatically on first start.
# To re-seed manually:
docker compose exec web python manage.py seed_demo_data
```

Navigate to **http://localhost:8000** to access the portal.

### Demo Credentials

| Role     | Username      | Password       |
|----------|---------------|----------------|
| Admin    | `admin`       | `admin`          |
| Client   | `hrmsclient1` | `password@123`   |
| Employee | `employee1`   | `password@123`   |

Login URL: http://localhost:8000/app/login/

### Manual Setup (without Docker)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements/local.txt

# Configure PostgreSQL and set DATABASE_URL, then:
python manage.py migrate
python manage.py loaddata countries states
python manage.py seed_demo_data
python manage.py runserver
```

## Development

```bash
# Run tests
pytest

# Lint
flake8 apps config
black --check apps config
```

## Contributing

We use this repository to **discover engineering talent** and welcome **collaborators** who want to ship real features. Read [CONTRIBUTING.md](CONTRIBUTING.md) for the evaluation workflow, PR standards, and how to get involved.

## License

Proprietary — Sevendyne. Contact hr@sevendyne.com for licensing inquiries.
