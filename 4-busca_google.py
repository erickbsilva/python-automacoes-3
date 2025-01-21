from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# 1 - Termo de pesquisa
term = input("Digite o que deseja pesquisar:\n")

# 2 - Iniciando o Driver
browser = webdriver.Firefox()
browser.get("https://www.bing.com")

try:
    # 3 - Encontrando o elemento de pesquisa
    elem = browser.find_element(By.XPATH, "//textarea[@type='search']")

    # 4 - Enviando termo para pesquisa
    elem.send_keys(term)
    time.sleep(5)
    elem.send_keys(Keys.ENTER)

    # 5 - Esperando os resultados carregarem
    time.sleep(2)

    # 6 - Encontrando o elemento que contém o número de resultados
    results = browser.find_element(By.CLASS_NAME, "sb_count").text
    print(f"Foram encontrados {results}")

except Exception as e:
    print("Erro encontrado:")
    print(e)

finally:
    # Certifique-se de que o navegador será fechado
    browser.quit()
