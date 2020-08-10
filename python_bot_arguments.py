import time
import sys

def main():
    time.sleep(5)
    print("Hello!")
    print("I got the following input arguments:")
    for arg in sys.argv[1:]:
        print("- " + str(arg))

if __name__ == "__main__":
    main()