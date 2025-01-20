# A naive recursive Python program to find the minimum number of operations to convert str1 to str2
def editDistance(str1, str2, m, n):
    # If the first string is empty, the only option is to insert all characters of the second string into the first
    if m == 0:
        return n
    # If the second string is empty, the only option is to remove all characters of the first string
    if n == 0:
        return m
    # If the last characters of two strings are the same, ignore the last characters and get the count for the remaining strings
    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)
    # If the last characters are not the same, consider all three operations on the last character of the first string,
    # recursively compute the minimum cost for all three operations, and take the minimum of three values
    return 1 + min(editDistance(str1, str2, m, n-1),    # Insert
                   editDistance(str1, str2, m-1, n),    # Remove
                   editDistance(str1, str2, m-1, n-1))  # Replace

# Driver code
str1 = "sunday"
str2 = "saturday"
print('Edit Distance is:', editDistance(str1, str2, len(str1), len(str2)))
