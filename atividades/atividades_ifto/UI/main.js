// faz com que a linguagem fique em portugues 
document.documentElement.lang="pt-br";

// procura o aqrqquivo de menu 
async function include_menu_bar() {
    // coleta o caminho do menu 
    const menu_bar = await fetch('complementos/barra_menu.html');

    document.getElementById('menu_div').innerHTML = await menu_bar.text();
    
}

include_menu_bar()