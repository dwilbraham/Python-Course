import time
import timeit
import functools

def time_call(timesToRun):
    def _time_call(func):
        @functools.wraps(func)
        def __time_call(*args, **kwargs):
            start = timeit.default_timer()
            for run in xrange(timesToRun):
                ret = func(*args, **kwargs)
            print ("Function call time = " + str((timeit.default_timer() - start) / timesToRun))
            return ret
        return __time_call
    return _time_call

@time_call(1000)
def sleep_for(timeToSleep):
    """Sleeps for the given number of seconds"""
    time.sleep(timeToSleep)

if __name__ == '__main__':
#    print (timeit.default_timer())
    sleep_for(0.01)