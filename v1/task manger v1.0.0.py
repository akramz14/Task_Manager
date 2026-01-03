#1 دوال لاضافه مهام(من صنعي)
c_tasks=[]
tasks=[]
def  add_tasks(tasks):
    while True:
        print("هل تريد اضافه مهمه اختر(نعم/لا) ")
        choice= input("").strip().lower()
        if choice =="نعم" :
            task = input("ادخل مهمه لي بدك تضيفها:\n").strip().lower()
            tasks.append(task) 
        elif choice== "لا":
            break
        else:
            print("اختر نعم او لا")
#2دوال ل مهام مكتمله (منطق وفكره كود من صنعي تنسيق من ai))
def add_c_tasks(tasks, c_tasks):
    print("مبروك كملت مهمه عطني رقم مهمه عشان اسجلها لك يفنان")
    
    while True:
        try:
            choice = int(input("اكتب رقم مهمه: "))
            c_tasks.append(tasks[choice - 1])
            tasks.pop(choice - 1)             
        except ValueError:
            print("يرجى كتابه رقم مهمه")
        except IndexError:
            print("لاتوجد هذه مهمه في قائمه خاصه بك ")
            choice = input("هل تريد ان اعرض قائمه مهامك فحال انك نسيتها (نعم/لا): ").strip().lower()
            if choice == "نعم":
                print("حسنا اليك قائمه مهامك")
                for i in range(len(tasks)):
                    print(i + 1, "-", tasks[i])
            elif choice == "لا":
                print("فحال انك لم تنسى رقم مهمه يرجى اعاده محاوله")
            else:
                print("يرجى تروي في كتابة لكي تكتب بشكل صحيح سيتم اعاده البرنامج")
        
        choice = input("هل تريد كتابه مهمه اخرى اختر(نعم/لا): ").strip().lower()
        if choice == "نعم":
            print("تمام")
            continue
        elif choice == "لا":
            return "سيتم رجوع لواجهه تفاعليه"
        else:
            print("اعد محاوله")
#3 عرض قاذمه مهام مكتمله وغير متكمله(منطق من صنعي تنسيق من صنعي)
def list_tasks(c_tasks, tasks):
    print("اختار هل تريد عرض مهامك منجزه او غير منجزه")

    while True:
        try:
            choice = int(input('اختر "1" مهام غير منجزه  "2" مهام منجزه: '))

            if choice == 1:
                print("مهام غير منجزه:")
                for i in range(len(tasks)):
                    print(i + 1, "-", tasks[i])

            elif choice == 2:
                print("مهام منجزه:")
                for i in range(len(c_tasks)):
                    print(i + 1, "-", c_tasks[i])

            else:
                print("اختار رقم (1/2)")

        except ValueError:
            print('اختار "1" مهام غير منجزه أو "2" مهام منجزه')
            print("بدك تشوف شي ثاني؟")
            choice = input("اختر (نعم/لا): ").strip().lower()

            if choice == "نعم":
                continue
            elif choice == "لا":
                return "حسنا وداعا"
            else:
                print("اعد محاوله اكتب نعم او لا")
#4 حذف مهام مكتمله وغير متكمله (منطق من صنعي تنسيق من ai)
def delete_tasks_and_completed_tasks(tasks, c_tasks):
    while True:
        try:
            choice = int(input("اختر هل تريد حذف مهامك غير مكتملة (1) أو مهامك مكتملة (2): "))

            if choice == 1:
                task_num = int(input("اختر رقم المهمة: "))
                ur_sure = input("هل أنت متأكد من الحذف (نعم/لا): ").strip().lower()
                if ur_sure == "نعم":
                    tasks.pop(task_num - 1)
                    print("تم حذف المهمة بنجاح")
                elif ur_sure == "لا":
                    print("تم إلغاء العملية")
                else:
                    print("اختر نعم أو لا")

            elif choice == 2:
                task_num = int(input("اختر رقم المهمة: "))
                ur_sure = input("هل أنت متأكد من الحذف (نعم/لا): ").strip().lower()
                if ur_sure == "نعم":
                    c_tasks.pop(task_num - 1)
                    print("تم حذف المهمة بنجاح")
                elif ur_sure == "لا":
                    print("تم إلغاء العملية")
                else:
                    print("اختر نعم أو لا")
            else:
                print("اختر 1 أو 2")

        except IndexError:
            print("رقم المهمة غير موجود")
            show_choice = input("هل تريد أن أعرض لك قائمة المهام؟ (نعم/لا): ").strip().lower()
            if show_choice == "نعم":
                list_choice = int(input("هل تريد قائمة مهام مكتملة (2) أو غير مكتملة (1): "))
                if list_choice == 1:
                    print("مهام غير مكتملة:")
                    for i, t in enumerate(tasks, 1):
                        print(i, "-", t)
                elif list_choice == 2:
                    print("مهام مكتملة:")
                    for i, t in enumerate(c_tasks, 1):
                        print(i, "-", t)
                else:
                    print("اختر رقم 1 أو 2")
            elif show_choice == "لا":
                print("حسنا، أعد المحاولة لاحقًا")

        except ValueError:
            print("اكتب رقم صحيح")

        again = input("هل تريد حذف مهمة أخرى؟ (نعم/لا): ").strip().lower()
        if again == "نعم":
            continue
        elif again == "لا":
            print("العودة إلى الواجهة الرئيسية")
            break
        else:
            print("اعد اختيار صحيح")
#واجهه cli (من صنع وتنسيق ai) )

def main_menu():
    print("\n--- مدير المهام ---")
    print("1 - إضافة مهمة")
    print("2 - حذف مهمة")
    print("3 - إكمال مهمة")
    print("4 - عرض المهام")
    print("5 - خروج")

while True:
    main_menu()
    choice = input("اختر رقم: ").strip()

    if choice == "1":
        add_tasks(tasks)
    elif choice == "2":
        delete_tasks_and_completed_tasks(tasks,c_tasks)
    elif choice == "3":
        add_c_tasks(c_tasks)
    elif choice == "4":
        list_tasks(c_tasks,tasks)
    elif choice == "5":
        print("إلى اللقاء")
        break
    else:
        print("خيار غير صحيح")
        >













