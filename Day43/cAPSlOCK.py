s = input()

rule1 = s.isupper()
rule2 =  s[0].islower() and s[1:].isupper()
rule3 =  s.islower() and len(s) == 1

if rule1 or rule2 or rule3:
    print(s.swapcase())
else:
    print(s)
