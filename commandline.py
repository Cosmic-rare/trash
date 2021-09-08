import sys

if __name__ == '__main__':
    args = sys.argv
    if 3 <= len(args):
        if args[2].isdigit():

            if args[2] == "1":
                print("1")
            elif args[2] == "2":
                print("2")
            elif args[2] == "3":
                print("3")
            else:
                print("Error")

        else:
            print('Argument is not digit')
    else:
        print('Arguments are too short')
