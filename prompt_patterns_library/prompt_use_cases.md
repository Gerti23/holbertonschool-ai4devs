# Prompt Use Cases

## Code Quality
- **Refactoring**
  - **Goal**: Improve readability, maintainability, and performance without changing behavior  
  - **Input**: Source function/class in [LANGUAGE] + constraints (style guide, complexity limit)  
  - **Output**: Refactored code + explanation of changes and trade-offs  

- **Style Enforcement**
  - **Goal**: Enforce consistent naming, formatting, and idioms across a codebase  
  - **Input**: Code block or file + style rules (ESLint/Black/GoFmt conventions, naming rules)  
  - **Output**: Rewritten code following the style + list of rule violations fixed  

- **Dead Code & Smell Detection**
  - **Goal**: Identify unused code, risky patterns, and maintainability “smells”  
  - **Input**: File(s) or module + context about expected behavior and usage  
  - **Output**: Ranked list of issues + suggested safe removals/rewrites  

## Debugging
- **Stack Trace Triage**
  - **Goal**: Explain an error quickly and propose the most likely fix  
  - **Input**: Stack trace + relevant code snippet + runtime/version info  
  - **Output**: Root-cause hypothesis + minimal fix + verification steps  

- **Logic Bug Investigation**
  - **Goal**: Fix “wrong output” problems when code runs but behaves incorrectly  
  - **Input**: Failing input/output example + function code + expected behavior description  
  - **Output**: Explanation of the incorrect logic + corrected code + added edge-case tests  

- **Performance Regression Diagnosis**
  - **Goal**: Find why code became slower and how to optimize safely  
  - **Input**: Before/after timings + hot path code + data sizes/constraints  
  - **Output**: Bottleneck analysis + optimized implementation + measurement plan  

## Documentation
- **API Doc Generation**
  - **Goal**: Produce accurate docs so others can use the API correctly  
  - **Input**: Function signatures + examples + error cases + constraints  
  - **Output**: Docstring/Markdown docs + usage examples + parameter/return details  

- **README / Onboarding Guide**
  - **Goal**: Help new developers run, test, and contribute quickly  
  - **Input**: Project structure + commands + env vars + prerequisites  
  - **Output**: Step-by-step setup/run/test instructions + troubleshooting section  

- **Change Log / Release Notes Drafting**
  - **Goal**: Summarize changes clearly for users and stakeholders  
  - **Input**: PR description, commit summary, or list of changes  
  - **Output**: Release notes with highlights, breaking changes, and migration notes  

## Testing
- **Unit Test Authoring**
  - **Goal**: Add targeted tests that lock in expected behavior and prevent regressions  
  - **Input**: Function/module code + expected behavior + edge cases  
  - **Output**: Unit tests (framework-specific) + explanation of coverage and gaps  

- **Test Failure Explanation**
  - **Goal**: Explain why a test failed and how to fix code or test correctly  
  - **Input**: Failing test output + relevant code + recent changes  
  - **Output**: Failure analysis + fix options + recommended next test to run  

- **Mocking & Test Doubles Setup**
  - **Goal**: Make code testable by isolating external dependencies (DB, network, clock)  
  - **Input**: Code that calls external services + desired test behavior  
  - **Output**: Mock/stub strategy + example tests + suggested refactor for dependency injection  

## Architecture & Design
- **Module Boundary Definition**
  - **Goal**: Split responsibilities cleanly to reduce coupling and improve scalability  
  - **Input**: Current folder/module layout + pain points + future features  
  - **Output**: Proposed module boundaries + data flow summary + migration steps  

- **Dependency Review**
  - **Goal**: Decide whether to add, replace, or remove a library safely  
  - **Input**: Current dependency + requirements (license, size, performance, security)  
  - **Output**: Recommendation + risks + integration plan + rollback plan  

- **Design Review Prompt**
  - **Goal**: Stress-test a proposed solution before implementing it  
  - **Input**: Design doc/approach + constraints (latency, cost, security, maintainability)  
  - **Output**: Identified risks + alternative designs + questions to validate assumptions  
