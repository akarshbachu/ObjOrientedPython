class Add:
    x=0;
    #constructor
    def __init__(self,x):
        self.x=x;
        print "Inside parameterized Constructor and parameter val: ",self.x
    
    #self is nothing but instance of that class it self, it is must when method is inside class
    def addition(self,x,y):
        return x+y
    
    #destructor
    def __del__(self):
        print "in destructor"
 
obj=Add(25)
print obj.addition(1,2)

#inheritance
class Sub(Add):
    def minus(self,x,y):
        return abs(x-y);

obj2=Sub(10)
print "Using child class",obj2.addition(1,2);
print "child class method",obj2.minus(1,2);

