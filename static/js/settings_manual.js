function updateTable(){

    const numRows = parseInt(document.getElementById('numRows').value);
    const tableBody = document.getElementById('pointsTable').getElementsByTagName('tbody')[0];

    tableBody.innerHTML = '0';

    for(let i = 1; i <= numRows; i++){
        const row = tableBody.insertRow();
        const cell1 = row.insertCell(0);
        const cell2 = row.insertCell(1);

        cell1.textContent = i;
        cell2.textContent = `Valor ${i}`;
    }
}