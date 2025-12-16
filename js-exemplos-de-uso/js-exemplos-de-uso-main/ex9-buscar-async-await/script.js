// Seleciona o botão de busca e adiciona um evento de clique
document.getElementById("fetchUser").addEventListener("click", async function () {
  // Seleciona o elemento onde os dados do usuário serão exibidos
  const userDataElement = document.getElementById("userData");

  // Bloco try: tenta executar o código assíncrono
  try {

    // Async e await são usados em JavaScript para simplificar o trabalho com código assíncrono.

    // No exemplo:
    // async define funções como assíncronas, permitindo o uso de await.
    // await pausa a execução até que a operação assíncrona (como fetch) seja concluída e retorna o resultado.
    
    // Juntos, tornam o código mais legível, eliminando a necessidade de cadeias complexas de .then() e .catch().

    // Faz a requisição à API usando fetch e espera a resposta (await)
    const response = await fetch('https://jsonplaceholder.typicode.com/users/5');
    // const response = await fetch('https://invalidurl.example.com');

    // Verifica se a resposta da API foi bem-sucedida (status 200-299)

    if(!response.ok) {
      throw new Error("Erro ao buscar dados do usuário.");
    }

    // Converte a resposta para JSON e espera o resultado (await)
    const user = await response.json();

    // Exibe os dados do usuário na página
    userDataElement.innerHTML = `
    <h2>Dados do usuário:</h2>
    <p><strong>Nome:</strong>${user.name}</p>
    <p><strong>Email:</strong>${user.email}</p>
    <p><strong>Telefone:</strong>${user.phone}</p>

    `;

  } catch (error) {
    // Bloco catch: captura e trata erros que ocorreram no bloco try
    userDataElement.innerHTML = `<p style="color: red;">Erro: ${error.message}</p>`; // Exibe a mensagem de erro
    console.error(error); // Exibe o erro no console para debugging
  }
});