# Write a program to count total number of common subsequences. (Dynamic Programming)


string1 = input("enter the first string: ")
string2 = input("enter the second string: ")
m = len(string1)
n = len(string2)
dp = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(m + 1):
    dp[i][0] = 1
for j in range(n + 1):
    dp[0][j] = 1
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if string1[i - 1] == string2[j - 1]:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
print(f'total common subsequences = {dp[m][n]}')
