import csv
from PIL import Image
import requests
from io import BytesIO
from tqdm import tqdm

def open_and_execute(file_number):
    Image.MAX_IMAGE_PIXELS = None
    if file_number == 1:
        with open("Pattern_URL.py", 'r') as file:
            code = file.read()
            exec(code)
    elif file_number == 2:
        with open("Pattern_On_PC.py", 'r') as file:
            code = file.read()
            exec(code)
    elif file_number == "image_generator.py":
        with open("image_generator.py", 'r') as file:
            code = file.read()
            exec(code)
    else:
        print("Invalid input. Please enter 1 or 2.")

print("[1] URL")
print("[2] PC")  
choice = input(":")

try:
    choice = int(choice)
    open_and_execute(choice)
    open_and_execute("image_generator.py")  # Run image_generator.py after executing the chosen script
except ValueError:
    print("Invalid input. Please enter a number.")
