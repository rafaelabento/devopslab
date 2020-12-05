from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps" from flask import Flask
  2 from flask_wtf.csrf import CSRFProtect
  3 
  4 app = Flask(__name__)
  5 
  6 csrf = CSRFProtect(app)
  7 
  8 @app.route("/")
  9 def pagina_inicial():
 10     return "Laboratório Pipeline DevOps"                                                                                          
 11 
 12 if __name__ == '__main__':
 13     app.run(debug=True)                                                                                                                 
        
if __name__ == '__main__':
    app.run(debug=True)
