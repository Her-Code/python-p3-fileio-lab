from pathlib import Path

# lib/file_io.py

def write_file(file_name, file_content):
    """Write content to a file with a .txt extension. Overwrites if file exists."""
    # Convert file_name to a string if it is a PosixPath object
    if isinstance(file_name, Path):
        file_name = str(file_name)
    
    with open(file_name + '.txt', 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """Append content to a file with a .txt extension. Creates file if it does not exist."""
    # Convert file_name to a string if it is a PosixPath object
    if isinstance(file_name, Path):
        file_name = str(file_name)
    
    with open(file_name + '.txt', 'a') as file:
        # Remove leading newline characters from append_content
        append_content = append_content.lstrip('\n')
        
        # Write content with a newline at the end
        file.write('\n' + append_content)

def read_file(file_name):
    """Read content from a file with a .txt extension and return it. Returns empty string if file does not exist."""
    # Convert file_name to a string if it is a PosixPath object
    if isinstance(file_name, Path):
        file_name = str(file_name)
    
    try:
        with open(file_name + '.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ''

