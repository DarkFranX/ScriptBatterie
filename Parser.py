#Takes all data from result.txt and put it in a dataframe
import pandas as pd
import numpy as np
import collections

result=pd.DataFrame(np.nan, index=[], columns=['Salve','Cellule','InternalRes','Capacity'])

file=open('result.txt','r')
for num, line in enumerate(file):
    list=line.split(":")
    list[0]=str(list[0])[-1]
    list[1]=str(list[1])[8:]
    list[2]=str(list[2])[7:]
    list[3]=str(list[3])[9:-1]
    result.loc[num]=list
file.close()

#La variance représente le niveau d'écart des données avec la moyenne.
#Pour optimiser les groupes de cellules, on cherche à avoir la plus petite variance de résistance interne

final=result.groupby('Cellule')['InternalRes','Capacity'].mean()
final=final.sort_values('Capacity', ascending=False)
final['index'] = range(1, len(final) + 1)
final = final[final['index'] < 418]
