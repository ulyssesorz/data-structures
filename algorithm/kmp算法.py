def getnext(p):
    j = 0
    k = -1
    next = [-1]
    for i in range(len(p) - 1):
        next.append(0)
    while j < len(p) - 1:
        if k == -1 or p[j] == p[k]:
            j += 1             #重复了此前的字符串，则向后移动，且把重复的长度k赋给next
            k += 1
            next[j] = k
        else:
            k = next[k]        #映射
    return next


def kmp(s, t):
    slen = len(s)
    tlen = len(t)
    if slen >= tlen:
        i = 0
        j = 0
        next = getnext(t)

        while i < slen:
            if j==-1 or s[i]==t[j]:
                i+=1
                j+=1
            else:
                j=next[j]            #j将后移next[j]位
            if j==tlen:
                return i-tlen
    return -1

s1="abawrabcdeabd"
s2="abc"
print(getnext(s2))
print(kmp(s1,s2))