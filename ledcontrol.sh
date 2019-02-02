#!/bin/bash
ADDR="192.168.1.151:80"

#USAGE: ledcontrol.sh [room - narnia 5, kupelka 0, 1404a - 1, 1404b - 2, undefined - 3, undefined - 4] [red] [green] [blue]
#0-4: 12-bit: 0-4095, 5: 8-bit: 0-255

case $1 in
0) curl -X POST "http://$ADDR/led" -d "{led0: $2, led1: $3, led2: $4}" --header 'content-type: application/json';;
1) curl -X POST "http://$ADDR/led" -d "{led3: $2, led4: $3, led5: $4}" --header 'content-type: application/json';;
2) curl -X POST "http://$ADDR/led" -d "{led6: $2, led7: $3, led8: $4}" --header 'content-type: application/json';;
3) curl -X POST "http://$ADDR/led" -d "{led9: $2, led10: $3, led11: $4}" --header 'content-type: application/json';;
4) curl -X POST "http://$ADDR/led" -d "{led12: $2, led13: $3, led14: $4}" --header 'content-type: application/json';;
5) curl -X POST "http://192.168.1.2:8080" -d '{"r": $2, "g": $3, "b": $4}' --header 'content-type: application/json';;
esac

