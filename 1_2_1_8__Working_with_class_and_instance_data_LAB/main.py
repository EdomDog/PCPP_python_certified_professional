'''
Estimated time
    20 minutes

Level of difficulty
    Easy

Objectives
    creating classes, class and instance variables;
    accessing class and instance variables;
    Scenario
    Imagine that you receive a task description of an application that monitors the process of apple packaging before the apples are sent to a shop.

    A shop owner has asked for 1000 apples, but the total weight limitation cannot exceed 300 units.

    Write a code that creates objects representing apples as long as both limitations are met. When any limitation is exceeded, than the packaging process is stopped, and your application should print the number of apple class objects created, and the total weight.

    Your application should keep track of two parameters:

    the number of apples processed, stored as a class variable;
    the total weight of the apples processed; stored as a class variable. Assume that each apple's weight is random, and can vary between 0.2 and 0.5 of an imaginary weight unit;
    Hint: Use a random.uniform(lower, upper) function to create a random number between the lower and upper float values.
'''
# Author: Sebastian Faber, 24.09.2024    

import random
total_count_limit=1000
total_wheight_limit=300

class get_apple():
    def __init__(self):
        self.__wheight=random.uniform(0.2, 0.5)
    
    def get_wheight(self):
        return(self.__wheight)       

class package():
    total_wheight=0
    count_of_items=0

    def do_packaging(self):
       item=get_apple()
       sum_wheight = package.total_wheight + item.get_wheight()
       sum_count = package.count_of_items + 1

       if (sum_wheight < total_wheight_limit) and (sum_count < total_count_limit):
          package.total_wheight  = sum_wheight
          package.count_of_items = sum_count
          return(True)
       else:
          return(False)
     
    @classmethod
    def show_summary(cls):
        print(" Package done. ".center(30, "-"))
        print(f"Total wheight:     {cls.total_wheight:.2f}")
        print(f"Total nb of items: {cls.count_of_items}")

pack=package()   
progress=True

while progress:
   progress=pack.do_packaging()

pack.show_summary()    
