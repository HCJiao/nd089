def question_1(start_num, end_num, count_by):
    num = start_num
    break_num = num
    while num <= end_num:
        num += count_by
    break_num = num - count_by
    print(break_num)

def question_2(start_num, end_num, count_by):
    # Consider you want to count from some number `start_num` by 
    # another number `count_by` until you hit a final number `end_num`.  
    # Use the quiz below to put this idea to work. However, if someone
    # gives a `start_num` that is greater than `end_num`, you should 
    # provide the user with a print statement of "Oops!  Looks 
    # like your start value is greater than the end value.  Please try again."
    # Also set break_num to "None".

    # write a condition to check that end is larger than start before looping
    if start_num > end_num:
        print("Oops!  Looks like your start value is greater than the end value.  Please try again.")
        break_num = None
    else:        
    # write a while loop that saves break_num as the ongoing number to 
        question_1(start_num, end_num, count_by)
    # check against end_num

def question_1_udacity_solution(start_num,end_num,count_by):
    break_num = start_num
    while break_num <= end_num:
        break_num += count_by
    break_num -= count_by

    print(break_num)

question_1(0,10,2)
question_1(0,10,3)
question_1(0,10,4)
question_1(0,10,5)
question_1(5, 100, 2)
question_1_udacity_solution(5, 100, 2)
question_1(300, 548, 23)
question_1_udacity_solution(300, 548, 23)
question_2(5, 100, 2)
question_2(199, 4, 10)

