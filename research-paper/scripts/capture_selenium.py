import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

def run():
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    
    driver = webdriver.Edge(options=options)
    
    try:
        # 1. Empty Dashboard
        driver.get('http://127.0.0.1:5000')
        time.sleep(1)
        driver.save_screenshot(os.path.join(output_dir, 'ui_01_dashboard.png'))
        print("Captured ui_01_dashboard.png")
        
        # 2. Benign Network Traffic
        inputs = driver.find_elements(By.CSS_SELECTOR, 'input[type="number"]')
        for inp in inputs:
            inp.send_keys('0')
            
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(1)
        driver.save_screenshot(os.path.join(output_dir, 'ui_02_benign.png'))
        print("Captured ui_02_benign.png")
        
        # 3. Malicious Intrusion
        driver.get('http://127.0.0.1:5000')
        time.sleep(1)
        driver.find_element(By.NAME, 'syn_flag_count').send_keys('1')
        driver.find_element(By.NAME, 'rst_flag_count').send_keys('1')
        driver.find_element(By.NAME, 'flow_bytes_per_sec').send_keys('9999999')
        
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(1)
        driver.save_screenshot(os.path.join(output_dir, 'ui_03_malicious.png'))
        print("Captured ui_03_malicious.png")
        
    finally:
        driver.quit()

if __name__ == '__main__':
    run()
