#السكربت المهام v4. 6
from datetime import datetime
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
class Logic:
	def __init__(self):
		#تخزين
		self.tasks = {}#قائمة المهام
		self.Ctasks = {}#قائمة المهام مكتملة
		#معرفات
		self.taskID = 0#معرف المهمه
		self.CtaskID = 0#معرف المهمه مكتلمه
		#ادخالات
		self.user_input = None #ادخال مستخدم 
		self.choice = None #ادخال خيارات مستخدم
	def verify_input(self,prompt):#تحقق ادخال (منع من ادخال فراغات) 
		while True:
			self.user_input = input(prompt)#ادخال مطلوب من مستخدم
			if not self.user_input.strip():
				print("ادخال غير صحيح")
			else:
				return self.user_input
	def choiceForALL(self,prompt,true,false,error_msg):#داله ل ادخال خيارات متعدده
		while True:
			choice = input(prompt)
			if not choice.strip():
				print("خطأ انت لم تكتب شيء")
				continue
			else:
				if choice == true:
					return True
				elif choice == false:
					return False
				else:
					print(error_msg)
	def view_task(self):
		print("قائمه المهام".center(60, "="))
		if self.choiceForALL("بدك تطلع (نعم/لا): ","نعم","لا","اختر نعم او لا"):
			return #رجوع لقائمه رئيسيه
		else:
			if self.choiceForALL("وش بدك 1 مهامك او 2 مهامك مكتمله:","1", "2","اختر نعم او لا"):
				if not self.tasks:
					print("قائمه مهامك فارغه")
				else:
					print("قائمه مهامك هي:")
					for i,(key,value) in enumerate(self.tasks.items(),1):
						print(i,"-",value["task"],"   ",value["date"],"   ",value["status"])
			else:
				if not self.Ctasks:
					print("قائمه انجازاتك فارغه")
				else:
					print("قائمه مهامك هي:")
					for i,(key,value) in enumerate(self.Ctasks.items(),1):
						print(i,"-",value["task"],"   ",value["date"],"   ",value["status"])
	def add_task(self):
		while True:
			print("اضافه مهام".center(60, "="))
			if self.choiceForALL("بدك تطلع (نعم/لا):","نعم","لا","اختر نعم او لا"):
					return
			else:
					if self.choiceForALL("بدك تضيف مهمه 1 بدك تضيف مهمه مكتلمه 2","1","2","اختر نعم او لا"):
						self.taskID+=1
						inputU = self.verify_input("اكتب مهمه لي بدك تضيفها:")#Uinput متغير بسيط لادخال مستخدم مهمه
						self.tasks[f"task{self.taskID}"] = {"task":inputU,"date":date,"status":"غير مكتمله"}
						if self.choiceForALL("بدك تضيف مهمه اخرى (نعم/لا):","نعم","لا","اختر نعم او لا"):
							continue
						else:
							return
					else:
						try:
							self.CtaskID+=1
							inputU = int(self.verify_input("اكتب رقم مهمه لي انهيتها:"))
							inputU = f"task{inputU}"
							if inputU in self.tasks:
								self.Ctasks[f"task{self.CtaskID}"] = {"task":self.tasks[inputU]["task"],"date":date,"status":"مكتلمه"}
								del self.tasks[inputU]
							if self.choiceForALL("بدك تضيف مهمه اخرى (نعم/لا):","نعم","لا","اختر نعم او لا"):
								continue
							else:
								return
						except ValueError:
							print("اكتب رقم")
						except KeyError:
							print("لم اجد هذا مفتاح")
	def delete_task(self):
		while True:
			try:
				print("حذف المهام".center(60, "="))				
				if self.choiceForALL("بدك تطلع(نعم/لا):","نعم","لا","اختر نعم او لا"):
					return
				else:
					if self.choiceForALL("بدك تحذف مهام 1 بدك تحذف مهام مكتمله 2","1","2","اختر نعم او لا"):
						Uinput = int(self.verify_input("اكتب رقم المهمه:")) 
						Uinput = f"task{Uinput}"
						if Uinput in self.tasks:
							if self.choiceForALL("هل انت متأكد من حذف(نعم/لا):","نعم","لا","اختر نعم او لا"):
								del self.tasks[Uinput]
								print("تم حذف✅")
							else:
								print("حسنا اعد محاوله")
								continue
						else:
								print("لا توجد هذه مهمه اعد محاوله")
								continue								
					else:
						Uinput = int(self.verify_input("اكتب رقم المهمه:")) 
						Uinput = f"task{Uinput}"
						if Uinput in self.Ctasks:
							if self.choiceForALL("هل انت متأكد من حذف(نعم/لا):","نعم","لا","اختر نعم او لا"):
								del self.Ctasks[Uinput] 
								print("تم حذف✅")
							else:
								print("حسنا اعد محاوله")
								continue
						else:
								print("لا توجد هذه مهمه مكتمله اعد محاوله")
								continue
				
			except ValueError:
				print("اكتب رقم")
			except KeyError:
				print("لا توجد هذه المهمه")
	def menu_main(self):
		while True:
			print("الواجهه رئيسيه".center(60, "="))
			print("1-اضافه المهام")
			print("2-عرض المهام")
			print("3-حذف المهام")
			print("4-خروج")
			choice = input("اختر:")
			if not choice.strip():
				print("لا تكتب فراغ")
			else:
				if choice == "1":
					self.add_task()
				elif choice == "2":
					self.view_task()
				elif choice == "3":
					self.delete_task()
				elif choice == "4":
					return
				else:
						print("يرجى اختيار من قائمه اعلاه")
						continue					
TaskManger = Logic()
TaskManger.menu_main()
print(TaskManger.tasks)
print(TaskManger.Ctasks)
																	

																																		
																																																																				
																																																																																																						
																																																																																																																																								
																																																																																																																																																																										
																																																																																																																																																																																																																																														
																																																																			