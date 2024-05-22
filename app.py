import PySimpleGUI as sg
from time import sleep

sg.theme('reddit')

# layout
tela_login = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(password_char='*',key='senha')],
    [sg.Button('Enviar')],
    [sg.Output(size=(45,10))]
]

# criar janela
janela = sg.Window('Login', layout=tela_login)

# ler eventos
while True: 
    event,values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Enviar':
        usuario_digitado = values['usuario']
        senha_digitada = values['senha']
        print('passo 1... feito')
        sleep(5)
        print('passo 2... feito')
        sleep(5)
        print('passo 3... feito')