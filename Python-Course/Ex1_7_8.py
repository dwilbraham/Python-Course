class Wrapper(object):
    def __init__(self, wrapped, forbidden):
        self._wrapped = wrapped
        self._forbidden = forbidden
        
    def __getattr__(self, attr):
        if attr in self._forbidden:
            raise AttributeError("Forbidden attribute = " + attr)
        return getattr(self._wrapped, attr)

class Wrapped(object):
    def okMethod(self):
        pass
    
    def append(self):
        pass
    
def MultiplyFactory(factor):
    def Multiply(value):
        return factor * value
    return Multiply
 
class UnderscoreClass(object):
    def __init__(self):
        self.__randomAttribute = 22

if __name__ == '__main__':
    w = Wrapper(Wrapped(), ['append'])
    try:
        w.append()
    except AttributeError:
        print "Caught expected exception"
    print "Got to the end of section 1!"
    
    print MultiplyFactory(5)(5)
    
    uc = UnderscoreClass()
    print uc._UnderscoreClass__randomAttribute
    uc._UnderscoreClass__randomAttribute = None
    print uc._UnderscoreClass__randomAttribute
    