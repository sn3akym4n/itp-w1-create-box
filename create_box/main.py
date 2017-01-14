"""This is the entry point of the program."""


def create_box(height, width, character):
    string =''
    for i in range(height):
        for x in range(width):
            string += character
        string += '\n'
    return string

if __name__ == '__main__':
    create_box(3, 4, '*')
