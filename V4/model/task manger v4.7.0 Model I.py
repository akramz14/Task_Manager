#pylint:disable=W0201
#سكربت مهام 4.7
#تغيير هيكل تخزين بيانات
#الغاء فكره ids
#تغير بنيه الكود
#هذه ربما تكون اخر نسخه من سلسله v4
class Logic:
	def __init__(self):
		self.tasks = []
		self.Ctasks = []
		self.choice = None
		self.user_input = None
	def viewTask(self):
		for i, task in enumerate(self.choice, start=1):
			print(i,"-",task["task"]," ",task["date"]," ",task["status"])
	def addTask(self):
			try:
				if self.choice:
					self.tasks.append({"task":self.user_input,"date":date,"status":"غير مكتلمه"})
				else:
					self.Ctasks.append(self.tasks[self.user_input])
					self.tasks.pop(self.user_input)
			except KeyError:
				print("لا يوجد هذا مفتاح")
			except ValueError:
				print("اكتب رقم") 
	def deleteTask(self):
		try:
			self.choice.pop(self.user_input)
		except KeyError:
			print("لا يوجد هذا مفتاح")
		except ValueError:
			print("اكتب رقم")
class CLI:
	def verify_input(self,prompt):
		self.value = input(prompt)
		if not self.verify_input.strip():
			print("خطأ،انت لم تكتب شيء")
		else:
			return self.verify_input
	def choiceForALL(self,prompt,true,false,error_msg):
			self.user_input = input(prompt)
			if not self.user_input.strip():
				print("خطأ انت لم تكتب شيء")
			else:
				if self.user_input == true:
					return True
				elif self.user_input == false:
					return False
				else:
					print(error_msg)
	def viewTaskCLI(self):
		if not self.tasks and not self.Ctasks:
			print("لا توجد مهام مكتمله او غير مكتلمة لعرضها يرجى اعاده محاوله")
		else:
			if self.choiceForALL("وش بدك تعرض قائمه مهامك 1 او قائمه مهامك مكتمله 2:","1","2","اختر 1 او 2"):
				self.choice = self.tasks()
				self.view_task()
			else:
				self.choice = self.Ctask()
				self.view_task()
	def addTasksCLI(self):
		while True:
			if self.choiceForALL("اختر بدك تضيف مهام 1 او بدك تضيف مهام مكتلمه 2:","1","2","اختر 1 او 2"):
				self.choice = True
				self.user_input = self.value("اكتب مهمه لي بدك تضيفها:")
				self.addTask()
				return
			else:
				try:
					self.choice = False
					self.user_input = int(self.value("اكتب رقم مهمه لي انهيتها"))
					if not self.user_input < 0 or self.user_input >= (self.task):
						print("ذا شرط كتبه ai😃")
						print("لا توجد هذه مهمه اعد محاوله")
					else:
						self.addTask()
				
			
		
	
			

			
						
									
												
															
																		
																					
																								
																											
																																	