
# Duplicate Image Finder

  

## Description

This Python script is designed to find duplicate image files within a specified folder and move them to a "delete" folder. It utilizes the `Pillow` library for image processing and hashing to compare image files.

  

## Setup

1.  **Clone the Repository**: Clone this repository to your local machine using the following command:

```bash
git clone <repository-url>
```

2.  **Install Dependencies**: Make sure you have Python 3 installed on your system. Install the required dependencies using `**pip**`:
```bash
pip install -r requirements.txt
```
3.  **Activate the Virtual Environment**: Activate the virtual environment and install the packages (This one happens to be on mac). 

4.  **Run the Program**: Add duplicate photos in the `photos` folder and run the script:
```bash
python main.py
```

## How It Works

The script works by recursively traversing the specified folder and its subfolders, calculating an MD5 hash for each image file. If it encounters a duplicate hash, it moves the duplicate image file to a "delete" folder within the original folder.

### Workflow:

1.  Traverse the specified folder and its subfolders.
2.  For each image file encountered:
    -   Calculate the MD5 hash of the file.
    -   Check if the hash already exists in the hash dictionary.
    -   If it does, move the file to the "delete" folder.
    -   If not, add the hash to the dictionary.
3.  Move any duplicate files found to the "delete" folder.

## Notes

-   Ensure that you have sufficient permissions to move files within the specified folder.
-   Make sure to review the `delete` folder after running the script to confirm that duplicate images have been moved correctly.