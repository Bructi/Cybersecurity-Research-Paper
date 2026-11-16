import time
import os
from playwright.sync_api import sync_playwright

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

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # 1. Empty Dashboard
        page.goto('http://127.0.0.1:5000')
        page.screenshot(path=os.path.join(output_dir, 'ui_01_dashboard.png'), full_page=True)
        print("Captured ui_01_dashboard.png")
        
        # 2. Benign Network Traffic
        for name, val in benign_values.items():
            page.locator(f'input[name="{name}"]').fill(val)
        
        page.click('button[type="submit"]')
        page.wait_for_selector('#resultBox.success', state='visible', timeout=5000)
        time.sleep(0.5)
        page.screenshot(path=os.path.join(output_dir, 'ui_02_benign.png'), full_page=True)
        print("Captured ui_02_benign.png")
        
        # 3. Malicious Intrusion
        page.goto('http://127.0.0.1:5000')
        for name, val in mal_values.items():
            page.locator(f'input[name="{name}"]').fill(val)
        
        page.click('button[type="submit"]')
        page.wait_for_selector('#resultBox.danger', state='visible', timeout=5000)
        time.sleep(0.5)
        page.screenshot(path=os.path.join(output_dir, 'ui_03_malicious.png'), full_page=True)
        print("Captured ui_03_malicious.png")
        
        browser.close()

if __name__ == '__main__':
    run()
