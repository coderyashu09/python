import os

# Get the directory path from the user
directory = input("Enter the directory path: ")

# Check if the path exists
if os.path.exists(directory):
    print("\nContents of the directory:")
    contents = os.listdir(directory)
    for item in contents:
        print(item)
else:
    print("Directory not found. Please check the path.")
