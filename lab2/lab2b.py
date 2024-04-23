# Initialize a dictionary to store the count of people for each age
age_count = {}

# Open the file for reading
with open('lab2-data.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Skip the header line
        if line.startswith('#'):
            continue

        # Split the line by the pipe symbol '|'
        parts = line.strip().split('|')

        # Extract the age
        age = int(parts[2])

        # Update the count for the age
        if age in age_count:
            age_count[age] += 1
        else:
            age_count[age] = 1

# Display the count of people for each age
for age, count in age_count.items():
    print(f'Age: {age} -> Count: {count}')
