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
ver.1.7
'''


from PIL import Image
from progress.bar import Bar
import os
import glob
import hashlib
import shutil



choice = input(
  '------------------------------------------\n'
  'Which type of function do you want to use?\n'
  '1. Remove metadata and create MD5 checksums\n'
  '2. Remove metadata from images\n'
  '3. Read metadata from image\n'
  '4. Exit\n'
  '------------------------------------------\n'
)


def remove_metadata_and_hash():
  source_dir = input('Enter source image directory: ')
  
  parent_dir = input('Enter output parent directory path: ')
  dir_name = input('Enter output directory name: ')

  path1 = os.path.join(parent_dir, dir_name)

  try:
    pngCounter = len(glob.glob1(source_dir,'*.png'))
    bar = Bar('Removing metadata...', max=pngCounter, suffix = '%(percent).1f%% - ETA: %(eta)ds')

    os.mkdir(path1)
    path2 = os.path.join(path1, 'ComfyUI_ALL_no_meta')
    os.mkdir(path2)

    for filename in os.listdir(source_dir):

      # Check if the file is a PNG file
      if filename.endswith('.png'):
        # Open the image file
        image_path = os.path.join(source_dir, filename)
        #Load image
        img = Image.open(image_path)
        #Save new image without metadata
        new_file_path = os.path.join(path2, 'no_metadata_' + filename)
        img.save(new_file_path)
        bar.next()

    bar.finish()
    print('Removing Done!')

    bat = open(os.path.join(path1, 'Verify files.bat'), 'w')
    bat.write(
    '@echo off\n'
    'cd /d "%~dp0"\n'
    'cd MD5\n'
    'start QuickSFV.EXE data-checksum.md5\n'
    )
    bat.close()
    print('BAT created!')

    path3 = os.path.join(path1, 'MD5')
    shutil.copytree(os.path.join(os.getcwd(), 'QuickSFV'), path3)
    print('MD5 folder created!')
    print('QuickSFV files copied')

    pngCounter = len(glob.glob1(source_dir,'*.png'))
    bar = Bar('Creating MD5 checksums...', max=pngCounter, suffix = '%(percent).1f%% - ETA: %(eta)ds')

    output_path = os.path.join(path3, 'data-checksum.md5')
    checksum_file = open(output_path, 'w')

    for filename in os.listdir(path2):

      # Check if the file is a PNG file
      if filename.endswith('.png'):
        # Open the image file
        image_path = os.path.join(path2, filename)
        #Load image
        img = open(image_path, 'rb')
        data = img.read()
        md5_returned = hashlib.md5(data).hexdigest()


        checksum_file.write(f'{md5_returned} *..\\ComfyUI_ALL_no_meta\\{filename}\n')

        bar.next()

    bar.finish()
    print('MD5 checksums done!')


  except:
    print('An error occurred!')


def remove_metadata():
  source_dir = input('Enter source image directory: ')
  
  parent_dir = input('Enter output parent directory path: ')
  dir_name = input('Enter output directory name: ')

  path = os.path.join(parent_dir, dir_name)

  try:
    pngCounter = len(glob.glob1(source_dir,'*.png'))
    bar = Bar('Processing...', max=pngCounter, suffix = '%(percent).1f%% - ETA: %(eta)ds')

    os.mkdir(path)

    for filename in os.listdir(source_dir):

      # Check if the file is a PNG file
      if filename.endswith('.png'):
        # Open the image file
        image_path = os.path.join(source_dir, filename)
        #Load image
        img = Image.open(image_path)
        #Save new image without metadata
        new_file_path = os.path.join(path, 'no_metadata_' + filename)
        img.save(new_file_path)
        bar.next()

    bar.finish()
    print('Done!')
  except:
    print('An error occurred!')


def read_metadata():
  source_dir = input('Enter image source directory: ')

  try:
    image = Image.open(source_dir)
    print(image.info)
    image.close()
    print('Done')
  except:
    print('Wrong path!')
    exit(0)


def print_menu():
  if choice in ['1', '2', '3', '4']:
    pass
  else:
    print('Select valid number and try again')
    exit(0)


  if choice == '1':
    remove_metadata_and_hash()
    exit(0)

  elif choice == '2':
    remove_metadata()
    exit(0)

  elif choice == '3':
    read_metadata()
    exit(0)

  elif choice == '4':
    print('Exiting ...')
    exit(0)


print_menu()