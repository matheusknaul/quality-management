function showActiveContent() {
    // Seleciona os containers corretamente
    const contentContainers = document.querySelectorAll('#content-normas, #content-fornecedores, #content-analise-critica');

    // Esconde todos os containers
    contentContainers.forEach(container => {
        container.style.display = 'none'; // Esconde todos os containers
    });

    // Exibe apenas o container com a classe 'activate'
    const activeContent = document.querySelector('.activate');
    if (activeContent) {
        activeContent.style.display = 'block'; // Exibe o container ativado
    }
}

// Função para ativar o container correto e desativar os outros
function toggleActive(containerId) {
    // Remove a classe 'activate' de todos os containers
    const contentContainers = document.querySelectorAll('#content-normas, #content-fornecedores, #content-analise-critica');
    contentContainers.forEach(container => {
        container.classList.remove('activate'); // Remove a classe 'activate' de todos
    });

    // Adiciona a classe 'activate' ao container clicado
    document.getElementById(containerId).classList.add('activate');

    // Chama a função para atualizar a exibição dos containers
    showActiveContent();
}

// Adiciona o evento de clique ao link de "Normas"
document.getElementById('normas-link').addEventListener('click', function(event) {
    event.preventDefault();
    toggleActive('content-normas'); // Ativa o conteúdo de Normas
});

// Adiciona o evento de clique ao link de "Fornecedores"
document.getElementById('fornecedores-link').addEventListener('click', function(event) {
    event.preventDefault();
    toggleActive('content-fornecedores'); // Ativa o conteúdo de Fornecedores
});

// Adiciona o evento de clique ao link de "Análise Crítica"
document.getElementById('analys-link').addEventListener('click', function(event) {
    event.preventDefault();
    toggleActive('content-analise-critica'); // Ativa o conteúdo de Análise Crítica
});

// Chama a função no início para garantir que o conteúdo certo apareça
showActiveContent();
