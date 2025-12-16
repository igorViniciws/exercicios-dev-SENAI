// Seleciona o botão de cálculo e adiciona um evento de clique
document.getElementById("calculate").addEventListener("click", function () {
  // Obtém os valores dos campos de entrada e converte para números decimais
  const num1 = parseFloat(document.getElementById("num1").value);
  const num2 = parseFloat(document.getElementById("num2").value);

  // Seleciona o elemento onde o resultado será exibido
  const resultElement = document.getElementById("result");

  // Bloco try: tenta executar o código
  try {
    // Verifica se os valores inseridos são números válidos (NaN (Not-a-Number))
    if (isNaN(num1) || isNaN(num2)) {
      throw new Error("Por favor, insira números válidos."); // Lança um erro personalizado
    }

    // Verifica se o segundo número é zero (divisão por zero não é permitida)
    if (num2 === 0) {
      throw new Error("Divisão por zero não é permitida."); // Lança um erro personalizado
    }

    // Calcula a divisão
    const result = num1 /num2;

    // Exibe o resultado no parágrafo
    resultElement.textContent = `Resultado: ${result}`;
  } catch (error) {
    // Bloco catch: captura e trata erros que ocorreram no bloco try
    resultElement.textContent = `Erro: ${error.message}`; // Exibe a mensagem de erro
    console.error(error); // Exibe o erro no console para debugging
  } finally {
    // Bloco finally: executado sempre, independentemente de erro
    console.log("Operação concluída."); // Mensagem de log no console
  }
});