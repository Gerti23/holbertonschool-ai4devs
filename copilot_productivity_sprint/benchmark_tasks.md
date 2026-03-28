# Benchmark Tasks

## Task 1 - User Registration Endpoint
**Estimated Time**: 20–30 minutes  
**Requirements**: Implement `POST /users` with name/email validation and duplicate email prevention; persist to in-memory storage.  
**Inputs**: HTTP `POST /users` with JSON `{ "name": string, "email": string }`.  
**Outputs**: HTTP response with status code and JSON body containing created user `{ "id", "name", "email" }` or validation error.  
**Acceptance Criteria**:
- Returns `201` and created user object when payload is valid.
- Returns `400` for missing or empty `name`.
- Returns `400` for invalid `email` format.
- Returns `409` when email already exists.
- Success response includes a generated `id`.

## Task 2 - Refactor Price Calculator with Tests
**Estimated Time**: 15–25 minutes  
**Requirements**: Refactor `calculateTotal(items, taxRate, discountCode)` into smaller helpers without changing behavior and add unit tests.  
**Inputs**: Function arguments `items` (array of `{ price, quantity }`), `taxRate` (decimal), and `discountCode` (`"NONE"` or `"SAVE10"`).  
**Outputs**: Numeric total rounded to two decimals and passing unit test results.  
**Acceptance Criteria**:
- Behavior matches original implementation for valid inputs.
- Adds at least 5 passing unit tests.
- Returns `0` for an empty `items` array.
- Applies `SAVE10` discount before tax calculation.
- Uses at least 2 helper functions in the refactor.

## Task 3 - Log Parser CLI Summary
**Estimated Time**: 20–30 minutes  
**Requirements**: Create `log_summary.py` to read a log file and print counts by `INFO`, `WARN`, `ERROR` plus top 3 frequent error messages.  
**Inputs**: CLI command `python3 log_summary.py <path-to-log-file>` and log lines in format `YYYY-MM-DD HH:MM:SS LEVEL Message...`.  
**Outputs**: Terminal report showing per-level counts and top 3 `ERROR` messages with frequencies.  
**Acceptance Criteria**:
- Exits with non-zero status when the file path is missing or invalid.
- Correctly counts `INFO`, `WARN`, and `ERROR` lines.
- Ignores malformed lines without crashing.
- Prints top 3 error messages sorted by descending frequency.
- Runs successfully on a sample log with at least 100 lines.

## Task 4 - Frontend Form Validation
**Estimated Time**: 15–25 minutes  
**Requirements**: Build a signup form with fields `name`, `email`, `password`; validate on client side and keep submit disabled until valid.  
**Inputs**: User-entered form values with rules: name min 2 chars, valid email format, password min 8 chars and at least 1 number.  
**Outputs**: Inline validation messages, submit-button enabled state when valid, and submitted structured payload.  
**Acceptance Criteria**:
- Shows validation feedback on blur or submit.
- Prevents submit when any field is invalid.
- Clears error message when a field becomes valid.
- Enables submit button only when all fields are valid.
- Produces structured payload with all three fields on submit.
