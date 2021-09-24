from tkinter import *
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Checkbox
from time import localtime

class Janela:
    def __init__(self,toplevel):
        self.frame=Frame(toplevel)
        self.frame.pack()
        self.b1=Button(self.frame)
        self.b1.bind("<Button-1>", self.press_b1)
        self.b1.bind("<ButtonRelease>", self.release_b1)
        self.b1['text'] = 'Clique em mim!'
        self.b1['width'], self.b1['bg'] = 20, 'brown'
        self.b1['fg']='yellow'
        self.b1.pack(side=LEFT)
        self.b2=Button(self.frame)
        self.b2['width'], self.b2['bg'] = 20, 'brown'
        self.b2['fg']='yellow'
        self.b2.pack(side=LEFT)
        self.b3=Button(self.frame, command=self.click_b3)
        self.b3['width'], self.b3['bg'] = 20, 'brown'
        self.b3['fg']='yellow'
        self.b3.pack(side=LEFT)
    def press_b1(self,event):
        self.b1['text']=''
        self.b2['text']='Errou! Estou aqui!'
    def release_b1(self,event):
        self.b2['text']=''
        self.b3['text']='OOOpa! Mudei de novo!'
    def click_b3(self):
        self.b3['text']='Ok... Você me pegou...'

class Horas:
    
    def __init__(self,raiz):
        self.canvas=Canvas(raiz, width=200, height=100)
        self.canvas.pack()
        self.frame=Frame(raiz)
        self.frame.pack()
        self.altura = 100 # Altura do canvas
        # Desenho do relógio-----------------------------
        pol=self.canvas.create_polygon
        ret=self.canvas.create_rectangle
        self.texto=self.canvas.create_text
        self.fonte=('BankGothic Md BT','20','bold')
        pol(10, self.altura-10,
        40, self.altura-90,
        160, self.altura-90,
        190, self.altura-10, fill='darkblue')
        pol(18, self.altura-15,
        45, self.altura-85,            
        155, self.altura-85,
        182, self.altura-15, fill='dodgerblue')
        ret(45, self.altura-35,
        90, self.altura-60, fill='darkblue', outline='')
        ret(110, self.altura-35,
        155, self.altura-60, fill='darkblue', outline='')
        self.texto(100, self.altura-50, text=':',
        font=self.fonte, fill='yellow')
        # Fim do desenho do relógio-----------------------
        self.mostrar=Button(self.frame, text='Que horas são?',
        command=self.mostra,
        font=('Comic Sans MS', '11', 'bold'),
        fg='darkblue', bg='deepskyblue')
        self.mostrar.pack(side=LEFT)
        
    def mostra(self):
        self.canvas.delete('digitos_HORA')
        self.canvas.delete('digitos_MIN')
        HORA = str(localtime()[3])
        MINUTO = str(localtime()[4])
        self.texto(67.5, self.altura-50, text=HORA, fill='yellow',
        font=self.fonte, tag='digitos_HORA')
        self.texto(132.5, self.altura-50, text=MINUTO, fill='yellow',
        font=self.fonte, tag='digitos_MIN')

class Pacman:
    def __init__(self, raiz):
        self.canvas=Canvas(raiz, height=200, width=200,
        takefocus=1, bg='deepskyblue',
        highlightthickness=0)
        self.canvas.bind('<Left>', self.esquerda)
        self.canvas.bind('<Right>', self.direita)
        self.canvas.bind('<Up>', self.cima)
        self.canvas.bind('<Down>', self.baixo)
        self.canvas.focus_force()
        self.canvas.pack()
        # Desenho da carinha----------------------------------
        self.canvas.create_oval(90, 90, 110, 110,
        tag='bola', fill='yellow')
        self.canvas.create_oval(93, 100, 98, 95,
        tag='bola', fill='blue')
        self.canvas.create_oval(102, 100, 107, 95,
        tag='bola', fill='blue')
        self.canvas.create_arc(92, 87, 108, 107, tag='bola',
        start=220, extent=100, style=ARC)
        # Fim do desenho da carinha----------------------------
    def esquerda(self, event): self.canvas.move('bola', -10, 0)
    def direita(self, event): self.canvas.move('bola', 10, 0)
    def cima(self, event): self.canvas.move('bola', 0, -10)
    def baixo(self, event): self.canvas.move('bola', 0, 10)

class Nao_Redimensiona:
    def __init__(self,janela):
        janela.resizable(width=False, height=False)
        janela.title('Não redimensiona!')
        Canvas(janela, width=200, height=100, bg='moccasin').pack()
class Tamanhos_Limite:
    def __init__(self,janela):
        janela.maxsize(width=300, height=300)
        janela.minsize(width=50, height=50)
        janela.title('Tamanhos limitados!')
        Canvas(janela, width=200, height=100, bg='moccasin').pack()

