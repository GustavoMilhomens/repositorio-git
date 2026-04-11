// faz com que a linguagem fique em portugues 
document.documentElement.lang="pt-br";

// procura o aqrqquivo de menu 
async function include_complement() {
    // coleta o caminho do menu 
    const menu_bar = await fetch('complementos/barra_menu.html');

    document.getElementById('menu_div').innerHTML = await menu_bar.text();
    
    // coleta o caminho da caxa de preferencias
    const preference_box = await fetch('complementos/preferencias.html');
    document.getElementById('preference_div').innerHTML = await preference_box.text();

}


// abre e fecha o menu 
function open_close_menu(){
        const menu = document.getElementById('menu_div_bar');
        menu.classList.toggle('active') 
    }

//abre e fecha a caixa de preferencias 
function open_close_preference(){
        const prefe = document.getElementById('preference_div_box');
        prefe.classList.toggle('active') 
}



include_complement()