#!/usr/bin/env sh

git pull


echo videoId
read videoId

echo filename
read filename

youtube-dl -f mp4 "https://www.youtube.com/watch?v=$videoId" --output "$filename.mp4"

ffmpeg -i "$filename.mp4" -vn -acodec libmp3lame -ac 2 -ab 160k "$filename.mp3"

python3 update_songlist.py

git add .

git commit -m "added $filename.mp4 $filename.mp3"
git push --all

