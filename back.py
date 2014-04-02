import os
from collections import OrderedDict
from json import dumps


class Database():
    """Mail list database"""
    def __init__(self, name):
        self._name = name
        self._subscribers = OrderedDict()

    def get_name(self):
        return self._name

    def get_file_name(self):
        return self._name.replace(" ", "_")

    def get_subscriber_name(self, subscriber_id):
        return list(self._subscribers.keys())[subscriber_id]

    def get_subscriber_email(self, subscriber_id):
        name = self.get_subscriber_name(subscriber_id)
        return self._subscribers[name]

    def add_subscriber(self, name, email):
        if name not in self._subscribers.keys():
            if email not in self._subscribers.values():
                self._subscribers[name] = email
                return True
        return False

    def remove_subscriber(self, name):
        if name not in self._subscribers:
            return False
        self._subscribers.pop(name)
        return True

    def update_subscriber(self, old_name, name, email):
        del self._subscribers[old_name]
        self._subscribers[name] = email
        return True

    def show_subscribers(self):
        output = []
        for i, key in enumerate(self._subscribers):
            output.append("[{}] {} - {}".format(i+1, key, self._subscribers[key]))
        return "\n".join(output)

    def has_subscriber_with_email(self, email):
        if email in self._subscribers.values():
            return True
        else:
            return False

    def prepare_json(self):
        json_output = []
        for key in self._subscribers:
            json_dict = OrderedDict()
            json_dict["name"] = key
            json_dict["email"] = self._subscribers[key]
            json_output.append(json_dict)
        return dumps(json_output, indent=4)

    def get_length(self):
        return len(self._subscribers)

    def get_subscribers(self):
        subscribers = []
        for subscriber in self._subscribers:
            subscribers.append((subscriber, self._subscribers[subscriber]))
        return subscribers

    def prepare_file(self):
        subscribers = self.get_subscribers()
        subscribers = map(lambda t: "{} - {}".format(t[0], t[1]), subscribers)
        return subscribers

    def save(self, to):
        if not os.path.exists("Lists"):
            os.makedirs("Lists")
        filename = "./Lists/{}".format(self.get_file_name())
        if to == "file":
            contents = "\n".join(self.prepare_file())
        elif to == "json":
            filename += ".json"
            contents = self.prepare_json()
        file_to_save = open(filename, "w")
        file_to_save.write(contents)
        file_to_save.close()

    def remove_list(self):
        prompt = input("Are you sure you want to delete <{}>?".format(self.get_name()))
        if prompt.lower() == "y":
            os.remove("./Lists/{}".format(self.get_file_name()))
            return True
        return False
