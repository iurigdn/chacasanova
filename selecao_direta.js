// Adiciona funcionalidade para clicar diretamente nos números da cartela
document.addEventListener('DOMContentLoaded', () => {
    carregarDados();
    document.getElementById('form-participante').addEventListener('submit', adicionarParticipante);
    
    // Adiciona evento de clique para os números da cartela
    document.getElementById('cartela').addEventListener('click', (event) => {
        if (event.target.classList.contains('numero') && !event.target.classList.contains('selecionado')) {
            const numero = parseInt(event.target.textContent);
            if (confirm(`Deseja selecionar o número ${numero}?`)) {
                document.getElementById('numero').value = numero;
                // Foca no campo de nome para continuar o cadastro
                document.getElementById('nome').focus();
            }
        }
    });
});
