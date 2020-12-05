from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(_name_)

csrf = CSRFProtect(app)
 
 @app.route("/")
 def pagina_inicial():
    return "Laboratório Pipeline DevOps"                                                                                                                           

 
 if _name_ == '_main_':
     app.run(debug=True)
