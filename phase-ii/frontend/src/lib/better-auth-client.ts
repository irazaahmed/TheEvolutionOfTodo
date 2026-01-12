'use client';

// Since Better Auth doesn't have a native Python/FastAPI backend implementation,
// we'll use a custom client that communicates with our FastAPI backend
// that's designed to be compatible with Better Auth token format

interface SessionData {
  user: {
    id: string;
    email: string;
  };
  session: {
    token: string;
  };
}

class BetterAuthClient {
  private baseUrl: string;

  constructor(baseURL: string) {
    this.baseUrl = baseURL;
  }

  async getSession(): Promise<SessionData | null> {
    if (typeof window === 'undefined') {
      return null;
    }

    const token = localStorage.getItem('access_token');
    if (!token) {
      return null;
    }

    try {
      // Verify token with backend
      const response = await fetch(`${this.baseUrl}/api/auth/session`, {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        const userData = await response.json();
        return {
          user: {
            id: userData.userId || userData.user_id,
            email: userData.email,
          },
          session: {
            token: token,
          },
        };
      }
      return null;
    } catch (error) {
      console.error('Error getting session:', error);
      return null;
    }
  }

  async signInEmail(credentials: { email: string; password: string }) {
    try {
      const response = await fetch(`${this.baseUrl}/api/auth/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(credentials),
      });

      if (!response.ok) {
        throw new Error('Login failed');
      }

      const data = await response.json();

      // Store the token
      if (typeof window !== 'undefined') {
        localStorage.setItem('access_token', data.access_token);
      }

      return {
        data: {
          user: { id: data.user_id },
          session: { token: data.access_token },
        },
      };
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    }
  }

  async signUp(credentials: { email: string; password: string; confirmPassword: string }) {
    try {
      const response = await fetch(`${this.baseUrl}/api/auth/register`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: credentials.email,
          password: credentials.password,
        }),
      });

      if (!response.ok) {
        throw new Error('Registration failed');
      }

      const data = await response.json();

      // Store the token
      if (typeof window !== 'undefined') {
        localStorage.setItem('access_token', data.access_token);
      }

      return {
        data: {
          user: { id: data.user_id },
          session: { token: data.access_token },
        },
      };
    } catch (error) {
      console.error('Registration error:', error);
      throw error;
    }
  }

  async signOut() {
    if (typeof window !== 'undefined') {
      localStorage.removeItem('access_token');
    }
  }
}

// Initialize Better Auth client
export const authClient = new BetterAuthClient(process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000');

// Export convenience functions
export const signIn = {
  email: (credentials: { email: string; password: string }) => authClient.signInEmail(credentials),
};

export const signUp = (credentials: { email: string; password: string; confirmPassword: string }) =>
  authClient.signUp(credentials);

export const signOut = () => authClient.signOut();