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
        return render_template('base/index.html',programas=programas)
    else:
        Dframe.Generar_tabla()
        return'<h1>metodo post</h1>'  


@app.route('/peticion', methods=["POST"])
def nueva_ruta():
    response ={'status':200,'username':'Kevin','id':1}
    datos={}
    valores=list(request.form.values())
    keys=list(request.form.keys()) 
    for i in range(len(valores)):
        if valores[i]!='':
            datos[keys[i]]=valores[i]
    print(datos)
    return json.dumps(response)



if __name__ == "__main__":
    app.run(port=5000, debug=True )