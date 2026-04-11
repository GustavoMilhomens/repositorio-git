// 1. Busca a sidebar assim que o script carregar
async function includeSidebar() {
    try {
        const response = await fetch('sidebar.html');
        if (!response.ok) throw new Error('Arquivo sidebar.html não encontrado');
        
        const data = await response.text();
        document.getElementById('sidebar-placeholder').innerHTML = data;
    } catch (error) {
        console.error('Erro ao carregar a sidebar:', error);
    }
}

// 2. Função para abrir/fechar (alterna a classe CSS)
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar-placeholder');
    sidebar.classList.toggle('active');
}

// 3. configura a linguagem para portugues 
document.documentElement.lang = "pt-br";


// Inicia o carregamento
includeSidebar();