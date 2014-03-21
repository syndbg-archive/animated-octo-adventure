import os


class Database():
    """Mail list database"""
    def __init__(self, name):
        self._name = name
        self._subscribers = {}

    def get_name(self):
        return self._name

    def get_file_name(self):
        return self._name.replace(" ", "_")

    def add_subscriber(self, name, email):
        if name not in self._subscribers.keys():
            if email not in self._subscribers.values():
                self._subscribers[name] = email
        else:
            return "A person with the given name {} or given email {} already exists".format(name, email)

    def remove_subscriber(self, name):
        if name not in self._subscribers:
            return False
        else:
            self._subscribers.pop(name)

    def show_subscribers(self):
        output = []
        i = 1
        for key in self._subscribers:
            output.append("[{}] {} - {}".format(i, key, self._subscribers[key]))
        return "\n".join(output)

    def has_subscriber_with_email(self, email):
        if email in self._subscribers.values():
            return True
        else:
            return False

    def get_length(self):
        return len(self._subscribers)

    def get_subscribers(self):
        subscribers = []
        for subscriber in self._subscribers:
            subscribers.append((subscriber, self._subscribers[subscriber]))
        return subscribers

    def prepare_for_save(self):
        subscribers = self.get_subscribers()
        subscribers = map(lambda t: "{} - {}".format(t[0], t[1]), subscribers)
        return sorted(subscribers)

    def save(self):
        if not os.path.exists("Lists"):
            os.makedirs("Lists")
        filename = "./Lists/{}".format(self.get_file_name())
        # filename = "{}.list".format(self.get_file_name())
        file_to_save = open(filename, "w")
        contents = "\n".join(self.prepare_for_save())
        file_to_save.write(contents)
        file_to_save.close()
