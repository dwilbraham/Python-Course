import threading
import sys

class ThreadedEx(threading.Thread):                      #2
    """The thread.
    """

    _lock = threading.Lock()

    def run(self):
        """Printing thread name and a number.
        """
        for x in range(5):
            with ThreadedEx._lock:
#                ThreadedEx._lock.acquire()
                if self.name == 'Thread-1':
                    for _ in xrange(int(1e6)):
                        1 + 1
                sys.stdout.write('%s: % d\n' % (self.name, x))
                sys.stdout.flush()
#                ThreadedEx._lock.release()
        
if __name__ == '__main__':
#    sys.setcheckinterval(int(1e9))
#    sys.setcheckinterval(1)
    numOfThreads = 2
    ThreadedExList = []
    for i in xrange(numOfThreads):
        thread_inst = ThreadedEx()
        thread_inst.start()
        ThreadedExList.append(thread_inst)
    for inst in ThreadedExList:
        inst.join()
        