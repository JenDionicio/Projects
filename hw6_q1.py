"""
Author: Jen Martinez
Assignment / Part: HW6 - Q1 (depending on the file name)
Date due: 2022-10-20, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
# how exactly would I use these varible and functions
from touchTypes import TouchType, SwipeDirection
SINGLE_TOUCH = TouchType.SINGLE_TOUCH
DOUBLE_TAP = TouchType.DOUBLE_TAP
SWIPE = TouchType.SWIPE
HOLD = TouchType.HOLD
UP = SwipeDirection.UP
DOWN = SwipeDirection.DOWN
LEFT = SwipeDirection.LEFT
RIGHT = SwipeDirection.RIGHT
NO_DIRECTION = SwipeDirection.NO_DIR


def give_haptic_feedback(touch_ratio: float):
    if touch_ratio> 0.0 and touch_ratio < 0.5:
         print('Vibrating once...')
    elif touch_ratio >= 0.5 and touch_ratio < 2.0:
        print('Vibrating twice...')
    elif touch_ratio > 2.0:
        print('Vibrating thrice...')


def register_touch(touch_type, strength, duration = 0.1, direction = None):
    
    if touch_type == SINGLE_TOUCH :
        print('Registering single touch...')
    elif touch_type == DOUBLE_TAP:
        print('Registering double tap...')
    elif touch_type == SWIPE:
        print('Registering swipe...')
        if direction == UP:
            print('Exiting app...')
        elif direction == LEFT or direction == RIGHT:
            print('Changing page...')
        else: # direction = DOWN
            print('Scrolling up...')
    else: # touch_type = HOLD
        print('Registering hold...')
        touch_ratio = (strength/duration)
        return give_haptic_feedback(touch_ratio)


def get_touch():

    touch_type = input('What type of touch did the user perform? [single/double/swipe/hold] ')
    duration = None
    direction = NO_DIRECTION

    if touch_type == 'swipe':
        touch_type = SWIPE
        direction = input('In what direction did the user swipe? ')
    elif touch_type == 'hold':
        touch_type = HOLD
        duration = float(input('For how long did the user hold the touch? '))
    elif touch_type == 'single':
        touch_type = SINGLE_TOUCH
    elif touch_type == 'double':
        touch_type = DOUBLE_TAP
    
    strength = float(input("How strong was the user's touch? [0.0 to 1.0] "))
    register_touch(touch_type, strength, duration, direction)


def main():
    get_touch()
main()