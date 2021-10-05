from flask  import Flask, render_template,request
import pandas as pd
from data_frame import *
app = Flask(__name__)

Dframe=Data_frame()


@app.route('/',methods=['GET','POST'])
def Index():
    if request.method=='GET':
        return render_template('base/index.html')
    else:
        aux=request.form['sexo']
        print(str(aux))
        Dframe.Generar_tabla()
        return'<h1>metodo post</h1>'  

@app.route('/prueba')
def nueva_ruta():
    return  render_template('formulario.html')




if __name__ == "__main__":
    app.run(port=5000, debug=True )