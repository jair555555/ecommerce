from flask import Flask, render_template
app = Flask(__name__,template_folder='template') 

@app.route('/') 
def render():
	return render_template('index.html')
	
@app.route('/productos')
def productos():
   return render_template('productos.html')

@app.route('/micuenta')
def productos():
   return render_template('productos.html')



app.run() #se encarga de ejecutar el servidor 5000