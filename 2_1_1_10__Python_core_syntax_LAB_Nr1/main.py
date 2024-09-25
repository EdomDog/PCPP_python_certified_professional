'''
Estimated time
    30-60 minutes

Level of difficulty
    Medium

Objectives
    improving the student's skills in operating with special methods

Scenario
    - Create a class representing a time interval;
    - the class should implement its own method for addition, subtraction on time interval class objects;
    - the class should implement its own method for multiplication of time interval class objects by an integer-type value;
    - the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
    - the __str__ method should return an HH:MM:SS string, where 
            HH represents hours, 
            MM represents minutes and 
            SS represents the seconds attributes of the time interval object;
    - check the argument type, and in case of a mismatch, raise a TypeError exception.

Hint #1    
    just before doing the math, convert each time interval to a corresponding 
    number of seconds to simplify the algorithm;
    for addition and subtraction, you can use one internal method, 
    as subtraction is just ... negative addition.
    
    Test data:
    the first time interval (fti) is hours=21, minutes=58, seconds=50
    the second time interval (sti) is hours=1, minutes=45, seconds=22
    the expected result of addition (fti + sti) is 23:44:12
    the expected result of subtraction (fti - sti) is 20:13:28
    the expected result of multiplication (fti * 2) is 43:57:40

Hint #2
    you can use the assert statement to validate if the output 
    of the __str__ method applied to a time interval object equals the expected value.
'''
# Sebastian Faber, 25.09.2024

class time_interval:
    def __init__(self, hh, mm, ss):        
        if (type(hh)==int) and (type(mm)==int) and (type(hh)==int) :     
           self.hh ,self.mm, self.ss  =hh, mm, ss
           self.set_timestamp()
        else:
            raise TypeError

    def __sub__(self, obj):
        obj.timestamp=-obj.timestamp
        return(self.__add__(obj))
               
    def __add__(self, obj):
        self.get_time(self.timestamp + obj.timestamp)
        return(self.ftime)
    
    def __mul__(self, factor):
        self.get_time(self.timestamp * factor)
        return(self.ftime)
        
    def __str__(self):
        self.get_time(self.timestamp)
        return(self.ftime)
    
    def set_timestamp(self):
        self.timestamp=3600 * self.hh + 60*self.mm + self.ss

    def get_time(self, timestamp):
        self.hh = timestamp // 3600
        self.mm = (timestamp % 3600) // 60
        self.ss = timestamp % 60
        self.ftime=f"{self.hh:02}:{self.mm:02}:{self.ss:02}"


            
       
# set time
fti=time_interval(21, 58, 50)    # 21:58:00
sti=time_interval(1, 45, 22)     # 21:22:00  

result1=(fti + sti)              # excpected result: 23:44:12
result2=(fti - sti)              # excpected result: 20:13:28
result3=(fti * 2)                # excpected result: 43:57:40

print("result1:", result1)
print("result2:", result2)
print("result3:", result3)
