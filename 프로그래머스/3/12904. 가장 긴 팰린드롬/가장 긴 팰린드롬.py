def solution(s):
    answer = 1 # 팰린드롬이 안되면 최소값 1

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                answer = max(answer, len(s[i:j]))
        

    return answer