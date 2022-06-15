import threading
import time


class StoppableThread(threading.Thread):
    def ___init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop = self.stop_event.set()

    def stopped(self):
        return self.stop_event.is_set()


class ThreeSumUnitOfWork(StoppableThread):
    def __init__(self, ints, name='TestThreads'):
        super().__init__(name=name)
        self.ints = ints

    def run(self):
        print(f'{self.getName()} starts')

        self.count_three_sum(self.ints)

        print(f'{self.getName()} ends')

    def count_three_sum(self, ints):
        print(f'started count_three_sum')

        n = len(ints)
        counter = 0

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if super().stopped():
                        print('Task was cancelled')
                        counter = -1
                        return counter

                    if ints[i] + ints[j] + ints[k] == 0:
                        counter += 1
                        print(f'Triple found {ints[i]} {ints[j]} {ints[k]}', end='\n')

        print(f'ended count_three_sum. Triplet count={counter}')
        return counter

if __name__ == '__main__':
    print('start main')

    ints = read_ints('#path')

    task = ThreeSumUnitOfWork(ints)
    task.start()

    time.sleep(5)

    task.stop()

    task.join()

    print(task.stopped())
    print('ended main')