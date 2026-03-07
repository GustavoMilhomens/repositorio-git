from appium import webdriver
from appium.options.common import AppiumOptions

# Passo 1: Configurar as "Desired Capabilities"
# Isso é como você diz ao Appium Server que tipo de dispositivo e app você quer testar
options = AppiumOptions()
options.set_capability("platformName", "Android") # ou "iOS"
options.set_capability("appium:platformVersion", "15 AP3A.240905.015.A2")
options.set_capability("appium:deviceName", "POCO C65")

# Passo 2: Conectar ao Appium Server
# O servidor do Appium geralmente roda em http://127.0.0.1:4723
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

# Passo 3: Executar a ação desejada
# Esta é a linha que você pediu!
print("Voltando para a tela inicial...")
driver.press_keycode(3)

# Passo 4: Fechar a sessão do driver
# É sempre uma boa prática finalizar a sessão de teste
driver.quit()

print("Teste finalizado.")