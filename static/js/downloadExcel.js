function downloadExcel(){
    fetch('/export_excel')
        .then(response =>{
            if (!response.ok) throw new Error('Erro ao gerar o arquivo');
            return response.blob();
        })
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'dados_exportados.xlsx';
            document.body.appendChild(a);
            a.click();
            a.remove();
            window.URL.revokeObjectURL(url);
        })
        .catch(error => console.error('Erro no download: ', error));
}