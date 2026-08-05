if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    
    new_arr=[]
    
    for x in arr:
        if x not in new_arr:
           new_arr.append(x)
    
    arr=new_arr
    
    arr.sort()
    
    print (arr[-2])
    
        