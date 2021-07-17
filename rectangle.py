import math

class Rectangle:
 def  __init__(self,width,length):	
       self.width=width
       self.length=length
 def   area(self):
      return  self.width*self.length	    
 def  perimeter(self):
       return 	2*(self.width+self.length)
print"---------------------"


c=Rectangle(2,3)

print c.area()
print c.perimeter()

c1=Rectangle(1,1)
print c1.area()
print c1.perimeter()
