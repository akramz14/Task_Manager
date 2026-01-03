#pylint:disable=W0012
#pylint:disable=W0622
#2025-12-28 12:31:01

from datetime import datetime
from enum import Enum

class Status(Enum):
	FINISHED = "مكتلمة"
	UNFINISHED = "غير مكتلمة"
	WORKING = "قيد انجاز"
	
class Logic:
	def __init__(self):
		self.tasks = {}
		self.id = 0
	#date valid date
	def valid_date(self,value,fmt="%Y-%m-%d %H:%M:%S") :
		try:
			datetime.strptime(value,fmt)
			return True
		except (TypeError,ValueError) :
			raise ValueError("يجب ان تكتب صيغه صحيحه ل تاريخ وهي YYYY-MM-DD HH:MM:SS")
	#id Error
	def idError(self,id:int):
		if id is None:
			raise ValueError("يجب ان تكتب رقم مهمة") 
		if not isinstance(id, int):
			raise TypeError("خطأ يجب ان تكتب رقما")
		if id not in self.tasks:
			raise KeyError("خطأ مهمة غير موجودة")
	#Date
	def now(self):
		return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	#AddTask
	def AddTask(self,title,details,status = Status.UNFINISHED):
		if not title.strip():
			raise ValueError("لا يمكن ان يكون عنوان مهمة فارغا")
		self.id +=1
		start_task = self.now()
		end_task = None
		self.tasks[self.id] = {
		"title": title, 
		"details": details, 
		"status" : status,
		"date":{
		"start task": start_task, 
		"end task":  end_task
		} 
			}
	#delete Task
	def DeleteTask(self, id):
		self.idError(id)
		del self.tasks[id]
	#editStatus
	def EditStatus(self,id,status=None):
		self.idError(id)
		if status is None:
			raise ValueError("انت لم تكتب حاله مهمة")
			
		if not isinstance(status,Status):
			raise TypeError("خطأ يجب ان تختار حالة من Status(خطأ مستحيل يظهر لمستخدم اصلا🤓 )")
		if status == Status.WORKING:
			if self.tasks[id]["status"] == Status.FINISHED:
				raise ValueError("لا يمكنك تحويل مهمة غير مكلتمة الى غير مكتلمة")
			self.tasks[id]["status"] = Status.WORKING
		
		if status == Status.FINISHED:
			if self.tasks[id]["status"] == Status.UNFINISHED:
				raise ValueError("لا يمكنك تحويل مهمة غير مكتلمة الى مكتلمة")
			self.tasks[id]["status"]=Status.FINISHED
	#edit endtask
	def EditETask(self,id,end_task):
		self.valid_date(end_task)
		self.idError(id)
		if self.tasks[id]["status"] == Status.UNFINISHED:
			raise ValueError("لايمكنك تعديل نهايه تاريخ مهمة")
		if self.tasks[id]["status"] == Status.WORKING:
			raise ValueError("لا يمكنك تعديل تاريخ مهمة قيد انجاز")
			
		start_str = self.tasks[id]["date"]["start task"]		
		end_str = end_task
		start_dt = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
		end_dt = datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")
		if start_dt > end_dt:
			raise ValueError("لا يمكنك ان تجعل نهاية اصغر من بداية مهمة")
		self.tasks[id]["date"]["end task"] = end_task
	#Edit Start task
	def EditStask(self,id,start_task):
		self.valid_date(start_task)
		self.idError(id)
		if self.tasks[id]["date"]["end task"] is None:
			self.tasks[id]["date"]["start task"]=start_task
			return
		end_str = self.tasks[id]["date"]["end task"]		
		start_str =  start_task
		end_dt = datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")
		start_dt = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
		if end_dt < start_dt:
			raise ValueError("لا يمكنك ان تجعل بداية مهمة اصغر من نهايتها")
		self.tasks[id]["date"]["start task"] = start_task
	#Edit title
	def EditTitle(self,id,title=None):
		self.idError(id)
		if title is None:
			raise ValueError("لا يمكنك ترك عنوان مهمة فارغ")
		if not isinstance(title,str):
			raise TypeError("يجب ان يكون عنوان نصا")
		if not title.strip():
			raise ValueError("لا يمكنك ترك عنوان مهمة فارغ")#حمايه مزدوجة😁
		self.tasks[id]["title"]=title
	def EditDetails(self,id,details=None):
		self.idError(id)
		self.tasks[id]["details"]=details #ملاحضه من مسموح ان يترك مستخدم تفاصيل فارغة
	# Time calculation
	def TimeCalculation(self,id):
		self.idError(id)
		if self.tasks[id]["date"]["end task"] == None:
			raise ValueError("خطأ مهمة لي بدك تحسب وقتها ليس لديها وقت انتهاء")
		start_str = self.tasks[id]["date"]["start task"]
		end_str = self.tasks[id]["date"]["end task"]
		start_dt = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
		end_dt = datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")
		duration = end_dt - start_dt
		return duration
#2025-12-28 13:43:53
#تم تعديل
#تعديلات بسيطه
#اضافه حمايه لتحقق من ادخال مستخدم لتاريخ
#تعديل حمايه id
#تحسين منطق edit task
#غير مكتملة >قيد انجاز>مكتلمة
#اما باقي لم يتم تحسينه 
#عموما حاولت اتجنب اخطاء مدخلات اكثر من اخطاء منطق

#2025-12-30 12:40:00







