from flask import Flask, render_template

app = Flask(__name__,template_folder='template') 

@app.route('/') 
def render():
	return render_template('index.html')
	
@app.route('/productos')
def productos():
   return render_template('productos.html')

@app.route('/login')
def micuenta():
   return render_template('login.html')

if __name__ == '__main__':
   app.run(debug=True ,port=8080) #se encarga de ejecutar el servidor 5000