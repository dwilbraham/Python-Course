import itertools as it

def init_coroutine(func):
    def init(*args, **kwargs):
        gen = func(*args, **kwargs)
#        gen.next()
        return gen
    return init

@init_coroutine
def count_in(start, step=1):
    x = start
    for i in it.count():
        if i >= 10:
            raise StopIteration
        ret = yield x
        if ret is not None:
            step = ret
        x += step
        ++i

if __name__ == '__main__':
    c = count_in(10, 5)
    try:
        print (c.next())
        print (c.next())
        print (c.send(10))
        print (c.next())
        print (c.next())
        print (c.next())
        print (c.send(5))
        print (c.next())
        print (c.next())
        print (c.send(20))
        c.close()
        print (c.next())
        print (c.next())
        print (c.send(1))
    except StopIteration:
        print ("Finished iteration")