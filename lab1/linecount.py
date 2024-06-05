import sys

def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return "File not found. Please check the filename and try again."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python linecount.py <filename>")
    else:
        filename = sys.argv[1]
        line_count = count_lines(filename)
        print(f"The file {filename} has {line_count} lines.")
