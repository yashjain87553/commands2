    ql=len(queries)
    al=len(arr)
    result=[]
    for k in range (ql):
        mq=[]
        a=queries[k]
        kl=al-a
        if kl==0:
        	kl=1
        for i in range (kl):
            max_t=arr[i]
            for j in range (i+1,i+a):
                if max_t<arr[j]:
                    max_t=arr[j]
            mq.append(max_t)
        min_1=mq[0]
        for p in range (1,kl):
            if min_1 > mq[p]:
                min_1=mq[p]
        result.append(min_1)
    return result