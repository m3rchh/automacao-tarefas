import pyautogui
import time

pyautogui.PAUSE = 0.5

## Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
#abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(5)

#digitar o site
pyautogui.click(x=1393, y=82)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#esperar 3 segundos
time.sleep(3)

## Passo 2: Realizar login
#preencher email
pyautogui.click(x=626, y=449)
pyautogui.write("pythonimpressionador@gmail.com")

#preencher senha
pyautogui.press("tab")
pyautogui.write("123senha")

#botao logar
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3) #espera 3s


## Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv") #criar variavel para armazenar a base de dados csv que vai ser lida pelo pandas | a mesma deve estar na pasta
print(tabela) #exibe a tabela no terminal


#apesar de haver números, passamos todas as informações entre aspas duplas como strings, pois queremos escrever algo (.write) -> requer texto
## Passo 4: Cadastrar 1° produto
for linha in tabela.index: #para cada linha da minha tabela
    pyautogui.click(x=846, y=317)

#variavel = tabela. localizar informação na tabela | para tabela usa-se colchetes no formato: [linha, coluna]
    codigo = str(tabela.loc[linha, "codigo"]) 
    pyautogui.write(codigo)
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab") #passa para o botão enviar
    pyautogui.press("enter") #aperta enter no enviar
    
    pyautogui.scroll(10000) #scrolla a tela -- número positivo rola para cima | número negativo rola para baixo -- testar valores