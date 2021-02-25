#!/bin/bash

# en-US, ja-JP, en-AU, en-UK, de-DE, en-NZ, en-CA
echo 'Which locale? Choose us, jp, au, de, nz or ca or wait 10 sec'
read -t 10 l
case $l in 
    us)
    l='en-US'
    ;;
    jp)
    l='ja-JP'
    ;;
    au)
    l='en-AU'
    ;;
    de)
    l='de-DE'
    ;;
    nz)
    l='en-NZ'
    ;;
    ca)
    l='en-CA'
    ;;
    *)
    l='de-DE'
    ;;
esac

URL="https://www.bing.com"$(curl -s 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=$l' | jq -r '.images[0].url')
wget -q -O $HOME/Pictures/wallpaper.jpg $URL
convert $HOME/Pictures/wallpaper.jpg -filter Gaussian -blur 0x3 $HOME/Pictures/wallpaper-blur.jpg
gsettings set org.gnome.desktop.background picture-uri file://$HOME/Pictures/wallpaper.jpg