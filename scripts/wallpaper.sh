#!/bin/sh
URL="https://www.bing.com"$(curl -s 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=de-DE' | jq -r '.images[0].url')
#echo $URL
wget -q  -O /tmp/wallpaper.jpg $URL
gsettings set org.gnome.desktop.background picture-uri file:////tmp/wallpaper.jpg

