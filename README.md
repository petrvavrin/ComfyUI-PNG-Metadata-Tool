# ComfyUI PNG Metadata Tool


## Overview

C.P.M.T. can remove/read generation metadata from the ComfyUI output image.
<img src="https://raw.githubusercontent.com/petrvavrin/ComfyUI-PNG-Metadata-Tool/master/CPMT_v1.drawio.svg" width="800px">

## Usage

Upon running the script, you will be prompted to choose between the following options:

1. **Remove metadata and create MD5 checksums:** 
   - You will be asked to enter the source directory of the images, the output parent directory, and the desired output directory name.
   - The script will process all PNG images in the source directory, remove their metadata, and save the new images in the specified output directory.
   - The script also generates an MD5 checksum for each file separately. It then creates an MD5 folder where the "data-checksum.md5" file is saved. The "Verify files.bat" startup script is also created to make it easier to run the data check with QuickSFV.

2. **Remove metadata from images:** 
   - You will be asked to enter the source directory of the images, the output parent directory, and the desired output directory name.
   - The script will process all PNG images in the source directory, remove their metadata, and save the new images in the specified output directory.

3. **Read metadata from image:** 
   - You will be prompted to provide the path to a PNG image.
   - The script will read and display the metadata of the specified image.

4. **Exit:** 
   - Terminates the script.
