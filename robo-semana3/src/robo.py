# Módulos necessários para o funcionamento do código
from serial.tools import list_ports
import inquirer
import pydobot 

# Classe criada pelo professor, para permitir a utilização de movimento de juntas
class InteliArm(pydobot.Dobot):
    def __init__(self, port=None, verbose=False):
        super().__init__(port=port, verbose=verbose)
    
    def movej_to(self, x, y, z, r, wait=True):
        super()._set_ptp_cmd(x, y, z, r, mode=pydobot.enums.PTPMode.MOVJ_XYZ, wait=wait)

    def movel_to(self, x, y, z, r, wait=True):
        super()._set_ptp_cmd(x, y, z, r, mode=pydobot.enums.PTPMode.MOVL_XYZ, wait=wait)


# Cria uma instância da classe ()
robo = InteliArm(port="COM6", verbose=False)

robo.speed(150, 150)

programa = True

while programa:
    # Cria uma pergunta para o usuário selecionar uma das respostas possíveis
    menu = inquirer.prompt([inquirer.List( 'funcionalidade',
                    message="Qual função você quer iniciar?",
                    choices=['Home', 'Ligar Ferramenta', 'Desligar Ferramenta', 'Atual', 'Mover'])])

    # Verifica a resposta selecionada pelo usuário
    match menu["funcionalidade"]:
        case "Home":
            # Move para a posição home do programa DobotLab
            robo.movej_to(240.2, 0 , 150.5, 0, wait=True)
        case "Ligar Ferramenta":
            # Ativa a função de sucção 
            robo.suck(True)
        case "Desligar Ferramenta": 
            # Desliga a função de sucção 
            robo.suck(False)
        case "Atual": 
            # Pega a posição atual do robô
            print(f"Posição atual: {robo.pose()}")    
        case "Mover":
            # Cria uma nova questão, definindo em que eixo será feita a mudança de posição
            eixo = inquirer.prompt([inquirer.List( 'eixo',
                    message="Qual eixo você deseja virar?",
                    choices=['X', 'Y', 'Z', 'R'])])
            # Para que posição
            quantidade = int(inquirer.text("Para qual posição ? "))
            posicaoAtual = robo.pose()
            # Realiza as movimentações, dependendo do eixo escolhido pelo usuário
            match eixo["eixo"]:
                case "X":
                    robo.move_to(quantidade,posicaoAtual[1],posicaoAtual[2],posicaoAtual[3])
                case "Y":
                    robo.move_to(posicaoAtual[1],quantidade,posicaoAtual[2],posicaoAtual[3])
                case "Z":
                    robo.move_to(posicaoAtual[0],posicaoAtual[1],quantidade,posicaoAtual[3])
                case "R":
                    robo.move_to(posicaoAtual[0],posicaoAtual[1],posicaoAtual[2],quantidade)
    # Permite o usuário encerrar o programa ou realizar mais comando 
    continuar = inquirer.prompt([inquirer.List( 'continuar',
                    message="Deseja continuar?",
                    choices=['Y', 'N'])])
    # Verifica a opção escolhida pelo usuário
    if continuar['continuar'] == 'Y':  programa = True
    else: programa = False 
    
# Fecha a conexão com o robô
robo.close()