#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    while True:
        if wall_is_on_the_right:
            break
        else:
            move_right()
            if not wall_is_above():
                while True:
                    if wall_is_above():

                        break
                    else:
                        move_up()
                        fill_cell()
                    while not wall_is_beneath():
                            move_down()
    while not wall_is_on_the_left:
        move_left()

    move_right()


if __name__ == '__main__':
    run_tasks()
