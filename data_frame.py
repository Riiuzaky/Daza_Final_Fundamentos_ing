import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Data_frame:   

    def __init__(self):
        self.data_frame =pd.read_excel('data_frame.xlsx')
        self.diccionario ={'proyecto':'Programa Académico','year':'Año','sexo':'Sexo','semestre':'Semestre'}
        self.sexov={'M':'HOMBRE','F':'MUJER'}
        datas= self.data_frame.groupby(['Programa Académico'],as_index=False)['Graduados'].sum()
        self.programas = datas['Programa Académico']
             
    def Generar_tabla2(self,diccio):
        keys= list(diccio.keys())
        valores= list(diccio.values())
        columnas=[]
        consulta=None
        grafica=None
        for i in range(len(keys)) :
            aux=self.diccionario.get(keys[i])
            columnas.append(aux)

        df = self.data_frame.groupby(columnas,as_index=False).agg({
            'Graduados':'sum'
        })

        for i in range(len(columnas)):
            if columnas[i] =='Sexo':
                if i==0:
                    consulta=df[(df[columnas[i]]==self.sexov.get(valores[i]))]
                    grafica=consulta    
                else:
                    aux=consulta[(consulta[columnas[i]]==self.sexov.get(valores[i]))]
                    consulta=aux
            else:
                if valores[i].isnumeric():
                    if i==0:
                        consulta=df[(df[columnas[i]]==int(valores[i]))]
                        grafica=consulta
                    else:
                        aux=consulta[(consulta[columnas[i]]==int(valores[i]))]
                        consulta=aux
                else:
                    if i==0:
                        consulta=df[(df[columnas[i]]==(valores[i]))]
                        grafica=consulta
                    else:
                        aux=consulta[(consulta[columnas[i]]==(valores[i]))]
                        consulta=aux        
        
        return consulta,grafica       


    

    def Get_programs(self):
        return self.programas