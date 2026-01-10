# Frontend Data Models: Frontend Application and Full-Stack Integration

## Frontend-Specific Data Structures

### Task Model (Client Side)
```typescript
interface Task {
  id: string;              // UUID from backend
  title: string;           // Task title
  description?: string;    // Optional task description
  completed: boolean;      // Completion status
  user_id: string;         // Associated user ID (from JWT)
  created_at: string;      // ISO timestamp from backend
  updated_at: string;      // ISO timestamp from backend
}
```

### Auth State Model
```typescript
interface AuthState {
  isAuthenticated: boolean;
  user?: {
    id: string;
    email: string;
  };
  isLoading: boolean;
  error?: string;
}
```

### API Response Models
```typescript
interface ApiResponse<T> {
  data?: T;
  error?: {
    message: string;
    code?: string;
    details?: any;
  };
  success: boolean;
}

interface TaskApiResponse {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  user_id: string;
  created_at: string;
  updated_at: string;
}
```

### Form Data Models
```typescript
interface TaskFormData {
  title: string;
  description?: string;
}

interface SignInFormData {
  email: string;
  password: string;
}

interface SignUpFormData {
  email: string;
  password: string;
}
```

## API Contract Definitions

### Authentication Endpoints
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login
- Response: `{ access_token: string, user_id: string }`

### Task Management Endpoints
- `GET /api/v1/tasks` - Get user's tasks
- `POST /api/v1/tasks` - Create new task
- `GET /api/v1/tasks/{task_id}` - Get specific task
- `PUT /api/v1/tasks/{task_id}` - Update task
- `DELETE /api/v1/tasks/{task_id}` - Delete task
- `PATCH /api/v1/tasks/{task_id}/toggle` - Toggle task completion

### Required Headers
All authenticated endpoints require:
- `Authorization: Bearer {jwt_token}`
- `Content-Type: application/json`

## Theme State Model
```typescript
type Theme = 'light' | 'dark';

interface ThemeState {
  currentTheme: Theme;
  systemPreference: 'light' | 'dark';
  isSystemPreferred: boolean;
}
```

## UI State Models
```typescript
interface TaskUIState {
  tasks: Task[];
  loading: boolean;
  error?: string;
  searchTerm?: string;
  filter: 'all' | 'active' | 'completed';
}

interface FormState {
  isSubmitting: boolean;
  error?: string;
  success?: boolean;
}
```