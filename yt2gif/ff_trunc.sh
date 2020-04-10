#!/bin/sh

if ! [ $1 ]; then
  echo "please give yt url"
  exit
else
  URL=$1
fi

FILENAME='out.webm'
if [ $2 ]; then
  FILENAME = $2
fi

echo "url $URL"
echo "filename $FILENAME"

ffmpeg -ss 0 -i $(youtube-dl -f 22 --get-url $URL) -t 2 -c libvpx-vp9 -an $FILENAME
