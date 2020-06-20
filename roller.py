#!/home/pi/roller/env/bin/python

import sys, getopt
from gpiozero import LED as pin
from time import sleep
import os.path
from os import path

# GPIO 
button_up       = pin(5)    # RED
button_pause    = pin(6)    # ORANGE
button_down     = pin(13)   # YELLOW
button_prev     = pin(19)   # GREEN
button_next     = pin(26)   # BLUE

# config
debounce = 0.06
throttle = 0.07
cooldown = 4

# rooms
room_all            = 0
room_parents        = 1
room_living_left    = 2
room_living_right   = 3
room_kitchen        = 4
room_laundry        = 5
room_study          = 6
room_bedroom        = 7

def press_button(button):
    button.on()
    sleep(debounce)
    button.off()
    sleep(throttle)


def wake_up():
    press_button(button_pause)
    press_button(button_pause)
    press_button(button_pause)


def select_room(room):
    for _ in range(room + 1):
        press_button(button_next)


def deselect_room(room):
    for _ in range(room):
        press_button(button_prev)


def open_room(room):
    wake_up
    select_room(room)
    press_button(button_up)
    press_button(button_up)
    press_button(button_up)
    deselect_room(room)
    sleep(cooldown)


def close_room(room):
    wake_up
    select_room(room)
    press_button(button_down)
    press_button(button_down)
    press_button(button_down)
    deselect_room(room)
    sleep(cooldown)


def check_locked():
    return path.exists("lock")


def create_lock():
    lock = open('lock', 'w')
    lock.close()


def remove_lock():
    os.remove('lock')


# arguments: <user>, <open/close>, <room>, <room>, <room>...
def main(argv):
    sleep(1)
    # prevent other instances of script being run
    # this is important as it will mess with channel selection on the remote
    if not check_locked():
        
        create_lock()
    
        if argv[1] == 'open':
            for i in range(2, len(argv)):
                print('opening: ' + argv[i])
                open_room(eval(argv[i]))
        elif argv[1] == 'close':
            for i in range(2, len(argv)):
                print('closing: ' + argv[i])
                close_room(eval(argv[i]))
        else:
            print('no room selected')

        remove_lock()

    else:
        print('Please Wait...')


if __name__ == "__main__":
   main(sys.argv[1:])