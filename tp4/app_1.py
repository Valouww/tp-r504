from flask import Flask, request, render_template
from re import *
import mysql.connector

app = Flask(__name__)
 
# MySQL configuration
db_config = {
    'host': 'tp4-sql',
    'user': 'root',
    'password': 'foo',
    'database': 'demosql',
	'port': '3306'
}

@app.route("/form")
def monForm():
	return render_template("form.html")

@app.route('/newuser',methods = ['POST', 'GET'])
def saisie():
	patt1=".{6,}"
	patt2=".*\d.*"
	patt3=".*([a-z])*.*[A-Z].*([a-z])*.*"
	patt4=".*(#|%|\{|\}|@).*" 	
	if request.method == 'POST':
		res = request.form.get( "entree" )
		if fullmatch( patt1, res ) == None:
			return "La chaîne de caractère ne contient pas 6 caractères"
		else:
			if fullmatch( patt2, res ) == None:
				return "La chaîne de caractère doit contenir au moins 1 chiffre"
			else:
				if fullmatch( patt3, res ) == None:
					return "La chaîne de caractère doit contenir au moins 1 majuscule et 1 minuscule" 
				else:
					if fullmatch( patt4, res ) == None:
						return "La chaîne de caractère doit contenir au moins 1 caractère parmi les 5 suivants : #%{}@"
					else:
						return "Le mot de passe est valide"



@app.route('/')
def index():

    # Initialize MySQL connection
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor() 
    # Sample query
    query = "SELECT * FROM myTable"
    cursor.execute(query)
    data = cursor.fetchall()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
    

