#!/usr/bin/python3

from pyrob.api import *


@task (delay=0.1)
def task_8_29():
    a = False

    while not wall_is_on_the_left():
        move_left()
    if not wall_is_above():
        a = True
    else:
        while not wall_is_on_the_right():
            move_right()
        if not wall_is_above():
            a = True
    if a:
        while not wall_is_above():
            move_up()
        while not wall_is_on_the_left():
            move_left()







if __name__ == '__main__':
    run_tasks()
