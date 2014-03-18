class MailListDatabase():
    """docstring for MailListDatabase"""

    def write_maillist(maillist):
        subscribers = maillist.get_subscibers()
        modified_subscribers = []

        for s in subscribers:
            s2 = "{} - {}".format(s[0], s[1])
            modified_subscribers.append(s2)

        filename = maillist.get_file_name()
        f = open(filename, "w")
        f.write("\n".join(modified_subscribers))
        f.close()
