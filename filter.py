input_file = 'search_results.txt'
output_file = 'output.txt'

try:
    # Open input file for reading
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Filter lines containing "' found on'"
    filtered_lines = [line.strip() for line in lines if "' found on" in line]

    # Print filtered lines
    print("Filtered lines:")
    for line in filtered_lines:
        print(line)

    print("Number of filtered lines:", len(filtered_lines))

    # Open output file for writing
    with open(output_file, 'w') as file:
        for line in filtered_lines:
            file.write(line + '\n')

    print("Filtered lines have been written to", output_file)

except FileNotFoundError:
    print("Input file not found:", input_file)

except Exception as e:
    print("An error occurred:", str(e))
