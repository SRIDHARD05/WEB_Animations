import os

def search_folder_in_directories(directories, target_folder_name):
    # List to hold paths of found folders
    found_folders = []
    
    # Loop over the directories to search
    for directory in directories:
        # Check if the directory exists
        if os.path.exists(directory) and os.path.isdir(directory):
            # Walk through the directory and check for the target folder
            for root, dirs, files in os.walk(directory):
                if target_folder_name in dirs:
                    # Append the full path of the target folder to the list
                    found_folders.append(os.path.join(root, target_folder_name))
                    # Optionally break if only the first instance is needed
                    # break
    return found_folders

# List of directories to search in
directories_to_search = [
   "."
]

# Folder name you are looking for
target_folder = "fbx"

# Call the function
found_folders = search_folder_in_directories(directories_to_search, target_folder)

# Print the results
if found_folders:
    print("Found 'gltf' folder in the following locations:")
    for folder in found_folders:
        print(folder)
else:
    print(f"'{target_folder}' folder not found in the specified directories.")
