import time
import os
from playwright.sync_api import sync_playwright

def run():
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # 1. Empty Dashboard
        page.goto('http://127.0.0.1:5000')
        page.screenshot(path=os.path.join(output_dir, 'ui_01_dashboard.png'), full_page=True)
        print("Captured ui_01_dashboard.png")
        
        # 2. Benign Network Traffic
        # Fill all inputs with 0 for benign
        inputs = page.locator('input[type="number"]')
        count = inputs.count()
        for i in range(count):
            inputs.nth(i).fill('0')
        
        page.click('button[type="submit"]')
        time.sleep(1) # wait for response
        page.screenshot(path=os.path.join(output_dir, 'ui_02_benign.png'), full_page=True)
        print("Captured ui_02_benign.png")
        
        # 3. Malicious Intrusion
        # Reload page
        page.goto('http://127.0.0.1:5000')
        # Fill specific anomalous values
        page.locator('input[name="syn_flag_count"]').fill('1')
        page.locator('input[name="rst_flag_count"]').fill('1')
        page.locator('input[name="flow_bytes_per_sec"]').fill('9999999')
        
        page.click('button[type="submit"]')
        time.sleep(1) # wait for response
        page.screenshot(path=os.path.join(output_dir, 'ui_03_malicious.png'), full_page=True)
        print("Captured ui_03_malicious.png")
        
        browser.close()

if __name__ == '__main__':
    run()
