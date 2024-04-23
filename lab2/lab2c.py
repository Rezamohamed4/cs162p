from collections import defaultdict

# Open the file for reading
with open('lab2-data.txt', 'r') as file:
    profession_rates = defaultdict(list)

    # Read each line in the file
    for line in file:
        # Skip the header line
        if line.startswith('#'):
            continue

        # Split the line by the pipe symbol '|'
        parts = line.strip().split('|')

        # Extract the profession and rate
        profession = parts[3].strip()
        rate = float(parts[4])

        # Add the rate to the list of rates for the profession
        profession_rates[profession].append(rate)

# Calculate the average rate for each profession
average_rates = {}
for profession, rates in profession_rates.items():
    average_rates[profession] = sum(rates) / len(rates)

# Sort the professions in alphabetical order
sorted_professions = sorted(average_rates.keys())

# Display the professions and their average rates
for profession in sorted_professions:
    print(f'Profession: {profession} -> Average Rate: {average_rates[profession]:.2f}')
    