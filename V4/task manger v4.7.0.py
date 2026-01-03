#pylint:disable=W0201
#سكربت مهام 4.7
#تغيير هيكل تخزين بيانات
#الغاء فكره ids
#تغير بنيه الكود
#هذه ربما تكون اخر نسخه من سلسله
"""بنيه مطلوبه
class logic:
def init()
task, ctask, choice, user_input
def view task
def add task
def delete task
class cli:
def verifyInput:
selfverifyinput
def choiceForALL:
	###
"""



class Logic:
	def __init__(self):
		self.tasks = []
		self.Ctasks = []
		self.user_input = None
		self.selection = None
		self.reception = None
		self.choice = None #متغير بسيط عشان داله deletee
		self.notcomplete="غير مكتلمه";self.completed ="مكتمله"#عشان اسهل ع نفسي كتابه😘  
	
	def viewTask(self):
		for i, item in enumerate(self.reception,start=1):
			print(i,"-",item["task"],item["date"],item["status"])
			
	def addTask(self):
		if self.selection:
			self.tasks.append({"task":self.reception,"date":date,"status":self.notcomplete})
		else:
			self.Ctasks.append({"task":self.tasks[self.reception]["task"],"date":date,"status":self.completed})
			self.tasks.pop(self.reception)
			
	def deleteTask(self):
		self.choice.pop(self.reception)
manger = Logic()
class CLI:
	
	def verify_input(self,prompt):
		self.value = input(prompt)
		if not self.value.strip():
			print("خطأ! انت لم تكتب شي")
		else:
			return self.value
	
	def choiceForALL(self,prompt,true,false,error_msg):
		self.input = input(prompt)
		if not self.input.strip():
			print("خطأ انت لم تكتب شيء")
		else:
			if self.input == true:
				return True
			elif self.input == false:
				return False
			else:
				print(error_msg)

	def viewTaskCLI(self):
		if self.choiceForALL(" "," "," "," "):
			self.reception = self.tasks
			manger.viewTask()
		else:
			self.reception = self.Ctasks
			manger.viewTask()
	
	def addTaskCLI(self):
		if choiceForALL(" "," "," "," "):
			self.selection = True
			self.user_input = self.verify_input(" ")
			self.reception = self.user_input
			manger.addTask()
		else:
			try:
				self.selection = False
				self.user_input = int(self.value(""))
				if self.user_input < 0 or self.user_input >= len(self.tasks):
					print("لا توجد هذه مهمه")
				else:
					self.reception = self.user_input
					manger.addTask()
			except ValueError:
				print("")
			except IndexError:
				print("")
			except KeyError:
				print("")
	def deleteTask(self):
		if self.choiceForALL(" "," "," "," "):
			self.user_input = int(self.verify_input(" "))
			if self.user_input < 0 or self.user_input >= len(self.tasks):
				print(" ")
			else:
				self.reception = self.user_input
				self.choice = self.tasks
				manger.deleteTask()
		else:
			self.user_input = int(self.verify_input(""))
			if self.user_input < 0 or self.user_input >= len(self.Ctasks):
				print("")
			else:
				self.reception = self.user_input
				self.choice = self.Ctasks
				manger.deleteTask()
			















































































































