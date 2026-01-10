import axios, { AxiosInstance, AxiosRequestConfig } from 'axios';

// Create axios instance with base configuration
const apiClient: AxiosInstance = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000/api/v1',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor to add auth token
apiClient.interceptors.request.use(
  (config: AxiosRequestConfig) => {
    const token = typeof window !== 'undefined' ? localStorage.getItem('access_token') : null;
    if (token && config.headers) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor to handle common errors
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token might be expired, clear it and redirect to login
      if (typeof window !== 'undefined') {
        localStorage.removeItem('access_token');
      }
      // Optionally redirect to login page
      // window.location.href = '/auth/sign-in';
    }
    return Promise.reject(error);
  }
);

export default apiClient;

// Authentication API functions
export const authAPI = {
  register: (email: string, password: string) =>
    apiClient.post('/auth/register', { email, password }),

  login: (email: string, password: string) =>
    apiClient.post('/auth/login', { email, password }),
};

// Task API functions
export const taskAPI = {
  getTasks: () => apiClient.get('/tasks'),

  createTask: (title: string, description?: string) =>
    apiClient.post('/tasks', { title, description }),

  getTask: (taskId: string) => apiClient.get(`/tasks/${taskId}`),

  updateTask: (taskId: string, title: string, description?: string, completed?: boolean) =>
    apiClient.put(`/tasks/${taskId}`, { title, description, completed }),

  deleteTask: (taskId: string) => apiClient.delete(`/tasks/${taskId}`),

  toggleTaskCompletion: (taskId: string) => apiClient.patch(`/tasks/${taskId}/toggle`),
};