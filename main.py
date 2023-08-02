import os # Lets us access files and directories
import easygui # Lets the user select a directory
folder_path = easygui.diropenbox() # Lets user select the [vehicles] path
new_file_names = set() # Creates a set named "new_file_names"

for root, dirs, files in os.walk(folder_path): # For each folder and file inside of the set folder path:
    if "stream" in dirs: # If "stream" is in the directory
        stream_path = os.path.join(root, "stream") # Sets "stream_path" to the stream directory
        stream_files = os.listdir(stream_path) # Gets a list of all the file names in the "stream" folder
        for file_name in stream_files: # For each file name in stream_files:
            if file_name.endswith("+hi.ytd") or file_name.endswith(".ytd"): # If file ends with "+hi.ytd" or ".ytd":
                file_name = file_name.replace("+hi.ytd", "").replace(".ytd", "") # Remove "+hi.ytd" or ".ytd" from file name
            if file_name.endswith("_hi.ytf") or file_name.endswith(".ytf"): # if file name ends with "_hi.ytf" or ".ytf":
                file_name = file_name.replace("_hi.ytf", "").replace(".ytf", "") # Remove "_hi.ytf" or ".ytf" from file name
            if not os.path.isdir(os.path.join(stream_path, file_name)): # If the content inside of stream is not a folder:
                new_file_names.add(os.path.splitext(os.path.basename(file_name))[0]) # Add the file name to the set

new_file_names = sorted(set([x for x in new_file_names if not x.endswith("_hi")])) # Remove duplicate files from the set
print(",\n".join(['"' + name + '"' for name in new_file_names])) # Print out new list of file names in the specified format with a new line after each comma

while True: # Repeats the code
    quit = input("Would you like to exit? [Y/N]: ").upper() # Asks the user to type y or n and converts the input to uppercase
    if quit == "Y": # If the user typed "Y":
        quit() # Quits the program
