const dataNorma = document.getElementById('data-norma')

if(dataNorma){
    const dataOriginal = dataNorma.textContent;

    const dia = String(dataObj.getDate()).padStart(2, '0');
    const mes = String(dataObj.getMonth() + 1).padStart(2, '0'); // Janeiro é 0, por isso +1
    const ano = dataObj.getFullYear();

    // Extraia os componentes do horário
    const horas = String(dataObj.getHours()).padStart(2, '0');
    const minutos = String(dataObj.getMinutes()).padStart(2, '0');

    // Formate a data no padrão desejado
    const dataFormatada = `${dia}/${mes}/${ano} às ${horas}:${minutos}`;

    // Atualize o conteúdo da célula com a data formatada
    dataNorma.textContent = dataFormatada;
}