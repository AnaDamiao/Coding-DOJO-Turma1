# inicia a aplicação Flask, define as rotas e lidar com as requisições

from flask import Flask, request, jsonify, render_template
from sort_service import sort_numbers

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./templates/index.html')

@app.route('/api/sort', methods=['POST'])
def sort_api():
    data = request.get_json()

    if not isinstance(data, dict) or 'numbers' not in data:
        return jsonify({'error': 'Invalid input format. Expected a JSON object with a "numbers" key.'}), 400
    
    numbers = data['numbers']
    if not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
       return jsonify({'error': 'Invalid data. Expected a list of numbers.'}), 400

    sorted_numbers = sort_numbers(numbers)
    return jsonify({'sorted_numbers': sorted_numbers})

if __name__ == '__main__':
    app.run(debug=True)
