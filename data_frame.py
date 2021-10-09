import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Data_frame:   

    def __init__(self):
        self.data_frame =pd.read_excel('data_frame.xlsx')
        self.diccionario ={'proyecto':'Programa Académico','year':'Año','sexo':'Sexo','semestre':'Semestre'}
        datas= self.data_frame.groupby(['Programa Académico'],as_index=False)['Graduados'].sum()
        self.programas = datas['Programa Académico']

    def Generar_tabla(self,year=0,sexo='',Proyecto='',semestre=0):        
        if year==0 and  sexo=='' and Proyecto=='' and semestre==0: 
            return "No a Seleccionado los datos, por favor escoja  datos validos"
        else:
            if Proyecto ==''and year!=0 and sexo!='' and semestre!=0:
                retorno =self.data_frame[(self.data_frame['Año']==year)&(self.data_frame['Sexo']==sexo)&(self.data_frame['Semestre']==semestre)]
                return retorno
            elif year!=0 or sexo!=''or Proyecto!=''or semestre!=0:
                
                return'Por favor rellene todos los campos ade mas del proyecto'
    """
    def Generar_tabla(diccionario):

    
    
    
    
    
    """    

    def Get_programs(self):
        return self.programas