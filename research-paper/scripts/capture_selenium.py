import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

def run():
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    
    benign_values = {
        'flow_duration_ms': '7.60', 'fwd_packet_count': '4.58', 'bwd_packet_count': '-4.60',
        'fwd_header_len_bytes': '2.12', 'bwd_header_len_bytes': '-0.95', 'flow_bytes_per_sec': '-1.63',
        'flow_pkts_per_sec': '0.77', 'pkt_len_mean': '3.04', 'pkt_len_std': '-0.35',
        'syn_flag_count': '0.31', 'ack_flag_count': '-6.24', 'rst_flag_count': '-0.76',
        'psh_flag_count': '-3.46', 'urg_flag_count': '2.09', 'avg_bwd_segment_size': '-6.58',
        'init_win_bytes_fwd': '4.69', 'init_win_bytes_bwd': '-0.58', 'active_mean_ms': '0.10',
        'idle_mean_ms': '-2.42', 'subflow_fwd_bytes': '0.20'
    }

    mal_values = {
        'flow_duration_ms': '-2.95', 'fwd_packet_count': '-1.02', 'bwd_packet_count': '-4.14',
        'fwd_header_len_bytes': '-8.40', 'bwd_header_len_bytes': '1.32', 'flow_bytes_per_sec': '-1.63',
        'flow_pkts_per_sec': '4.23', 'pkt_len_mean': '-4.96', 'pkt_len_std': '-1.32',
        'syn_flag_count': '-0.82', 'ack_flag_count': '0.95', 'rst_flag_count': '3.74',
        'psh_flag_count': '2.22', 'urg_flag_count': '-0.65', 'avg_bwd_segment_size': '2.10',
        'init_win_bytes_fwd': '1.70', 'init_win_bytes_bwd': '1.42', 'active_mean_ms': '-0.23',
        'idle_mean_ms': '-5.25', 'subflow_fwd_bytes': '2.51'
    }

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1280,900')
    
    driver = webdriver.Edge(options=options)
    
    try:
        # 1. Empty Dashboard
        driver.get('http://127.0.0.1:5000')
        time.sleep(1)
        driver.save_screenshot(os.path.join(output_dir, 'ui_01_dashboard.png'))
        print("Captured ui_01_dashboard.png")
        
        # 2. Benign Network Traffic
        for name, val in benign_values.items():
            elem = driver.find_element(By.NAME, name)
            elem.clear()
            elem.send_keys(val)
            
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(1.5)
        driver.save_screenshot(os.path.join(output_dir, 'ui_02_benign.png'))
        print("Captured ui_02_benign.png")
        
        # 3. Malicious Intrusion
        driver.get('http://127.0.0.1:5000')
        time.sleep(1)
        for name, val in mal_values.items():
            elem = driver.find_element(By.NAME, name)
            elem.clear()
            elem.send_keys(val)
        
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(1.5)
        driver.save_screenshot(os.path.join(output_dir, 'ui_03_malicious.png'))
        print("Captured ui_03_malicious.png")
        
    finally:
        driver.quit()

if __name__ == '__main__':
    run()
