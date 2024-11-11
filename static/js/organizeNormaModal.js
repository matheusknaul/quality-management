document.addEventListener("DOMContentLoaded", () => {
    const devInfoContainer = document.getElementById('exibir-norma-devinfo');

    // Seleciona o modal e define o evento para executar o script quando o modal for aberto
    const modal = document.getElementById('exampleModal');
    modal.addEventListener('shown.bs.modal', () => {
        const devInfo = document.querySelectorAll('div.dev-info');
        // if(devInfo.length > 1){
        //     devInfo.shift();
        // }
        console.log(devInfo)

        // Limpa o conteúdo da div para evitar duplicações
        devInfoContainer.innerHTML = '';

        devInfo.forEach(info => {
            devInfoContainer.appendChild(info);
        });
    });
});
