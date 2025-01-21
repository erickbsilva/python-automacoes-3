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

    # 5 - Retornando a Qtd de Registros
    results = browser.find_element(By.CLASS_NAME, "sb_count").text
    print(f"Foram encontrados {results}")

    # 6 - Retornando o Número de Páginas
    qtd_results = float(
        results.split("About ")[1].split(" results")[0].replace(",", "")
    )

    numero = int(results.split("About ")[1].split(" results")[0].replace(",", ""))
    print(numero)
    # qtd_results
    # print(int(numero))
    print(f"Número de resultados formatado: {qtd_results}")
    tot_pages = qtd_results / 10
    print(f"Número de páginas {round(tot_pages)}")

    # 7 - Navegando entre páginas
    url_page = browser.find_element(
        By.XPATH, '//a[@aria-label="Page 2"]'
    ).get_attribute("href")

    current_page = 0
    start = 1
    list_results = []

    while current_page <= 10:
        if not current_page == 0:
            url_page = url_page.replace(
                "first=%s" % start,
                "first=%s" % (start + 10),
            )
            start += 10
        current_page += 1
        browser.get(url_page)

    # 8 - Recuperando informações
    divs = browser.find_elements(By.XPATH, '//li[@class="b_algo"]')
    for div in divs:
        name = div.find_element(By.TAG_NAME, "h2")
        link = div.find_element(By.TAG_NAME, "a")
        result = "%s,%s" % (name.text, link.get_attribute("href"))
        print(result)
        list_results.append(result)

except Exception as e:
    print(f"Erro encontrado: {e}")

# finally:
#     # Certifique-se de que o navegador será fechado
#     browser.quit()
