import sys

# initialize clipboard storage 
clipboard_storage = {}

# Copy text to clipboard
def copy(keyword, text):
    pass

# Paste text from clipboard
def paste(keyword):
    pass

# list available keywords
def list_keywords():
    return list(clipboard_storage.keys())

def clear(keyword):
    if keyword in clipboard_storage.keys():
        del clipboard_storage[keyword]
    else:
        print(f'{keyword} not found.')

def clipboard():
    copy('work', 'work-related notes')
    copy('home', 'grocery-list')
    
    print(paste('work'))
    print(paste('home'))
    
    print(f'Available keywords: {list_keywords()}')
    
    clear('work')
    
    print(f'Available keywords: {list_keywords()}')

if __name__ == '__main__':
    clipboard()
        