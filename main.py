import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import config


def iniciar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver


def login_clear(driver):
    driver.get("https://trader.clear.com.br/home-broker")
    time.sleep(3)
    driver.find_element(By.NAME, "username").send_keys(config.USUARIO)
    driver.find_element(By.NAME, "password").send_keys(config.SENHA)
    driver.find_element(By.TAG_NAME, "form").submit()
    time.sleep(10)  # Aguarda autenticação manual (caso haja captcha)


def consultar_cotacao(driver, ativo):
    search_box = driver.find_element(By.XPATH, '//input[@placeholder="Buscar ativo"]')
    search_box.clear()
    search_box.send_keys(ativo)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)
    try:
        cotacao = driver.find_element(By.XPATH, '//span[contains(@class,"price")]').text
        print(f"Cotação atual de {ativo}: {cotacao}")
    except Exception as e:
        print(f"Não foi possível obter a cotação de {ativo}: {e}")


def main():
    driver = iniciar_driver()
    try:
        login_clear(driver)
        consultar_cotacao(driver, config.ATIVO)
        # Aqui você pode adicionar funções para enviar ordens, consultar posições, etc.
        input("Pressione Enter para sair e fechar o navegador...")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
