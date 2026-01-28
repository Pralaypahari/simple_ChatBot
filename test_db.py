from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg://chatbot_user:091023@localhost:5432/chatbot"

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result.scalar())