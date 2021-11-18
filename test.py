a = [13, 12, 15, 11, 9, 12, 16]

def detacted (x: list):
    answer = []
    for i in range(0, len(x), 1):
        for j in range(i+1, len(x), 1):
            if x[i] < x[j]:
                answer.append(j-i)
                break
    return answer

print(detacted(a))