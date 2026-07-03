# Write a program to count common subsequence in two strings. (longest common subsequence)
# [length of LCS]
# The Longest Common Subsequence is the longest sequence of characters that 
# appears in both strings in the same order, but not necessarily consecutively.

string1 = input('enter the first string: ')
string2 = input('enter the second string: ')
m = len(string1)
n = len(string2)
dp = [[0] * (n+1) for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        if string1[i-1] == string2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(f'length of longest common subsequence = {dp[m][n]}')
