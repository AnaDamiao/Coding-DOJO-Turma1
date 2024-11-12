# Projeto de Ordenação - Front-End, API e Back-End

Este projeto consiste em uma aplicação web integrada que permite ao usuário inserir uma lista de números, enviar para uma API e receber a lista ordenada. A implementação é composta por três partes principais: Front-End, API (Flask) e Back-End (Python). Abaixo estão descritos os requisitos e instruções para cada parte do sistema, além de informações para a integração do projeto.

Estrutura do Repositório

- /frontend: Contém o código da interface de usuário (HTML/JS) para inserir e enviar a lista de números.

- /api: Contém o código da API em Flask para comunicação entre o Front-End e o Back-End.

- /backend: Contém o código do algoritmo Selection Sort em Python para ordenar a lista.

Requisitos

# Questão 1
Front-End: Página HTML que permite inserir uma lista de números separados por vírgula e enviar para a API, além de exibir a lista ordenada recebida como resposta.

# Questão 2 
API (Flask): API que recebe uma lista de números desordenada, valida os dados e os envia para o Back-End para ordenação, retornando o resultado ao Front-End.

# Questão 3
Back-End (Python): Algoritmo de ordenação Selection Sort manual implementado em Python, que ordena a lista de números recebida e devolve o resultado para a API.

# Questão 4
Integração: Testes de comunicação entre Front-End, API e Back-End, garantindo o envio e recebimento corretos dos dados.

# **Questão 5**
Estrutura e Entrega no GitHub: Organização do repositório no GitHub com subpastas e instruções detalhadas de uso para cada componente.


# Configuração e Execução

# Pré-requisitos:
Python 3.8+
Flask para a API (pip install Flask)
Navegador para visualizar o Front-End (caso utilize apenas HTML e JS simples, sem frameworks)
Front-End:

- Navegue até a pasta /frontend.
Abra o arquivo index.html no navegador para acessar a interface.
Insira uma lista de números separados por vírgula e clique no botão para enviar.

- API (Flask):
Navegue até a pasta /api.
Instale as dependências necessárias (Flask).

- Inicie a API executando:
bash
Copiar código
python app.py
A API estará disponível no endereço http://localhost:5000.

- Back-End (Python):
Navegue até a pasta /backend.
Execute o código do algoritmo de ordenação Selection Sort.
O código do algoritmo é acionado pela API quando a lista de números é enviada pelo Front-End.
Testando a Integração
Acesse a página HTML do Front-End, insira uma lista de números e clique em “Enviar”.
O Front-End enviará a lista para a API.
A API validará a lista e a enviará para o Back-End.
O Back-End ordenará a lista usando Selection Sort e retornará o resultado para a API.
A API enviará a lista ordenada de volta para o Front-End, que exibirá o resultado.

- Observações:
  
Certifique-se de que o servidor da API esteja em execução antes de enviar dados a partir do Front-End.
Teste a integração completa do sistema antes de rodar o projeto em um ambiente de avaliação.
Use o GitHub para acompanhar o andamento da atividade e garantir que todas as frentes estejam sincronizadas.
