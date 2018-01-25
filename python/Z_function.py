s = "aaaabaa"

def z(s):
    n = len(s)
    ans = [0]*n
    ans[0] = 0
    l,r=0,0
    for i in range(1,n):
        if i<=r: ans[i] = min(r-i+1,ans[i-l])
        while i+ans[i]<n and s[ans[i]]==s[i+ans[i]]: ans[i]+=1
        if i+ans[i]-1>r: l = i;r = i+ans[i]-1
    return ans

a = z(s)
print(a)
