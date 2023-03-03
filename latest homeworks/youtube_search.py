import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_youtube(query):
    driver = webdriver.Chrome()

    driver.get("https://www.youtube.com/results?search_query=" + query)

    wait = WebDriverWait(driver, 10)
    results_container = wait.until(EC.presence_of_element_located((By.ID, 'contents')))
    results = results_container.find_elements(By.XPATH, '//ytd-video-renderer')

    search_results = []
    for result in results:
        title = result.find_element(By.ID, 'video-title').text
        url = "https://www.youtube.com" + result.find_element(By.ID, 'video-title').get_attribute('href')
        description = result.find_element(By.ID, 'description-text').text
        search_results.append({'title': title, 'url': url, 'description': description})

    driver.quit()

    return search_results

def print_json_results(search_results):
    json_results = json.dumps(search_results)

    print(json_results)

def main():
    query = input("Enter your YouTube search query: ")

    search_results = search_youtube(query)
    print_json_results(search_results)

if __name__ == '__main__':
    main()
