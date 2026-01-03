import time
from datetime import datetime
time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
completed_tasks={}

#كلاس ل منطق متكرر
class Logic:
	@staticmethod
	def Nothing_input(prompt):
		while True:
			User_input = input(prompt)
			if not User_input:
				print("ادخال غير صحيح")
				continue
				return User_input
	#دوال لخيارات 
	@staticmethod
	def choiceForALL(prompt,correct,worng,error_msg):
		while True:
			Logic.Nothing_input = input(prompt).strip().lower()#كتابه مطلوب من مستخدم 
			if Logic.Nothing_input== correct:#كتابه خيار تأكيد
				return True
			elif Logic.Nothing_input== worng:#كتابه خيار عدم تأكيد
				return False
			else:
				print(error_msg) #كتابه رساله خطأ
	def __init__(self):
		self.tasks=[]
		self.completed_tasks=[]
		self.i=0
		self.z=0
	def EditTasks(self):
		while True:
			self.i +=1
			if Logic.choiceForALL('بدك تضيف مهمه "1" بدك تضيف مهمه مكتلمه "2":',"1","2",'اختر "1" او "2"'  ):
				input_user = Logic.Nothing_input("ادخل مهمه لي بدك تضيفها:")
				self.tasks.append({f"task{self.i}":{"Task":input_user,"date":time,"status":False}})						
				if Logic.choiceForALL('بدك تضيف مهمه او مهمه مكتلمه أخرى (نعم/لا) :',"نعم","لا",'اختر "نعم" او "لا"' ):
					continue
				else:
					return
			else:
					try:
						input_user=int(Logic.Nothing_input("ادخل رقم مهمه لي اكملتها: ")) 
						self.z+=1
						key = f"task{input_user}"
						for task in self.tasks:
							if key in task:
								task=task[key]
								self.completed_tasks.append({f"task_completed{self.z}":{"task":task["Task"],"date":time,"status":True}})
								break
						if Logic.choiceForALL('بدك تضيف مهمه او مهمه مكتلمه أخرى (نعم/لا) :',"نعم","لا",'اختر "نعم" او "لا"' ):
							continue
						else:
							return
				except ValueError:
					print("اكتب رقم من فضلك")
				except KeyError:
					print("خطأ غير متوقع1")
					
obj = Logic()
obj.EditTasks()
print("مهام غير مكتلمه") 
print(obj.tasks)
print("مهام مكتلمه")
print(obj.completed_tasks)										
														
																
																		
																				
																						
																										