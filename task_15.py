#!/usr/bin/python3

from pyrob.api import *


@task (delay=0.01)
def task_8_21():

    if wall_is_on_the_left():
        move_right(9)
    else:
        move_left(9)
    if wall_is_above():
        move_down(9)
    else:
        move_up(9)



if __name__ == '__main__':
    run_tasks()
