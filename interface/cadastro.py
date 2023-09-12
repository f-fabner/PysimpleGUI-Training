from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
lay = [
    [sg.Text('Usuário', size=(7,0)), sg.Input(key='usuario', size=(20,1))], 
    [sg.Text('Senha', size=(7,0)), sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]
# Janela
janela = sg.Window('Tela de Login', lay)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Fernando' and valores['senha'] == '123456':
            print('Janelinha de programa on!')   

