from selenium import webdriver
import time, random


class bot_enrollapp:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        print('Abrindo Webdriver')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        print('Abrindo o enrollapp')
        self.driver.get(f'http://www.enrollapp.com/login'), time.sleep(4)

    def logar(self):
        print('Logando...')
        #caixa de login / por login
        self.driver.find_element_by_xpath("//input[@name=\"user[email]\"]") \
            .send_keys(self.login)

        time.sleep(1)
        #rolando a pagina
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(1)
        #caixa de senha / por senha
        self.driver.find_element_by_xpath("//input[@name=\"user[password]\"]") \
            .send_keys(self.senha)

        #botão entrar
        self.driver.find_element_by_xpath("//input[@name=\"commit\"]") \
            .click()

    def votar(self):
        print("Direcionando para dashboard!")
        self.driver.get(f'https://enrollapp.com/dashboard'), time.sleep(3)

        while True:
            #sorteando resposta
            button_1 = '/html/body/div[1]/main/div/div/div/div/div[2]/div[2]/div/button[1]'
            button_2 = '/html/body/div[1]/main/div/div/div/div/div[2]/div[2]/div/button[2]'
            list_button = [button_1, button_2, button_1] #ir mais em sim que não
            res_sort = random.choice(list_button)
            try:
                print('Verificando pergunta...')
                #pergunta sim/não
                self.driver.find_element_by_xpath(f'{button_1}')
            except:
                print('Multiplas escolhas detectada!')
                #pergunta mutiplas opçoes
                self.driver.find_element_by_xpath(
                    f'/html/body/div[1]/main/div/div/div/div/div[2]/div[2]/form/ul/li[{random.randint(1, 3)}]/label') \
                    .click()
                print('Votando...')
                time.sleep(1)
                #comfirmar resposta
                self.driver.find_element_by_xpath(
                    '/html/body/div[1]/main/div/div/div/div/div[2]/div[2]/form/div/button')\
                    .click()
                time.sleep(1)
                # continuar
                self.driver.find_element_by_xpath(
                    '/html/body/div[1]/main/div/div/div/div/div[2]/div[2]/div/div[2]/button')\
                    .click()
                time.sleep(1)

            else:
                print('Pergunta sim/não')
                # pergunta sim/não
                self.driver.find_element_by_xpath(f'{res_sort}').click()
                print('Votou...')
                time.sleep(1)
                # continuar
                self.driver.find_element_by_xpath(
                    '/html/body/div[1]/main/div/div/div/div/div[2]/div[2]/div/div[2]/button') \
                    .click()
                time.sleep(1)

            #verificando se ganhou badget
            try:
                self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div/div[2]/div[2]/a[2]')
            except:
                print()
            else:
                print('Novo Badget :)')
                print()
                time.sleep(1)
                self.driver.find_element_by_xpath(
                    '/html/body/div[1]/main/div/div/div/div/div[2]/div[2]/a[2]').click()


bot = bot_enrollapp('email', 'senha')
bot.logar()
bot.votar()
