'''
Estimated time
    10-20 minutes

Level of difficulty
    Medium

Objectives
    improving the student's skills in operating with special methods
    Scenario
    Extend the class implementation prepared in the previous lab to support the addition and subtraction of integers to time interval objects;
    to add an integer to a time interval object means to add seconds;
    to subtract an integer from a time interval object means to remove seconds.

Hint    
    in the case when a special method receives an integer type argument, instead of a time interval object, create a new time interval object based on the integer value.

Test data:
    the time interval (tti) is hours=21, minutes=58, seconds=50
    the expected result of addition (tti + 62) is 21:59:52
    the expected result of subtraction (tti - 62) is 21:57:48
   
'''
# Sebastian Faber, 25.09.2024

class time_interval:
    def __init__(self, hh, mm, ss):        
        if (type(hh)==int) and (type(mm)==int) and (type(hh)==int) :     
           self.hh ,self.mm, self.ss  =hh, mm, ss
           self.set_timestamp()
        else:
            raise TypeError

    def __sub__(self, param):
        if isinstance(param, time_interval):
           subtr=param.timestamp
        elif isinstance(param, int):
           subtr=param
        else: 
           TypeError  
           
        self.get_time(self.timestamp - subtr)
        return(self.ftime)
           
    def __add__(self, param):
        if isinstance(param, time_interval):
           add=param.timestamp
        elif isinstance(param, int):
           add=param
        else: 
           TypeError

        self.get_time(self.timestamp + add)
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




if __name__== "__main__":
   tti=time_interval(21, 58, 50)    # 21:58:00

   result1=(tti + 62)               # expected result: 21:59:52
   result2=(tti - 62)               # expected result: 21:57:48

   print("result1:", result1)
   print("result2:", result2)


