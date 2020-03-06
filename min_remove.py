arr = list(map(int,input().split()))

def solution(arr):
    answer = []
    for i in range(len(arr)) :
        answer.append(arr[i])
    answer.remove(min(answer))

    if len(answer) == 0 :
        answer.append(-1) 
    return answer 

print(solution(arr))