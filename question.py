import pandas as pd
import numpy as np
df = pd.read_csv("..\Question_Papers.csv")
quest=df.iloc[:,:-1]
objt=quest.iloc[:,2:]
ans=df.iloc[:,-1]
objt=np.array(objt)
quest=np.array(quest)
ans=np.array(ans)
#print(quest)
#print(ans)
#print(objt)
print(objt.shape)
z=0
flag=0
for x in df.Question_Number:
    print(z+1," ",df.Question_Text[z])
    for w in range(0,4):
        print("option ",w+1," ",objt[z][w])
    for y in range(0,4):
                    
        if objt[z][y]== ans[z]:
            
            flag=1
            break
        else:
            continue
    if flag==1:
        print("correct answer is Option ",y+1)
        print(ans[z])
        flag=0
        z=z+1
    else:
        print("correct answer is  ")
        print(ans[z])
        print('Answer not in given option')
        z=z+1
    
