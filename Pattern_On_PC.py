import csv
from PIL import Image
import os

def get_image_resolution(image_path):
    try:
        with Image.open(image_path) as image:
            width, height = image.size
            return width, height
    except Exception as e:
        print("Error:", e)
        return None

#This section if a test for adding color to the prosses

# def count_touching_pixels(image_path, new_width=None, output_file="pixel_data.csv"):
#     print(new_width)
#     # Load image from file path
#     image = Image.open(image_path)
    
#     # Check if resizing is requested
#     if new_width is not None:
#         # Calculate height while maintaining aspect ratio
#         original_width, original_height = image.size
#         aspect_ratio = original_height / original_width
#         new_height = int(new_width * aspect_ratio)
        
#         # Resize the image to the new dimensions
#         image = image.resize((new_width, new_height))
        
#     else:
#         pass
   
#     # Convert original image to grayscale
#         image_bw = image.convert("L")

#     # Get pixel data
#     pixel_data = list(image.getdata())
#     width, height = image.size
    
#     # Initialize variables to store counts
#     current_count = 0
#     current_color = None
#     total_pixels_in_row = 0
    
#     # Open output file for writing
#     with open(output_file, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['Color', 'Count'])
        
#         # Loop through each pixel
#         for y in range(height):
#             for x in range(width):
#                 pixel_value = pixel_data[y * width + x]
#                 pixel_brightness = 0.2126 * pixel_value[0] + 0.7152 * pixel_value[1] + 0.0722 * pixel_value[2]

                
#                 # Check if pixel is red uncomment if you want to add color
                
#                 if pixel_value[0] > pixel_value[1] + pixel_value[2]:
#                     pixel_color = 'red'
#                 elif pixel_brightness < 100:
#                     pixel_color = 'black'
#                 elif pixel_brightness > 200:
#                     pixel_color = 'white'
#                 else:
#                     pixel_color = 'gray'

                
#                 # If it's the first pixel or pixel color changed, write the count
#                 if current_color is None:
#                     current_color = pixel_color
#                     current_count = 1
#                 elif pixel_color != current_color:
#                     writer.writerow([current_color.capitalize(), current_count])
#                     current_color = pixel_color
#                     current_count = 1
#                 else:
#                     current_count += 1
                    
#                 total_pixels_in_row += 1
            
#             # Write the count for the last color in the row
#             writer.writerow([current_color.capitalize(), current_count])
#             writer.writerow(['End of Row - Total Pixels', total_pixels_in_row])
            
#             # Reset variables for the next row
#             current_color = None
#             current_count = 0
#             total_pixels_in_row = 0


# Default Grayscale

def count_touching_pixels(image_path, new_width=None, output_file="pixel_data.csv"):
    # Load image from file path
    image = Image.open(image_path)
    
    # Check if resizing is requested
    if new_width is not None:
        # Calculate height while maintaining aspect ratio
        original_width, original_height = image.size
        aspect_ratio = original_height / original_width
        new_height = int(new_width * aspect_ratio)
        
        # Resize the image to the new dimensions
        image_resized = image.resize((new_width, new_height))
        
        # Convert image to grayscale`
        image_bw = image_resized.convert("L")
    else:
        # Convert original image to grayscale
        image_bw = image.convert("L")

    # Get pixel data
    pixel_data = list(image_bw.getdata())
    width, height = image_bw.size
    
    # Initialize variables to store counts
    current_count = 0
    current_color = None
    total_pixels_in_row = 0
    
    # Open output file for writing
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Color', 'Count'])
        
        # Loop through each pixel
        for y in range(height):
            for x in range(width):
                pixel_value = pixel_data[y * width + x]
                if pixel_value < 100:
                    pixel_color = 'black'
                elif pixel_value > 200:
                    pixel_color = 'white'
                else:
                    pixel_color = 'gray'
                
                # If it's the first pixel or pixel color changed, write the count
                if current_color is None:
                    current_color = pixel_color
                    current_count = 1
                elif pixel_color != current_color:
                    writer.writerow([current_color.capitalize(), current_count])
                    current_color = pixel_color
                    current_count = 1
                else:
                    current_count += 1
                    
                total_pixels_in_row += 1
            
            # Write the count for the last color in the row
            writer.writerow([current_color.capitalize(), current_count])
            writer.writerow(['End of Row - Total Pixels', total_pixels_in_row])
            
            # Reset variables for the next row
            current_color = None
            current_count = 0
            total_pixels_in_row = 0
            

if __name__ == "__main__":
    image_path = input("Enter the path to the image file: ")
    if os.path.exists(image_path):
        resolution = get_image_resolution(image_path)
        if resolution:
            print("Resolution:", resolution)
    else:
        print("Error: File not found.")
    resize_choice = input("Do you want to resize the image? (y/n): ").lower()
    if resize_choice == 'y':
        new_width = int(input("Enter the width of the new resolution: "))
    else:
        new_width = None
    
    count_touching_pixels(image_path, new_width)
    
