import subprocess

videoId = input("videoId:")
output = input("filename:")
filename_webm = output + ".webm"
filename_mp3 = output + ".mp3"
url = "https://www.youtube.com/watch?v="+videoId
subprocess.call("youtube-dl -x --audio-format mp3 "+ url +" --output " + filename_webm, shell=True)

subprocess.call("ffmpeg -i " + filename_webm + " " + filename_mp3, shell=True)

subprocess.call("rm " + filename_webm, shell=True) 
