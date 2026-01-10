# Todo App Frontend

A Next.js frontend application for the Todo application with authentication and task management features.

## Features

- **Authentication**: Secure signup and sign-in with JWT-based authentication
- **Task Management**: Create, read, update, and delete tasks
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Dark/Light Mode**: User preference-based theme switching
- **Full Stack Integration**: Connects to the secured backend API

## Tech Stack

- Next.js 16.1.1 with App Router
- React 19.2.3
- TypeScript
- Tailwind CSS
- Better Auth for authentication
- Axios for API communication

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Copy the environment file:
   ```bash
   cp .env.example .env.local
   ```

3. Update the environment variables in `.env.local` with your backend API URL

4. Run the development server:
   ```bash
   npm run dev
   ```

The application will be available at http://localhost:3000

## Environment Variables

- `NEXT_PUBLIC_API_BASE_URL`: Base URL for the backend API (e.g., http://localhost:8000/api/v1)

## Project Structure

```
frontend/
├── app/
│   ├── auth/
│   │   ├── sign-in/
│   │   └── sign-up/
│   ├── dashboard/
│   └── layout.tsx
├── src/
│   ├── components/
│   ├── contexts/
│   ├── hooks/
│   ├── lib/
│   └── styles/
└── package.json
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint
