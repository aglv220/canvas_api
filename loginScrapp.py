#clases importadas 
import imp
from lib2to3.pgen2 import driver
from telnetlib import EC
import time
from tkinter import BROWSE
from token import OP
from traceback import print_tb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#definir opciones de ingreso a chrome
opts = Options()
opts.add_argument("Chrome/51.0.2704.103")

#definir driver de google chrome
driver = webdriver.Chrome('./chromedriver.exe',options=opts)
#ejecutar pagina semilla
driver.get('https://canvas.utp.edu.pe/login/ldap')

#definir boton de acceder con cuenta de canvas y hacer click 
buton1= driver.find_element(By.XPATH,'//div[@class="ctacanvas_main"]')
buton1.click() 

#definir credenciales 
user = "U21213625@utp.edu.pe"
#definir contraseña y leer el archivo  
password = open('password.txt').readline().strip()

#recorrer el doom y buscar el input 
input_user = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,'//input[@id="pseudonym_session_unique_id"]'))
)
input_pass = driver.find_element(By.XPATH,'//input[@id="pseudonym_session_password"]')
#ingresar credenciales de usuario y contraseña en canvas 
input_user.send_keys(user)
input_pass.send_keys(password)

#declarar el boton de login y hacer click
boton = driver.find_element(By.XPATH,'//button[@class="Button Button--login"]')
boton.click()

#acceder al menu de cursos y hacer click 
menuCurso = driver.find_element(By.XPATH,'//header[@id="header"]//button[@id="global_nav_courses_link"]')
menuCurso.click()


#repositorios = driver.find_elements(By.XPATH,'//span[@class="Grouping-styles__title"]')
repositorios = driver.find_elements(By.XPATH,'//div[@class="tray-with-space-for-global-nav"] a')

for repositorio in repositorios:
  print (repositorio.get_attribute("innerHTML"))
  
time.sleep(10)
BROWSE.close()