#سكربت مهام v4

from datetime import datetime
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
class Logic:
	def __init__(self):
		#Basis
		self.tasks={};self.Ctasks={}#completed tasks			
		#input
		self.user_input = None;self.choice=None
		#Features
		self.tasksID=0;self.CtasksID=0#this for def added tasks
		#def
	def Nothing_input(self,prompt):#Function to check user entry
		while True:
			self.user_input=input(prompt)
			if not self.user_input.strip():
				print("خطأ اعد محاوله");continue
			else:
				return self.user_input		
	def choiceForALL(self,prompt,true,false,error_msg):
		while True:
			self.choice = input(prompt)
			if self.choice == true:
				return True
			elif self.choice==false:
				return False
			else:
				print(error_msg);continue
	def show_tasks(self):
			while True:
				print("---عرض المهام---")
				if self.choiceForALL("بدك تطلع (نعم/لا): ","نعم", "لا","اختر نعم او لا"):
					self.menu_main()
				else:
						if self.choiceForALL('بدك تعرض مهام"1" او بدك تعرض مهامك مكتلمه "2":',"1","2",'اختر "1" او "2"'):
							if not self.tasks:
								print("قائمه مهامك فارغه")
							else:
								for i, (key,value) in enumerate(self.tasks.items(),1):
									print("قائمه مهامك(مهمه تاريخ حاله)")
									print(i,"-",value["task"],"  ",value["date"],"  ", value["staus"])
						else:
							if not self.Ctasks:
								print("قائمه انجازاتك فارغه")
							else:
								for i, (key,value) in enumerate(self.Ctasks.items(),1):
									print("قائمه مهامك مكتلمه(مهمه تاريخ حاله)")
									print(i,"-",value["task"],"  ",value["date"],"  ", value["staus"])		
	def tasks_added(self):
		while True:
			print("---اضافه مهام & اضافه مهام مكتلمة---")
			if self.choiceForALL("بدك تطلع (نعم/لا): ","نعم", "لا","اختر نعم او لا"):
				self.menu_main()
			else:
					if self.choiceForALL('بدك تضيف المهمة "1" بدك تضيف مهمه مكتلمه "2":',"1","2",'اختر "1" او "2"'):
						self.tasksID+=1
						self.user_input=self.Nothing_input("اكتب مهمه لي بدك تضيفها: ")
						self.tasks[f"task{self.tasksID}"]={"task":self.user_input,"date":date,"status":"غير مكتلمة"}
						print("تم اضافه بالنجاح✅")
						if self.choiceForALL('بدك تضيف مهمه او مهمه مكتمله (نعم/لا):',"نعم","لا", "اختر نعم او لا من فضلك"):
							continue
						else:
							self.menu_main()
					else:
						try:
							self.CtasksID+=1
							self.user_input=int(self.Nothing_input("اكتب رقم مهمه لي انجزتها"))
							self.Ctasks[f"Ctasks{self.CtasksID}"]={"task":self.tasks[f"task{self.user_input}"]["task"] ,"date":date,"status":"مكتلمة" }
							del self.tasks[f"task{self.user_input}"]
							if self.choiceForALL('بدك تضيف مهمه مكتلمه او مهمه مره اخرى  (نعم/لا):',"نعم","لا", "اختر نعم او لا من فضلك"):
								continue
							else:
								self.menu_main()
						except ValueError:
							print("اكتب رقم")
						except KeyError:
							if not self.tasks:
								print("قائمه مهامك فارغه")
							else:
								print("قائمه مهامك(فالحال انك نسيتها)")
								for i, (key,value) in enumerate(self.tasks.items(),1):
									print("قائمه مهامك(مهمه تاريخ حاله)");print(i,"-",value["task"],"  ",value["date"],"  ", value["staus"])
	def delete_tasks(self):
		while True:
			print("---حذف المهام---")
			if self.choiceForALL("بدك تطلع (نعم/لا): ","نعم", "لا","اختر نعم او لا" ):
				self.menu_main()
			else:
				try:
					if self.choiceForALL('وش بدك تحذف مهمه "1" او مهمه مكتمله "2":',"1","2","اختر 1 او 2"):
						self.user_input=int(input("اكتب رقم مهمه: "))
						task=f"task{self.user_input}"
						if self.choiceForALL("هل انت متأكد (نعم/لا) :","نعم","لا","اختر نعم او لا"):
							if task in self.tasks:
								del self.tasks[task]
								print("تم حذف✅")
							else:
								print("لا توجد هذه مهمه يرجى اطلاع ع قائمه مهام")
								continue
						else:
								print("حسنا اعد محاوله")
					else:
							self.user_input=int("اكتب رقم مهمه مكتلمه: ")
							Ctask=f"task{user_input}"
							if choiceForALL("هل انت متأكد (نعم/لا): ","نعم","لا","اختر نعم او لا"):
								if Ctask in self.tasks:
									del self.tasks[Ctask]#delete Complete Task
									print("تم حذف✅")
								else:
									print("لا توجد هذه مهمه مكتلمه اعد محاوله")
									continue
							else:
								print("حسنا اعد محاوله")
								continue
								
					
				except KeyError:
					print("لاتوجد هذه مهمه(مكتمله) لتي تريد حذفها")
	def menu_main(self):
		while True:
			try:
				print("---قائمه رئيسيه لمدير المهام---")
				print("1-اضافه المهام&اضافه مهام مكتلمه\n2-عرض المهام&مهام المكتلمه\n3-حذف مهام&حذف مهام مكتمله")
				print("4-خروج")
				self.user_input=int(input("اختر: "))
				if self.user_input == 1:
					self.tasks_added()
					return
				elif self.user_input == 2:
					self.show_tasks()
					return
				elif self.user_input == 3:
					self.delete_tasks()
					return
				elif self.user_input == 4:
					print("وداعا")
					return
				else:
					print("اختر خيار صحيح")
					continue
			except ValueError:
				print("اكتب رقم من فضلك")




Logic=Logic()
Logic.menu_main()








