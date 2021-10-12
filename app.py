from flask import Flask, render_template

app = Flask(__name__,template_folder='template') 

@app.route('/') 
def render():
	return render_template('index.html')
	
@app.route('/productos')
def productos():
   return render_template('productos.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/registro')
def registro():
   return render_template('Registro.html')

@app.route('/eliminarp')
def deleteProduct():
   return render_template('Eliminar-producto.html')

@app.route('/Listaproductos')
def listaproductos():
   return render_template('Lista-de-productos.html')

@app.route('/Listad')
def listad():
   return render_template('Lista-de-deseos.html')

if __name__ == '__main__':
   app.run(debug=True ,port=8080) #se encarga de ejecutar el servidor 5000