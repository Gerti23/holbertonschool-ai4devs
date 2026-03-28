# Benchmark Tasks

## Task 1 - User Registration Endpoint
**Estimated Time**: 20–30 minutes  
**Requirements**: Implement `POST /users` endpoint with payload validation and duplicate email check. Persist users in memory or local JSON file.  
**Inputs**: JSON body `{ "name": string, "email": string }`  
**Outputs**: JSON response `{ "id": number|string, "name": string, "email": string }` on success.  
**Acceptance Criteria**:
- Returns `201` with created user when payload is valid.
- Returns `400` when `name` is missing/empty.
- Returns `400` when `email` format is invalid.
- Returns `409` when email already exists.
- Response includes generated `id`.

## Task 2 - Refactor Price Calculator with Tests
**Estimated Time**: 15–25 minutes  
**Requirements**: Refactor a `calculateTotal(items, taxRate, discountCode)` function into smaller helper functions while preserving behavior. Add unit tests for common and edge cases.  
**Inputs**:
- `items`: array of `{ price: number, quantity: number }`
- `taxRate`: decimal number (e.g., `0.16`)
- `discountCode`: optional string (`"NONE"`, `"SAVE10"`)
**Outputs**: Final numeric total rounded to 2 decimals.  
**Acceptance Criteria**:
- Existing behavior remains unchanged for valid inputs.
- At least 5 unit tests are added and passing.
- Handles empty `items` array and returns `0`.
- Applies `SAVE10` discount correctly before tax.
- Code is split into at least 2 helper functions.

## Task 3 - Log Parser CLI Summary
**Estimated Time**: 20–30 minutes  
**Requirements**: Create a CLI script that reads an application log file and prints a summary of log counts by level (`INFO`, `WARN`, `ERROR`) plus the top 3 most frequent error messages.  
**Inputs**:
- Command: `python3 log_summary.py <path-to-log-file>`
- Log line format: `YYYY-MM-DD HH:MM:SS LEVEL Message...`
**Outputs**:
- Terminal summary report with:
  - Count per level
  - Top 3 `ERROR` messages with frequencies
**Acceptance Criteria**:
- Script exits with non-zero code if file path is missing or file does not exist.
- Correctly counts `INFO`, `WARN`, and `ERROR` lines.
- Ignores malformed lines without crashing.
- Prints top 3 error messages sorted by frequency (desc).
- Runs successfully on a sample file of at least 100 lines.

## Task 4 - Frontend Form Validation
**Estimated Time**: 15–25 minutes  
**Requirements**: Build a small signup form (`name`, `email`, `password`) with client-side validation and inline error messages. Submit button remains disabled until form is valid.  
**Inputs**:
- User text input in browser fields.
- Validation rules:
  - `name` minimum 2 chars
  - valid `email`
  - `password` minimum 8 chars with at least 1 number
**Outputs**:
- Inline validation messages and enabled submit state when valid.
- Submitted payload logged to console or displayed on page.
**Acceptance Criteria**:
- Validation feedback appears on blur or submit.
- Submit is blocked when any field is invalid.
- Error messages clear when field becomes valid.
- Submit button enables only when all fields pass validation.
- Form submission produces structured payload with all fields.
