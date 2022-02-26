import sys
import re
import time 
s = sys.stdin.readline().strip()

start = time.time()
s1 = re.sub("(c=)|(c-)|(dz=)|(d-)|(lj)|(nj)|(s=)|(z=)", "1", s)
print(len(s1))
end = time.time()
print(end-start)
# #s = re.sub("[a-z]", "1", s) # length여서 바꿀 필요 없음

start = time.time()
voca =["c=","c-","dz=","d-","lj","nj","s=","z="]
for word in voca:
    s = s.replace(word, "1")
print(len(s))
end = time.time()
print(end-start)

## re.sub보다 string의 replace가 더 빠르다