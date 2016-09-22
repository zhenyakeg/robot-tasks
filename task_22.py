#!/usr/bin/python3

from pyrob.api import *


@task (delay=0.005)
def task_5_10():
    while True:
        while True:
            fill_cell()
            if not wall_is_on_the_right():
                move_right()
            else:
                break
        while not wall_is_on_the_left():
            move_left()
        if wall_is_beneath():
            break
        else:
            move_down()




if __name__ == '__main__':
    run_tasks()
