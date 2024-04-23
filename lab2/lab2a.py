# Open the file for reading
with open('lab2-data.txt', 'r') as file:
    data = []
    
    # Read each line in the file
    for line in file:
        # Skip the header line
        if line.startswith('#'):
            continue
        
        # Split the line by the pipe symbol '|'
        parts = line.strip().split('|')
        
        # Extract the data
        person = {
            'Person ID': int(parts[0]),
            'Name': parts[1],
            'Age': int(parts[2]),
            'Profession': parts[3],
            'Rate': float(parts[4])
        }
        
        # Append the person data to the list
        data.append(person)

# Print the parsed data
for person in data:
    print(person)