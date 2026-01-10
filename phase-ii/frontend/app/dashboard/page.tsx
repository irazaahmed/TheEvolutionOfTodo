'use client';

import React, { useState, useEffect } from 'react';
import ProtectedRoute from '../../src/components/ProtectedRoute';
import { taskAPI } from '../../src/lib/api';
import TaskList from '../../src/components/tasks/TaskList';
import TaskCreateForm from '../../src/components/tasks/TaskCreateForm';

const DashboardPage = () => {
  const [tasks, setTasks] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Fetch tasks on component mount
  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      setLoading(true);
      const response = await taskAPI.getTasks();
      setTasks(response.data);
      setError(null);
    } catch (err: any) {
      console.error('Error fetching tasks:', err);
      setError('Failed to load tasks. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleCreateTask = async (title: string, description?: string) => {
    try {
      const response = await taskAPI.createTask(title, description);
      setTasks([...tasks, response.data]);
    } catch (err: any) {
      console.error('Error creating task:', err);
      alert('Failed to create task. Please try again.');
    }
  };

  const handleUpdateTask = async (taskId: string, title: string, description?: string, completed?: boolean) => {
    try {
      const response = await taskAPI.updateTask(taskId, title, description, completed);
      setTasks(tasks.map(task => task.id === taskId ? response.data : task));
    } catch (err: any) {
      console.error('Error updating task:', err);
      alert('Failed to update task. Please try again.');
    }
  };

  const handleDeleteTask = async (taskId: string) => {
    try {
      await taskAPI.deleteTask(taskId);
      setTasks(tasks.filter(task => task.id !== taskId));
    } catch (err: any) {
      console.error('Error deleting task:', err);
      alert('Failed to delete task. Please try again.');
    }
  };

  const handleToggleTask = async (taskId: string) => {
    try {
      const response = await taskAPI.toggleTaskCompletion(taskId);
      setTasks(tasks.map(task => task.id === taskId ? response.data : task));
    } catch (err: any) {
      console.error('Error toggling task:', err);
      alert('Failed to update task status. Please try again.');
    }
  };

  return (
    <ProtectedRoute>
      <div className="min-h-screen bg-gray-50 dark:bg-gray-900 p-4 md:p-8">
        <div className="max-w-4xl mx-auto">
          <header className="mb-8">
            <h1 className="text-3xl font-bold text-gray-800 dark:text-white">My Tasks</h1>
            <p className="text-gray-600 dark:text-gray-400 mt-2">Manage your tasks efficiently</p>
          </header>

          <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-lg p-6 mb-8">
            <TaskCreateForm onCreate={handleCreateTask} />
          </div>

          {error && (
            <div className="mb-6 p-4 bg-red-100 text-red-700 dark:bg-red-900 dark:text-red-100 rounded-lg">
              {error}
            </div>
          )}

          {loading ? (
            <div className="flex justify-center items-center h-32">
              <div className="animate-spin rounded-full h-10 w-10 border-t-2 border-b-2 border-indigo-500"></div>
            </div>
          ) : (
            <TaskList
              tasks={tasks}
              onUpdate={handleUpdateTask}
              onDelete={handleDeleteTask}
              onToggle={handleToggleTask}
            />
          )}
        </div>
      </div>
    </ProtectedRoute>
  );
};

export default DashboardPage;