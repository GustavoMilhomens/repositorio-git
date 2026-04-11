const btn = document.getElementById("button_theme");
const currentTheme = localStorage.getItem("theme");

// 1. Verifica se o usuário já tinha uma preferência salva
if (currentTheme === "dark") {
document.body.classList.add("dark_theme");
}

// 2. Adiciona o evento de clique
btn.addEventListener("click", function() {
// Alterna a classe no body
document.body.classList.toggle("dark_theme");

// Verifica se o tema atual é dark para salvar a preferência
let theme = "light";
if (document.body.classList.contains("dark_theme")) {
    theme = "dark";
}

// Salva no LocalStorage
localStorage.setItem("theme", theme);
});

