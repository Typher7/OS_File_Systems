class File:
    def __init__(self, name, content=""):  # This class instantiates a file empty by default
        self.name = name
        self.content = content

class Directory:
    def __init__(self, name):  # This class instantiates a directory implemented with dictionaries
        self.name = name
        self.files = {}  # Dictionary to store files
        self.subdirectories = {}  # Another dictionary to store sub-directories

class FileSystem:
    def __init__(self):
        self.root = Directory("/")
    
    def create_file(self, path, file_name, content=""):
        # Navigate to the directory 'path' where the file will be created
        directory = self.navigate_to_directory(path)
        if directory is not None:
            # Check if the file already exists
            if file_name in directory.files:
                print(f"Error: File '{file_name}' already exists.")
            else:
                # Create the new file
                directory.files[file_name] = File(file_name, content)
                print(f"File '{file_name}' created in '{path}'.")
        else:
            print(f"Error: Directory '{path}' not found.")

    def read_file(self, path, file_name):
        # Navigate to the directory 'path' containing the file
        directory = self.navigate_to_directory(path)

        if directory and file_name in directory.files:
            return directory.files[file_name].content
        
        return f"Error: File '{file_name}' not found in '{path}'."

    def write_to_file(self, path, file_name, content):
        # Navigate to the directory 'path' containing the file
        directory = self.navigate_to_directory(path)
        if directory and file_name in directory.files:
            # Update the content of the file
            directory.files[file_name].content = content
            print(f"File '{file_name}' in '{path}' updated.")
        else:
            print(f"Error: File '{file_name}' not found in '{path}'.")

    def delete_file(self, path, file_name):
        directory = self.navigate_to_directory(path)
        if directory and file_name in directory.files:
            del directory.files[file_name] # Removes the file from the directory
            print(f"File '{file_name}' deleted from '{path}'.")
        else:
            print(f"Error: File '{file_name}' not found in '{path}'.")

    def create_directory(self, path, directory_name):
        # Navigate to the parent directory
        directory = self.navigate_to_directory(path)
        if directory:
            # Check if directory already exists
            if directory_name in directory.subdirectories:
                print(f"Error: Directory '{directory_name}' already exists.")
            else:
                # Create the new directory in the parent directory
                directory.subdirectories[directory_name] = Directory(directory_name)
                print(f"Directory '{directory_name}' created in '{path}'.")
        else:
            print(f"Error: Directory '{path}' not found.")
        
    def navigate_to_directory(self, path):
        # If the path is root return it
        if path == "/":
            return self.root
        
        #Initialize the current directory to the root
        current_directory = self.root
        # Split the path into parts [stored in a list/array]
        path_parts = path.strip("/").split("/")
        for part in path_parts:
            # Assign part to current dir if it's a sub-dir of the current dir
            # Else return None to indicate the directory wasn't found
            if part in current_directory.subdirectories:
                current_directory = current_directory.subdirectories[part]
            else:
                return None
        #Since loop wasn't truncated, return the current dir which should correspond to 'path'
        return current_directory