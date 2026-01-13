#private attribute
#attributes and methoods which can be access only inside the class are called private 
#eg
class account:
    def __init__(self,acc_num,acc_pass):
        self.num=acc_num
        self.__acc_pass=acc_pass#the understore before the acc is use to denote the attribute is a private attribute and 
                                 #             will not be shown outside the class

    def reset_pass(self):
        print(self.__acc_pass)
    
    #private method
    
    def __hello():
                print("Hello world")

s1=account(1234,"abc34")
print(s1.reset_pass())