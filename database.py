from glob import glob


class Database():
    def __init__(self):
        self.lists = glob("list_*")


    # def show_lists(self):
    #     return glob()
    # def show_list(self, file):

    # def add_to_list(self, list_id):

    # def create_list(self, list_name):

    # def search_by_email(self, email):

    # def merge_lists(self, list_a, list_b, new_list):

    # def export_list_to_json(self, list_name):
    #