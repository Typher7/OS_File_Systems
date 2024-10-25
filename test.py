from main import FileSystem

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

#Test same file creating error
fs.create_file("/docs", "file1.txt", "Hello World!")
fs.create_file("/docs", "file1.txt", "Hello World!")

#Test unknown directory
fs.create_file("/user", "file1.txt", "Hello World!")

#Tests deletion of files that don't exist
fs.delete_file("/docs", "file4.txt")

#Reads file that doesn't exist
print("Reading 'file5.txt':", fs.read_file("/docs", "file5.txt"))

#Writing file that doesn't exist
fs.write_to_file("/docs", "file5.txt", "Updated content")

#Empty Path
fs.create_file("", "file.txt", "Content")
if fs.navigate_to_directory("") is None:
    print("Test create_file_empty_path: PASSED")
else:
        print("Test create_file_empty_path: FAILED")



# fs.create_file("/", "file.txt", "Content")
# if fs.read_file("/", "") is None:
#         print("Test read_file_empty_path: PASSED")
# else:
#         print("Test read_file_empty_path: FAILED")

# # Backtracking (using '..')
# fs.create_directory("/", "docs")
# fs.create_file("/docs/../", "file.txt", "Content") 
# if fs.navigate_to_directory("/docs/../") is None:
#         print("Test create_file_backtrack: PASSED")
# else:
#             print("Test create_file_backtrack: FAILED")

# if fs.read_file("/docs/../", "file.txt") is None:
#         print("Test read_file_backtrack: PASSED")
# else:
#         print("Test read_file_backtrack: FAILED")