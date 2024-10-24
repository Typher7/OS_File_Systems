# File System Implementation in Python  

This Python implementation provides a simple file system with the following features:  

- **File Management**: Create, read, write, and delete files within the file system.  
- **Directory Management**: Create and navigate directories to manage the file system hierarchy.  
- **Error Handling**: The system provides informative error messages when operations fail.  

## Classes  

### `File`  
This class represents a file in the file system. Each file has a name and content (which is empty by default).  

### `Directory`  
This class represents a directory in the file system. Each directory has a name, a dictionary to store files, and another dictionary to store subdirectories.  

### `FileSystem`  
This is the main class that manages the entire file system. It has the following methods:  

1. `create_file(path, file_name, content="")`: Creates a new file in the specified directory path.  
2. `read_file(path, file_name)`: Reads the content of the specified file in the given directory path.  
3. `write_to_file(path, file_name, content)`: Updates the content of the specified file in the given directory path.  
4. `delete_file(path, file_name)`: Deletes the specified file from the given directory path.  
5. `create_directory(path, directory_name)`: Creates a new directory in the specified parent directory path.  
6. `navigate_to_directory(path)`: Navigates to the specified directory path and returns the directory object.  

## Usage Example  

Here's an example of how to use the `FileSystem` class:  

```python  
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