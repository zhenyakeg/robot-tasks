#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.007)
def task_4_3():
    move_right()
    for i in range (26):
        for j in range(12):
            fill_cell()
            move_down()
        move_up(12)
        move_right()
        fill_cell()
    move_down()
    for k in range (11):

        fill_cell()
        move_down()

    move_left(26)



if __name__ == '__main__':
    run_tasks()
