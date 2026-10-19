---
name: aspnet-efcore-postgres
description: "ASP.NET Core (.NET 10) minimal APIs with EF Core and PostgreSQL (Npgsql): endpoints, migrations, cookie auth with Identity, background workers, OpenAPI to TypeScript types, idempotent commands, xUnit and database tests. Use when editing a .NET server, a .csproj/.slnx solution, EF Core migrations or Npgsql config, or when a server-owns-all-state game or app needs a command/ledger design."
---

# ASP.NET Core + EF Core + PostgreSQL

For a server-authoritative app: the server owns all state, the client only sends commands. Check the project's own CLAUDE.md first; where it disagrees with this, it wins. Verify any API against current Microsoft docs before relying on it from memory (.NET 10 is newer than most training data).

## Solution layout
- `Api` (endpoints, auth, hosting), `Application` (commands/queries), `Domain` (pure rules, no EF, no I/O; unit-test it hardest), `Infrastructure` (DbContext, migrations, workers). Dependencies point inward: Domain depends on nothing.
- Keep `Directory.Build.props` for shared settings (nullable on, warnings as errors if the project already does).

## Endpoints
- Minimal APIs grouped per feature (`app.MapGroup("/api/x")` in an `Endpoints/` folder). Return typed results (`TypedResults.Ok/NotFound/Problem`) so OpenAPI is accurate.
- Commands are POSTs that carry an idempotency key. Store the key with the result in the same transaction as the change; a repeat returns the stored result and changes nothing.
- Views are GETs shaped for the screen, not entity dumps.
- OpenAPI comes from `Microsoft.AspNetCore.OpenApi`; generate TypeScript types from it in a script and fail the check script when the committed types are stale.

## EF Core + Npgsql
- One DbContext in Infrastructure; entity configuration in `IEntityTypeConfiguration<T>` classes, not attributes.
- Migrations: `dotnet ef migrations add <Name> -p <Infrastructure project> -s <Api project>`, then `dotnet ef database update` against the dev database. Commit the migration with the model change. Never edit an applied migration; add a new one.
- Use `decimal`/integers for money and quantities (no `double`). Use `xmin` or an explicit version column for optimistic concurrency where two writers can meet.
- Lock a unit of state (a company, an account) with a short transaction plus a row lock or advisory lock before changing it, so concurrent commands apply one after another.
- Time: take a clock abstraction (`TimeProvider`) so tests control it. Store UTC.
- Randomness that must replay: a seeded generator (for example PCG32) kept in the entity, never `Random.Shared`.

## Auth
- ASP.NET Core Identity with cookie auth for a browser client: HttpOnly, SameSite, antiforgery for state-changing calls if cross-site is possible. Never put secrets in the client or in tracked config; use user-secrets/env vars.

## Background workers
- `BackgroundService` for the event queue: poll due rows, process each in its own transaction, mark done in the same transaction, catch per-item so one failure does not stop the loop. Test the restart case: kill mid-batch, start again, nothing runs twice or is lost.

## Tests
- xUnit. Domain tests are plain and fast. Database tests go behind a trait (`[Trait("Category","Db")]`) and run only when a connection string env var is set, so `dotnet test` stays green without Docker.
- Simulation rules: also keep a reference run, a long scenario compared against a slow step-by-step version of the same rules.
- Run with `dotnet test`; filter with `--filter Category=Db` or `--filter "FullyQualifiedName~Name"`.

## Pitfalls
- A tracked `appsettings.json` with a real password. Use the dev compose credentials only.
- Forgetting to await inside a transaction scope, or holding a transaction open across an HTTP call.
- Changing an enum's numeric values after data exists.
- Regenerating API types but not committing them.
