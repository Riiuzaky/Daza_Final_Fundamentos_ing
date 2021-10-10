from flask  import Flask, render_template,request
import matplotlib.pyplot as plt
import json
import io
import base64
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
    response ={}
    datos={}
    valores=list(request.form.values())
    keys=list(request.form.keys()) 
    for i in range(len(valores)):
        if valores[i]!='':
            datos[keys[i]]=valores[i]
    df,grafica=Dframe.Generar_tabla2(datos)
    response['tabla']=df.to_html(classes='data', header=True, index=False)
    response['grafica']=grafica.to_json()
    return json.dumps(response)



if __name__ == "__main__":
    app.run(port=5000, debug=True )