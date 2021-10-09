from flask  import Flask, render_template,request
import pandas as pd
import json
from data_frame import *
app = Flask(__name__)

Dframe=Data_frame()


@app.route('/',methods=['GET','POST'])
def Index():
    if request.method=='GET':
        programas=Dframe.Get_programs()
        return render_template('index.html',programas=programas)  


@app.route('/peticion', methods=["POST"])
def nueva_ruta():
    response ={'status':200,'username':'Kevin','id':1}
    datos={}
    valores=list(request.form.values())
    keys=list(request.form.keys()) 
    for i in range(len(valores)):
        if valores[i]!='':
            datos[keys[i]]=valores[i]
    df=Dframe.Generar_tabla2(datos)
    print(df)
    return json.dumps(response)



if __name__ == "__main__":
    app.run(port=5000, debug=True )