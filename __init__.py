import time

import pyautogui
from numpy.ma.core import logical_not

#pyautogui.press() -> aperta 1 tecla
#pyautogui.click() -> clica em algo
#pyautogui.write() -> escreve um texto
#pyautogui.hotkey() -> acionar um comando (ctrl+shift, por exp)

#PASSO 1: Entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login

 #Abrir navegador (chrome)
 #Digitar o site (link)

pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('Opera')
pyautogui.press('enter')

#É preciso delay entre códigos em algumas situações
#Pode ser com time.sleep ou com o pyautogui.PAUSE = 'tempo que quero

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

#Para que eu tenha certeza que o site está aberto quando for executar o passo 2, eu seto um delay

time.sleep(3)

#PASSO 2: Fazer login
#Para saber onde seu mouse está na tela (x,y), é preciso utilizar uma função do pyautogui, chamada position

#Agora, veja qual a posição quando o mouse está na área do email e a utilize no click

pyautogui.click(882, 451)

#Login
pyautogui.write('pedrokhpms@gmail.com')
pyautogui.click(802, 580)

#Ou use o TAB: pyautogui.press('tab')

#Senha (Aqui também podemos usar o click Ou usar o tab)
pyautogui.write('Henriquinho00.')
pyautogui.press('enter')

#Delay para abertura do site
time.sleep(3)

#PASSO 3: Importar a base de dados (informações que cadastraremos no site - produtos)
import pandas
tabela = pandas.read_csv('produtos.csv')

#PASSO 4: Cadastrar 1 produto
for linha in tabela.index: #Para cada linha da tabela
    pyautogui.click(893, 308)
    #Tenho que abrir banco de dados, copiar primeira info, colar no write, e escrever no site
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan': #Quando o valor de tabela.loc for vazio, o pandas seta como 'nan'
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.scroll(1000)
    #Número positivos dão scroll para cima (negativos, para baixo)
    #Para voltar para cima é preciso dar um pyautogui.scroll

#PASSO 5: Repetir para todos os produtos


