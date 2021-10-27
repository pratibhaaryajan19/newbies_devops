from collections import Counter
s1=str(input())
s2=str(input())
s3=Counter(s1)
s4=Counter(s2)
if(s3==s4):
  print("anagram")
else:
   print("not anagram")
