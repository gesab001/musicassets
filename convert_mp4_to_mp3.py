import subprocess
import os

def showList():
 jukebox = []
 for file in os.listdir("./"):
   if file.endswith(".mp4"):
      #print(os.path.join("/mydir", file))
      jukebox.append(file)
 lastNumber = len(jukebox) 
 print("lastNumber: " + str(lastNumber))
 for x in range(0, len(jukebox)):
   print(str(x) +"."+ "\t" + jukebox[x])  
 return jukebox   
 
def convert(number, jukebox):
  filename_mp4 = jukebox[number]
  if " " in filename_mp4:
    newfilename = filename_mp4.replace(" ", "_")
    os.rename(filename_mp4, newfilename )
    filename_mp4 = newfilename
  output = input("output filename:")
  filename_mp3 = output + ".mp3"
  #url = "https://www.youtube.com/watch?v="+videoId
  #subprocess.call("youtube-dl -x --audio-format mp3 "+ url +" --output " + filename_webm, shell=True)
  subprocess.call("ffmpeg -i " + filename_mp4 + " -f mp3 -ab 160000 -vn " + filename_mp3, shell=True)
  
while True:		
   jukebox = showList()
   selection = int(input("select number: "))
   convert(selection, jukebox)


