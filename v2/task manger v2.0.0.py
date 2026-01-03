c_tasks = []
tasks = []

def yes_or_no(prompt):
    while True:
        choice = input(prompt+"(نعم/لا): ").strip().lower()
        if choice == "نعم":
            return True
        elif choice == "لا":
            return False
        else:
            print("اختر (نعم او لا)")
def numone_or_numtwo(prompt):
         while True:
             try:
                 choice = int(input(prompt+"1 او 2: "))
                 if choice == 1:
                     return True
                 elif choice == 2:
                     return False
                 else:
                     print("اختر 1 او 2")
             except ValueError:
                 print("اختر رقم من فضلك")
def list_tasks(tasks):
    for i in range(len(tasks)):
        print(i+1,"-",tasks[i])
def list_ctasks(c_tasks):
    for i in range(len(c_tasks)):
        print(i+1,"-",c_tasks[i])



def add_tasks(tasks):
         while True:
             if yes_or_no("هل تريد اضافه مهمه "):
                 if yes_or_no("هل انت متأكد "):
                     enter = input("اكتب مهمه لي بدك تضيفها: ")
                     tasks.append(enter)
                 else:
                     print("حسنا اذا لم ترغب ب اضافه مهمه ف سنعيدك لقائمه رئيسيه")
                     return 
             else:
                 print("سيتم ارجاعك لقائمه رئيسيه")
                 return
def add_c_tasks(c_tasks,tasks):
       print("كملت مهمه؟ذا انجاز عظيم عطني رقم مهمه ب قائمه مهامك عشان اضيفها لمهام منجزه")
       while True:
           try:
               enter = int(input("ادخل رقم مهمه عشان اظيفها لقائمه انجازاتك🎉: "))-1
               if yes_or_no("هل انت متأكد من رقم مهمه "):
                   c_tasks.append(tasks[enter])
                   tasks.pop(enter)
                   print("تم اضافه انجازك🎉")
                   if yes_or_no("هل تريد اضافه انجاز اخر "):
                       print("حسنا يابطل واضع انك الأنجزت كثير ستمر ب كاتبه باقي إنجازاتك🌹")
                       continue
                   else:
                       print("لما تسوي انجاز جديد لاتنسى تحطه هني 🌹")
                       return
               else:
                  print("حسنا تحقق من رقم(في قائمه مهام وارجع لكي تضيفها لقائمه انجازاتك😊")
                  return
           except ValueError:
                        print("اكتب ارقام من فضلك♥️")
           except IndexError:
                        print("مالقيت رقم ذي مهمه يرجى كتابه رقم صحيح")
                        if yes_or_no("هل تريد ان اريك قائمه ماهمك عشان تختار اناجز لي بدك تحطه "):
                            print("قائمه مهامك😊")
                            list_tasks(tasks)
                            print("بما انك رأيت قائمه مهامك اختر مهمه لي انجزتها🔥")
                            continue
                        else:
                          print("يبدو انك لم تنسى رقم انجازك بل اخطات بةتابه لا باس هذا خطأ شائع اهم شي انك فاكر شو سويت🔥😎")
                          print("اعد محاوله")
                          continue
def show_list(c_tasks,tasks):
        if numone_or_numtwo("هل تريد عرض قائمه مهام منجزه (1) غير منجزه (2)"):
         print("اليك قائمه مهامك منجزه")
         list_ctasks(c_tasks)
         return
        else:
         print("اليك قائمه مهامك غير منجزه(انجزها😡)")
         list_tasks(tasks)
def delete_tasks(tasks, c_tasks ):
         while True:
             try:
                 if numone_or_numtwo("شو بدك تحذف مهامك (1) إنجازاتك (2)"):
                     enter = int(input("اكتب رقم مهم لي بدك تحذفها"))-1
                     if yes_or_no("هل انت متأكد من حذفها "):
                         tasks.pop(enter)
                     else:
                         print(" حسأوحع لقائمه رئيسيه")
                         return
                 else:
                      enter = int(input("اكتب رقم انجاز لي بدك تحذفه"))-1
                      if yes_or_no("هل انت متأكد من حذفه"):
                          c_tasks.pop(enter)
                      else:
                          print("حسنا سأوحعك لقائمه رئيسيه")
                          return 
             except IndexError:
                 print("مالقيت مهمه لي بدك تحذفها ")
                 print("قائمه مهامك وانجازاتك (فحال انك نسيتها) ")
                 print("قائمه مهامك")
                 list_tasks(tasks)
                 print("قائمه انجازاتك")
                 list_ctasks(c_tasks)
             except ValueError:
                 print("اكتب ارقام")
def main():
         print("----واجهه رئيسيه لبرنامج مهام----")
         print("1-اضافه مهمه")
         print("2-اضافه انجاز")
         print("3-عرض مهام منجزه/غير منجزه")
         print("4-حذف إنجازات/مهام")
         print("5-خرَوج من برنامج")
while True:
         main()
         try:
             choice = int(input("اختر لي بدك تسويه: "))
             if choice == 1:
                 add_tasks(tasks)
             elif choice == 2:
                     add_c_tasks(c_tasks, tasks)
             elif choice == 3:
                    show_list(c_tasks,tasks)
             elif choice == 4:
                      delete_tasks(tasks, c_tasks )
             elif choice == 5:
                 break
             else:
                 print("اختر من قائمه ادناه")     
         except ValueError:
             print("اكتب ارقام")
         
