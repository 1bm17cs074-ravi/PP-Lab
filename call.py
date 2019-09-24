class callDetail:
    def __init__(self,a,b,c,d):
        self.fno = a
        self.tno = b
        self.dur = c
        self.type = d

    def display(self):
        print("From:",self.fno)
        print("To:",self.tno)
        print("Duration:",self.dur,"hr")
        print("Type:",self.type)

class Util:
    def __init__(self):
        self.list_of_call_objects = None

    def parse_customer(self,list_of_call_string):
        calls = []
        for i in list_of_call_string:
            info = i.split(',')
            calls.append(callDetail(info[0],info[1],info[2],info[3]))
        for i in calls:
            i.display()

call1 = "9620252724,8217688308,10,STD"
call2 = "9658952724,8255588308,19,ISD"
call3 = "9620230224,8217677708,18,LOCAL"
list_of_call_string = [call1,call2,call3]
Util().parse_customer(list_of_call_string)
            
    
        
