def solution(array, commands):
    
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]

        sub_array = sorted(array[i-1:j]) # 부분 배열 정렬,
        answer.append(sub_array[k-1]) # 정렬된 부분 배열에서 k번째 수 선택하여 answer에 담기
    return answer
