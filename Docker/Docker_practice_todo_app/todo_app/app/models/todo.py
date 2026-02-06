class Todo:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed
        }
