import time
import timeit
import functools

def time_call(timesRun):
    def _time_call(func):
        @functools.wraps(func)
        def __time_call(*args, **kwargs):
            start = timeit.default_timer()
            ret = func(*args, **kwargs)
            print ("Function call time = " + str((timeit.default_timer() - start) / timesRun))
            return ret
        return __time_call
    return _time_call

@time_call(2)
def sleep_for(timeToSleep):
    """Sleeps for the given number of seconds"""
    time.sleep(timeToSleep)

if __name__ == '__main__':
#    print (timeit.default_timer())
    sleep_for(5)