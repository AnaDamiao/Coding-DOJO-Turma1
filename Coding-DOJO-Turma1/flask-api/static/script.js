// envia os dados para a API e exibe o resultado.

async function sortNumbers() {
    const input = document.getElementById('numbers-input').value;
    const numbersArray = input.split(',').map(num => parseFloat(num.trim())).filter(num => !isNaN(num));

    const response = await fetch('/api/sort', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ numbers: numbersArray })
    });

    const result = await response.json();
    if (response.ok) {
        document.getElementById('result').textContent = JSON.stringify(result.sorted_numbers, null, 2);
    } else {
        document.getElementById('result').textContent = result.error;
    }
}
