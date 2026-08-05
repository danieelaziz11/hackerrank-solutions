list=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    list.append([name,score])

scores=[]
for name , score in list :
    if score not in scores :
        scores.append(score)
    
scores.sort()

names= []

for name , score in list :
    if score==scores[1]:
        names.append(name)
    
names.sort()   
 
for name in names :
    print(name)
    
 
