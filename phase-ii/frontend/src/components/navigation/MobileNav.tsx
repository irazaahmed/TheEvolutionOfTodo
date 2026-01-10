import React, { useState } from 'react';
import Link from 'next/link';
import { useTheme } from '../../contexts/ThemeContext';
import ThemeToggle from './ThemeToggle';

const MobileNav = () => {
  const [isOpen, setIsOpen] = useState(false);
  const { theme } = useTheme();

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <nav className="md:hidden bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
      <div className="px-4 py-3 flex items-center justify-between">
        <div className="text-xl font-bold text-indigo-600 dark:text-indigo-400">Todo App</div>

        <div className="flex items-center space-x-3">
          <ThemeToggle />

          <button
            onClick={toggleMenu}
            className="p-2 rounded-md text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white focus:outline-none"
            aria-expanded={isOpen}
            aria-label="Main menu"
          >
            <svg
              className="h-6 w-6"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              {isOpen ? (
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              ) : (
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              )}
            </svg>
          </button>
        </div>
      </div>

      {/* Mobile menu */}
      {isOpen && (
        <div className="px-2 pt-2 pb-3 space-y-1 bg-white dark:bg-gray-800">
          <Link
            href="/dashboard"
            className="block px-3 py-2 rounded-md text-base font-medium text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
            onClick={() => setIsOpen(false)}
          >
            Dashboard
          </Link>
          <Link
            href="/"
            className="block px-3 py-2 rounded-md text-base font-medium text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
            onClick={() => setIsOpen(false)}
          >
            Home
          </Link>
          <button
            onClick={() => {
              // Log out functionality would go here
              localStorage.removeItem('access_token');
              window.location.href = '/auth/sign-in';
            }}
            className="w-full text-left block px-3 py-2 rounded-md text-base font-medium text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
          >
            Sign Out
          </button>
        </div>
      )}
    </nav>
  );
};

export default MobileNav;