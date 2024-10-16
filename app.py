import time
import pandas as pd
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def enviar(numero, mensaje, driver):
    
    url = f"https://web.whatsapp.com/send?phone={numero}&text={mensaje}"
    driver.get(url)
    time.sleep(60)
    try:
        boton_enviar = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        boton_enviar.click()
        print(f"Mensaje enviado a {numero}")
    except Exception as e:
        print(f"No se pudo enviar el mensaje a {numero}. Error: {e}")

def delay():
    return random.randint(10, 60)

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
archivo = pd.read_excel('agenda.xlsx')

for index, row in archivo.iterrows():
    numero = str(row['numero']).strip()
    mensaje = row['mensaje']
    
    enviar(numero, mensaje, driver)
    
    segundos_espera = delay()
    print(f"Esperando {segundos_espera} segundos antes de enviar el próximo mensaje...")
    time.sleep(segundos_espera)

driver.quit()
