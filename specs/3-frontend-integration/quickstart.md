# Quickstart Guide: Frontend Application and Full-Stack Integration

## Prerequisites

- Node.js 18+ installed
- The Phase II Part 1 backend (FastAPI) running
- The Phase II Part 2 authentication endpoints available
- Access to backend API endpoints

## Setup Instructions

### 1. Clone and Navigate
```bash
# Assuming the frontend will be in a separate directory
mkdir -p frontend
cd frontend
```

### 2. Initialize Next.js Project
```bash
npm create next-app@latest .
# Or use yarn create next-app
```

### 3. Install Dependencies
```bash
npm install @better-auth/react @better-auth/client better-auth
npm install -D tailwindcss postcss autoprefixer
npm install axios # or your preferred HTTP client
npx tailwindcss init -p
```

### 4. Configure Environment Variables
Create a `.env.local` file:
```env
# Backend API configuration
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:8000

# Better Auth configuration (these will match backend settings)
AUTH_SECRET=your_jwt_secret_here
```

### 5. Configure Tailwind CSS
Update `tailwind.config.js`:
```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  darkMode: 'class', // Enable dark mode with class strategy
  theme: {
    extend: {},
  },
  plugins: [],
};
```

### 6. Start Development Server
```bash
npm run dev
```

## Backend Connection

The frontend connects to the existing backend at `http://localhost:8000` (or your configured API URL). All authenticated requests will include the JWT token in the Authorization header.

## Better Auth Integration

Better Auth will handle user sessions and authentication state. The integration will include:

- Sign-up and sign-in pages
- Session management
- Protected routes
- User profile access

## API Service Setup

An API service will be created to handle all communication with the backend, including:

- Authentication requests
- Task management operations
- Error handling
- JWT token management