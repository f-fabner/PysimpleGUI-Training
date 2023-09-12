import PySimpleGUI as sg
#sg.theme_previewer() #serve rpa dar preview nas opções de temas disponíveis
class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBrown4')
        # Layout (colocar aqui os botões e os parâmetros que vou utilizar)
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(15,0),key='nome')],#modificando o número do primeiro size, vai modificar o espaçamento da plavra nome até a caixinha e segundo size, vai mudar o tamanho da caixinha onde se escreve os parâmetros que recebem o imput
            [sg.Text('Idade', size=(5,0)), sg.Input(size=(15,0),key='idade')],
            # abaixo temos os checkbox, radiobuttons, sliders
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook',key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],# é como se fosse perguntar quais provedores de e-mails vc aceitaria.
            #abaixo temos um check de aceitão ou não cartão ams é um ou outro
            [sg.Text('Aceita Cartão')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartao' ),sg.Radio('Não', 'cartoes', key='naoAceitaCartao')],
            [sg.Slider(range=(0,100), default_value=0, orientation='h',size=(15, 20), key='sliderVelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,10))]
        ]
        # Janela(aqui colocar o que vai aparecer na janela do programa)
        self.janela = sg.Window("Dados do Usuário").layout(layout)
        
    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            #print(self.values) #vai printar todas as coisas em um dicionário só
            #abaixo vai printar variaveis separadas em uma "lista" pra ficar mais facil de lidar com o nome da variável
            nome = self.values['nome']
            idade = self.values['idade']
            aceitagmail = self.values['gmail']
            aceitaoutlook = self.values['outlook']
            aceitayahoo = self.values['yahoo']
            aceitacartao = self.values['aceitaCartao']
            naoaceitacartao = self.values['naoAceitaCartao'] 
            velocidadescript = self.values['sliderVelocidade']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita Gmail: {aceitagmail}')
            print(f'Aceita Outlook: {aceitaoutlook}')
            print(f'Aceita Yahoo: {aceitayahoo}')
            print(f'Aceita Cartão: {aceitacartao}')
            print(f'Não Aceita Cartão: {naoaceitacartao}')
            print(f'Velocidade Scripts: {velocidadescript}')
        

tela = TelaPython()
tela.Iniciar()       