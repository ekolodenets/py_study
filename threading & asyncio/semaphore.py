import threading
import time


class NightClub:
    """Using semaphore to limit entering guests to the nightclub"""
    def __init__(self):
        self.bouncer = threading.Semaphore(3)   # guests limit in the club

    def open_club(self):
        for x in range(1, 51):
            t = threading.Thread(target=self.guest, args=[x])
            t.start()


    def guest(self, guest_id):
        print(f'\nGuest {guest_id} is waiting to entering nightclub')
        self.bouncer.acquire()

        print(f'\nGuest {guest_id} is dancing')
        time.sleep(1)

        print(f'\nGuest {guest_id} is leaving the nightclub')
        self.bouncer.release()



if __name__ == '__main__':
    club = NightClub()
    club.open_club()
