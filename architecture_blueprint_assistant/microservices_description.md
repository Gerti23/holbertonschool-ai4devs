# Microservices Architecture (SmartCloset Lite)

- **API Gateway**: Single entry point for the frontend. Routes requests to services, handles rate limiting, request validation, and unified error responses.
- **Wardrobe Service**: Manages clothing items (CRUD), tags, categories, colors, seasons, and item state (available/in laundry).
- **Outfits Service**: Manages outfits (CRUD) and outfit-item relationships. Provides endpoints to build, duplicate, and update outfits.
- **Planner Service**: Manages the calendar plan (outfit assigned to date), weekly views, and “recently worn” lookups.
- **Media Service**: Handles image uploads and retrieval (item photos), generates thumbnails (optional), and stores references to images.
- **Suggestions Service**: Generates rule-based outfit suggestions using occasion/season and availability (e.g., avoid laundry items). Can optionally use weather data.
- **Search/Index Service**: Provides fast search and filtering across wardrobe items and outfits using a dedicated index.
- **Notifications Service (Optional)**: Sends reminders (e.g., tomorrow’s outfit) via email/push/SMS if the product later adds accounts and notifications.
- **Analytics Service (Optional)**: Collects product metrics (most-used tags, outfit reuse rate) and supports reporting.

## Data Ownership
- Each service owns its data store (separate DB per service, or separate schema with strict boundaries).
- Cross-service calls:
  - Outfits Service reads wardrobe item metadata (e.g., category/color) via Wardrobe Service.
  - Planner Service reads outfit summaries via Outfits Service.
  - Suggestions Service reads items/outfits via Wardrobe/Outfits Services and may call a Weather API.
