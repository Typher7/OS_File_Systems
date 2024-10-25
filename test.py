from main import FileSystem

fs = FileSystem()

# Test Invalid Paths:
print("\nTesting Invalid Paths:")

# Multiple Consecutive Slashes
fs.create_file("//docs/", "file.txt", "Content")
if "file.txt" in fs.navigate_to_directory("/docs").files:
        print("Test create_file_multiple_slashes: PASSED")
else:
        print("Test create_file_multiple_slashes: FAILED")clear
fs.create_file("/docs", "file.txt", "Content")
if fs.read_file("/docs//", "file.txt") == "Content":
        print("Test read_file_multiple_slashes: PASSED")
else:
        print("Test read_file_multiple_slashes: FAILED")

# Backtracking (using '..')
fs.create_directory("/", "docs")
fs.create_file("/docs/../", "file.txt", "Content") 
if fs.navigate_to_directory("/docs/../") is None:
        print("Test create_file_backtrack: PASSED")
else:
            print("Test create_file_backtrack: FAILED")
if fs.read_file("/docs/../", "file.txt") is None:
        print("Test read_file_backtrack: PASSED")
else:
        print("Test read_file_backtrack: FAILED")

# Empty Path
fs.create_file("", "file.txt", "Content")
if fs.navigate_to_directory("") is None:
    print("Test create_file_empty_path: PASSED")
else:
        print("Test create_file_empty_path: FAILED")
fs.create_file("/", "file.txt", "Content")
if fs.read_file("/", "") is None:
        print("Test read_file_empty_path: PASSED")
else:
        print("Test read_file_empty_path: FAILED")