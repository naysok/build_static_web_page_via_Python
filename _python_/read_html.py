def access_file(fp):

    f = open(fp, "r")
    fr = f.readlines()

    return fr


FILEPATH = "../_html_/template.html"

fd = access_file(FILEPATH)
print(fd)
