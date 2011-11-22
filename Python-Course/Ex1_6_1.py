class MethodNameSizeLimit(type):
    def __init__(self, name, bases, dict):
        for key, value in dict.items():
            if hasattr(value, '__call__'):
                if len(key) > 30:
                    raise Exception("Method name too long!")
                
class LongMethodName:
    __metaclass__ = MethodNameSizeLimit
    
    def shortmethod(self):
        pass
    
#    def thisisaverylongmethodnamenorealyitis(self):
#        pass
    
class MustHaveDocString(type):
    def __init__(self, name, bases, dict):
        alwaysAllowed = set(['__metaclass__'])
        for key, value in dict.items():
            if hasattr(value, '__call__') and (key not in alwaysAllowed):
                if (value.__doc__ is None) or (len(value.__doc__) == 0):
                    print value.__doc__
                    raise Exception("Method " + key + " doesn't have a doc string!")

class DocStringClass:
    __metaclass__ = MustHaveDocString
    
    def withdocstring(self):
        """It has a Doc String"""
        pass
    
#    def withoutdocstring(self):
#        pass

if __name__ == '__main__':
    try:
        longnameclass = LongMethodName()
    except Exception:
        print "Caught exception"
    
    docstringclass = DocStringClass()
    print "Got to the end!"