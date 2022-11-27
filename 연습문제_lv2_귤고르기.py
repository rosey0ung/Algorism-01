#귤 고르기

def solution(k, tangerine):
    answer = 1
    #사이즈 별 넣기
    size = [0 for _ in range(max(tangerine))]
    for i in tangerine:
        size[i-1] += 1
    #내림차순
    size.sort(reverse=True)
    #k체크
    for j in size:
        if j >= k:
            return answer
        else:
            k -= j
            answer += 1
    return answer
