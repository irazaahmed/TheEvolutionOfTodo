import { useState, useEffect } from 'react';
import { isAuthenticated, getUserIdFromToken } from '../lib/auth';

export const useAuth = () => {
  const [isAuth, setIsAuth] = useState<boolean | null>(null);
  const [userId, setUserId] = useState<string | null>(null);

  useEffect(() => {
    const checkAuth = () => {
      const authStatus = isAuthenticated();
      setIsAuth(authStatus);

      if (authStatus) {
        const userIdFromToken = getUserIdFromToken();
        setUserId(userIdFromToken);
      } else {
        setUserId(null);
      }
    };

    checkAuth();

    // Listen for storage events to update auth state across tabs
    window.addEventListener('storage', checkAuth);

    return () => {
      window.removeEventListener('storage', checkAuth);
    };
  }, []);

  return { isAuth, userId, isLoading: isAuth === null };
};