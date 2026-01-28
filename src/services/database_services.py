from langgraph.checkpoint.postgres import PostgresSaver
from psycopg.pool import ConnectionPool
from typing import Optional

class DatabaseManager:
    """
    """
    def __init__(self):
        """
        """
        self.pool: Optional[ConnectionPool] = None

    def initialize(self, connection_string: str):
        """
        Initialize the connection pool and saver
        """
        self.pool = ConnectionPool(
            conninfo=connection_string,
            max_size=20,
            kwargs={"autocommit": True, "prepare_threshold": 0}
        )

        # Setup the checkpointer
        with self.pool.connection() as conn:
            saver = PostgresSaver(conn)
            saver.setup()

    def close(self):
        """
        Close the connection pool
        """
        if self.pool:
            self.pool.close()

    def get_saver(self) -> PostgresSaver:
        """
        Get a saver instance for use in your graph
        """
        if not self.pool:
            raise RuntimeError("Database not initialized")
        return PostgresSaver(self.pool)

db_manager = DatabaseManager()

