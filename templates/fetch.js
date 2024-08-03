function getData(params) {
    //Escolher prato
    fetch('/api/data')
    .then(resposta => resposta.json())
    .then(dados =>{
        document.getElementById('response').innerText = JSON.stringify(dados)
    })
    .catch(erro => console.error('Erro:', error));
}

function postData(params) {
    const dataToSend = {key: 'value'}

    fetch('/api/data',  {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(dataToSend),
    })
    .then(responder => responder.json())
    .then(dados =>{
        document.getElementById('response').innerText = JSON.stringify(dados);
    })
    .catch(error => console.error('Erro:', error));
    
}