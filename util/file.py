# ----------------------------------------------------------------------------------------------------------------------


def open_file(file_name):
    file = open(file_name, "r")
    content = file.read()
    file.close()
    return content

# ----------------------------------------------------------------------------------------------------------------------
