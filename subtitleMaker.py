import time
import os

print(os.listdir())
files = os.listdir()
for f in files:
  if f.endswith(".lyrics"):
    print(f)
f = open("HAVE__A_LITTLE_TALK_WITH_JESUS(African_Edition)___Jehovah_Shalom_Acapella-LlGXmAggHWQ.mp4.lyrics", "r")
string = f.readlines()
print(string)
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("{0}:{1}:{2}".format(int(hours),int(mins),sec))

count = 0
start = "00:00:00"
end = "00:00:00"
"""
1
00:00:00,498 --> 00:00:02,827
- Here's what I love most
about food and diet.

2
00:00:02,827 --> 00:00:06,383
We all eat several times a day,
and we're totally in charge

3
00:00:06,383 --> 00:00:09,427
of what goes on our plate
and what stays off.
"""
lineNumber = 1
while count<len(string):
  line = string[count].strip()

  input(line)
  count = count + 1

  start_time =  time.time()
  print()
  print(lineNumber)
  print(start + " --> " + end )
  print(line)
  print()
  with open("test.srt", "a") as outfile:
    outfile.write(str(lineNumber))
    outfile.write("\n")
    outfile.write(start + " --> " + end)
    outfile.write("\n")
    outfile.write(line)
    outfile.write("\n\n")
  lineNumber = lineNumber + 1
  input("Press Enter to stop")
  end_time = time.time()
  time_lapsed = end_time - start_time
  time_convert(time_lapsed)

