import subprocess
import os

def showList():
 jukebox = []
 for file in os.listdir("./"):
   if file.endswith(".mp4"):
      #print(os.path.join("/mydir", file))
      jukebox.append(file)
 jukebox.append("SEARCH") 
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

def searchSong(keyword, jukebox):
 searchresults = []
 for song in jukebox:
    if keyword.lower() in song.lower():
      searchresults.append(song)
 searchresults.append("MENU") 

 lastNumber = len(searchresults) 
 print("lastNumber: " + str(lastNumber))
 for x in range(0, len(searchresults)):
   print(str(x) +"."+ "\t" + searchresults[x])  
 return searchresults  
 
while True:		
   jukebox = showList()
   selection = int(input("select number: "))
   if jukebox[selection]=="SEARCH":
     keyword = input("search: ")
     jukebox = searchSong(keyword, jukebox)
     if len(jukebox)==0:
       print("no match found")
       keyword = input("search again? (y/n)")
       if keyword.lower()=="y":
         keyword = input("search again? (y/n)")     
         jukebox = searchSong(keyword, jukebox)       
         selection = int(input("select number: "))
         convert(selection, jukebox)   
     else:  
       selection = int(input("select number: "))
       if jukebox[selection]=="MENU":
          print("back to menu")
       else:          
          convert(selection, jukebox)
   else:
     convert(selection, jukebox)


