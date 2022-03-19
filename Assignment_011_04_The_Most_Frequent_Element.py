'''

Task : Find out the most frequent number and its frequency.

Write a program that;

Finds out the most frequent number in the given list.
Calculates its frequency.
Prints out the result such as :

Given list						Desired Output
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]			the most frequent number is 3 and it was 4 times repeated

'''

from collections import Counter
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
cnt = Counter(numbers).most_common(5)
print("List of numbers:", numbers)
print("Most frequent number and its frequency: ", cnt)
print('The most frequent number is {} and it was {} times repeated'.format(cnt[0][0], cnt[0][1]))
