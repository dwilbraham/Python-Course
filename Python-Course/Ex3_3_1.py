import threading
import sys

class ThreadedEx(threading.Thread):                      #2
    """The thread.
    """

    def run(self):
        """Printing thread name and a number.
        """
        for x in range(5):
            if self.name == 'Thread-1':
                for y in range(int(1e6)):
                    1 + 1
            sys.stdout.write('%s: % d\n' % (self.name, x))
            sys.stdout.flush()
        
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
        