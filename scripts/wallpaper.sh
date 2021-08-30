#!/bin/bash

# en-US, ja-JP, en-AU, en-UK, de-DE, en-NZ, en-CA
# echo 'Which locale? Choose us, jp, au, de, nz or ca or wait 10 sec'
# read -t 3 l
# case $l in 
#     us)
#     l='en-US'
#     ;;
#     jp)
#     l='ja-JP'
#     ;;
#     au)
#     l='en-AU'
#     ;;
#     de)
#     l='de-DE'
#     ;;
#     nz)
#     l='en-NZ'
#     ;;
#     ca)
#     l='en-CA'
#     ;;
#     *)
#     l='de-DE'
#     ;;
# esac
l='en-US'

URL="https://www.bing.com"$(curl -s 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=$l' | jq -r '.images[0].url')
wget -q -O $HOME/Pictures/wallpaper-new.jpg $URL

if command -v convert &> /dev/null
then
    convert $HOME/Pictures/wallpaper-new.jpg -filter Gaussian -blur 0x3 $HOME/Pictures/wallpaper-blur.jpg
fi

wallpaper=$(gsettings get org.gnome.desktop.background picture-uri)
gsettings set org.gnome.desktop.background picture-uri file://$HOME/Pictures/wallpaper-new.jpg

echo -n "Nice wallpaper? (Y/n)? "
read answer
if [ "$answer" != "${answer#[Nn]}" ] ;then
    echo "Oh, ok... reverting"
else
    cp -r $HOME/Pictures/wallpaper-new.jpg $HOME/Pictures/wallpaper.jpg
    wallpaper="file://$HOME/Pictures/wallpaper.jpg"
fi

rm $HOME/Pictures/wallpaper-new.jpg

gsettings set org.gnome.desktop.background picture-uri "${wallpaper}"
