import pandas as pd

def trim_header(filename):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(fullpath, nrows=0)
    
    # Trim whitespace, replace spaces/tabs with underscores, and convert to lowercase
    new_header = [col.strip().replace(' ', '_').replace('\t', '_').lower() for col in df.columns]
    
    # Format the modified header as a multi-line string
    header_lines = '\n'.join(new_header) + '\n'
    
    # Save the modified header to a new file
    output_filename = f"trimmed_{filename}"
    full_output_path = fr'{output_filename}.csv'
    with open(full_output_path, 'w') as file:
        file.write(header_lines)
    
    print(f"Trimmed header saved to {output_filename}")

# Ask the user to input the filename
filename = input("Enter the CSV filename: ")
fullpath = fr'C:\Users\datamicron\Documents\Sample Dataset\CSV\{filename}.csv'

# Call the function to trim the header
trim_header(filename)
