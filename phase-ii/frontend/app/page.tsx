'use client';

import React from 'react';
import Navbar from '../src/components/navigation/Navbar';
import { isAuthenticated } from '../src/lib/auth';

const Home = () => {
  const handleCreateTaskClick = () => {
    if (isAuthenticated()) {
      window.location.href = '/dashboard';
    } else {
      window.location.href = '/auth/sign-in';
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-gray-900 dark:to-gray-800">
      <Navbar />

      {/* Hero Section */}
      <section className="relative py-20 md:py-32 overflow-hidden">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
          <div className="text-center">
            <h1 className="text-4xl md:text-6xl font-extrabold text-gray-900 dark:text-white tracking-tight">
              Welcome to <span className="text-indigo-600 dark:text-indigo-400">TaskHub</span>
            </h1>
            <p className="mt-6 max-w-2xl mx-auto text-xl text-gray-600 dark:text-gray-300">
              A secure and intuitive task management application designed to help you organize your work and boost productivity.
            </p>
            <div className="mt-10">
              <button
                onClick={handleCreateTaskClick}
                className="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 dark:focus:ring-offset-gray-900 transition-colors duration-200"
              >
                Create Task
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-20 bg-white dark:bg-gray-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h2 className="text-3xl font-extrabold text-gray-900 dark:text-white sm:text-4xl">
              Powerful Features
            </h2>
            <p className="mt-4 max-w-2xl mx-auto text-xl text-gray-500 dark:text-gray-300">
              Everything you need to manage your tasks efficiently
            </p>
          </div>

          <div className="mt-16 grid gap-8 md:grid-cols-3">
            <div className="bg-gray-50 dark:bg-gray-700 p-8 rounded-lg shadow-sm">
              <div className="flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                </svg>
              </div>
              <h3 className="mt-6 text-lg font-medium text-gray-900 dark:text-white">Task Organization</h3>
              <p className="mt-2 text-base text-gray-500 dark:text-gray-300">
                Easily create, categorize, and prioritize your tasks with our intuitive interface.
              </p>
            </div>

            <div className="bg-gray-50 dark:bg-gray-700 p-8 rounded-lg shadow-sm">
              <div className="flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                </svg>
              </div>
              <h3 className="mt-6 text-lg font-medium text-gray-900 dark:text-white">Secure & Private</h3>
              <p className="mt-2 text-base text-gray-500 dark:text-gray-300">
                Your data is protected with industry-standard encryption and security practices.
              </p>
            </div>

            <div className="bg-gray-50 dark:bg-gray-700 p-8 rounded-lg shadow-sm">
              <div className="flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
                </svg>
              </div>
              <h3 className="mt-6 text-lg font-medium text-gray-900 dark:text-white">Cross-Platform</h3>
              <p className="mt-2 text-base text-gray-500 dark:text-gray-300">
                Access your tasks anywhere, anytime with our responsive web application.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* About Section */}
      <section id="about" className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="lg:text-center">
            <h2 className="text-3xl font-extrabold text-gray-900 dark:text-white sm:text-4xl">
              About TaskHub
            </h2>
            <p className="mt-4 max-w-2xl text-xl text-gray-500 dark:text-gray-300 lg:mx-auto">
              We believe that everyone deserves a simple, effective way to manage their tasks and boost productivity.
            </p>
          </div>

          <div className="mt-16">
            <div className="bg-white dark:bg-gray-800 shadow-xl rounded-lg overflow-hidden">
              <div className="px-4 py-5 sm:p-6">
                <p className="text-lg text-gray-600 dark:text-gray-300">
                  TaskHub is a modern task management application built with security and usability in mind. Our platform provides a seamless experience for organizing your daily activities, managing projects, and tracking progress. With robust authentication and data protection, you can trust us with your important tasks and information.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-indigo-600">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl font-extrabold text-white sm:text-4xl">
            Ready to get started?
          </h2>
          <p className="mt-4 max-w-2xl mx-auto text-xl text-indigo-100">
            Join thousands of users who trust TaskHub for their daily task management needs.
          </p>
          <div className="mt-10">
            <button
              onClick={handleCreateTaskClick}
              className="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-indigo-600 bg-white hover:bg-indigo-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-colors duration-200"
            >
              Create Your First Task
            </button>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;
