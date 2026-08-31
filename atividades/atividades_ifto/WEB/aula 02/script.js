//? coloca a linguagem em portugues
document.documentElement.lang = "pt-br";

//? coloca o arquivo css nas paginas
async function add_element() {
    const link = document.createElement('link'); //? cria uma variavel que recebe o elemento link
    link.rel = 'stylesheet'; //? configura 
    link.href = base + '/style.css'; //? referencia o css
    document.head.append(link); //? adiciona o elemento
}
