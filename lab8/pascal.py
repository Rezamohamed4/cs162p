# pascal.py
class Pascal:
    def __init__(self):
        self.data = {}

    def get_value(self, row, col):
        if (row, col) in self.data:
            return self.data[(row, col)]
        if col == 0 or col == row:
            self.data[(row, col)] = 1
            return 1
        value = self.get_value(row - 1, col - 1) + self.get_value(row - 1, col)
        self.data[(row, col)] = value
        return value

    def display(self, num_lines):
        for row in range(num_lines):
            for col in range(row + 1):
                print(self.get_value(row, col), end=' ')
            print()

def main():
    pascal_triangle = Pascal()
    pascal_triangle.display(5)  # Change this to display the number of lines you want

if __name__ == '__main__':
    main()
