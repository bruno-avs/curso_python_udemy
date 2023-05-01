from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from pathlib import Path
from time import sleep
import os

# modulo selenium fornece maneiras de se automatizar ou testas processos no
# navegador
# neste meu exemplo usarei um site que me permite testar facilmente os métodos
# e classes que o modulo oferece

# primeiro crio as opções
options = webdriver.ChromeOptions()

# defino a pasta de usuário, isso permite que eu configure coisa no navegador,
# por exemplo extensões, e elas fiquem sempre salvas em todas as execuções
ROOT_FOLDER = Path(__file__).parent
USER_DATA_PATH = ROOT_FOLDER / "perfil"
options.add_argument(f"--user-data-dir={USER_DATA_PATH}")
options.add_argument("--start-maximized")

# defino o page load strategy, que controla o comportamento de espera se o
# código será executado só depois que toda a pagina carregar ou não
options.page_load_strategy = "eager"  # no caso só espera o DOM carregar

# configurando um diretório de downloads

DOWNLOAD_PATH = os.path.join(
    os.getcwd(), "sesao_5_python_modulos", "018_selenium", "downloads"
)

prefs = {
    "profile.default_content_settings.popups": 0,
    "download.default_directory": DOWNLOAD_PATH,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
}
options.add_experimental_option("prefs", prefs)

# aqui, utilizo o ChromeDriverManager() para baixar astomaticamente a versão do
# chrome mais recente e estancio a classe de serviço que é a encarregada de
# iniciar e parar o driver
service = Service(ChromeDriverManager().install())

# aqui estancio o chrome, passando o serviço e as opções iniciais
chrome = webdriver.Chrome(service=service, options=options)

# acesso o site
chrome.get("https://jqueryui.com/draggable/")

# usando e WebDriverWait para definir esperas para selecionar objetos
wait = WebDriverWait(chrome, timeout=5, poll_frequency=0.2)
iframe = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#content > iframe")),
    "Erro ao encontrar iframe",
)
chrome.switch_to.frame(iframe)

box = chrome.find_element(By.ID, "draggable")

# crio uma instancia de ActionsChains classe que me permite lidar com
# interações de baixo nível, nesta ocasião usarei ele para mover o elemento de
# posição
action = ActionChains(chrome)
sleep(2)
action.drag_and_drop_by_offset(box, xoffset=100, yoffset=100).pause(2)
action.drag_and_drop_by_offset(box, xoffset=100, yoffset=100).perform()

# chrome.save_screenshot(os.path.join(DOWNLOAD_PATH, "screenshot.png"))

sleep(10)
