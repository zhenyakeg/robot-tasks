#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    k=0
    while not wall_is_on_the_right():
        if cell_is_filled():
            k+=1
        if k==5:
            return
        else:
            move_right()


if __name__ == '__main__':
    run_tasks()
