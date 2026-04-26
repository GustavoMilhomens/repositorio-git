// faz com que a linguagem fique em portugues 
document.documentElement.lang="pt-br";

// adiciona o style e as divs, menu e preference, em todos os arquivos que receberem o main.js
function add_element(){
    //* add style 
    const link = document.createElement('link'); //? cria uma variavel que recebe o elemento link
    link.rel = 'stylesheet'; //? configura 
    link.href = '/atividades/atividades_ifto/UI/style.css'; //? referencia o css
    document.head.append(link); //? adiciona o elemento
    //! o append() adiciona no final 

    //* add div preference
    const div_preference = document.createElement('div'); //? cria a varivel do elemento
    div_preference.id = 'preference_div'; //? adiciona o id
    document.body.prepend(div_preference); //? adiciona a div ao body 
    //! o prepend() adiciona no inicio

    //* add div menu
    const div_menu = document.createElement('div'); 
    div_menu.id = 'menu_div'; 
    document.body.prepend(div_menu);

    


}

// procura o arquivo de menu 
async function include_complement() {
    // coleta o caminho do menu 
    const menu_bar = await fetch("/atividades/atividades_ifto/UI/complementos/barra_menu.html");
    document.getElementById('menu_div').innerHTML = await menu_bar.text();
    
    // coleta o caminho da caxa de preferencias
    const preference_box = await fetch('/atividades/atividades_ifto/UI/complementos/preferencias.html');
    document.getElementById('preference_div').innerHTML = await preference_box.text();
    
}

// abre e fecha o menu 
function open_close_menu(){
        const menu = document.getElementById('menu_div_bar');
        menu.classList.toggle('active') 
    }

// abre e fecha a caixa de preferencias 
function open_close_preference(){
        const prefe = document.getElementById('preference_div_box');
        prefe.classList.toggle('active') 
}

// deixa o sistema funcionando de forma assincrona 
async function start() {
    await include_complement();

    // cria um botão onde de para mudar o tema do site
    const btn_theme = document.getElementById("btn_theme");
    const var_theme = localStorage.getItem("theme");

    // verifica a preferencia do usuario 
    if (var_theme === "dark"){
        document.body.classList.add('dark_theme');
    }

    // adiciona o tema com o click
    btn_theme.addEventListener("click", function(){
        document.body.classList.toggle('dark_theme');

        // ve se o atual é dark e salva a preferencia
        let theme = 'light';
        if (document.body.classList.contains("dark_theme")){
            theme = "dark";
        }
        // salva o tema
        localStorage.setItem('theme', theme); 
    });
}

// chama as funções
add_element();
start();

