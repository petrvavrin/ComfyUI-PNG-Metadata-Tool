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
ver.1.3
'''


from PIL import Image
import json
import os
import sys


#input_dir = os.path.dirname(os.path.abspath(__file__))

choice = input(
  "------------------------------------------\n"
  "Which type of function do you want to use?\n"
  "1. Remove metadata from image\n"
  "2. Read metadata from image\n"
  "3. Exit\n"
  "------------------------------------------\n"
)


def remove_metadata():
  source_dir = input('Enter source image directory: ')
  
  parent_dir = input('Enter output parent directory path: ')
  dir_name = input('Enter output directory name: ')

  path = os.path.join(parent_dir, dir_name)
  os.mkdir(path)

  for filename in os.listdir(source_dir):
    # Check if the file is a PNG file
    if filename.endswith(".png"):
      # Open the image file
      image_path = os.path.join(source_dir, filename)
      
      #Load image
      img = Image.open(image_path)

      #Save new image without metadata
      new_file_path = os.path.join(path, 'no_metadata_' + filename)
      img.save(new_file_path)
      print(f"Saved image without metadata: {new_file_path}")


def read_metadata():
  source_dir = input('Enter image source directory: ')

  image = Image.open(source_dir)
  print(image.info)
  image.close()


def print_menu():
  if choice in ["1", "2", "3"]:
    pass
  else:
    print('Select valid number and try again')
    exit(0)


  if choice == '1':
    remove_metadata()
    print('Done')
    exit(0)

  elif choice == '2':
    read_metadata()
    print('Done')
    exit(0)

  elif choice == '3':
    print('Exiting ...')
    exit(0)


print_menu()