import os, sys
from termcolor import colored

if __name__ == "__main__":
    paths = os.environ["PATH"].split(";")
    if len(sys.argv) != 2:
        print("usage: where_command [command]")
        sys.exit(1)
    req_command = sys.argv[1]
    found = False
    for path in paths:
        if not os.path.exists(path):
            # print("cannot find: ", path)
            continue
        files = os.listdir(path)
        for file in files:
            dot_pos = file.rfind(".")
            filename_no_ext = file[:dot_pos]
            if filename_no_ext == req_command:
                print(path, os.path.sep, sep="", end="")
                print(colored(filename_no_ext, "green"), file[dot_pos:], sep="")
                found = True
    if not found:
        print(colored("command not found.", "red"))