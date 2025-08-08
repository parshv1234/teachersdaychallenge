'''
Input
The first line contains a non-empty string, that contains only lowercase English letters — the user name. This string contains at most 100 letters.

Output
If it is a female by our hero's method, print "CHAT WITH HER!" (without the quotes), otherwise, print "IGNORE HIM!" (without the quotes).\
'''

usrname = input()
distinct_chars = set(usrname)
if len(distinct_chars) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")