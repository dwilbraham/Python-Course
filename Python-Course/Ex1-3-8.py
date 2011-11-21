import time
import timeit

def time_call(func):
    def _time_call(*args, **kwargs):
        start = timeit.default_timer()
        ret = func(*args, **kwargs)
        print ("Function call time = " + str(timeit.default_timer() - start))
        return ret
    return _time_call

@time_call
def sleep_for(timeToSleep):
    time.sleep(timeToSleep)

if __name__ == '__main__':
    print (timeit.default_timer())
    sleep_for(5)