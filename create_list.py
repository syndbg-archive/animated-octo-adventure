def create_list(list_name):
    filename = "list_%s" % filename
    file = open(filename, "w")
    print("New list <%s> was created" % list_name)
    file.close()
