'use client';

import React, { ReactNode, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { isAuthenticated } from '../lib/auth';

interface ProtectedRouteProps {
  children: ReactNode;
}

const ProtectedRoute = ({ children }: ProtectedRouteProps) => {
  const router = useRouter();

  useEffect(() => {
    if (!isAuthenticated()) {
      // Redirect to sign-in page if not authenticated
      router.push('/auth/sign-in');
    }
  }, [router]);

  // If not authenticated, return null (or a loading component) while redirect happens
  if (!isAuthenticated()) {
    return <div className="flex items-center justify-center min-h-screen">Redirecting...</div>;
  }

  return <>{children}</>;
};

export default ProtectedRoute;