import csv



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



FILEPATH = "../_data_/datasheet.csv"

fd = get_data(FILEPATH, True)
print(fd)

