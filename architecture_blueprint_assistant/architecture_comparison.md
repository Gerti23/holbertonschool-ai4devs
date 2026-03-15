# Architecture Comparison: Monolith vs Microservices (SmartCloset Lite)

| Aspect | Monolith | Microservices | Winner & Why |
|---|---|---|---|
| Scalability | Scale the whole app together (app + DB as one unit). | Scale only the hot services (e.g., Media/Search) independently. | **Microservices**: more flexible scaling when different parts have different loads. |
| Deployment & DevOps Complexity | Single deployment pipeline, simpler monitoring. | Multiple deployments, service discovery, distributed tracing, more tooling. | **Monolith**: much simpler to deploy and operate early on. |
| Engineering Complexity | One codebase, fewer moving parts, easier debugging. | Many services, contracts, versioning, and coordination overhead. | **Monolith**: better fit for a solo developer and a 6-week timeline. |
| Cost (early stage) | Fewer servers/services; cheaper hosting and monitoring. | More infrastructure and observability tooling; higher overhead. | **Monolith**: lower cost and less operational overhead at small scale. |
| Fault Tolerance | A bug or spike can impact the entire app if not isolated well. | Failures can be isolated (e.g., Suggestions down, core CRUD still works). | **Microservices**: better isolation if designed well (with retries/timeouts). |

## Summary
For **SmartCloset Lite** (solo, ~6 weeks), a **monolith** is usually the best starting point because it minimizes complexity and speeds up delivery. Microservices can be a good future evolution if the app grows (high traffic or heavier operational needs).
