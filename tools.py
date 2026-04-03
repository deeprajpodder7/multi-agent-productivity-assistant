from database import engine
from sqlalchemy import text

def create_task_tool(task):
    with engine.connect() as conn:
        conn.execute(text(f"INSERT INTO tasks (title, status) VALUES ('{task}', 'pending')"))
        conn.commit()
    return f"Task '{task}' created"

def create_event_tool(title, datetime):
    with engine.connect() as conn:
        conn.execute(text(f"INSERT INTO events (title, datetime) VALUES ('{title}', '{datetime}')"))
        conn.commit()
    return f"Event '{title}' scheduled at {datetime}"

def save_note_tool(content):
    with engine.connect() as conn:
        conn.execute(text(f"INSERT INTO notes (content) VALUES ('{content}')"))
        conn.commit()
    return f"Note saved: {content}"