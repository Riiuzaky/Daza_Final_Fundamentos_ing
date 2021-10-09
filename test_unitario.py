#%%

from data_frame import *
import pandas as pd
import numpy as np 

dframe= Data_frame()
print(dframe)

dicc={'proyecto':'ADMINISTRACION DEPORTIVA','sexo':'M'}

datah= dframe.Generar_tabla2(dicc)

print(len(datah))
print(datah)

"""

# %%
diccionario ={'a':1,'b':2,'c':3}
for i in diccionario.values():
    print(i)

"""

# %%
