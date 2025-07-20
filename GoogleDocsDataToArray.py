import pandas as pd

def getData(link):

    # Attempt to load HTML table from the provided link
    try:
        file = pd.read_html(link, encoding='utf-8')
    except ValueError:
        print("No tables found at the provided link.")
        return
    
    # Get the first table from the list of tables
    table = file[0]

    # Initialise variables to track the maximum x and y values for the grid
    x_max = 0
    y_max = 0
    data = []
    
    # Parse each row in the table to extract the character and its coordinates
    for index, row in table.iterrows():
        try:
            x_value = int(row[0])           # X-coordinate
            y_value = int(row[2])           # Y-coordinate
            char_value = row[1]             # Unicode character
            data.append((x_value, y_value, char_value)) #Store data as a tuple
            x_max = max(x_max, x_value)     # Update grid width if needed
            y_max = max(y_max, y_value)     # Update grid height if needed
        except (ValueError, IndexError):
            # Skip header row
            continue
    
    # Create a 2d grid filled with space characters
    image_array = [[' ' for _ in range(x_max+1)] for _ in range(y_max+1)]

    # Populate the grid with characters at their specified coordinates
    for x_value, y_value, char_value in data:
        image_array[y_value][x_value] = char_value
    
    # Print the grid row by row
    for row in image_array:
        print(''.join(row))

# Link to the published Google Doc containing the data    
link = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
getData(link)

