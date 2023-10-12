import os

# Size constants
KB = 1000
MB = KB * 1000
GB = MB * 1000

# Initial bytes for filetypes
pdf = bytes.fromhex('25 50 44 46')
gif = bytes.fromhex('47 49 46')
png = bytes.fromhex('89 50 4E 47 0D 0A 1A 0A')
jpeg_start = bytes.fromhex('FF D8')
jpeg_end = bytes.fromhex('FF D9')
utf8_bom = bytes.fromhex('EF BB BF')

def file_size(filename):
    file_size_in_bytes = os.stat(filename).st_size  # returns file size in bytes
    # Write the functionality to check the file size and convert it to their respective KB, MB or GB
        
def file_type(filename):
    pass

def file_info(filename):
    if not os.path.isfile(filename):
        return f"Error: File [{filename}] does not exist"
    else:
        file_name = f'{filename}'
        file_size1 = file_size(filename)
        file_type1 = file_type(filename)
        file_info = f'File Statistics:\nFile Name: {file_name}\nFile Size: {file_size1}\nFile Type: {file_type1}'
        return file_info


# Run the fileinfo function on a provided filename
def main():
    filename = input("Enter a file name please: ")
    print(file_info(filename))

if __name__ == "__main__":
    main()
