print('1- add a student\n2- showing the students\n3- finding avg\n4- finding the best student\n5- showing excepted students\n6- exit')
students = {}

def add_student (name, grade:list):
        students[name] = grade
    
    

def showing_student ():
    if len(students) != 0 :
        names = []
        for n in students.keys():
            names.append(n)
        return names
    
def avg_student (name):
    if name in students.keys():
        return (sum(students[name])) / (len(students[name]))
    else :
        print('name is not difind')


def best_student ():
    if len(students) != 0 :
        best_avg = 0
        best_name = None
        for ke, va in students.items():
            avrage = sum(va)/len(va)
            if avrage > best_avg :
                best_avg = avrage
                best_name = ke
            elif avrage == best_avg :
                best_name = best_name +f' and {ke}'
        return (f'best names: {best_name} with avg {best_avg}')
    
def excepted_students ():
    excepted = []
    for k,v in students.items():
        x = avg_student(k)
        if x >= 15 :
            excepted.append(k)
    return excepted        


while True:
    input1 = input('what do you want to do :')
    if not input1.isdigit():
        print('we need a number')
        continue
    if (int(input1) >= 1 and int(input1) <= 6): 
        if input1 == '1':
            input_name = input('what is his name ?')
            input_grades = []
            times =1
            going = True
            while going == True :
                if times == 1 :
                    input_num = input('enter a number : ')
                    if input_num == 'done':
                        print('you can not do that.firs enter a number')
                        continue
                    elif int(input_num) == False or (int(input_num) < 0 or int(input_num) > 20):
                        print('that not rihgt.enter a number in the range')
                        continue
                    else:
                        input_grades.append(int(input_num))
                        times += 1
                else:
                    input_num = input('enter a number or if you ara done enter done : ')
                    
                    if input_num == 'done':
                        going = False
                    elif not input_num.isdigit() or int(input_num) < 0 or int(input_num) > 20:
                        print('that not rihgt.enter a number in the range')
                    else :
                        input_grades.append(int(input_num))
            
            add_student(input_name,input_grades)
        elif input1 == '2':
            show = showing_student()
            print(show)
        elif input1 == '3':
            input_avg = input('enter the name :')
            a =avg_student(input_avg)
            print(a) 
        elif input1 == '4':
            the_best = best_student()
            print(the_best)
        elif input1 == '5':
            excepted = excepted_students()
            print(excepted)
        elif input1 == '6':
            break        
    else :
        print('enter a number in the range')
        continue

