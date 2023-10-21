import os
import subprocess

def downloadMusic():
  youtubeurlOrId = input("youtube url or id: ")
  subprocess.call("yt-dlp -f mp4 " + youtubeurlOrId, shell=True)
  
def renameSong(number, jukebox):
  filename = jukebox[number]
  if " " in filename:
    newfilename = filename.replace(" ", "_")
    os.rename(filename, newfilename )
    filename = newfilename
  path = os.path.join(r"C:\Users\giova\Videos\musicassets", filename)
  newname = input("enter new song name for " + filename +" :")
  while newname in jukebox:
    print(newname + " already exists")
    newname = input("try a different new song name for " + filename +" :")
  newname = newname + ".mp4"  
  newpath = os.path.join(r"C:\Users\giova\Videos\musicassets", newname)
  os.rename(path, newpath)
  
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
 
def showList():
 jukebox = []
 for file in os.listdir("./"):
   if file.endswith(".mp4"):
      #print(os.path.join("/mydir", file))
      jukebox.append(file)
 jukebox.append("DOWNLOAD NEW MUSIC") 
 jukebox.append("RENAME SONG") 
 jukebox.append("SEARCH") 
 jukebox.append("EXIT") 
 lastNumber = len(jukebox) 
 print("lastNumber: " + str(lastNumber))
 for x in range(0, len(jukebox)):
   print(str(x) +"."+ "\t" + jukebox[x])  
 return jukebox   
def play(number, jukebox):
  filename = jukebox[number]
  if " " in filename:
    newfilename = filename.replace(" ", "_")
    os.rename(filename, newfilename )
    filename = newfilename
  path = os.path.join(r"C:\Users\giova\Videos\musicassets", filename)
  subprocess.call("ffplay " + path, shell=True)
 
while True:		
   jukebox = showList()
   selection = int(input("select number: "))

   if jukebox[selection]=="DOWNLOAD NEW MUSIC":
     downloadMusic()
   elif jukebox[selection]=="RENAME SONG":
     selection = int(input("select song number: "))
     renameSong(selection, jukebox)
   elif jukebox[selection]=="SEARCH":
     keyword = input("search: ")
     jukebox = searchSong(keyword, jukebox)
     if len(jukebox)==0:
       print("no match found")
       keyword = input("search again? (y/n)")
       if keyword.lower()=="y":
         keyword = input("search again? (y/n)")     
         jukebox = searchSong(keyword, jukebox)       
         selection = int(input("select number: "))
         play(selection, jukebox)   
     else:  
       selection = int(input("select number: "))
       if jukebox[selection]=="MENU":
          print("back to menu")
       else:          
          play(selection, jukebox)
                 
   elif jukebox[selection]=="EXIT":   
     break   
   else:
     play(selection, jukebox)  