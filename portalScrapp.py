#clases importadas 
import imp
from lib2to3.pgen2 import driver
from telnetlib import EC
from token import OP
from traceback import print_tb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#definir opciones de ingreso a chrome
opts = Options()
opts.add_argument("user-agent=Chrome/51.0.2704.103")

#definir driver de google chrome
driver = webdriver.Chrome('./chromedriver.exe',options=opts)
#ejecutar pagina semilla
driver.get('https://portalestudiante03.utp.edu.pe/')

#definir credenciales user y password
user = "U17200379@utp.edu.pe"
#definir contraseña y leer el archivo  
password = open('password.txt').readline().strip()

#recorrer el doom y buscar el input
input_user = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,'//input[@id="tcActDir"]'))
)
input_pass = driver.find_element(By.XPATH,'//input[@id="tcActPas"]')
#ingresar credenciales de usuario y contraseña en canvas 
input_user.send_keys(user)
input_pass.send_keys(password)

#definir boton de captcha

capchat = FindElementByXPath("//iframe[contains(@src, 'recaptcha') and not(@title='recaptcha challenge')]", timeout:=10000)
capchat.FindElementByCss("div.recaptcha-checkbox-checkmark").click()




