import re
import sys

def grep(pattern, file):
    with open(file, 'r') as f:
        for line in f:
            if re.search(pattern, line):
                print(line, end='')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep.py <pattern> <file>")
        sys.exit(1)

    pattern = sys.argv[1]
    file = sys.argv[2]
    grep(pattern, file)
