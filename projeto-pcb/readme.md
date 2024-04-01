# Atividade de PCB

A atividade consistiu em criar uma pcb através do software KICAD. Em minha PCB, utilizei de um transistor para permitir ou bloquear a passagem de energia para um led.

## Componentes utilizados

- 2x Connector 1x2
- 1x Raspberry Pi Pico
- 1x Transistor
- 1x Resistor de 10kΩ
- 1x Resistor de 220Ω
- 1x LED simples

## Funcionamento da PCB

O transistor se conecta com a Raspberry Pico através da GPIO16, recebendo um sinal HIGH ou LOW. Com isso, o transistor, passa através do emissor, o output de corrente ou não. Seu emisso está ligado a um conector, que também está ligado a um pino de alimentação de um led.  

## Estrutura de pastas

```bash
projeto-pcb/
├── pcb-atividade/
│   ├── pcb-atividade-backups/    (Contém backups do projeto)
│   │   ├── [Arquivos de backup do projeto]
│   ├── pcb-gbr/                  (Contém todos os arquivos Gerber necessários do projeto)
│   │   ├── [Arquivos Gerber do projeto]
│   ├── fp-info-cache/
│   ├── pcb-atividade.kicad_pcb
│   ├── pcb-atividade.kicad_prl
│   ├── pcb-atividade.kicad_pro
│   ├── pcb-atividade.kicad_sch
│   ├── pcb-atividade.kicad_pcb.lck
│   ├── pcb-atividade.kicad_sch.lck
│   └── readme.md
```

## Projeto PCB

Para facilitar, um glossário do que é cada arquivo e pasta existente no projeto.

- `pcb-atividade/`: Esta pasta contém os arquivos relacionados à atividade do PCB.

  - `pcb-atividade-backups/`: Esta pasta contém backups do projeto PCB.

  - `pcb-gbr/`: Esta pasta contém todos os arquivos Gerber necessários para a fabricação do PCB.

  - `fp-info-cache/`: Esta pasta pode conter informações de cache relacionadas aos footprints utilizados no projeto.

  - `pcb-atividade.kicad_pcb`: Arquivo principal do projeto no formato KiCad PCB, que contém o layout da placa de circuito impresso.

  - `pcb-atividade.kicad_prl`: Arquivo de regras de projeto do KiCad.

  - `pcb-atividade.kicad_pro`: Arquivo de configurações de projeto do KiCad.

  - `pcb-atividade.kicad_sch`: Arquivo principal do esquemático do projeto no formato KiCad.

  - `pcb-atividade.kicad_pcb.lck`: Arquivo de trava associado ao arquivo principal do projeto PCB do KiCad.

  - `pcb-atividade.kicad_sch.lck`: Arquivo de trava associado ao arquivo principal do esquemático do KiCad.

- `readme.md`: Este arquivo contém informações importantes sobre o projeto PCB.


