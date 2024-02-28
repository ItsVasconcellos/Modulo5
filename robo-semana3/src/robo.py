# Traz a ferramenta serial para apresentar quais portas estão disponíveis
from serial.tools import list_ports
import inquirer
import pydobot 

class InteliArm(pydobot.Dobot):
    def __init__(self, port=None, verbose=False):
        super().__init__(port=port, verbose=verbose)
    
    def movej_to(self, x, y, z, r, wait=True):
        super()._set_ptp_cmd(x, y, z, r, mode=pydobot.enums.PTPMode.MOVJ_XYZ, wait=wait)

    def movel_to(self, x, y, z, r, wait=True):
        super()._set_ptp_cmd(x, y, z, r, mode=pydobot.enums.PTPMode.MOVL_XYZ, wait=wait)

# Cria uma instância do robô
robo = InteliArm(port="COM4", verbose=False)

robo.speed(150, 150)


menu = inquirer.prompt([inquirer.List( 'funcionalidade',
                message="Qual função você quer iniciar?",
                choices=['Home', 'Ligar Ferramenta', 'Desligar ferramenta', 'Atual', 'Small', 'Micro'])])

match menu["funcionalidade"]:
    case "Home":
        robo.movej_to(240.2, 0 , 150.5, 0, wait=True)
    case "Ligar Ferramenta":
        robo.suck(enable)
    case "Desligar Ferramenta": 
        robo.suction(enable)
    case "Atual": 
        # Pega a posição atual do robô
        posicao_atual = robo.pose()
        print(f"Posição atual: {posicao_atual}")    

#robo.movej_to(240.2, 0, posicao_atual[2], posicao_atual[3],wait=True)
# Fecha a conexão com o robô
robo.close()