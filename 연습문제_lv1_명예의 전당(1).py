#명예의 전당(1)

def solution(k, score):
    answer = []
    rank = [2000 for _ in range(k)]
    n = 0
    for i in score:
        if n < k:
            rank[n] = i
            n += 1
        elif min(rank) < i:
            rank.sort(reverse=True)
            rank[k-1] = i
#        print(rank)
        answer.append(min(rank))
    return answer


def solution(k, score):
    answer = []
    rank = []
    n = 0
    for i in score:
        if n < k:
            rank.append(i)
            n += 1
        elif min(rank) < i:
            rank[k-1] = i
        rank.sort(reverse=True)
#        print(rank, i)
        answer.append(min(rank))
    return answer


#다른 사람 풀이 참고
def solution(k, score):
    answer = []
    rank = []
    
    for i in score:
        rank.append(i)
        if len(rank) > k:
            rank.remove(min(rank))
        answer.append(min(rank))
    return answer
