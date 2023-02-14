import os

# Get the current working directory
cwd = os.getcwd()
print(cwd)
print("Current working directory:", cwd)

# Check if the file you want to serve is present
file_path = "./src/public/index.html"
if os.path.isfile(file_path):
    print("File found at:", file_path)
else:
    print("File not found:", file_path)