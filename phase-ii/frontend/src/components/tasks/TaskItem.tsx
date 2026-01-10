import React, { useState } from 'react';

interface Task {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  user_id: string;
  created_at: string;
  updated_at: string;
}

interface TaskItemProps {
  task: Task;
  onUpdate: (taskId: string, title: string, description?: string, completed?: boolean) => void;
  onDelete: (taskId: string) => void;
  onToggle: (taskId: string) => void;
}

const TaskItem = ({ task, onUpdate, onDelete, onToggle }: TaskItemProps) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editTitle, setEditTitle] = useState(task.title);
  const [editDescription, setEditDescription] = useState(task.description || '');

  const handleSave = () => {
    onUpdate(task.id, editTitle, editDescription, task.completed);
    setIsEditing(false);
  };

  const handleCancel = () => {
    setEditTitle(task.title);
    setEditDescription(task.description || '');
    setIsEditing(false);
  };

  const handleToggle = () => {
    onToggle(task.id);
  };

  const handleDelete = () => {
    onDelete(task.id);
  };

  return (
    <div className={`border rounded-xl p-4 transition-all duration-200 ${
      task.completed
        ? 'border-green-200 bg-green-50 dark:border-green-900/50 dark:bg-green-900/20'
        : 'border-gray-200 bg-white dark:border-gray-700 dark:bg-gray-700/50'
    }`}>
      {isEditing ? (
        <div className="space-y-3">
          <input
            type="text"
            value={editTitle}
            onChange={(e) => setEditTitle(e.target.value)}
            className="w-full px-3 py-2 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
            autoFocus
          />
          <textarea
            value={editDescription}
            onChange={(e) => setEditDescription(e.target.value)}
            className="w-full px-3 py-2 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
            rows={2}
          />
          <div className="flex space-x-2">
            <button
              onClick={handleSave}
              className="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition"
            >
              Save
            </button>
            <button
              onClick={handleCancel}
              className="px-4 py-2 bg-gray-300 text-gray-700 dark:bg-gray-600 dark:text-gray-200 rounded-lg hover:bg-gray-400 dark:hover:bg-gray-500 transition"
            >
              Cancel
            </button>
          </div>
        </div>
      ) : (
        <div className="flex items-start gap-3">
          <button
            onClick={handleToggle}
            className={`flex-shrink-0 w-6 h-6 rounded-full border-2 flex items-center justify-center mt-1 ${
              task.completed
                ? 'bg-green-500 border-green-500 text-white'
                : 'border-gray-300 dark:border-gray-500 hover:border-indigo-500'
            }`}
            aria-label={task.completed ? 'Mark as incomplete' : 'Mark as complete'}
          >
            {task.completed && (
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" d="M5 13l4 4L19 7" />
              </svg>
            )}
          </button>

          <div className="flex-grow min-w-0">
            <h3 className={`font-medium truncate ${task.completed ? 'line-through text-gray-500 dark:text-gray-400' : 'text-gray-900 dark:text-white'}`}>
              {task.title}
            </h3>
            {task.description && (
              <p className={`mt-1 text-sm ${task.completed ? 'line-through text-gray-500 dark:text-gray-400' : 'text-gray-600 dark:text-gray-300'}`}>
                {task.description}
              </p>
            )}
          </div>

          <div className="flex space-x-2">
            <button
              onClick={() => setIsEditing(true)}
              className="p-2 text-gray-500 hover:text-indigo-600 dark:text-gray-400 dark:hover:text-indigo-400 rounded-full hover:bg-gray-100 dark:hover:bg-gray-600 transition"
              aria-label="Edit task"
            >
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
              </svg>
            </button>

            <button
              onClick={handleDelete}
              className="p-2 text-gray-500 hover:text-red-600 dark:text-gray-400 dark:hover:text-red-400 rounded-full hover:bg-gray-100 dark:hover:bg-gray-600 transition"
              aria-label="Delete task"
            >
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default TaskItem;