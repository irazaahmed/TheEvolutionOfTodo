import axios, { AxiosInstance, AxiosRequestConfig } from 'axios';
import { authClient } from './better-auth-client';

// Create axios instance with base configuration
const apiClient: AxiosInstance = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000', // Base URL without /api/v1 since the backend routes are configured as /api/{user_id}/tasks
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor to add Better Auth token
apiClient.interceptors.request.use(
  async (config: AxiosRequestConfig) => {
    const session = await authClient.getSession();
    if (session?.session && config.headers) {
      config.headers.Authorization = `Bearer ${session.session.token}`;
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
      // Session might be expired, clear it and redirect to login
      authClient.signOut();
      // Optionally redirect to login page
      // window.location.href = '/auth/sign-in';
    }
    return Promise.reject(error);
  }
);

export default apiClient;

// Better Auth API functions
export const authAPI = {
  register: (email: string, password: string) =>
    authClient.signUp({
      email,
      password,
      confirmPassword: password, // assuming we want to confirm password
    }),

  login: (email: string, password: string) =>
    authClient.signIn.email({
      email,
      password,
    }),
};

// Task API functions - updated to use user_id in path
export const taskAPI = {
  getTasks: (userId: string) => apiClient.get(`/${userId}/tasks`),

  createTask: (userId: string, title: string, description?: string) =>
    apiClient.post(`/${userId}/tasks`, { title, description }),

  getTask: (userId: string, taskId: string) => apiClient.get(`/${userId}/tasks/${taskId}`),

  updateTask: (userId: string, taskId: string, title: string, description?: string, completed?: boolean) =>
    apiClient.put(`/${userId}/tasks/${taskId}`, { title, description, completed }),

  deleteTask: (userId: string, taskId: string) => apiClient.delete(`/${userId}/tasks/${taskId}`),

  toggleTaskCompletion: (userId: string, taskId: string) => apiClient.patch(`/${userId}/tasks/${taskId}/complete`),
};