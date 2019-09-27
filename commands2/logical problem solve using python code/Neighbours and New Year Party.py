def main():
    n=int(input())
    for i in range (n):
        n1=int(input())
        n1new=n1
        listnum=input()
        listnum=listnum.split()
        listnum = list(map(int, listnum))
        listnum=[ele for ele in reversed(listnum)]
        max=0
        a1=0
        a2=0
        for j in range (n1):
            if listnum[j]>max:
                a1=listnum[j]
                max=listnum[j]
                for k in range(n1):
                    if k-1 == j or k+1 == j:
                        continue
                    else:
                        if listnum[j]+listnum[k]>max:
                            max = listnum[j]+listnum[k]
                            a1=listnum[j]
                            a2 =listnum[k]
                        elif listnum[j]+listnum[k]==max:
                             if listnum[k]>a2:
                                 a1=listnum[j]
                                 a2=listnum[k]
        if a1==a2:
            print(a1)
        else:
            print(f'{a1}{a2}') 
