#مشروع مهام v3
tasks = []
c_tasks = []
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
        #تاريخ تحسين 15 ديسمبر بدأ في 12:6صباحا تم انتهاء ساعه 12:13
def tryagain():
    while True:
        choice = input("هل تريد اعاده محاوله(نعم/لا): ").strip().lower()
        if choice == "نعم":
            print("حسنا اعد محاوله")
            return True
        elif choice == "لا":
            print("حسنا سيتم ارجاعك لقائمه رئيسيه")
            return False
        else:
           print("اختر نعم او لا")
#دوال بسيط لتجنب تكرار       
def add_tasks(tasks):
    while True:
        if yes_or_no("هل تريد اضافه المهمة(نعم/لا) " ):
            if yes_or_no("هل انت متأكد(نعم/لا)"):
                enter = input("اكتب مهمه لي بدك تضيفها: ")
                tasks.append(enter)
            else:
                print("حسنا اذا لم ترغب ب اضافه مهمه ف سنعيدك لقائمه رئيسيه")
                return 
        else:
            print("سيتم ارجاعك لقائمه رئيسيه")
            return
def add_c_tasks(c_tasks,tasks):
    print("كملت مهمه؟\nعظيم اكتب رقمها عشان اسجلها لك")
    while True:
        try:
               enter = int(input("ادخل رقم مهمه عشان اظيفها لقائمه انجازاتك🎉: "))-1
               if yes_or_no("هل انت متأكد من رقم مهمه "):
                   c_tasks.append(tasks[enter])
                   tasks.pop(enter)
                   print("تم اضافه انجازك🎉")
                   if yes_or_no("هل تريد اضافه انجاز اخر "):
                       print("يبدو انك سويت انجاز ثاني لاتتردد بكتابته♥️")
                       continue
                   else:
                       print("لما تسوي انجاز ثاني لا تنسى تحطها هني")
                       return
               else:
                  print("حسنا تحقق من رقم(في قائمه مهام وارجع لكي تضيفها لقائمه انجازاتك😊")
                  return
        except ValueError:
            print("اكتب ارقام من فضلك♥️")
        except IndexError:
            print("مالقيت رقم ذي مهمه يرجى كتابه رقم صحيح")
            if yes_or_no("هل تريد ان اريك قائمه مهامك "):
                 print("قائمه مهامك😊")
                 show_tasks(c_tasks,tasks)
                 print("اختر مهمه لي انجزتها") 
                 continue
            else:
                print("فحال عدم نسيانك ل رقم مهمه لي انجزتها يرجى اعاده محاوله♥️")
                continue
#تاريخ تحسين الأثنين 15 ديسمبر                          تم انتهاء ساعه 12 صباحا
#لم اضف ميزات جديده فقط عدلت سكربت ليصير بشكل متناسق وحسنت بعض اخطاء املائيه(ليس كل) 
def show_tasks(c_tasks,tasks):
    if numone_or_numtwo("هل تريد عرض قائمه مهام منجزه (1) غير منجزه (2)"):
        print("اليك قائمه مهامك المنجزه")
        list_ctasks(c_tasks)
        return
    else:
        print("اليك قائمه مهامه غير المنجزة")
        list_tasks(tasks)
        #تحسين بسيط مايحتاج احط معلومات اضافيه له                        
def delete_tasks(tasks, c_tasks ):
    while True:
        try:
            if numone_or_numtwo("شو بدك تحذف مهامك (1) إنجازاتك (2)"):
                enter = int(input("اكتب رقم المهمة لي بدك تحذفها"))-1
                if yes_or_no("هل انت متأكد من حذفها "):
                    tasks.pop(enter)
                else:
                    tryagain()
            else:
                enter = int(input("اكتب رقم انجاز لي بدك تحذفه"))-1
                if yes_or_no("هل انت متأكد من الحذف"):
                    c_tasks.pop(enter)
                else:
                    if tryagain():
                        continue
                    else:
                        return
        except IndexError:
                 print("لم اجد رقم هذه مهمه/انجاز")
                 if yes_or_no("هل تريد ان اعرض قائمه مهامك/انجازاتك"):
                     show_tasks(c_tasks,tasks)
                     print("اعد محاوله♥️")
                     continue
                 else:
                     print("حسنا اعد محاوله")
                     continue
        except ValueError:
            print("اكتب ارقام")                         
    #تاريخ بدأ تعديل 15/ديسمبر/2025 12:50        

def menu_main():
         print("----واجهه رئيسيه لبرنامج مهام----")
         print("1-اضافه مهمة")
         print("2-اضافه انجاز")
         print("3-عرض مهام/انجازات")
         print("4-حذف مهام /انجازات") 
         print("5-خروج من برنامج") 
while True:
    menu_main()
    try:
        choice = int(input("اختر لي بدك تسويه: "))
        if choice == 1:
            add_tasks(tasks)
        elif choice == 2:
            add_c_tasks(c_tasks, tasks)
        elif choice == 3:
            show_tasks(c_tasks,tasks)
        elif choice == 4:
           delete_tasks(tasks, c_tasks )
        elif choice == 5:
            break
        else:
             print("اختر من قائمه ادناه")     
    except ValueError:
        print("اكتب ارقام")