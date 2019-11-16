import csv
import os


def access_csv(fp):
    # filePath = '../result/WashingRice_out_edit.csv'
    file_path = fp
    f = open(file_path, "r")
    reader = csv.reader(f)

    return reader


def get_data(fp, haed_bool):
    all_data = []
    tmp_reader = access_csv(fp)

    ### HEADER : True
    if haed_bool:
        for i, row in enumerate(tmp_reader):
            if i is not 0:
                all_data.append(row)

    ### HEADER : False
    else:
        for i, row in enumerate(tmp_reader):
            all_data.append(row)

    return all_data


def access_file(fp):

    f = open(fp, "r")
    fr = f.readlines()
    
    return fr


def write_file(fp, write_objs):
    f = open(fp, "w")
    f.writelines(write_objs)


def merge_html_csv_all(fp_html, fp_csv, csv_header_bool, fp_out):

    print("Build Start, All Data\n---")

    fd_html = access_file(fp_html)
    fd_csv = get_data(fp_csv, csv_header_bool)

    ### debug
    # INDEX = 0
    # data_title, data_date, data_descrpition, data_link = fd_csv[INDEX]
    # print("\"data_title\" : {}".format(data_title))
    # print("\"data_date\" : {}".format(data_date))
    # print("\"data_description\" : {}".format(data_description))
    # print("\"data_link\" : {}".format(data_link))
    ### debug

    a_href =  []

    COUNT = len(fd_csv)

    for j in range(COUNT):

        data_title, data_date, data_descrpition, data_link = fd_csv[j]

        out_obj = []

        for i in range(len(fd_html)):
            line = fd_html[i]
            # print(type(line))

            line = line.replace("$TITLE", data_title)
            line = line.replace("$DATE", data_date)
            line = line.replace("$DESCRIPTION", data_descrpition)
            line = line.replace("$LINK", data_link)

            out_obj.append(line)

        path_mkdir = fp_out + data_title
        path_out = path_mkdir + "/index.html"
        os.makedirs(path_mkdir, exist_ok=True)
        write_file(path_out , out_obj)

        ### master link
        a_href.append("<a href=\"{}\">{}</a><br>\n".format("html/" + data_title, "html/" + data_title))

        print("Build, {}".format(data_title))



    print("---\nBuild Complete, All Data")

    return a_href



def merge_index(fp, master):

    f = open(fp+"/index_master.html", "r")
    fr = f.readlines()
    f.close()

    joined ="".join(master)
    # print(joined)

    out = []
    for i in range(len(fr)):
        line = fr[i]
        line = line.replace("$ALL_LINK", joined)
        out.append(line)

    write_file(fp+"/index.html", out)

    return None



FILEPATH_HTML = "../_html_/template.html"
FILEPATH_CSV = "../_data_/datasheet.csv"
FILEPATH_OUT = "../html/"
FILEPATH_MASTER = "../"


master = merge_html_csv_all(FILEPATH_HTML, FILEPATH_CSV, True, FILEPATH_OUT)
merge_index(FILEPATH_MASTER, master)

