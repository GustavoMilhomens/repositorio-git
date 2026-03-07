
# 9. Biblioteca rich
# A biblioteca rich é fantástica para adicionar rich text (cores, estilos, tabelas, barras de progresso) ao seu terminal e para logs e tracebacks bonitos. Torna a saída do console muito mais legível e atraente.
#  * Não é uma biblioteca nativa.
#  * Para instalar, use: pip install rich
#  * Geralmente importada como from rich.console import Console ou from rich.table import Table.
# <!-- end list -->
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
import time

console = Console()

# console.print()
# Imprime texto com estilo e cor.
console.print("[bold green]Olá, Rich![/bold green] Este é um texto colorido.")
console.print("[italic blue]Texto em itálico e azul.[/italic blue]")

# console.log()
# Imprime mensagens de log com data/hora e nome do arquivo/linha.
console.log("Esta é uma mensagem de log normal.")
console.log("[bold red]ATENÇÃO![/bold red] Algo importante aconteceu.")

# Panel
# Cria um painel com borda ao redor do texto.
console.print(Panel("[bold yellow]Informação Importante[/bold yellow]\n\n"
                      "Este é um painel para destacar conteúdo.",
                      title="[bold cyan]Aviso[/bold cyan]",
                      border_style="purple"))

# Barra de Progresso (track)
# Adiciona uma barra de progresso a um loop.
for i in track(range(10), description="Processando itens..."):
    time.sleep(0.5) # Simula algum trabalho
console.print("[green]Processo concluído![/green]")

######################################################

# # link com mais informações
#  * rich:
#    https://rich.readthedocs.io/en/stable/