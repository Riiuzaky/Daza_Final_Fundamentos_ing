from data_frame import *
import pandas as pd
import numpy as np 

dframe= Data_frame()

def test_leer_dataframe():
   assert type(dframe) is not type(None)

def test_cantidad_programas():
    assert len(dframe.Get_programs())==41

def test_generar_consulta():
    dicc={'proyecto':'ADMINISTRACION DEPORTIVA','sexo':'M'}
    datah= dframe.Generar_tabla2(dicc)
    assert type(datah) is not type(None)
    





