# Módulos necessários para o funcionamento do código
from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from tinydb import TinyDB
from serial.tools import list_ports
import pydobot 

# Classe criada pelo professor, para permitir a utilização de movimento de juntas
class InteliArm(pydobot.Dobot):
    def __init__(self, port=None, verbose=False):
        super().__init__(port=port, verbose=verbose)
    
    def movej_to(self, x, y, z, r, wait=True):
        super()._set_ptp_cmd(x, y, z, r, mode=pydobot.enums.PTPMode.MOVJ_XYZ, wait=wait)

    def movel_to(self, x, y, z, r, wait=True):
        super()._set_ptp_cmd(x, y, z, r, mode=pydobot.enums.PTPMode.MOVL_XYZ, wait=wait)

def verifyRobotConnection():    
    try:
        available_ports = list_ports.comports() 
        port = available_ports[0].device
    except:
        port = None
    if port is not None:
        # Cria uma instância da classe ()
        robo = InteliArm(port=port, verbose=False)
    elif port is None:
        robo = None
    return robo

def position():
    return robo.pose()


robo = None
app = Flask(__name__)
db = TinyDB('db.json')
CORS(app)
verifyRobotConnection()

@app.route("/")
def index():
    if (verifyRobotConnection() is not None):
        print("teste") 
        position = position()
        return render_template("index.html")
    return render_template("index.html", coordinates = { "x":2,"y": 1,"z":3, "r":4})

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/log")
def logs():
    return render_template("logs.html")

@app.route("/verifyConnection")
def verifyConnection():
    return verifyRobotConnection()

@app.route("/move-page")
def movePage():
    if (verifyRobotConnection() is None):
        # db.insert()
        return render_template("positions.html")
    return redirect("/home")

@app.route("/move", methods=["POST"])
def move():
    verifyRobotConnection()
    x = request.form['x']
    y = request.form['y']
    z = request.form['z']
    r = request.form['r']
    current = robo.pose()
    robo.movej_to(x, y, current.z, r)
    robo.movel_to(x,y,z,r)

@app.route("/move-home")
def moveHome():
    robo.movej_to(240.2, 0 , 150.5, 0, wait=True)
    return redirect("/home")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)