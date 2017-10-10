# using imagemagic to write my name on the screen

SIZE=320x240
TMP_FILE=/tmp/frame.png


convert boris.png -resize 25% \
      -background lightblue -fill blue -font Times-Roman -pointsize 24 \
      label:'Charles Eagle Beard' \
      -gravity Center -append \
      $TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE

# convert -list font
