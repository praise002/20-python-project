# Project - Directory Maintainer

The Directory Maintainer is a Python program designed to automate the organization of files within a directory. It simplifies the task of creating folders for specific file extensions, categorizing files, removing older log files, moving large text files to a separate folder, and segregating cleaned log files from raw ones. With this tool, you can maintain order and structure within your file repository effortlessly.

## Usage
To use the Directory Maintainer, execute the following command in your terminal:

```python3 main.py [path/to/directory] [option1] [option2]``

- `[path/to/directory]`: Provide the path to the directory you want to organize.
- `[option1]`: Specify the first option according to the program requirements.
- `[option2]`: Specify the second option as required by the program.

## Features

### Automated File Organization
The Directory Maintainer automates the process of creating folders for various file extensions and organizing the files accordingly. You no longer need to manually sort files; this tool does it for you.

### Removal of Older Log Files
It identifies and deletes older log files, helping you manage storage space efficiently.

### Segregation of Cleaned and Raw Log Files
The program separates cleaned log files from raw ones, streamlining data processing and analysis.

### Handling Large Text Files
Large text files are moved to a separate folder within the '.txt' directory, making it easier to access and manage them.

## Usage Example
Suppose you have a directory named "MyFiles" that contains various files, including logs, text files, and PDFs. To use the Directory Maintainer, you would run the following command:

```python3 main.py /path/to/MyFiles --organize --delete-logs```

This command instructs the program to organize the files and delete older log files.
You can do yours differently. You don't need to follow the same structure. This is just an hint.
