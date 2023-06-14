import os
import subprocess

#\\wsl.localhost\Ubuntu\home\trevor\iQuadra\collegeWebScraping\Github repo\completed colleges

for x in os.listdir("\completed colleges"):
    if x.endswith(".py"):
        # Prints only text file present in My Folder
        print(x)
        # Execute the other file and capture its output
        output = subprocess.check_output(['python3', x])
        # Decode the output from bytes to string
        output = output.decode('utf-8')
        # Print the output
        print(output)

