from sympy import *

x = symbols('x')

a = input("첫 번째 식을 입력하세요 : ")
b = input("두 번째 식을 입력하세요 : ")

equation_a = Eq(parse_expr(a[:-4]), int(a[-1]))
equation_b = Eq(parse_expr(b[:-4]), int(b[-1]))

solutions_a = solve(equation_a, x)
solutions_b = solve(equation_b, x)

result_list = []
for i in solutions_a:
    if i in solutions_b:
        result_list.append(i)
print("연립 방정식의 해 : {0}".format(result_list))