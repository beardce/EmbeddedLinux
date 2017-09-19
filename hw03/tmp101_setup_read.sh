#!/bin/bash
temp1=`i2cget -y 1 0x48`
temp2=`i2cget -y 1 0x4a`
temp1=$(($temp1 * 9))
temp2=$(($temp2 * 9))
temp1=$(($temp1 / 5))
temp2=$(($temp2 / 5))
temp1=$(($temp1 + 32))
temp2=$(($temp2 + 32))
echo "Temperature 1 is $temp1"
echo "Temperature 2 is $temp2"