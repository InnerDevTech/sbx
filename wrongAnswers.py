def getWrongAnswers(N, C):
    wrong_answers  = ""
    for i in range(N):
        if C[i] == "A":
            wrong_answers += "B"
        else:
            wrong_answers += "A"
    return wrong_answers

N = 7
C = "ABAAABB"
print(getWrongAnswers(N, C))