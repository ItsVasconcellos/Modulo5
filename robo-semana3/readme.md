# CLI - Pydobot 🤖

Construção de Interface por Linha de Comando (CLI) para Controle do Robô

## Introdução

Este projeto é uma aplicação CLI (Command Line Interface) desenvolvida em Python para controlar um robô, utilizando da biblioteca pydobot, possibilitando o uso de uma ferramenta de vácuo e movimentando o braço do robô.

## Requisitos

Para esse projeto foi utilizado venv, ou seja, um ambiente virtual. Sendo assim, para rodar o projeto é só criar a venv.


## Instalação

1. Clone o repositório para sua máquina local:

```console
git clone https://github.com/ItsVasconcellos/Modulo5
```

2. Entre na pasta do projeto 
```
cd Modulo5/robo-semana3
```

3. Para criar o ambiente virtual:

```console
python -m venv venv
```

4. Caso esteja no windows(bash), use o comando:

```console
source venv\Scripts\activate
```

5. Caso esteja no Linux/Mac 

```console
source venv/bin/activate
```

6. Para baixar as dependências, utilize o comando:

```console
pip install -r requirements.txt
```

# Funcionamento 

1. Para rodar o projeto, entre na pasta robo-semana3/src

```console
cd robo-semana3/src
```

2. Antes de inicializar o programa, é necessário encontrar a porta de comunicação entre o robô e o pc e alterar onde está escrito "COM6".

```python
InteliArm(port="COM6", verbose=False)
```

3. Finalmente para rodar o código, utilize o comando.

```console
python robo.py
```

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.

## Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato via email: seu-email@example.com.
