from BirdBrain import Finch
import time
from threading import Thread

finch = Finch('A')


def finchmove():
    finch.setBeak(255, 255, 0)
    finch.setTail(1, 0, 0, 100)
    finch.setTail(2, 0, 0, 100)
    finch.setTail(3, 100, 0, 0)
    finch.setTail(4, 100,0, 0)
    time.sleep(.1)
    finch.setMove('F', 100, 100)
    finch.setMove('F', 100, 100)
    finch.setMove('F', 100, 100)
    finch.setMove('F', 100, 100)
    finch.setMove('F', 90, 100)
    finch.setTurn('R', 90, 100)
    finch.setMove('F', 100, 100)
    finch.setTurn('R', 90, 100)
    finch.setMove(10, 100)
    finch.setTurn('R', 90, 100)
    finch.setMove('F', 1, 100)
    finch.setTurn('R', 90, 100)
    finch.setMove('F', 10, 100)

























def finchplay():
    time.sleep(3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)
    time.sleep(.3)
    finch.playNote(85, 1)
    time.sleep(.3)
    finch.playNote(90, 1)























t1 = Thread(target=finchmove)

t2 = Thread(target=finchplay)


t1.start()
t2.start()
t1.join()
t2.join()





finch.stopAll()
