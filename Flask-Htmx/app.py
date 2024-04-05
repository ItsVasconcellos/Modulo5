# Módulos necessários para o funcionamento do código
from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from tinydb import TinyDB
from serial.tools import list_ports
from datetime import datetime
import pydobot 

# Classe criada pelo professor, para permitir a utilização de movimento de juntas
class InteliArm(pydobot.Dobot):
    def __init__(self, port=None, verbose=False):
        super().__init__(port=port, verbose=verbose)
    
    def movej_to(self, x, y, z, r, wait=True):
        super()._set_ptp_cmd(x, y, z, r, mode=pydobot.enums.PTPMode.MOVJ_XYZ, wait=wait)

    def movel_to(self, x, y, z, r, wait=True):
        super()._set_ptp_cmd(x, y, z, r, mode=pydobot.enums.PTPMode.MOVL_XYZ, wait=wait)

robo = None
def verifyRobotConnection():    
    global robo
    try:
        available_ports = list_ports.comports() 
        port = available_ports[0].device
        robo = InteliArm(port=port, verbose=False)
        return robo
    except:
        return None


app = Flask(__name__)
db = TinyDB('db.json')
CORS(app)
verifyRobotConnection()

@app.route("/")
def index():
    verifyRobotConnection()
    if (robo is not None):
        print("teste") 
        position = robo.pose()
        return render_template("index.html")
    return render_template("index.html", coordinates = { "x":2,"y": 1,"z":3, "r":4})

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/log")
def logs():
    logs = db.all()
    return render_template("logs.html",logs = logs)

@app.route("/move-page")
def movePage():
    verifyRobotConnection()
    if (robo is not None):
        # db.insert()
        return render_template("positions.html")
    return redirect("/home")

@app.route("/move", methods=["POST"])
def move():
    verifyRobotConnection()
    x = float(request.form['x'])
    y = float(request.form['y'])
    z = float(request.form['z'])
    r = float(request.form['r'])
    current = robo.pose() 
    db.insert({'Type': 'Mover robot','Action':"Move to x = " + str(x) + "; y = " + str(y) + "; z =" + str(z) + "; r = " + str(r),'Date': datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
    robo.movej_to(x, y, current[2], r)
    robo.movel_to(x,y,z,r)

@app.route("/move-home")
def moveHome():
    db.insert({'Type': 'Move robot','Action':'Move to position Home','Date': datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
    robo.movej_to(240.2, 0 , 150.5, 0, wait=True)
    return redirect("/movepage")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)