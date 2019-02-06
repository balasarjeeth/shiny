def repeat(string,length):
cur , old = 1, string
while len(string) < length:
string += old[cur-1]
cur = (cur+1)%len(old)
return string
