# Write a program to remove brackets from an algebraic expression.

expression = input('enter an algebraic expression: ')
res = ""
for _ in expression:
    if _ not in  "(){}[]":
        res += _
print(f'expression after removing brackets: {res}')


# expression = input('enter an algebraic expression: ')
# res = "".join(_ for _ in expression if _ not in "(){}[]")
# print(f'expressiion after removing brackets: {res}')
