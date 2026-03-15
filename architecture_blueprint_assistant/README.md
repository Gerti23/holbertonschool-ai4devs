# Architecture Blueprint – SmartCloset Lite

## Overview
SmartCloset Lite is a simple web app for managing a personal closet. The core idea is to reduce “what should I wear?” friction by helping users: (1) add the clothes they already own, (2) build and save outfit combinations, and (3) plan what to wear on different dates. The product goal is a clean, beautiful UI with practical features that feel “fun” without being hard to build.

This blueprint intentionally avoids advanced account features (login/register, multi-user sharing, complex permissions) to keep the scope realistic for a solo developer and a ~6-week delivery window. Instead of a full user system, the app can use a single “Closet” workspace concept (an anonymous `closetId` stored in the browser). That approach still allows a backend database and photo storage, while keeping the overall system simple.

For the full application concept and constraints, see: [app_concept.md](./app_concept.md).

## Key Architecture Choices
For an MVP, the recommended path is a **monolithic architecture** (one backend API, one data model, one release unit). This choice is mainly driven by execution speed and simplicity:

- One codebase and one deployment pipeline.
- Easier debugging (no distributed failures).
- Straightforward data consistency across items, outfits, and planning.

Monolith deliverables:
- Diagram: [monolith_architecture.mmd](./monolith_architecture.mmd)
- Component description: [monolith_description.md](./monolith_description.md)

As an advanced exercise (and a future-scale option), the same app is also expressed as **microservices**. This version splits responsibilities into independent services (wardrobe, outfits, planner, media, suggestions, search, etc.) behind an API gateway. That decomposition can be helpful later if load grows unevenly (e.g., media and search become much heavier than the rest), or if multiple teams need independent release cycles.

Microservices deliverables:
- Diagram: [microservices_architecture.mmd](./microservices_architecture.mmd)
- Service description: [microservices_description.md](./microservices_description.md)

## Monolith vs Microservices (Insights)
The comparison matrix focuses on practical trade-offs relevant to SmartCloset Lite:

- **Monolith is stronger early**: it reduces DevOps and engineering complexity, which matters most for a solo MVP.
- **Microservices are stronger at scale**: they allow independent scaling and better fault isolation when services have different workloads.

A key takeaway for this project is that “best architecture” depends on context. In a 6-week solo build, the main risk is not theoretical scalability; it is shipping incomplete flows due to too much infrastructure overhead. Starting monolithic keeps effort focused on building a polished UI and complete end-to-end functionality.

See the full table here: [architecture_comparison.md](./architecture_comparison.md).

## Data Model
The data model supports the three main user workflows:

1. **Wardrobe**: store clothing items with basic attributes (category, color, season, tags) plus a simple status (available vs. in laundry).
2. **Outfits**: save combinations of items (many-to-many via a join entity) with light metadata like occasion and season.
3. **Planner**: schedule outfits by date and enable features like “recently worn” hints.

Data model deliverables:
- ER diagram: [data_model.mmd](./data_model.mmd)
- Documentation: [data_model.md](./data_model.md)

## Lessons Learned (AI Contribution)
AI is most helpful for accelerating **structure and completeness**:

- It helps create clear deliverables in the required formats (Mermaid diagrams, short component/service descriptions, and comparison tables).
- It quickly proposes reasonable components and entities that stay consistent across documents.
- It supports rapid iteration when requirements change (for example, simplifying language or adjusting a rubric constraint).

At the same time, AI outputs must be reviewed and aligned with reality:

- Rubrics and checkers can be strict (e.g., a table may need exactly a certain number of aspects), and AI won’t automatically know those constraints unless explicitly guided.
- Architectural suggestions can drift toward “enterprise” complexity. Human judgment is needed to keep scope realistic and focused on the MVP.

The most effective workflow is: use AI to draft, then validate against requirements, simplify aggressively, and keep architecture decisions tied to timeline and team size.
