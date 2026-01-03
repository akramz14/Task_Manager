
#creat by2025-12-28 12:31:01
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
		self.DataStored = 0
		self.error = 0#مابعرف كيف استعمل ذا متغير حاليا
	#date valid date
	def valid_date(self, value, fmt="%Y-%m-%d %H:%M:%S"):
	       try:
	       	datetime.strptime(value, fmt)
	       	return True  # التاريخ صحيح
	       except ValueError:
	       	return {"error": "صيغة الوقت خطأ، الصيغة الصحيحة هي YYYY-MM-DD HH:MM:SS"}
	#id Error
	def idError(self,id:int):
		if id is None:
			return {"error":"خطأ انت لم تكتب شيء" }
		if not isinstance(id, int):
			return {"error":"خطأ يحب ان تكتب رقما"}
		if id not in self.tasks:
			return {"error":"خطأ مهمة هذه غير موجودة"}
	#Date
	def now(self):
		return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	#AddTask
	def AddTask(self,title,details,status = Status.UNFINISHED):
		if not title.strip():
			return {"error":"خطأ يجب لا يمكنك ان تترك عنوان فارغا"}
		self.id +=1
		start_task = self.now()
		end_task = None
		self.DataStored = 0
		self.tasks[self.id] = {
		"title": title, 
		"details": details, 
		"status" : status,
		"date":{
		"start task": start_task, 
		"end task":  end_task
		}, 
		"info":{
		"success":True, 
		"type":"dict", 
		"data stored":self.DataStored, 
		"error":self.error
		}, 
		 }
	#delete Task
	def DeleteTask(self, id):
		self.idError(id)
		del self.tasks[id]
	#editStatus
	def EditStatus(self,id,status=None):
		self.idError(id)
		if status is None:
			return {"error":"انت لم تكتب حاله مهمة"}
		if status == Status.UNFINISHED:
			if self.tasks[id]["status"] is Status.UNFINISHED:
				return {"error":"خطا مهمة غير مكتملة بالفعل"}
			if self.tasks[id]["status"] in (Status.WORKING,Status.UNFINISHED):
				self.tasks[id]["status"] = Status.UNFINISHED
				self.tasks[id]["date"]["end task"] = None
				
		if status == Status.WORKING:
			if self.tasks[id]["status"] is Status.WORKING:
				return {"error":"خطا مهمة قيد انجاز بالفعل"}
			if self.tasks[id]["status"] in (Status.WORKING,Status.UNFINISHED):
				self.tasks[id]["status"] = Status.WORKING
				self.tasks[id]["date"]["end task"] = None
				
		if status == Status.FINISHED:
			if self.tasks[id]["status"] is Status.FINISHED:
				return {"error":"خطا مهمة مكتملة بالفعل"}
			if self.tasks[id]["status"] in (Status.WORKING,Status.UNFINISHED):
				self.tasks[id]["status"] = Status.FINISHED
				self.tasks[id]["date"]["end task"] = self.now()
			
			
		if status == Status.FINISHED:
			if self.tasks[id]["status"] == Status.UNFINISHED:
				return {"error":"خطأ لايمكنك تحويل مهمة قيد انجاز الى غير مكتملة" } 
			self.tasks[id]["status"]=Status.FINISHED
	#edit endtask
	def EditETask(self,id,end_task):
		self.valid_date(end_task)
		self.idError(id)
		if self.tasks[id]["status"] == Status.UNFINISHED:
			return {"error":"خطأ لا يمكنك تعديل تاريخ انتهاء مهمة غير مكتملة لانها غير مكتملة"}
		if self.tasks[id]["status"] == Status.WORKING:
			return {"error":"خطأ لا يمكنك تعديل تاريخ مهمة قيد انجاز"}			
		start_str = self.tasks[id]["date"]["start task"]		
		end_str = end_task
		start_dt = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
		end_dt = datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")
		if start_dt > end_dt:
			return {"error":"لا يمكنك جعل مهمة مكتملة نهايتها اصغر من بدايتها"} 
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
			return {"error":"خطأ لايمكن جعلك بدايه اكبر من النهايه"} 
		self.tasks[id]["date"]["start task"] = start_task
	#Edit title
	def EditTitle(self,id,title=None):
		self.idError(id)
		if title is None:
			return {"error":"خطأ لايمكنك ترك عنوان فارغا"}
		if not isinstance(title,str):
			return {"error":"خطأ لايمكنك يجب ان تكون مهمة نصا(خطأ مستحيل يظهر لمستخدم)"} 
		if not title.strip():
			return {"error":"خطا لايمكنك ترك عنوان فارغا"} #Dual protection😃
		self.tasks[id]["title"]=title
	def EditDetails(self,id,details=None):
		self.idError(id)
		self.tasks[id]["details"]=details#It is allowed to leave blank details
	# Time calculation
	def TimeCalculation(self,id):
		self.idError(id)
		if self.tasks[id]["date"]["end task"] == None:
			return {"error":"خطأ مهمة هذه ليس لديها وقت انتهاء(ربما تكون قيد انجاز او غير مكتملة)"} 
		start_str = self.tasks[id]["date"]["start task"]
		end_str = self.tasks[id]["date"]["end task"]
		start_dt = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
		end_dt = datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")
		duration = end_dt - start_dt
		return duration
#2025-12-28 13:43:53
# update 2025-12-30 12:40:00
#update  2025-12-31 11:50:41
#Last update on 2025-12-31 12:32:24
