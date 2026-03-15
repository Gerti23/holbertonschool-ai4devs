# Architecture Comparison: Monolith vs Microservices (SmartCloset Lite)

| Aspect | Monolith | Microservices | Winner & Why |
|---|---|---|---|
| Scalability | Scale the whole app together (app + DB as one unit). | Scale only the hot services (e.g., Media/Search) independently. | **Microservices**: more flexible scaling when different parts have different loads. |
| Development speed (small team) | One codebase, fewer moving parts, easier debugging. | Many repos/services, contracts, versioning, more coordination. | **Monolith**: faster for a solo developer and a 6-week timeline. |
| Deployment & DevOps | Single deployment pipeline, simpler monitoring. | Multiple deployments, service discovery, distributed tracing, more tooling. | **Monolith**: much simpler to deploy and operate early on. |
| Fault tolerance | A bug or spike can impact the entire app if not isolated well. | Failures can be isolated (e.g., Suggestions down, core CRUD still works). | **Microservices**: better isolation if designed well (with retries/timeouts). |
| Cost (early stage) | Fewer servers/services; cheaper hosting and monitoring. | More infrastructure (multiple services, logs, metrics), higher overhead. | **Monolith**: lower cost and less operational overhead at small scale. |
| Data consistency | Single database makes joins/transactions straightforward. | Cross-service data needs APIs/events; consistency is harder. | **Monolith**: simpler consistency for items↔outfits↔planner relationships. |
| Team autonomy (large org) | Changes can create bottlenecks in one shared codebase. | Teams can own services and release independently. | **Microservices**: better for multiple teams working in parallel. |
| Security surface area | One perimeter to secure; fewer inter-service attack paths. | Many service endpoints + internal traffic to secure. | **Monolith**: smaller surface area and fewer security concerns early on. |

## Summary
For **SmartCloset Lite** (solo, ~6 weeks), a **monolith** is usually the best starting point because it minimizes complexity and speeds up delivery. Microservices can be a good future evolution if the app grows (high traffic, multiple teams, heavy media/search workloads).
