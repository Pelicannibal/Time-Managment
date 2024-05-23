import sqlite3
from task import Task, Priority

class Connection:
    """A class to connect and communicate with the task database"""

    def __init__(self, conn):
        with conn as self.conn:
            self.c = conn.cursor()
            
    def admin_command(self, command: str, fetch: bool):
        with self.conn:
            self.c.execute(command)

            if(fetch):
                self.c.fetchall()

    def delete_table(self):
        self.c.execute("DROP TABLE IF EXISTS tasks")

    def create_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS tasks(
                    priority int,
                    goal text,
                    is_selected bool
                    )""")

    def append_task(self, t: Task):
        with self.conn:
            self.c.execute("INSERT INTO tasks VALUES (:priority, :task)",
                  {'priority': t.priority, 'task': t.goal})
            
    def set_task_selected(self, rowid: int):
        with self.conn:
            self.c.execute("""UPDATE tasks SET
                        is_selected = ((is_selected | 1) - (is_selected & 1))
                        WHERE rowid = :rowid""",
                        {'rowid': rowid})

    def get_tasks_by_priority(self, priority):
        self.c.execute("SELECT * FROM tasks WHERE priority=:priority",
                  {'priority': priority})
        return self.c.fetchall()

    def get_tasks_by_text(self, keyword: str):
        self.c.execute("SELECT * FROM tasks WHERE task LIKE '%keyword%'",
                  {'last': keyword})
        return self.c.fetchall()

    def update_goal(self, rowid: int, goal: str):
        with self.conn:
            self.c.execute("""UPDATE tasks SET goal = :goal
                      WHERE rowid = :rowid""",
                      {'goal': goal, 'rowid': rowid})

    def remove_task(self, rowid: int):
        with self.conn:
            self.c.execute("DELETE FROM tasks WHERE rowid = :rowid",
                      {'rowid': rowid})

    def view_tasks(self):
        task_list = ""
        for row in self.c.execute("SELECT * FROM tasks"):
            task_list += "{}\n".format(row)

        if task_list == "":
            return "No Data..."

        return task_list