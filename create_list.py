def create_list(list_name):
    file = open(list_name, "w")
    print("New list <%s> was created" % list_name)
    file.close()
