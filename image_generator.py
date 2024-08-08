import csv
from PIL import Image
from tqdm import tqdm  # Import tqdm for progress bar

# Dictionary to map color names to their hexadecimal codes
COLOR_MAP = {
    "Black": "#000000",
    "White": "#FFFFFF",
    "Gray": "#808080"
}

def create_pixel_art(csv_filepath, output_image):
    # Dictionary to map color names to their hexadecimal codes
    COLOR_MAP = {
        "Black": "#000000",
        "White": "#FFFFFF",
        "Gray": "#808080",
        # "Red": "#FF0000"
    }

    # Initialize image size and pixel size
    # Read the CSV file to determine width and height
    with open(csv_filepath, 'r') as file:
        reader = csv.reader(file)
        width = 0
        height = 0
        for row in reader:
            if row[0] == "End of Row - Total Pixels":
                height += 1
                if width == 0:
                    width = int(row[1])  # Set width based on the first occurrence
                #break  # Exit the loop after processing the first "End of Row - Total Pixels" row
    pixel_size = 10

    # Create a blank image
    image = Image.new("RGB", (width * pixel_size, height * pixel_size), "white")

    # Open the CSV file and read the data
    with open(csv_filepath, 'r') as file:
        reader = csv.reader(file)
        current_row = 0
        current_column = 0
        # Use tqdm to create a progress bar
        for row in tqdm(reader, desc="Processing CSV", unit=" rows"):
            if row[0] == "Color" or "End of Row - Total Pixels" in row[0]:
                continue  # Skip header row or "End of Row - Total Pixels" row
            color_name = row[0]
            count = int(row[1])
            # Get the hexadecimal code for the color
            color_code = COLOR_MAP.get(color_name, "#000000")  # Default to black if color not found
            # Convert color from hexadecimal to RGB
            r = int(color_code[1:3], 16)
            g = int(color_code[3:5], 16)
            b = int(color_code[5:7], 16)
            # Draw pixels of this color
            for _ in range(count):
                x = current_column * pixel_size
                y = current_row * pixel_size
                image.paste((r, g, b), (x, y, x + pixel_size, y + pixel_size))
                current_column += 1
                if current_column >= width:
                    current_column = 0
                    current_row += 1

    # Save the image
    image.save(output_image)
    #image.show(output_image)

if __name__ == "__main__":
    csv_filepath = "pixel_data.csv"  # Input CSV file
    output_image = "static\images\pixel_art.png"  # Output image file
    create_pixel_art(csv_filepath, output_image)
    im = Image.open(output_image)
    im.show()