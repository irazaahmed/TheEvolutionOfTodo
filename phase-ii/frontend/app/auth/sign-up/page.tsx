'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { authAPI } from '../../../src/lib/api';
import { setToken } from '../../../src/lib/auth';
import SignUpForm from '../../../src/components/auth/SignUpForm';

const SignUpPage = () => {
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  const handleSignUp = async (email: string, password: string) => {
    setLoading(true);
    setError(null);

    try {
      const response = await authAPI.register(email, password);
      const { access_token, user_id } = response.data;

      // Store the token
      setToken(access_token);

      // Redirect to dashboard
      router.push('/dashboard');
      router.refresh(); // Refresh to update auth state
    } catch (err: any) {
      console.error('Sign up error:', err);
      if (err.response?.data?.message) {
        setError(err.response.data.message);
      } else {
        setError('Failed to create account. Please try again.');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-gray-900 dark:to-gray-800 p-4">
      <div className="w-full max-w-md bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-800 dark:text-white mb-2">Create Account</h1>
          <p className="text-gray-600 dark:text-gray-300">Sign up to get started with your tasks</p>
        </div>

        <SignUpForm onSubmit={handleSignUp} loading={loading} />

        {error && (
          <div className="mt-4 p-3 bg-red-100 text-red-700 rounded-lg text-sm">
            {error}
          </div>
        )}

        <div className="mt-6 text-center text-sm text-gray-600 dark:text-gray-400">
          <p>
            Already have an account?{' '}
            <Link href="/auth/sign-in" className="text-indigo-600 dark:text-indigo-400 font-medium hover:underline">
              Sign in
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default SignUpPage;