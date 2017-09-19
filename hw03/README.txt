README file for hw03
tmp101_setup_read.sh: reads the temperature from each tmp101 sensor

tmp101_wait_for_alarm.py: sets up the tempHigh and tempLow registers on each tmp101
    then waits for an alarm to be triggered on either of them printing the temperature
    while the alarm is triggered. just run the script and warm up the tmp101s
    
etchASketch_with_buttons_and_ledmat.py: sets up the led matrix, tmp101 sensors
    and gpio inputs then uses the led matrix as the screen for the etch a sketch
    and uses the tmp101 alarm as the clear signal. To use just run the script and
    use the buttons to draw and the tmps to clear.