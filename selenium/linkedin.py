import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pdb

def use_Selenium_web_scraping():
    """A function to demonstrate basic Selenium operations with Chrome WebDriver."""
    # Palabras clave para búsqueda
    # KEYWORDS = ["SDET", "Firmware", "Test"]
    # LOCATION = "Netherlands"
    DAYS_POSTED = 10
    JOB_TYPE = "F"  # 'F' para tiempo completo
    PAGES_TO_CHECK = 5

    # Solicita credenciales
    # username = input("LinkedIn usuario: ")
    # password = input("LinkedIn contraseña: ")
    username = "gamezgonzalez@hotmail.com"
    password = "1qazzaq1$1"

    # Constantes para selectores y campos
    SELECTOR_JOB_CARD = "li.jobs-search-results__list-item"
    SELECTOR_TITLE = "a.job-search-card__title"
    SELECTOR_COMPANY = "a.job-search-card__subtitle-primary"
    SELECTOR_LOCATION = "span.job-search-card__location"
    FIELD_KEYWORD = ["SDET", "Firmware", "Test"]
    FIELD_TITLE = "Título"
    FIELD_COMPANY = "Empresa"
    FIELD_LOCATION = "Netherlands"
    FIELD_LINK = "Enlace"
    CSV_FILE = "linkedin_jobs.csv"

    # Inicializa el navegador
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    # Inicia sesión en LinkedIn
    driver.get("https://www.linkedin.com/login")
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
    time.sleep(3)

    results = []

    # Construye la URL de búsqueda con la frase completa
    SEARCH_PHRASE = "SDET Firmware Test"
    GEO_ID = "102890719"  # Netherlands
    search_url = (
        f"https://www.linkedin.com/jobs/search/?keywords={SEARCH_PHRASE}"
        f"&geoId={GEO_ID}"
        f"&f_JT={JOB_TYPE}"
        f"&distance=25"
        f"&origin=JOBS_HOME_KEYWORD_HISTORY"
        f"&refresh=true"
    )
    driver.get(search_url)
    time.sleep(3)
    
    for page in range(PAGES_TO_CHECK):
        # Imprime el HTML de la página de resultados para depuración
        print("\n--- HTML de la página de resultados ---\n")
        print(driver.page_source)
        print("\n--- Fin del HTML ---\n")
        # Extracción de empleos
        job_cards = driver.find_elements(By.CSS_SELECTOR, SELECTOR_JOB_CARD)
        #pdb.set_trace()  # Set a breakpoint here to inspect the state
        for job in job_cards:
            try:
                title = job.find_element(By.CSS_SELECTOR, SELECTOR_TITLE).text
                company = job.find_element(By.CSS_SELECTOR, SELECTOR_COMPANY).text
                location = job.find_element(By.CSS_SELECTOR, SELECTOR_LOCATION).text
                link = job.find_element(By.CSS_SELECTOR, SELECTOR_TITLE).get_attribute("href")
                results.append({
                    FIELD_TITLE: title,
                    FIELD_COMPANY: company,
                    FIELD_LOCATION: location,
                    FIELD_LINK: link
                })
                # Mensaje limpio y claro en consola
                print(f"Empresa: {company} | Título: {title} | Ubicación: {location} | Enlace: {link}")
            except Exception:
                continue

    # --- Guardado en archivo CSV comentado ---
    # if os.path.exists(CSV_FILE) and os.path.getsize(CSV_FILE) > 0:
    #     try:
    #         df_old = pd.read_csv(CSV_FILE)
    #     except pd.errors.EmptyDataError:
    #         df_old = pd.DataFrame()
    #     df_new = pd.DataFrame(results)
    #     df_final = pd.concat([df_old, df_new], ignore_index=True).drop_duplicates()
    # else:
    #     df_final = pd.DataFrame(results)
    # df_final.to_csv(CSV_FILE, index=False)
    # print(f"Se guardaron {len(df_final)} empleos en {CSV_FILE}")
    driver.quit()

def use_LinkedIn_APP():
    """
    Simula la comunicación con la app de LinkedIn usando Selenium.
    Busca empleos con la frase 'SDET Firmware Test' y muestra las empresas en consola.
    """
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # Parámetros de búsqueda
    SEARCH_PHRASE = "SDET Firmware Test"
    GEO_ID = "102890719"  # Netherlands
    JOB_TYPE = "F"
    username = "gamezgonzalez@hotmail.com"
    password = "1qazzaq1$1"

    # Selectores
    #SELECTOR_JOB_SEARCH = "jobs-search-results-list__title-heading"
    SELECTOR_JOB_CARD = "div.job-card-container"
    SELECTOR_TITLE = "a.job-card-container__link"
    SELECTOR_COMPANY = "div.artdeco-entity-lockup__subtitle span"
    SELECTOR_LOCATION = "ul.job-card-container__metadata-wrapper > li > span"

    # Inicializa el navegador
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    # Inicia sesión en LinkedIn
    driver.get("https://www.linkedin.com/login")
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
    time.sleep(3)

    # Construye la URL de búsqueda
    search_url = (
        f"https://www.linkedin.com/jobs/search/?keywords={SEARCH_PHRASE}"
        f"&geoId={GEO_ID}"
        f"&f_JT={JOB_TYPE}"
        f"&distance=25"
        f"&origin=JOBS_HOME_KEYWORD_HISTORY"
        f"&refresh=true"
    )
    driver.get(search_url)
    time.sleep(3)
    with open("linkedin_jobs.txt", "w", encoding="utf-8") as file:
        file.write(driver.page_source)
        
    # Extrae los empleos de la primera página
    job_cards = driver.find_elements(By.CSS_SELECTOR, SELECTOR_JOB_CARD)
    empresas = set()
    for job in job_cards:
        try:
            company = job.find_element(By.CSS_SELECTOR, SELECTOR_COMPANY).text
            title = job.find_element(By.CSS_SELECTOR, SELECTOR_TITLE).text
            location = job.find_element(By.CSS_SELECTOR, SELECTOR_LOCATION).text
            empresas.add(company)
            print(f"Empresa: {company} | Título: {title} | Ubicación: {location}")
        except Exception:
            continue
    print(f"\nEmpresas que ofertan trabajo como {SEARCH_PHRASE}:")
    for empresa in empresas:
        print(f"- {empresa}")
    driver.quit()

if __name__ == '__main__':
    #use_Selenium_web_scraping()
    use_LinkedIn_APP()
