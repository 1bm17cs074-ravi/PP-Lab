class CallDetail:
	def __init__(self,li) :
		self.ph_call=li[0]
		self.ph_called=li[1]
		self.duration=li[2]
		self.type=li[3]
	def print_r(self,count) :
	        print("  ",count,"   ",self.ph_call,"",self.ph_called,"  ",self.duration,"         ",self.type)
		
obj=[]
class Util:
	def parse_customer(self,list_of_call_string):
		for s in list_of_call_string :
			s1=s.replace("'","")
			li=s1.split(",")
			call=CallDetail(li)
			obj.append(call)


call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
count=1
Util().parse_customer(list_of_call_string)
print("call_id || caller || receiver || dur_in_sec || type")
for o in obj :
	o.print_r(count)
	count+=1
