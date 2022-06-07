#importar la libreria flask
from flask import Flask, redirect, request, render_template, url_for
import pickle
app = Flask(__name__, template_folder='templates')
#importar la libreria Unittest
import unittest

datosF = []

def buscarArchivo():
    try:
        archivo = pickle.load(open("dict.pickle","rb"))
    except:
        pickle.dump(datosF, open("dict.pickle","wb"))
        
buscarArchivo()

@app.route('/')
#contenedor para llamar a index.html 
def index():
    return render_template('/index.html', datosF=datosF)
#                         ENVIAR 
@app.route('/enviar', methods =["GET", "POST"])
#contenedor para llamar a enviar.html
def enviar():
    if request.method == 'POST':
        ##numID = pickle_load.__len__()
        tituloT = request.form['titulo']
        correoT = request.form['correo']
        prioridadT = request.form['prioridad']

        datosF.append({'titulo': tituloT,'correo': correoT,'prioridad': prioridadT})
        return redirect(url_for('index'))

#Controlador para borrar
@app.route('/borrar', methods=['POST'])
#contenedor para llamar a borrar.html
def borrar():
    datosF.clear()
    fichero = open('dict.pickle', 'wb')
    pickle.dump(datosF, fichero)
    fichero.close()
    return redirect(url_for('index'))

#ejecutar
if __name__ == '__main__':
    app.run(debug=True)