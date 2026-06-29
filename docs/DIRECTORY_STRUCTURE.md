# Production-Ready Directory Structure

A heavy Django app needs a clean separation between development, production configs, and documentation. This repository follows that layout.

```
sevendyne_hrms/
├── .github/
│   └── workflows/          # CI/CD pipelines (run pytest, linting)
├── config/                 # Root Django configuration directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py         # Common settings
│   │   ├── local.py        # Local dev settings
│   │   └── production.py   # Production environment settings
│   ├── urls.py
│   └── wsgi.py
├── apps/                   # Clean separation of Django apps
│   ├── authentication/     # Custom user management, roles (→ apps/user)
│   ├── attendance/         # Check-in, check-out logic (→ apps/employee)
│   ├── payroll/              # Salary slips, fixed-point calculation
│   └── leave_tracker/        # Leave management (→ apps/employee)
├── compose/                # Production & local deployment Docker files
│   ├── local/
│   └── production/
├── docs/                   # Full documentation folder
├── README.md               # The project storefront
├── CONTRIBUTING.md         # Guidelines for candidates/collaborators
├── docker-compose.yml      # Local orchestration file
└── requirements/           # Split dependencies
    ├── base.txt
    ├── local.txt
    └── production.txt
```

## App Domain Mapping

| Blueprint folder | Django implementation | Responsibility |
|------------------|----------------------|----------------|
| `apps/authentication/` | `apps/user` | Login, registration, groups |
| `apps/attendance/` | `apps/employee` | `AttendanceRegister` |
| `apps/leave_tracker/` | `apps/employee` | `Leave`, `LeaveType` |
| `apps/payroll/` | `apps/payroll` | Payroll items, salary slips |

Additional apps: `main`, `hrms`, `candidate`, `client`, `job`, `asset`.

## Settings Modules

| Environment | Import path |
|-------------|-------------|
| Local development | `config.settings.local` |
| Production | `config.settings.production` |

Set via `DJANGO_SETTINGS_MODULE` or `manage.py` defaults.
