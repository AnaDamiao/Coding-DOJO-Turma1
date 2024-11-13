# inicia a aplicação Flask, define as rotas e lidar com as requisições

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/api/sort', methods=['POST'])
def sort_api():
    data = request.get_json()
    print('Dados recebidos:', data)

    if not isinstance(data, dict) or 'numbers' not in data:
        return jsonify({'error': 'Invalid input format. Expected a JSON object with a "numbers" key.'}), 400

    numbers = data['numbers']
    if not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
        return jsonify({'error': 'Invalid data. Expected a list of numbers.'}), 400

    sorted_numbers = selection_sort(numbers)
    return jsonify({'sorted_numbers': sorted_numbers})

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == '__main__':
    app.run(debug=True)
