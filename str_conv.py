with open('dataset_3363_2.txt', 'r') as f:
    s = f.readline().strip()
i = 0
while i <= len(s) - 1:
    j = i + 1
    while j < len(s) and s[j].isdigit():
       j += 1
    print(s[i] * int(s[i+1:j]), end='')
    i = j
