// faz com que a linguagem fique em portugues 
document.documentElement.lang="pt-br";

// procura o aqrqquivo de menu 
async function include_menu_bar() {
    // coleta o caminho do menu 
    const menu_bar = await fetch('complementos/barra_menu.html');

    document.getElementById('menu_div').innerHTML = await menu_bar.text();
    
}


// abre e fecha o menu 
function open_close_menu(){
        const menu = document.getElementById('menu_div_bar');
        menu.classList.toggle('active')
    }

include_menu_bar()