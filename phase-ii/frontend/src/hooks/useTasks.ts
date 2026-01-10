import { useState } from 'react';
import { taskAPI } from '../lib/api';

interface Task {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  user_id: string;
  created_at: string;
  updated_at: string;
}

export const useTasks = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchTasks = async () => {
    setLoading(true);
    setError(null);

    try {
      const response = await taskAPI.getTasks();
      setTasks(response.data);
    } catch (err: any) {
      console.error('Error fetching tasks:', err);
      setError('Failed to load tasks. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const createTask = async (title: string, description?: string) => {
    setLoading(true);
    setError(null);

    try {
      const response = await taskAPI.createTask(title, description);
      setTasks([...tasks, response.data]);
      return response.data;
    } catch (err: any) {
      console.error('Error creating task:', err);
      setError('Failed to create task. Please try again.');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const updateTask = async (taskId: string, title: string, description?: string, completed?: boolean) => {
    setLoading(true);
    setError(null);

    try {
      const response = await taskAPI.updateTask(taskId, title, description, completed);
      setTasks(tasks.map(task => task.id === taskId ? response.data : task));
      return response.data;
    } catch (err: any) {
      console.error('Error updating task:', err);
      setError('Failed to update task. Please try again.');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const deleteTask = async (taskId: string) => {
    setLoading(true);
    setError(null);

    try {
      await taskAPI.deleteTask(taskId);
      setTasks(tasks.filter(task => task.id !== taskId));
    } catch (err: any) {
      console.error('Error deleting task:', err);
      setError('Failed to delete task. Please try again.');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const toggleTaskCompletion = async (taskId: string) => {
    setLoading(true);
    setError(null);

    try {
      const response = await taskAPI.toggleTaskCompletion(taskId);
      setTasks(tasks.map(task => task.id === taskId ? response.data : task));
      return response.data;
    } catch (err: any) {
      console.error('Error toggling task:', err);
      setError('Failed to update task status. Please try again.');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  return {
    tasks,
    loading,
    error,
    fetchTasks,
    createTask,
    updateTask,
    deleteTask,
    toggleTaskCompletion,
  };
};