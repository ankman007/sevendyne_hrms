# Docker — Plug-and-Play Setup

Any company or collaborator wanting to use this HRMS should be able to spin it up in about **one minute** without configuring Python, PostgreSQL, or Redis manually.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## One-Command Start

```bash
git clone https://github.com/sevendyne/sevendyne_hrms.git
cd sevendyne_hrms
docker compose up --build
```

On first boot the entrypoint automatically:

1. Waits for PostgreSQL
2. Runs `makemigrations` and `migrate`
3. Loads country/state fixtures
4. Seeds demo user accounts (`admin`, `hrmsclient1`, `employee1`)

Open **http://localhost:8000** when the web container is running.

## Services

The root `docker-compose.yml` defines:

| Service | Image | Purpose |
|---------|-------|---------|
| `db` | `postgres:15-alpine` | Primary database (`hrms_db`) |
| `redis` | `redis:7-alpine` | Celery broker (optional for basic usage) |
| `web` | Built from `compose/local/Dockerfile` | Django app on port 8000 |

## Reference Configuration

```yaml
services:
  db:
    image: postgres:15-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=hrms_db
      - POSTGRES_USER=sevendyne
      - POSTGRES_PASSWORD=securepassword

  web:
    build:
      context: .
      dockerfile: ./compose/local/Dockerfile
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgres://sevendyne:securepassword@db:5432/hrms_db

volumes:
  postgres_data:
```

See the live file at [`docker-compose.yml`](../docker-compose.yml) for the full stack including Redis and health checks.

## Useful Commands

```bash
# Run migrations manually
docker compose exec web python manage.py migrate

# Create a superuser
docker compose exec web python manage.py createsuperuser

# Re-seed demo accounts
docker compose exec web python manage.py seed_demo_data

# Stop and remove containers
docker compose down

# Reset database (destructive)
docker compose down -v
```

## Production

For production deployments, build with `compose/production/Dockerfile` (Gunicorn + `config.wsgi`). Set `DJANGO_SETTINGS_MODULE=config.settings.production` and provide `DATABASE_URL`, `DJANGO_SECRET_KEY`, and `DJANGO_ALLOWED_HOSTS` via your orchestrator.
