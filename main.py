from ast import parse

import Parse


def parse_baselight(data):
    split_data = data.replace("/baselightfilesystem1/", "")
    final = split_data.split(' ')
    print(final)
    """
        data_parsed = Parse(file, frames)
    """


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    raw_data = "/baselightfilesystem1/Dune2/reel1/partA/1920x1080 2 3 4 31 32 33 67 68 69 70 122 123 155 1023 1111 ' \
              '1112 1160 1201 1202 1203 1204 1205 1211 1212 1213 1214 1215"
    parse_baselight(raw_data)
