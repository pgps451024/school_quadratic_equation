print("사용법")
print("제곱 : ^")
print("*주의*:내림차순으로, 한 문자에 대해서 동일한 차수가 없도록(ex:3x + 2x), 가장 큰 차수의 계수는 1, 곱하는 상수는 앞에, 제곱하는 수는 뒤에 적어주세요!")
print("ex) x^3 + 2x^2 + 3x + 2 = 0")


a = input("첫 번째 식을 입력하세요 : ")
b = input("두 번째 식을 입력하세요 : ")

last_letter = 0
a_values = []
for i in range(a.count("^")):
    value = a.find("^", last_letter)
    if value != 1:
        a_values.append((int(a[value - 2]), int(a[value + 1])))
    else:
        a_values.append((1, int(a[value + 1])))
    last_letter = value + 1

if a.find("x", last_letter) != -1:
    a_values.append((int(a[a.find("x", last_letter) - 1]), 1))
    last_letter = a.find("x", last_letter) + 1

if a.find("+", last_letter) != -1:
    a_values.append((int(a[a.find("+", last_letter) + 2]), 0))

a_result_list = []
a_result = 0
for x in range(-100, 100):
    for i in a_values:
        a_result += x**i[1]*i[0]
    if a_result == int(a[-1]):
        a_result_list.append(x)
    a_result = 0
    if len(a_result_list) == int(a_values[0][1]):
        break

last_letter = 0
b_values = []
for i in range(b.count("^")):
    value = b.find("^", last_letter)
    if value != 1:
        b_values.append((int(b[value - 2]), int(b[value + 1])))
    else:
        b_values.append((1, int(b[value + 1])))
    last_letter = value + 1

if b.find("x", last_letter) != -1:
    b_values.append((int(b[b.find("x", last_letter) - 1]), 1))
    last_letter = b.find("x", last_letter) + 1

if b.find("+", last_letter) != -1:
    b_values.append((int(b[b.find("+", last_letter) + 2]), 0))

b_result_list = []
b_result = 0
for x in range(-100, 101):
    for i in b_values:
        b_result += x**i[1]*i[0]
    if b_result == int(b[-1]):
        b_result_list.append(x)
    b_result = 0
    if len(b_result_list) == int(b_values[0][1]):
        break

result_list = []
for i in a_result_list:
    if i in b_result_list:
        result_list.append(i)
print("연립 방정식의 해는 {0}입니다.".format(result_list))