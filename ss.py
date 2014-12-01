__author__ = 'Ayla'
### Create a social security number module
##### Create a social security number class:




class SS:
    class InvalidSocial(ValueError):
        pass


    def __init(self):
        #self.social = self.getsocial
        self.number=""
    def validatess(self):
        #self.ss = input("Input Social Security number")
        try:
            print (self.number)
            aaa,gg,ssss = str(self.number).split('-')
            #self.ss
            #print "aaa=" +aaa
            #print "gg=" + gg
            #print "ssss="+ssss
            if len(aaa) != 3 or len(gg) != 2 or len(ssss) != 4:
            #print('Invalid social security number')
                raise self.InvalidSocial
            if aaa == '000' or gg =='00' or ssss == '0000':
            #print("Invalid social security number")
                raise self.InvalidSocial
            if aaa =='666' or '900'>='999':
            #print("Invalid social security number")
                raise self.InvalidSocial
            if aaa =='078' or gg =='05' or ssss =='1120':
            #print("Invalid social security number")
                raise self.InvalidSocial

        #check that employee_class.ss is valid
        #Anywhere that you find the ss is invalid raise InvalidSocial

            aaa=int(aaa)
            gg=int(gg)
            ssss=int(ssss)

            return aaa, gg, ssss
        except ValueError:
            print("Enter a valid social security number")
            raise self.InvalidSocial

    def getsocial(self):
            self.number=input("Enter Social Security Number: ")
            # self.ss = input("Social: ")
            try:
                self.validatess()
            except self.InvalidSocial:
                print("Invalid SS, please try again\n")
                self.getsocial()


