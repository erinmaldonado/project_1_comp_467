import Parse


def parse_baselight(data):
    file = data.remove('/baselight')
    print(data)
    """
        data_parsed = Parse(file, frames)
    """

def get_baselight():
    file = open('Baselight_export.txt')
    lines = file.readlines()
    file.close()
    parse_baselight(lines)


def get_Xytech():
    file = open('Xytech.txt')
    lines = file.readlines()
    file.close()
    parse_Xytech(lines)


def parse_Xytech(lines):
    for line in lines:
        print(line)


def parse_baselight(lines):
    for line in lines:
        separate = line.split(' ', 1)
        file_path = separate[0].split('/')
        nums = separate[1] if len(separate) > 1 else ''
        print(file_path)
        print(nums)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_baselight()
    get_Xytech()
