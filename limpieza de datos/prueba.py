#%%
from numpy.core.function_base import _linspace_dispatcher
import pandas as pd
data = pd.read_excel('data_frame.xlsx')

df7 =data.groupby(['Programa Académico'],as_index=False).agg({
    "Código de la Institución":"max"
}) 

programasn =df7['Programa Académico']

posiciones=[]
print(len(data))

for i in programasn:
    for j in range(1,19):
        año=2000+j
        for h in ['HOMBRE','MUJER']:
            for g in [1,2]:
                if len(data[(data['Programa Académico']==i)&(data['Año']==año)&(data['Sexo']==h)&(data['Semestre']==g)].sort_values('Graduados',ascending=False))>=2:
                  aux2=data[(data['Programa Académico']==i)&(data['Año']==año)&(data['Sexo']==h)&(data['Semestre']==g)].sort_values('Graduados',ascending=False).index.tolist()
                  posiciones.append(aux2)

eliminar =[]
for i  in posiciones:
    for j in range(1,len(i)):
        eliminar.append(i[j])
eliminar.sort()

data_n=data.drop(eliminar,axis=0)

print(len(data_n))

#data_n.to_excel('data_frame.xlsx')

# %%
