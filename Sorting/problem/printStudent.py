n = int(input())

array = []

for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))
    
#키를 이용하여 !점수를 기준!으로 정렬    
array = sorted(array, key=lambda student: student[1])

#정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end=' ')