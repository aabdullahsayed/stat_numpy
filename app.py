from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__, static_folder='static')


@app.route('/analyze', methods=['POST'])
def analyze_numbers():
    try:
        data = request.get_json()
        numbers = np.array(data['numbers'], dtype=float)
        
        analysis = {
            'mean': float(np.mean(numbers)),
            'median': float(np.median(numbers)),
            'std_dev': float(np.std(numbers)),
            'min': float(np.min(numbers)),
            'max': float(np.max(numbers)),
            'percentiles': [float(np.percentile(numbers, p)) for p in [25, 50, 75]]
        }
        
        return jsonify(analysis)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/')
def home():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
