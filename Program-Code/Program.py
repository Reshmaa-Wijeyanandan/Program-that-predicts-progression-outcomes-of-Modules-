#Credit Marks and level count
pass_credit = ""
defer_credit = ""
fail_credit = ""
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
#Data Arrays
entered_credits = []
calculated_level =[]
all_user_inputs =  []


lecturer_response = "t"
menu = int(input("What menu option you want to select \n1, 2, 3, 4: "))

while lecturer_response != "q":

    result = ''
    level = ''
    user_input_dict = {}

    #Validity of Data ( Check Range and Integer )
    def user_func(credit_type):

        try:
            marks_input = int(input(f"Enter your credits at {credit_type}: "))
        except:
            print("Integer required")
            user_func(credit_type)
        else:
            if 120 >= marks_input >= 0 and marks_input % 20 == 0:
                global result
                result = marks_input


            else:
                print('Out of Range')

                user_func(credit_type)

        return result


    #Calling the Functions and Storing data
    pass_credit = user_func("pass")
    defer_credit = user_func("defer")
    fail_credit = user_func("fail")
    total_credits = pass_credit + defer_credit + fail_credit

    #Total Check
    while total_credits != 120:
        print("Total incorrect")
        pass_credit = user_func("pass")
        defer_credit = user_func("defer")
        fail_credit = user_func("fail")
        total_credits = pass_credit + defer_credit + fail_credit

    #Store Data
    current_credits = [pass_credit,defer_credit,fail_credit]
    entered_credits.append(current_credits)

    #Check the Level
    if pass_credit == 120:
        level = "Progress"
        user_input_dict["level"] = "Progress"
        progress_count+= 1
    elif pass_credit == 100:
        level = "Progress (module trailer)"
        trailer_count += 1
        user_input_dict["level"] = "Progress (module trailer)"
    elif pass_credit < 100 and fail_credit < 80:
        level = "Module retriever"
        user_input_dict["level"] = "Module retriever"
        retriever_count += 1
    else:
        level = "Exclude"
        user_input_dict["level"] = "Exclude"
        exclude_count += 1
    print(level)
    user_input_dict["credits"] = current_credits
    all_user_inputs.append(user_input_dict)
    lecturer_response = input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")


level_count =  progress_count + trailer_count + retriever_count + exclude_count

def main_part ():
    # Horizontal Histogram
    print()

    def star(star_count):
        stars = " * " * star_count
        return stars

    print('Horizontal Histogram')

    print(f'{"Progress" :15} ' + str(progress_count) + '   : ' + star(progress_count))
    print(f'{"Trailer" :15} ' + str(trailer_count) + '   : ' + star(trailer_count))
    print(f'{"Retriever" :15} ' + str(retriever_count) + '   : ' + star(retriever_count))
    print(f'{"Exclude" :15} ' + str(exclude_count) + '   : ' + star(exclude_count))
    print(' ')
    print(level_count, 'outcomes in total')

def PART2():
    #Vertical Histogram
    print()

    print("Vertical Histogram")
    Level_Dictionary = {0:"Progress",1:"Trailer",2:"Retriever", 3:"Exclude"}
    Level_count = [progress_count,trailer_count,retriever_count, exclude_count]
    print()


    for i in range(4):
        print(f'{Level_Dictionary[i]:20}', end= "  ")
    print()

    MaxCount = max(Level_count)
    for i in range(MaxCount):
        for x in range(4):
            if Level_count[x] >0:
                print(f'{"    x":22}',end="")
                Level_count[x] -=1

            else:
                print(f'{"     ":22}', end="")
        print()
    print(level_count, 'outcomes in total')

def Part3():
    #3rd Section - All data display
    print()
    for objects in all_user_inputs:
        print(f'{objects["level"] :12} : {objects["credits"][0]}, {objects["credits"][1]}, {objects["credits"][2]}')

def Part4 ():
    #File Handling
    print("\nFile handling")
    student_file = open("data file","w")
    for objects in all_user_inputs:
        student_file.write(f'{objects["level"] :12} : {objects["credits"][0]}, {objects["credits"][1]}, {objects["credits"][2]}' + "\n")
    student_file.close()
    student_file  = open("data file", "r")
    data_from_file = student_file.read()
    print(data_from_file)

if menu == 1:
    main_part()
elif menu == 2 :
    main_part()

    PART2()
elif menu == 3 :
    main_part()
    PART2()
    Part3()

elif menu == 4:
    main_part()
    PART2()
    Part3()
    Part4()

else:
    print("Your option is not valid")
