# sorting.py
def read_and_sort(filename, field_index):
    with open(filename, 'r') as file:
        lines = file.readlines()
        data = [line.strip().split(',') for line in lines]
        sorted_data = sorted(data, key=lambda x: x[field_index])
        return sorted_data

def main():
    filename = 'data.txt'
    field_to_sort_by = 1  # Change this to the index of the field you want to sort by
    sorted_data = read_and_sort(filename, field_to_sort_by)
    for entry in sorted_data:
        print(entry)

if __name__ == '__main__':
    main()
