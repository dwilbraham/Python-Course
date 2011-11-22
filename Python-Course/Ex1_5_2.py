class PositiveNumberDataDescriptor(object):
    def __init__(self):
        self.value = 0
        
    def __get__(self, instance, cls):
        return round(self.value, 2)
    
    def __set__(self, instance, value):
        if value >= 0:
            self.value = value
        else:
            raise ValueError
    
    def __delete__(self, instance):
        print 'NO DEL'

class PositiveHolder(object):
    attr = PositiveNumberDataDescriptor()

class Price(object):
    def __init__(self, price):
        self.value = total
        self.vat = 20.0
        
    def totalget(self):
        return total 
    
    def totalset(self, value):
        pass
    
    total = property(totalget, totalset)

if __name__ == '__main__':
    pos = PositiveHolder()
    print 'Start'
    pos.attr = 2
    print 'pos.attr = 2'
    print pos.attr
    try:
        pos.attr = -99
        print "pos.attr = -99"
    except ValueError:
        print 'CATCH pos.attr = -99'
    del pos.attr