#!/home/pi/roller/env/bin/python
import sys, getopt
from gpiozero import LED as pin
from time import sleep

# GPIO 
button_up       = pin(5)    # RED
button_pause    = pin(6)    # ORANGE
button_down     = pin(13)   # YELLOW
button_prev     = pin(19)   # GREEN
button_next     = pin(26)   # BLUE

# config
debounce = 0.03
throttle = 0.07
cooldown = 4

def press_button(button):
    button.on()
    sleep(debounce)
    button.off()
    sleep(throttle)


def main(argv):
    press_button(eval(argv[0]))
    

if __name__ == "__main__":
   main(sys.argv[1:])