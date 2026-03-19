# API Requirements – Virtual Wardrobe API

## Domain Overview
A personal wardrobe management domain that lets users catalog clothing items, build outfits from those items, and plan outfits on a calendar. The API supports item metadata (categories, colors, seasons, tags), outfit composition, wear history, and basic recommendation inputs (e.g., weather/season preferences).

## Target Users
- Mobile/Web clients: provide wardrobe, outfit building, and planning UX
- Third-party integrations (optional): import items from e-commerce receipts or photo scanners
- Data/ops tooling (internal): support moderation, troubleshooting, and user support (admin-only)

## Core Operations (8–12)
1. Create user account
2. Authenticate user (login) and refresh session
3. Get current user profile
4. Create wardrobe item (with optional image reference)
5. Update wardrobe item (metadata, tags, archived status)
6. List/search wardrobe items (filters: category, color, season, tag, archived)
7. Create outfit (name/occasion + item references)
8. Update outfit (items, name/occasion, archived status)
9. List outfits (filters: occasion, recently used, archived)
10. Create or update a plan entry (assign outfit to a date/time slot)
11. List plan entries for a date range (week/month view)
12. Mark outfit as worn (creates wear history entry)

## Data Validation Rules
- **Authentication**
  - Email must be valid format and normalized (case-insensitive compare).
  - Password must meet minimum strength requirements (e.g., length ≥ 8; server-enforced).

- **Wardrobe Items**
  - `name` is required, trimmed, 1–80 chars.
  - `category` must be one of an allowed set (e.g., `top`, `bottom`, `outerwear`, `dress`, `shoes`, `accessory`).
  - `color` must be from an allowed palette or a validated hex code (choose one approach and enforce consistently).
  - `season` must be one of: `spring`, `summer`, `fall`, `winter`, `all`.
  - `tags` max 20 per item; each tag 1–24 chars; tags are case-insensitive unique per item.
  - `imageUrl` (or `imageRef`) must be a valid URL/reference; only allow approved domains/buckets.
  - Archived items must not be returned in default lists unless `includeArchived=true`.

- **Outfits**
  - Outfit must reference at least 2 wardrobe items.
  - All referenced item IDs must exist and belong to the authenticated user.
  - An outfit must not include archived items (unless explicitly allowed for legacy outfits, but should be blocked by default).
  - `occasion` (optional) must be from an allowed set (e.g., `casual`, `work`, `formal`, `sport`, `event`) if provided.

- **Planner / Wear History**
  - Planner entry date must be a valid ISO-8601 date; time zone handling must be explicit.
  - Only one planned outfit per user per time slot (define slot granularity: day-level or AM/PM).
  - Mark-as-worn must not create duplicate wear entries for the same outfit and timestamp window (e.g., prevent rapid double taps).

## Non-Functional Requirements
- **Latency / Performance**
  - P95 response time < 200ms for read endpoints (list/search) under normal load.
  - P95 response time < 400ms for write endpoints (create/update) under normal load.
  - Support pagination for all list endpoints (cursor or page/limit); default page size 20, max 100.

- **Authentication & Authorization**
  - JWT-based auth (access token) required for all non-public endpoints.
  - Refresh token rotation and revocation supported.
  - Object-level authorization enforced: users can access only their own items/outfits/plans.

- **Rate Limiting**
  - Per-user limits (example): 60 requests/minute for standard endpoints.
  - Stricter limits for auth endpoints (example): 10 login attempts/minute per IP + per account.
  - Return `429` with retry guidance.

- **Reliability & Error Handling**
  - Use consistent error envelope with machine-readable codes.
  - Idempotency keys supported for create operations that could be retried by mobile clients (e.g., create item, create plan entry).

- **Security & Privacy**
  - TLS required.
  - Validate and sanitize all user-provided text to prevent injection.
  - Image upload/import must be scanned/validated; restrict content types.
  - Provide data export endpoint (user data portability) and delete account endpoint (privacy compliance).

- **Observability**
  - Structured logs with request IDs.
  - Basic metrics: request rate, error rate, latency, and DB time.
