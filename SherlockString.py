

def isValid(s):
    if(len(s)==1):
        return ('YES')
    else:
        dict={}
        for i in s:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        x={}
        for i in dict:
            if dict[i] in x:
                x[dict[i]]+=1
            else:
                x[dict[i]]=1
        new=list(x)
        return(new)
        max = 0
        res = new[0] 
        for i in new:
            freq=new.count(i)
            if freq > max: 
                max = freq 
                res = i
        k=0
        for i in x:
            if(i!=res):
                if(((i==res-1) or (i==res+1)) and (x[i]==1)):
                    k=1
        if((len(set(new))<3)and(k==1)):
            return('YES')
        else:
            return('NO')

if __name__ == '__main__':
    

    s = input('enter the string+\n')

    result = isValid(s)
    #isValid(s)
    print(result)
