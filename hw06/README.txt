Ece 497-01 Embedded 32-bit linux Homework 6

To rotate the image on the screen I just modified the reset.sh script to rotate 
the screen then re-display the image in its new rotated state

to rotate the video I found adding the -vf-add rotate=4 -framedrop flags to 
mplayer worked

for the two text scripts I started with the text.sh file and altered it to print
my own name. For the file that adds text to the image I had to make the image 
smaller because It wouldn't fit on my screen for some reason.

I could not figure out how to make pygame work with the frame buffer

I altered the code in the etch-a-sketch.c file to take user input for the color
of the line and the size of the line. 

to run all of these files make sure to use sudo
