import os
import time as tm
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# prepara as variaveis para enviar a mensagem 
mensagem = input('informe uma mensagem: ')  # prepara a mensagem 
pessoa = input('separe os nomes por virgulas(,)\ninforme para quem deseja enviar a mensagem')
mensagem_para= pessoa.split(',') # separa os nomes 

# configura as opções 
opicao = webdriver.ChromeOptions()

# cria uma pasta 
dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile" , "wpp") 

# salva a sessão do watzap
opicao.add_argument(f"user-data-dir={profile}") 

opicao.add_experimental_option("detach", True) 


# maximiza a tela 
opicao.add_argument("--start-maximized")

# cria um waddrive chrome com as configurações criadas 
driver = webdriver.Chrome(options = opicao)

# entra no watzapp web
driver.get('https://web.whatsapp.com')

# serve para tentar "sincronizar" o sistema , basicamente um time.sleep()
driver.implicitly_wait(15)
tm.sleep(35)

WDWait = WebDriverWait(driver, 30)

# repete o envio 
for pessoa in mensagem_para:
    # procura o perfil da pessoa que foi informada 
    perfil = WDWait.until(EC.presence_of_element_located((By.XPATH, f"//span[@title='{pessoa}']")))
    # clica no local 
    perfil.click()

    # procura a area de escrita 
    escrever_mensagem = WDWait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@aria-label, "Digite uma mensagem")]' )))
    # escreve algo 
    escrever_mensagem.send_keys(mensagem)

    # procura o botao de envio 
    enviar = WDWait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Enviar']" )))
    # clica
    enviar.click()