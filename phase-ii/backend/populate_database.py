import asyncio
import uuid
from datetime import datetime
from sqlmodel import SQLModel, create_engine, Session, select
from app.models.task import Task
from app.models.user import User
from app.core.config import settings

# Create sync engine for database operations (convert async URL to sync)
sync_db_url = settings.database_url.replace("+asyncpg", "").replace("+aiosqlite", "")
print(f"Connecting to database: {sync_db_url}")

# Create sync engine for database operations
engine = create_engine(sync_db_url, echo=True)

def create_tables():
    """Create database tables."""
    print("Creating tables...")
    SQLModel.metadata.create_all(engine)
    print("Tables created successfully!")

def add_dummy_data():
    """Add dummy data to the database."""
    print("Adding dummy data...")

    with Session(engine) as session:
        # Create some users first
        users = []
        for i in range(3):
            user = User(
                email=f"user{i+1}@example.com",
                hashed_password="$2b$12$VcCDgh2NDk07JBFgGFeQeuDa8Ujcug22dC5VSKXAXq/ZMjZmebpTO"  # This is 'password123' hashed
            )
            session.add(user)
            users.append(user)

        session.commit()  # Commit users first so they have IDs

        # Now create tasks for each user
        tasks_data = [
            {"title": "Complete project proposal", "description": "Finish the project proposal document", "completed": False},
            {"title": "Schedule team meeting", "description": "Arrange meeting with team for next week", "completed": True},
            {"title": "Review code changes", "description": "Review pull requests from team", "completed": False},
            {"title": "Update documentation", "description": "Update API documentation", "completed": False},
            {"title": "Prepare presentation", "description": "Prepare slides for client presentation", "completed": True},
        ]

        for i, user in enumerate(users):
            print(f"Creating tasks for user {i+1} (ID: {user.id})")

            for j, task_data in enumerate(tasks_data):
                task = Task(
                    title=f"User {i+1} - {task_data['title']}",
                    description=f"User {i+1}: {task_data['description']}",
                    completed=task_data['completed'],
                    user_id=user.id  # Use the actual user ID from the database
                )
                session.add(task)

        session.commit()
        print("Dummy data added successfully!")

def view_data():
    """View the data in the database."""
    print("\n--- Current Tasks in Database ---")

    with Session(engine) as session:
        statement = select(Task)
        results = session.exec(statement)
        tasks = results.all()

        for task in tasks:
            print(f"ID: {task.id}, Title: {task.title}, Completed: {task.completed}, User ID: {task.user_id}")

        print(f"\nTotal tasks: {len(tasks)}")

if __name__ == "__main__":
    print("Connecting to Neon PostgreSQL database...")
    print(f"Database URL: {settings.database_url}")

    try:
        create_tables()
        add_dummy_data()
        view_data()
        print("\n✅ Database populated with dummy data successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()