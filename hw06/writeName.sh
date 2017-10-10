# using imagemagic to write my name on the screen

SIZE=320x240
TMP_FILE=/tmp/frame.png


convert -background lightblue -fill blue -font Times-Roman -pointsize 24 \
      -size $SIZE \
      label:'Charles Eagle Beard' \
      -draw "text 100" \
      $TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE

# convert -list font
