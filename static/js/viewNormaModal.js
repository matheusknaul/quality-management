document.addEventListener("DOMContentLoaded", () => {
    const switchModal = () => {
        const modal = document.querySelector('.modal');
        const actualStyle = modal.style.display;
        if (actualStyle === 'block') {
            modal.style.display = 'none';
        } else {
            modal.style.display = 'block';
        }
    };

    // Adiciona o evento de clique para todos os botões com a classe modalBtn
    document.querySelectorAll('.modalBtn').forEach(btn => {
        btn.addEventListener('click', switchModal);
    });

    // Fecha o modal se o clique for fora dele
    window.onclick = function(event) {
        const modal = document.querySelector('.modal');
        if (event.target === modal) {
            switchModal();
        }
    };
});
