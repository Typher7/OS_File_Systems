class File:
    def __init__(self, name, content=""):
        self.name = name
        self.content = content

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.subdirectories = {}

class FileSystem:
    def __init__(self):
        self.root = Directory("/")
    
    def create_file(self, path, file_name, content=""):
        directory = self.navigate_to_directory(path)
        if directory is not None:
            if file_name in directory.files:
                print(f"Error: File '{file_name}' already exists.")
            else:
                directory.files[file_name] = File(file_name, content)
                print(f"File '{file_name}' created in '{path}'.")
        else:
            print(f"Error: Directory '{path}' not found.")

    def read_file(self, path, file_name):
        directory = self.navigate_to_directory(path)
        if directory and file_name in directory.files:
            return directory.files[file_name].content
        print(f"Error: File '{file_name}' not found in '{path}'.")
        return None

    def write_to_file(self, path, file_name, content):
        directory = self.navigate_to_directory(path)
        if directory and file_name in directory.files:
            directory.files[file_name].content = content
            print(f"File '{file_name}' in '{path}' updated.")
        else:
            print(f"Error: File '{file_name}' not found in '{path}'.")

    def delete_file(self, path, file_name):
        directory = self.navigate_to_directory(path)
        if directory and file_name in directory.files:
            del directory.files[file_name]
            print(f"File '{file_name}' deleted from '{path}'.")
        else:
            print(f"Error: File '{file_name}' not found in '{path}'.")

    def create_directory(self, path, directory_name):
        directory = self.navigate_to_directory(path)
        if directory:
            if directory_name in directory.subdirectories:
                print(f"Error: Directory '{directory_name}' already exists.")
            else:
                directory.subdirectories[directory_name] = Directory(directory_name)
                print(f"Directory '{directory_name}' created in '{path}'.")
        else:
            print(f"Error: Directory '{path}' not found.")
    
    def navigate_to_directory(self, path):
        if path == "/":
            return self.root
        current_directory = self.root
        path_parts = path.strip("/").split("/")
        for part in path_parts:
            if part in current_directory.subdirectories:
                current_directory = current_directory.subdirectories[part]
            else:
                return None
        return current_directory

# Main function to test the file system
def main():
    fs = FileSystem()
    
    # Test file creation
    fs.create_directory("/", "docs")
    fs.create_file("/docs", "file1.txt", "Hello World!")
    fs.create_file("/docs", "file2.txt", "Another file")
    
    # Test file reading
    print("Reading 'file1.txt':", fs.read_file("/docs", "file1.txt"))
    
    # Test file writing
    fs.write_to_file("/docs", "file1.txt", "Updated content")
    print("Reading 'file1.txt' after update:", fs.read_file("/docs", "file1.txt"))
    
    # Test file deletion
    fs.delete_file("/docs", "file1.txt")
    fs.read_file("/docs", "file1.txt")
    
if __name__ == "__main__":
    main()
