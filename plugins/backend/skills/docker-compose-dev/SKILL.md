---
name: docker-compose-dev
description: "Docker and Docker Compose for local development: a dev PostgreSQL container, ports, volumes, health checks, env files, running the app against it, Docker Desktop on Windows. Use when editing docker-compose.yml or a Dockerfile, starting or resetting a dev database, a port clash, a container that won't start, or wiring npm/dotnet dev scripts to Docker."
---

# Docker Compose for dev

Keep Docker to what dev needs: usually just the database. The app itself runs on the host so hot reload and debuggers work.

## A dev database service
- Pin the image tag (`postgres:17`), never `latest`.
- Map a non-default host port when a local Postgres may exist (for example `5433:5432`), and put that port in the connection string.
- Named volume for data so a restart keeps it. `docker compose down` keeps the volume; `docker compose down -v` deletes the data, so say so before running it.
- Add a `healthcheck` (`pg_isready -U <user>`) and make dependants wait on `condition: service_healthy`.
- Dev credentials live in the compose file and the project's dev docs only. Real secrets never go in tracked files.

## Everyday commands
- Start only the database: `docker compose up -d db`
- State and logs: `docker compose ps`, `docker compose logs -f db`
- Stop, keep data: `docker compose down`
- Reset data (destructive, confirm first): `docker compose down -v`
- Run SQL: `docker compose exec db psql -U <user> -d <db>`

## Windows notes
- Docker Desktop must be running first (and the WSL2 backend started); "cannot connect to the Docker daemon" almost always means it is not.
- Bind-mounted paths from Windows drives are slow; prefer named volumes for data.
- Line endings: shell scripts mounted into Linux containers need LF, not CRLF.

## When it fails
1. `docker compose ps`: is the container up, and healthy?
2. `docker compose logs db`: password, version or data-directory errors show here (a changed `POSTGRES_PASSWORD` is ignored once the volume exists; reset the volume or change the password inside).
3. Port in use: `netstat -ano | findstr :5433`, then change the mapping or stop the other process.
4. App cannot connect: from the host use `localhost` and the mapped host port; the service name and container port only work from another container.

## Wiring scripts
- A single `dev` script should start the database (`docker compose up -d db`), wait for health, then start the API and the web dev server, so a new machine needs one command.
- If the repo has IDE run configurations for this, keep them in step with the scripts.
