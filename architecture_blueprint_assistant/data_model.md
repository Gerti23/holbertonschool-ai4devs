# Data Model (SmartCloset Lite)

This data model supports a simple “Smart Closet” app without accounts. Instead of a user table, the app uses a **Closet** as the owner of all data. A `closetId` can be generated once and stored in the browser.

## Entities

- **Closet**: `id`, `created_at`, `updated_at`
  - Represents one person’s workspace (anonymous or single-user).

- **ClothingItem**: `id`, `closet_id`, `name`, `category`, `color`, `season`, `status`, `image_url`, `created_at`, `updated_at`
  - A single piece of clothing in the wardrobe.
  - `status` is used for features like “in laundry”.

- **Outfit**: `id`, `closet_id`, `name`, `occasion`, `season`, `comfort_rating`, `created_at`, `updated_at`
  - A saved combination template (e.g., “Office Casual”).

- **OutfitItem**: `id`, `outfit_id`, `clothing_item_id`, `slot`, `sort_order`
  - Join entity that links outfits to clothing items.
  - `slot` helps the UI place items (top/bottom/shoes/etc.).

- **PlanEntry**: `id`, `closet_id`, `outfit_id`, `wear_date`, `notes`, `created_at`
  - Scheduling layer: which outfit is planned for a specific date.

## Relationships

- A **Closet** owns many **ClothingItems**, **Outfits**, and **PlanEntries**.
- An **Outfit** contains many **OutfitItems**.
- A **ClothingItem** can appear in many **OutfitItems** (many-to-many through `OutfitItem`).
- A **PlanEntry** points to exactly one **Outfit** for a given `wear_date`.

## Notes / Constraints (Implementation)

- Enforce ownership by always filtering on `closet_id`.
- For “recently worn”, query `PlanEntry` by date range and count outfit usage.
- Image handling can start with `image_url`; later you can store files in object storage and keep only the public URL here.
