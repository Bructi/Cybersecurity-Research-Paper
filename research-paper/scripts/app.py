from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load trained Random Forest model
model_path = os.path.join(os.path.dirname(__file__), 'rf_ids_model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# 20 Standard Network Flow Telemetry Features
feature_names = [
    'flow_duration_ms', 'fwd_packet_count', 'bwd_packet_count',
    'fwd_header_len_bytes', 'bwd_header_len_bytes', 'flow_bytes_per_sec',
    'flow_pkts_per_sec', 'pkt_len_mean', 'pkt_len_std', 'syn_flag_count',
    'ack_flag_count', 'rst_flag_count', 'psh_flag_count', 'urg_flag_count',
    'avg_bwd_segment_size', 'init_win_bytes_fwd', 'init_win_bytes_bwd',
    'active_mean_ms', 'idle_mean_ms', 'subflow_fwd_bytes'
]

@app.route('/')
def home():
    return render_template('index.html', features=feature_names)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        raw_values = []
        for f in feature_names:
            val = request.form.get(f, '0.0')
            raw_values.append(float(val) if val.strip() != '' else 0.0)
            
        sample_vector = np.array(raw_values).reshape(1, -1)
        
        prediction = model.predict(sample_vector)[0]
        probabilities = model.predict_proba(sample_vector)[0]
        
        attack_prob = probabilities[1] * 100
        benign_prob = probabilities[0] * 100
        
        if prediction == 1:
            verdict = "MALICIOUS INTRUSION DETECTED"
            badge = "danger"
            summary = f"Confidence: {attack_prob:.2f}% (Attack Vector Identified)"
        else:
            verdict = "BENIGN NETWORK TRAFFIC"
            badge = "success"
            summary = f"Confidence: {benign_prob:.2f}% (Normal Operational Flow)"
            
        return jsonify({
            'status': 'success',
            'prediction': int(prediction),
            'verdict': verdict,
            'badge': badge,
            'summary': summary,
            'attack_prob': f"{attack_prob:.2f}%",
            'benign_prob': f"{benign_prob:.2f}%"
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    print("Serving Intrusion Detection System UI on http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=False)
