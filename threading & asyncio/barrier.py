import random
import threading
import time
import datetime


class HorseRace:
    """Using barrier for horse racing. Start race only after waiting for all horses on the starting line"""
    def __init__(self):
        self.barrier = threading.Barrier(4)
        self.horses = ['Artex', 'Frankel', 'Bucephalus', 'Barton']
        self.time = datetime.datetime.now()
        self.finish_line = []

    def lead(self):
        horse = self.horses.pop()
        time.sleep(random.randrange(1, 5))
        print(f'\n{horse} reached the barrier at: {datetime.datetime.now()-self.time}')
        self.barrier.wait()

        time.sleep(random.randrange(1, 5))
        print(f'\n{horse} started at: {datetime.datetime.now()-self.time}')

        time.sleep(random.randrange(1, 5))
        self.finish_line.append(horse)
        print(f'\n{horse} finished at: {datetime.datetime.now()-self.time}')

        if len(self.finish_line) == 4:
            print(f'1st: {self.finish_line[0]}\n2nd: {self.finish_line[1]}\n3rd: {self.finish_line[2]}\n4th: {self.finish_line[3]}')


        self.barrier.wait()
        print(f'\n{horse} went sleeping')






if __name__ == '__main__':
    print('Race preparation')

    race = HorseRace()
    for x in range(4):
        thread = threading.Thread(target=race.lead)
        thread.start()
