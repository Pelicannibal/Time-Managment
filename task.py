from enum import Enum

class Task:
    """A class to construct tasks"""

    def __init__(self, goal: str, priority: int, is_selected = False):
        self.goal = goal
        self.priority = priority
        self.is_selected = is_selected

    def __repr__(self):
        return "{} | {}: {}".format(self.is_selected, self.priority, self.goal)


class Priority(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    ASAP = 3