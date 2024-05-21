'''/$$$$$  /$$$$$$$  /$$      /$$ /$$$$$$$$
 /$$__  $$| $$__  $$| $$$    /$$$|__  $$__/
| $$  |__/| $$  | $$| $$$$  /$$$$   | $$
| $$      | $$$$$$$/| $$ $$/$$ $$   | $$
| $$      | $$____/ | $$  $$$| $$   | $$
| $$    $$| $$      | $$|  $ | $$   | $$
|  $$$$$$/| $$      | $$|    | $$   | $$
 |______/ |__/      |__/     |__/   |__/
        ComfyUI PNG Metadata Tool
which can remove/read generation metadata.
===========================================
ver.1.0
'''

# Add path argument, choice for create new files or replace

from PIL import Image
import json
import os


#######################################
'''
with open("metadata.txt", "w") as f:
        image = Image.open("pic.png")
        metadata = image.info
        result = str(metadata)
        f.write(result)
        f.close()
        image.close()
'''
#######################################
input_dir = os.path.dirname(os.path.abspath(__file__))

choice = input(
  "------------------------------------------\n"
  "Which type of function do you want to use?\n"
  "1. Remove metadata from image\n"
  "2. to be added\n"
  "3. Exit\n"
  "------------------------------------------\n"
)


def remove_metadata():

  for filename in os.listdir(input_dir):
    # Check if the file is a PNG file
    if filename.endswith(".png"):
      # Open the image file
      image_path = os.path.join(input_dir, filename)
      
      #Load image
      img = Image.open(image_path)

      #Save new image without metadata
      new_file_path = os.path.join(input_dir, 'no_metadata_' + filename)
      img.save(new_file_path)
      print(f"Saved image without metadata: {new_file_path}")


def print_menu():
  if choice in ["1", "2", "3"]:
    pass
  else:
    print('Select valid number and try again')
    exit(0)


  if choice == '1':
    remove_metadata()
    print('Done')

  elif choice == '2':
    exit(0)
    print('Done')

  elif choice == '3':
    print('Exiting ...')
    exit(0)


print_menu()
