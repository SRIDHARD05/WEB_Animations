import os

def search_file_in_directories(directories, target_file_name):
    # List to hold paths of found files
    found_files = []
    
    # Loop over the directories to search
    for directory in directories:
        # Check if the directory exists
        if os.path.exists(directory) and os.path.isdir(directory):
            # Walk through the directory and check for the target file
            for root, dirs, files in os.walk(directory):
                if target_file_name in files:
                    # Append the full path of the found file to the list
                    found_files.append(os.path.join(root, target_file_name))
                    # Optionally break if only the first instance is needed
                    # break
    return found_files

# List of directories to search in
directories_to_search = [
    "."
]

# File name you are looking for
target_file = "FBXLoader.js"

# Call the function
found_files = search_file_in_directories(directories_to_search, target_file)

# Print the results
if found_files:
    print(f"Found '{target_file}' file in the following locations:")
    for file in found_files:
        print(file)
else:
    print(f"'{target_file}' file not found in the specified directories.")
