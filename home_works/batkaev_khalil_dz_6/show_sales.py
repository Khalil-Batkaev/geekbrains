from sys import argv


def show_sales(start_line=None, stop_line=None):
    """
    Print all amount of bakery's sales.
    param start_line: from this line start print. By default is None
    param stop_line: on this line stop print. By default is None
    """
    with open('bakery.csv', 'tr', encoding='utf-8') as f:
        if not start_line and not stop_line:
            print(f.read())
        else:
            id_line = 0
            for line in f:
                id_line += 1
                if id_line >= start_line:
                    print(line.strip())
                if id_line == stop_line:
                    exit(0)


def get_argv_to_print(argv):
    """Get the args from cmd and start the print of bakery's sales"""
    if len(argv) == 1:
        show_sales()
    elif len(argv) == 2:
        command, start = argv
        show_sales(int(start))
    else:
        command, start, stop, *args = argv
        show_sales(int(start), int(stop))


get_argv_to_print(argv)
