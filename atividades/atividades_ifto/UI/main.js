// faz com que a linguagem fique em portugues 
document.documentElement.lang="pt-br";

// procura o aqrqquivo de menu 
async function include_painel_bar() {
    // coleta o caminho do menu 
    const painel_bar = await fetch('complementos/barra_painel.html');

    document.getElementById('painel_div').innerHTML = await painel_bar.text();
    
}

include_painel_bar()