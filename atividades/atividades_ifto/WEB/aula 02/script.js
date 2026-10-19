//?* coloca a linguagem em portugues
document.documentElement.lang = "pt-br";

//* coloca o arquivo css nas paginas
async function add_element() {
    const css = document.createElement('link'); //? cria uma variavel que recebe o elemento link
    css.rel = 'stylesheet'; //? configura 
    css.href = 'style.css'; //? referencia o css
    document.head.append(css); //? adiciona o elemento
};

function clear_search_input(){ //* limpa o impot de pesquisa 
    document.getElementById("search_input").value = "";
};

function search_btn(){ //* botão de pesquisa 
     alert('não ah cursos no momento'); //* alerta que bão há cursos
};

// 1. Seleciona os elementos que vamos usar
const botaoMenu = document.querySelector("#btn-menu");
const menu = document.querySelector(".main-nav");

// 2. Escuta o evento de clique no botão
botaoMenu.addEventListener("click", function () {
  // 3. Alterna (liga/desliga) a classe "ativo" no menu
  menu.classList.toggle("ativo");
});

add_element();
