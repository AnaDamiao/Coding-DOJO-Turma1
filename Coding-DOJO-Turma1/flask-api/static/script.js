// envia os dados para a API e exibe o resultado.

async function sortNumbers() {
    event.preventDefault();

    const input = document.getElementById('numbers-field').value;

    const numbersArray = input.split(',').map(num => parseFloat(num.trim())).filter(num => !isNaN(num));

    try {
        const requestBody = JSON.stringify({ numbers: numbersArray });
        console.log('Corpo da requisição:', requestBody);

        const response = await fetch('http://localhost:5000/api/sort', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: requestBody
        });

        if (!response.ok) {
            console.log(new Error(`HTTP error! status: ${response.status}`));
        }

        const result = await response.json();

        document.getElementById('sortedList').textContent = JSON.stringify(result.sorted_numbers, null, 2);
    } catch (error) {
        console.error('Erro ao enviar para a API:', error);
        document.getElementById('sortedList').textContent = 'Erro ao enviar para a API.';
    }
}
