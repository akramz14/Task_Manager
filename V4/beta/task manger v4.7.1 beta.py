#pylint:disable=W0201
#pylint:disable=W0612
#سكربت مهام 4.7.1
#نسخه سهله قراءه
#نسخه مكتمله
from datetime import datetime
import os
class Logic:
	def __init__(self):
		self.tasks=[]#normal tasks
		self.Ctasks=[] #completed Tasks
		self.conversion = None
		self.Reception_Task = None;self.Reception_Ctask = None
		self.task_Completed = "مكتلمه";self.task_NotCompleted = "غير مكتلمه"
	def get_time(self):
		return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	def viewTask(self):
		for i, item in enumerate(self.conversion,start = 1):
		print(i, "-", item["task"], item["date"], item["status"])
	def TaskAdd(self):
		date = self.get_time()
		self.tasks.append({"task":self.Reception_Task, "date":date,"status":self.task_NotCompleted})
	def CtaskAdd(self):
		date = self.get_time()
		self.Ctasks.append({"task":self.Reception_Ctask, "date":date, "status":self.task_Completed})
		self.tasks.pop(self.conversion)
	def DeleteTask(self):
		self.tasks.pop(self.conversion)
	def DeleteCtask(self):
		self.tasks.pop(self.conversion)
		manger = Logic()
class Cli:
	def clear_screen(self):
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')
	def empty_input(self,prompt):
		while True:
			self.verify_input = input(prompt)
		if not self.verify_input.strip()
			print("خطأ انت لم تكتب شيء")
			continue
		else:
			return self.verify_input
	def choices(self,prompt,true,false,error_msg):
		self.choice = input(prompt)
		if not self.choice.strip():
			print("انت لم تكتب شيء")
		else:
			if self.choice == true:
				return True
			elif self.choice == false:
				return False
			else:
				print(error_msg)
	def viewTaskCLI(self):
		while True:
			#menu Task
			print("قائمه المهام".center(60, "=" ))
			print("1-عرض المهام");print("2-عرض المهام مكتلمه");print("3-الخروج")
			self.user_input = self.empty_input("اختر: ")
			#view Task
			if self.user_input == "1":
				manger.conversion = manger.tasks
				manger.viewTask()
				return
			elif self.user_input == "2":
				manger.conversion = manger.Ctasks
				manger.viewTask()
				return
			elif self.user_input == "3":
				print("حسنا  وداعا")
				return
			else:
				print("اختر من قائمة من فضلك")
				continue
	def addTaskCLI(self):
		while True:
			try:
				#menu main
				print("اضافه مهام مكتمله او غير مكتمله".center(60, "="))
				print("1-اضافه مهام");print("2-اضافه مهام مكتلمه");print("3-خروج")
				self.user_input = self.empty_input("اختر: ")
				#add Task
				if self.user_input == "1":
					self.user_input = self.empty_input("اكتب مهمه لي بدك تضيفها: ")
					manger.Reception_Task  = self.user_input
					manger.TaskAdd()
					print("تم اضافه بالنجاح")
					return
				#add complete task
				elif self.user_input == "2":
					self.user_input = int(self.empty_input("اكتب رقم مهمه لي انجزتها"))
					self.user_input -=1
					if self.user_input < 0 or self.user_input >= len(manger.tasks):
						print("لاتوجد هذه مهمه اعد محاوله")
						continue
					else:
						manger.conversion= self.user_input
						manger.Reception_Ctask = manger.tasks[self.user_input]["task"]
						manger.CtaskAdd()
						print("تم اضافه بالنجاح")
						return
				elif self.user_input == "3":
						print("حسنا وداعا")
						return
				else:
						print("يرجى اختيار من خيارات اعلاه")
			except IndexError:
				print("لاتوجد هذه مهمه ")
			except ValueError:
				print("اكتب ارقام من فضلك")
	def deleteTaskCLI(self):
		while True:
			try:
				#menu main
				print("حذف المهام".center(60, "=")) 
				print("1-حذف مهام");print("2-اضافه مهام");print("3-الخروج")
				self.user_input = self.empty_input("اختر:")
				#delete Task
				if self.user_input == "1":
					self.user_input =int(self.empty_input("اكتب رقم مهمه لي بدك تحذفها:"))
					if self.user_input < 0 or self.user_input >= len(manger.Ctasks):
						print("لا توجد هذه مهمه اعد محاوله")
						continue
						else:
							if self.choices("هل انت متأكد من الحذف(نعم/لا):","نعم","لا","اختر نعم او لا"):
								self.conversion = self.user_input
								manger.deleteTask()
							else:
								print("حسنا حسنا اعد محاوله")
								continue
				#delete Completed Task			
				elif self.user_input == "2":
					self.user_input = self.empty_input("اكتب رقم مهمه مكتمله لي بدك تحذفها:")
					if self.user_input < 0 or self.user_input >= len(self.tasks):
						print("لا توجد هذه مهمه مكتمله اعد محاوله")
						continue
					else:
						if self.choices("هل انت متآكد من الحذف(نعم/لا):"):
							manger.conversion = self.user_input
							manger.deleteCtask()
							print("تم حذف بالنجاح")
							return
						else:
							print("حسنا حاول مره اخرى")
							continue
			except ValueError:
				print("اكتب ارقام")
			except IndexError:
				print("لا توجد هذه مهمه")
def menu_main(self):
	while True:
		print("قائمه رئيسيه ل مدير مهام v4.7.1".center(60,"="))
		print("1-اضافه مهام");print("2-عرض المهام");print("3-حذف المهام");print("4-خروج")
		self.user_input = self.empty_input("اختر:")
		if self.user_input == "1":
			self.addTaskCLI()
			self.clear_screen() 
		elif self.user_input == "2":
			self.viewTaskCLI()
			self.clear_screen()
		elif self.user_input == "3":
			self.deleteTaskCLI()
			self.clear_screen()
		elif self.user_input == "4":
			print("وداعا")
			return
		else:
			print("اختر من قائمه ادناه")
CLI = Cli()
CLI.menu_main()




