def solution(participant, completion):
    
    participant_table = dict()
    completion_table = dict()
    answer = ""
    
    for person in participant:
        ## 해쉬 키에 매칭되는 참가자를 리스트로 담음, 동명이인 수 만큼 value 리스트에 담길 예정
        if person not in participant_table.keys():
            participant_table[person] = [person]
        else:
            participant_table[person].append(person)
    
    for person in completion:

        ## 해쉬 키에 매칭되는 완주자를 리스트로 담음, 동명이인 수 만큼 value 리스트에 담길 예정
        if person not in completion_table.keys():
            completion_table[person] = [person]
        else:
            completion_table[person].append(person)
    
      
    for key, value in participant_table.items():
        # 이름을 활용하여 참가자 value list와 완주자 value list가 다르면 동명이인이 완주하고 안하고가 갈리기 때문에 리스트 길이가 다르다고 판단
        try:
            if participant_table[key] != completion_table[key]:
                answer = completion_table[key][0]
        except:
            answer = key # 참가자의 key로 검색을 하므로 완주자에게는 key가 없을 경우 예외발생 = 참가는 했으나 완주를 하지 못한 경우( 동명이인이 아닌 경우)
            
    return answer
