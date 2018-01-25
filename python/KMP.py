
def build_table(pat):
    table = [0]*len(pat)
    p = 0
    for i in range(1,len(pat)):
        while p>0 and pat[p]!=pat[i]:
            p = table[p-1]

        if pat[p]==pat[i]:
            table[i] = p+1
            p+=1

    return table

def search(string,pat):
    ftable = build_table(pat)
    p = 0
    for i in range(len(string)):
        while p>0 and string[i]!=pat[p]:
            p = ftable[p-1]

        if string[i]==pat[p]:
            p+=1
            if p==len(pat):
                print("Match:",i-len(pat)+1)
                p=0
    

s = "ABC ABCDAB ABCDABCDABDE"
p="ABCDA"
search(s,p)

