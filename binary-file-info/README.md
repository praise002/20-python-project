# Binary File Info

In this project, you will practice working with binary files that aren't encoded text.
You will write a program that accepts the name of a file from standard input, and prints out the following information about that file:
- File name (as it was entered to the program)
- File size (in bytes, KB, MB or GB)
- The type of the file, by checking for common patterns in the bytes 

## Steps
- Open the file in 'rb' read-binary mode
- It will use the first five letters or characters to determine the extension

## File Size Conversion
The script converts the file size to more human-readable units as follows:

- If the file size is less than 1 MB, it's displayed in kilobytes (KB).
- If the file size is less than 1 GB, it's displayed in megabytes (MB).
- If the file size is 1 GB or greater, it's displayed in gigabytes (GB).

## Detecting the file type from a byte pattern
Different kinds of files often begin with a specific pattern of bytes.

Here are the ones that your program needs to be able to detect, and their byte patterns:

- PDF: first four bytes are 0x25 0x50 0x44 0x46
- GIF: first three bytes are 0x47 0x49 0x46
- PNG image files begin with an 8-byte signature which identifies the file as a PNG file and allows detection of common file transfer - problems: 0x89 0x50 0x4E 0x47 0x0D 0x0A 0x1A 0x0A
- UTF-8 encoded text files sometimes begin with the bytes 0xEF 0xBB 0xBF (called a Byte Order Mark, BOM)
- JPEG image files begin with 0xFF 0xD8 and end with 0xFF 0xD9
Your program should print out the type of file it detects, or "Unknown file type" if none of these types match.

## Usage
1. **Clone or Download**: Clone this repository or download the Python script to your local machine.

2. **Run the Script**: Open your terminal or command prompt, navigate to the directory where the script is located, and run it by executing the following command:

```python main.py```

3. **Input a File Name**: You will be prompted to enter the name of the file you want to check.

4. **View File Information**: The script will display the file information as specified.

## Expected Results

Missing file:

```sh
python main.py
Enter a file name please: assets/does-not-exist.txt
Error: File [assets/does-not-exist.txt] does not exist
```

GIF:

```sh
python main.py
Enter a file name please: assets/test02.gif
File Statistics:
File Name: assets/test02.gif
File Size: 41.02 KB
File Type: GIF
```

## Testing
1. Define Test Cases
2. Write Test Cases
3. Run the Tests
   
```py test_main.py```