class Palheta:
    def __init__(self,raiz):
        raiz.title("Palheta")
        self.canvas=Canvas(raiz, width=200, height=200)
        self.canvas.pack()
        self.frame=Frame(raiz)
        self.frame.pack()
        self.canvas.create_oval(15, 15, 185, 185,
        fill='white', tag='bola')
        Label(self.frame,text='Vermelho: ').pack(side=LEFT)
        self.vermelho=Entry(self.frame, width=4)
        self.vermelho.focus_force()
        self.vermelho.pack(side=LEFT)
        Label(self.frame,text='Verde: ').pack(side=LEFT)
        self.verde=Entry(self.frame, width=4)
        self.verde.pack(side=LEFT)
        Label(self.frame,text='Azul: ').pack(side=LEFT)
        self.azul=Entry(self.frame, width=4)
        self.azul.pack(side=LEFT)
        Button(self.frame, text='Mostrar',
        command=self.misturar).pack(side=LEFT)
        self.rgb=Label(self.frame, text='', width=8,
        font=('Verdana','10','bold'))
        self.rgb.pack()

    def misturar(self):
        cor="#%02x%02x%02x" %(int(self.vermelho.get()),
        int(self.verde.get()),
        int(self.azul.get()))
        self.canvas.delete('bola')
        self.canvas.create_oval(15, 15, 185, 185,
        fill=cor, tag='bola')
        self.rgb['text'] = cor
        self.vermelho.focus_force()

class AutoCADE:
    def __init__(self, raiz):
        raiz.title('AutoCADÊ')
        self.canvas=Canvas(raiz, width=300, height=300,
        bg='#beff8c', cursor='hand2')
        self.canvas.bind('<1>',self.desenhar)
        self.canvas.pack()
    def desenhar(self,event):
        x_origem = self.canvas.winfo_rootx()
        y_origem = self.canvas.winfo_rooty()
        x_abs = self.canvas.winfo_pointerx()
        y_abs = self.canvas.winfo_pointery()
        try:
            P = (x_abs - x_origem, y_abs - y_origem)
            self.canvas.create_line(self.ultimo_P, P)
            self.ultimo_P = P
        except:
            self.ultimo_P=(x_abs - x_origem, y_abs - y_origem)

class Palheta2:
    def __init__(self,raiz):
        raiz.title('Palheta Gráfica')
        self.canvas=Canvas(raiz, width=200, height=200)
        self.canvas.bind('<1>', self.misturar)
        self.canvas.pack()
        bola = self.canvas.create_oval
        bola(20,180,70,130, fill='red', outline='')
        bola(75,180,125,130, fill='green', outline='')
        bola(130,180,180,130, fill='blue', outline='')
        bola(45, 120, 155, 10, fill='white',
        outline='', tag='bola')
        self.tom=[0,0,0]
    def misturar(self,event):
        xo=self.canvas.winfo_rootx()
        yo=self.canvas.winfo_rooty()
        xa=self.canvas.winfo_pointerx()
        ya=self.canvas.winfo_pointery()
        cor=self.canvas.find_closest(xa-xo, ya-yo)[0]
        self.tom[cor-1] = self.tom[cor-1]+10
        cor="#%02x%02x%02x" %(self.tom[0],
        self.tom[1],
        self.tom[2])
        self.canvas.delete('bola')
        self.canvas.create_oval(45, 120, 155, 10, fill=cor,
        outline='', tag='bola')

class Griding:
    def __init__(self,raiz):
        self.raiz = raiz
        self.raiz.title('Tchau!')
        Label(self.raiz,text='Nome:').grid(row=1, column=1,
        sticky=W, pady=3)
        Label(self.raiz,text='Senha:').grid(row=2, column=1,
        sticky=W, pady=3)
        self.msg=Label(self.raiz,text='Descubra a senha!')
        self.msg.grid(row=3, column=1, columnspan=2)
        self.nome=Entry(self.raiz, width=10)
        self.nome.grid(row=1, column=2, sticky=E+W, pady=3)
        self.nome.focus_force()
        self.senha=Entry(self.raiz, width=5, fg='darkgray',
        show='l',font=('Wingdings','10'))
        self.senha.grid(row=2,column=2, sticky=E+W, pady=3)
        self.ok=Button(self.raiz, width=8, command=self.testar, text='OK')
        self.ok.grid(row=4, column=1, padx=2, pady=3)
        self.close=Button(self.raiz, width=8, command=self.fechar, text='Fechar')
        self.close.grid(row=4, column=2, padx=2, pady=3)

    def testar(self):
        if self.nome.get()==self.senha.get()[::-1]:
            self.msg['text']='Senha correta!'
        else: 
            self.msg['text']='Senha incorreta!'

    def fechar(self): self.raiz.destroy()

