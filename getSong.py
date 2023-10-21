import subprocess
import os

files = os.listdir()
print(files)
filename = input("filename: ")
output = input("output filename: ")
output = output + ".mp3"
command = "ffmpeg -i " + filename + " -vn -ab 128k -ar 44100 -y " + output 
subprocess.call(command, shell=True)