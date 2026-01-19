---
name: frontend-skill
description: Build and maintain frontend pages, components, layouts, and styling. Use for creating responsive UI, consistent design systems, and clean component structures.
---

# Frontend Skill – Pages, Components, Layout, and Styling

## Instructions

1. **Pages**
   - Build pages aligned with product flows and user journeys
   - Separate public, authentication, and protected pages clearly
   - Ensure each page has a clear purpose and hierarchy
   - Handle loading, empty, and error states gracefully

2. **Components**
   - Create reusable, composable UI components
   - Keep components focused on a single responsibility
   - Avoid tightly coupling components to business logic
   - Pass data via clear and predictable props

3. **Layout Structure**
   - Define consistent layout patterns (headers, footers, navigation)
   - Use layout components to avoid duplication
   - Ensure layouts adapt correctly across screen sizes
   - Maintain visual balance and spacing consistency

4. **Styling**
   - Apply consistent styling rules across the application
   - Use a unified color system and typography scale
   - Support light and dark themes where required
   - Ensure styles are maintainable and predictable
   - Avoid inline or ad-hoc styling that breaks consistency

5. **Responsiveness**
   - Design mobile-first and scale up to larger screens
   - Test layouts across common breakpoints
   - Ensure interactive elements remain usable on touch devices

## Best Practices

- Treat the UI as a user-facing contract
- Prefer clarity and consistency over visual complexity
- Keep styling decisions centralized and reusable
- Ensure accessibility through contrast, semantics, and focus handling
- Review UI changes for regressions across pages

## Example Structure (Conceptual)

```text
Page
→ Layout
  → Header
  → Main Content
    → Reusable Components
  → Footer