class TelaPySimpleGuiExample:
  def __init__(self):
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Some text on Row 1')],
                [sg.Text('Enter something on Row 2'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print('You entered ', values[0])

    window.close()

class TelaTKInter:
  def __init__(self):
    '''
    Testes utilizando a biblioteca TkInter
    '''
    janela = Tk()

    def pegar_item(event):
      selection = event.widget.curselection()
      index = selection[0]
      value = event.widget.get(index)

    def clique_botao():
        #lsb_opcoes.
        print(lsb_opcoes.get(lsb_opcoes.index()))
        txt_opcao.insert(INSERT)
      
      # txt_opcao.insert(END, "Bye Bye.....")
      # txt_opcao.tag_add("here", "1.0", "1.4")
      # txt_opcao.tag_add("start", "1.8", "1.13")
      # txt_opcao.tag_config("here", background="yellow", foreground="blue")
      # txt_opcao.tag_config("start", background="black", foreground="green")
    janela.title('Tasker v2.0')
    janela.geometry('800x600')
    # Label
    lbl_informacao = Label(janela, text='Arraste a opção desejada para a caixa abaixo, ou digite, a opção desejada:', padx=10, pady=10)
    lbl_informacao.grid(column=1, row=0)
    lbl_informacao.bind('<<ListboxSelect>>', pegar_item)
    # List
    lsb_opcoes = Listbox(janela)
    lsb_opcoes.grid(column=1, row=2)
    lsb_opcoes.insert(1, 'linha 1')
    lsb_opcoes.insert(2, 'linha 2')
    # Botton
    btn_adicionar = Button(janela, text='Adicionar', command=clique_botao)
    btn_adicionar.grid(column=2, row=2)
    # TextBox
    txt_opcao = Text(janela, padx=10, pady=10, height=5)
    txt_opcao.grid(column=1, row=3)
    # Label
    lbl_obs = Label(janela, text='Observação:')
    lbl_obs.grid(column=0, row=4, )
    # TextBox
    txt_obs = Text(janela, padx=10, pady=10, height=1, width=2)
    txt_obs.grid(column=1, row=4)  

    janela.mainloop()

class telaPySimpleGui:
    
  def __init__(self):
    sg.change_look_and_feel('LightYellow') # LightYellow, Black
    # Layout
    leiate = [
      [sg.Text('Nome', size=(5,0)), sg.Input(size=(15,0),key='nome')],
      [sg.Text('Idade', size=(5,0)), sg.Input(size=(15,0),key='idade')],
      [sg.Text('Quais provedores de e-mail são aceitos?')],
      [sg.Checkbox('Gmail',key='gmail'), sg.Checkbox('Outlook',key='outlook'), sg.Checkbox('Yahoo',key='yahoo')],
      [sg.Text('Aceita cartão?')],
      [sg.Radio('Sim', 'cartoes', key='simcartao'), sg.Radio('Não','cartoes',key='naocartao')],
      [sg.Slider(range=(0,255),default_value=0,orientation='h',size=(15,20),key='slidervelocidade')],
      [sg.Button('Enviar Dados')],
      [sg.Output(size=(30,20))]
    ]
    # Janela
    self.janela = sg.Window('Dados do usuário').layout(leiate)

  def iniciar(self):
    while True:
      # Extrair dados na tela
      self.button, self.values = self.janela.Read()
      nome = self.values['nome']
      idade = self.values['idade']
      aceita_gmail = self.values['gmail']
      aceita_outlook = self.values['outlook']
      aceita_yahoo = self.values['yahoo']
      saceita_cartao = self.values['simcartao']
      naceita_cartao = self.values['naocartao']
      velocidade_script = self.values['slidervelocidade']
      print(f'Nome: {nome}')
      print(f'Idade: {idade}')
      print(f'Outlook? {aceita_outlook}')
      print(f'Gmail? {aceita_gmail}')
      print(f'Yahoo? {aceita_yahoo}')
      print(f'Sim, aceita cartão? {saceita_cartao}')
      print(f'Não, aceita cartão? {naceita_cartao}')
      print(f'Script? {velocidade_script}')

class TelaReddit:
    # Layout
    sg.theme('Reddit') # Procurar outros templates na documentação
    layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario', size=(30, 1))],
    [sg.Text('Senha'),sg.Input(key='senha', password_char='*', size=(31, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
    ]
    # Janela
    janela = sg.Window('Tela de Login', layout)
    # Eventos
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Entrar':
            if valores['usuario'] == 'isaias' and valores['senha'] == 'isaias':
                print('Bem-vindo!')

# tela = TelaReddit()
# tela = telaPySimpleGui()
# tela.iniciar()
# tela = TelaTKInter()
# tela = TelaPySimpleGuiExample()
# inst1=Tk()
# Griding(inst1)
# inst1.mainloop()
# inst = Tk()
# Palheta2(inst)
# inst.mainloop()
# inst = Tk()
# AutoCADE(inst)
# inst.mainloop()
# inst=Tk()
# Palheta(inst)
# inst.mainloop()
# inst1=Tk()
# inst2=Tk()
# Nao_Redimensiona(inst1)
# Tamanhos_Limite(inst2)
# inst1.mainloop()
# inst2.mainloop()
# instancia=Tk()
# Pacman(instancia)
# instancia.mainloop()
# instancia=Tk()
# Janela(instancia)
# instancia.mainloop()
# instancia=Tk()
# Horas(instancia)
# instancia.mainloop()

# Relógio analógico