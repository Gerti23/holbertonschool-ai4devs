# Monolithic Architecture (SmartCloset Lite)

- **Frontend Web App**: Responsive UI for managing items, building outfits, and planning what to wear.
- **Backend Monolith API**: Single backend application that exposes all endpoints and contains the core business logic.
- **Wardrobe Module**: CRUD for clothing items (category, color, tags, season) and item state (e.g., in laundry).
- **Outfits Module**: Creates, edits, and stores outfits by linking multiple wardrobe items into saved combinations.
- **Planner Module**: Assigns outfits to dates, provides weekly views, and tracks “recently worn” to reduce repeats.
- **Media/Images Module**: Handles photo upload, image processing (optional), and links items to stored photos.
- **Suggestions Module (Rule-based)**: Generates simple outfit suggestions using occasion/season rules and availability (e.g., avoid laundry items).
- **Validation & Error Handling**: Central input validation, consistent API errors, and basic logging.
- **Database**: Stores all application data (items, outfits, outfit-items relations, plans, flags).
- **Object Storage for Photos**: Stores item images separately from the database (e.g., Supabase Storage/S3).
- **External Weather API (Optional)**: Provides weather context for suggestions when enabled.
