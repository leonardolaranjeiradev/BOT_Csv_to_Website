import pyautogui
import pandas
import time

pyautogui.PAUSE = 0.5

# Apertar a tecla windows
pyautogui.press('win')

# Escrever opera
pyautogui.write('opera')

# Apertar enter
pyautogui.press('enter')

# Digitar o site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')

# Apertar enter
pyautogui.press('enter')

time.sleep(3)

# Clicar no campo de loguim
pyautogui.click(x=651, y=386)

# Digitar o loguim
pyautogui.write('admin')

# Apertar tab descer no campo senha
pyautogui.press('tab')

# Digitar a senha
pyautogui.write('123456')

# Apertar tab descer no botão Logar
pyautogui.press('tab')

# Apertar enter
pyautogui.press('enter')

# Importar a tabela csv
tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:

    # Clicar no 1º campo 
    pyautogui.click(x=632, y=278)

    # codigo
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    # marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    # tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    # categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    # preco_unitario
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    # custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    # obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')

    # Apertar enter
    pyautogui.press('enter')

    # Apertar home
    pyautogui.press('home')





























