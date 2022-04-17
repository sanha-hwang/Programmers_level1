def first(i):
    first_answer = [1,2,3,4,5]
    reminder = (i % len(first_answer))
    return first_answer[reminder]
    
    
def second(i):
    second_odd = 2
    second_even = [1,3,4,5]
    reminder = (i % (2*len(second_even)))
    if (reminder % 2) == 0:
        return second_odd
    else:
        return second_even[int(reminder // 2 )]

def third(i):
    third_answer = [3,1,2,4,5]
    reminder = (i % (2*len(third_answer)))
    reminder_ = (reminder // 2)
    return third_answer[int(reminder_)]

def solution(answers):
    counting ={'1': 0, '2':0, '3':0}   

    for i in range(len(answers)):
        if answers[i] == first(i):
            counting['1'] += 1
        
        if answers[i] == second(i):
            counting['2'] += 1
        
        if answers[i] == third(i):
            counting['3'] += 1
    answer = [int(k) for k, v in counting.items() if max(counting.values())==v]
    answer.sort()
    return answer
