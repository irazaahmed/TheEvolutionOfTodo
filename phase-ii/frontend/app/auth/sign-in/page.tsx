'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { authAPI } from '../../../src/lib/api';
import { setToken } from '../../../src/lib/auth';
import SignInForm from '../../../src/components/auth/SignInForm';

const SignInPage = () => {
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  const handleSignIn = async (email: string, password: string) => {
    setLoading(true);
    setError(null);

    try {
      const response = await authAPI.login(email, password);
      const { access_token, user_id } = response.data;

      // Store the token
      setToken(access_token);

      // Redirect to dashboard
      router.push('/dashboard');
      router.refresh(); // Refresh to update auth state
    } catch (err: any) {
      console.error('Sign in error:', err);
      if (err.response?.data?.message) {
        setError(err.response.data.message);
      } else {
        setError('Invalid credentials. Please try again.');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-gray-900 dark:to-gray-800 p-4">
      <div className="w-full max-w-md bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-800 dark:text-white mb-2">Welcome Back</h1>
          <p className="text-gray-600 dark:text-gray-300">Sign in to your account to continue</p>
        </div>

        <SignInForm onSubmit={handleSignIn} loading={loading} />

        {error && (
          <div className="mt-4 p-3 bg-red-100 text-red-700 rounded-lg text-sm">
            {error}
          </div>
        )}

        <div className="mt-6 text-center text-sm text-gray-600 dark:text-gray-400">
          <p>
            Don't have an account?{' '}
            <Link href="/auth/sign-up" className="text-indigo-600 dark:text-indigo-400 font-medium hover:underline">
              Sign up
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default SignInPage;