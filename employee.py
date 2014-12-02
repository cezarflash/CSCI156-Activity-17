__author__ = 'Ayla'
from ss import *

class Employee:
    def __init__(self,last=None,first=None,start=None,pay_rate=None,social=None):
        if last == None:
            self.last = input("Employee Last Name: ")
        else:
            self.last=last


        if first==None:
            self.first =input("Employee First Name: ")
        else:
            self.first=first
        if start == None:
            self.start=input("Employee Start Date: ")
        else:
            self.start=start
        if pay_rate == None:
            self.pay_rate=input("Employee Pay_rate: ")
        else:
            self.pay_rate=pay_rate

        ss_object = SS()
        if social == None:
            ss_object.getsocial()
        else:
            ss_object.number=social
            ss_object.validatess()

        self.social=ss_object.number

    def __str__(self):
        return "First Name:"+' '+self.first+"\nLast Name:"+' '+self.last+' '+"\nYear started:"+' '+\
        str(self.start)+'\n'+ "Salary:"+' '+str(self.pay_rate)+'\n'+"Social Security Number:"+' '+str(self.social)





