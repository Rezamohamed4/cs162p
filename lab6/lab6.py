import sys
from shapes import Point, Triangle, Diamond, Rectangle, Square

def create_shape(shape_data):
    # Logic to create shape objects based on shape_data

def main(filename):
    shapes = []
    with open(filename, 'r') as file:
        for line in file:
            shape_data = line.strip().split(' ')
            shape = create_shape(shape_data)
            shapes.append(shape)
    
    for shape in shapes:
        shape.draw()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python lab6.py <listfile>")
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)
