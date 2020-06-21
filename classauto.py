'''
#esta es la forma de hacerlo en java
# hay que hacerlo de forma pitonica
class Auto(object):
    
    _instance = None
    def __new__(cls):
        if Auto._instance is None:
            print('nueva instancia')
            Auto._instance = object.__new__(cls)

        return Auto._instance
    def __init__(self, caracteristics):
        self.caracteristics = { 
                                'color':'',
                                'marca':'',
                                'modelo':'',
                                'propietario' : '',
                                
                                }
'''
# forma pitonica
def sigleton(cls):
    instances = dict()

    def wrap(*args, **kargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kargs)

        return instances[cls]

    return wrap
class Auto(object):
    def __init__(self, caracteristics):
        self.caracteristics = caracteristics

if __name__ == "__main__":
    
    ferrari = Auto('Ferrari')

    print(ferrari)