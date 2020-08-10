import sys

def main():
    print("This robot prints the contents of the input file to the user.")
    if len(sys.argvs) < 2:
        raise SyntaxError("No input file given!")
    input_file = sys.argvs[1]
    with open(input_file, 'r') as file:
        for line in file:
            print(line)

if if __name__ == "__main__":
    main()