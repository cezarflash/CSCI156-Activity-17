__author__ = 'Ayla'


class SS:


class InvalidSocial(ValueError):
     pass


    def __init(self):
        self.social = self.getss

    def validatess(self):
        if self.ss:
            return True
         raise self.InvalidSocial

def getsocial(self):
    self.ss = input("Social: ")
    try:
        self.ss.validatess()
    except InvalidSocial:
        print("Invalid SS, please try again\n")
        self.ss.getsocial()
