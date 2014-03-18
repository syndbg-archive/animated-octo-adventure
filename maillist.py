class MailList():
    """A class to represent a single mail list"""
    def __init__(self, name):
        self._name = name
        self._subscribers = {}

    def get_name(self):
        return self._name

    def get_file_name(self):
        return self._name.replace(" ", "_")

    def add(self, name, email):
        self._subscribers[name] = email

    def get_length(self):
        return len(self._subscribers)

    def get_subscribers(self):
        result = []

        for key in self._subscribers:
            result.append((key, self._subscribers[key]))

        return result
