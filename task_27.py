#!/usr/bin/python3

from pyrob.api import *


@task (delay=0.01)
def task_7_5():
            if not wall_is_on_the_right():
                move_right()
                fill_cell()
            else:
                return
            i = 1
            while not wall_is_on_the_right():
                fill_cell()
                for k in range(i):
                    if not wall_is_on_the_right():
                        move_right()

                    else:
                       return

                i += 1



if __name__ == '__main__':
    run_tasks()
