// JWT token handling strategy for frontend

// Store token in localStorage
export const setToken = (token: string): void => {
  if (typeof window !== 'undefined') {
    localStorage.setItem('access_token', token);
  }
};

// Get token from localStorage
export const getToken = (): string | null => {
  if (typeof window !== 'undefined') {
    return localStorage.getItem('access_token');
  }
  return null;
};

// Remove token from localStorage
export const removeToken = (): void => {
  if (typeof window !== 'undefined') {
    localStorage.removeItem('access_token');
  }
};

// Check if user is authenticated
export const isAuthenticated = (): boolean => {
  const token = getToken();
  if (!token) {
    return false;
  }

  // Decode JWT to check expiration
  try {
    const payload = JSON.parse(atob(token.split('.')[1]));
    const currentTime = Math.floor(Date.now() / 1000);
    return payload.exp > currentTime;
  } catch (error) {
    // If token is malformed, consider user not authenticated
    return false;
  }
};

// Get user ID from token
export const getUserIdFromToken = (): string | null => {
  const token = getToken();
  if (!token) {
    return null;
  }

  try {
    const payload = JSON.parse(atob(token.split('.')[1]));
    return payload.user_id || payload.sub || null;
  } catch (error) {
    return null;
  }
};

// Check if token is expired
export const isTokenExpired = (): boolean => {
  const token = getToken();
  if (!token) {
    return true;
  }

  try {
    const payload = JSON.parse(atob(token.split('.')[1]));
    const currentTime = Math.floor(Date.now() / 1000);
    return payload.exp <= currentTime;
  } catch (error) {
    return true;
  }
};

// Decode token without verification (for UI purposes only)
export const decodeToken = (): any | null => {
  const token = getToken();
  if (!token) {
    return null;
  }

  try {
    const payload = JSON.parse(atob(token.split('.')[1]));
    return payload;
  } catch (error) {
    return null;
  }
};