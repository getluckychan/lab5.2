class Empty(Exception):
    def __init__(self):
        pass


class Error(Exception):

    def __init__(self):
        self.massage = None

    def __str__(self):
        self.massage = "Виклик помилки"
        return self.massage
