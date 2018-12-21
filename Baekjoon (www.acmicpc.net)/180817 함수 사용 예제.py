n = input()

def checking(num):
    diff_list=[]
    for i in range(len(num)-1):
        diff = int(num[i]) - int(num[i+1])
        diff_list.append(diff)
    if len(set(diff_list)) <=1:
        return(True)
    else:
        return(False)

ans=[]
for i in list(map(str, range(1, int(n)+1))):
    if checking(i) ==True:
        ans.append(i)
print(len(ans))