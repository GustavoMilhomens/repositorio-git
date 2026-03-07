
# Cores básicas
PRETO        = "\033[30m"
VERMELHO     = "\033[31m"
VERDE        = "\033[32m"
AMARELO      = "\033[33m"
AZUL         = "\033[34m"
ROXO         = "\033[35m"
CIANO        = "\033[36m"
BRANCO       = "\033[37m"

# Cores claras (bright)
PRETO_CLARO   = "\033[90m"
VERMELHO_CLARO= "\033[91m"
VERDE_CLARO   = "\033[92m"
AMARELO_CLARO = "\033[93m"
AZUL_CLARO    = "\033[94m"
ROXO_CLARO    = "\033[95m"
CIANO_CLARO   = "\033[96m"
BRANCO_CLARO  = "\033[97m"

# Formatações
NEGRITO      = "\033[1m"
SUBLINHADO   = "\033[4m"
REVERSO      = "\033[7m"
RESET        = "\033[0m"

# Cores em negrito
NEGRITOPRETO = '\033[90m'
NEGRITOVERMELHO = '\033[91m'
NEGRITOVERDE = '\033[92m'
NEGRITOAMARELO = '\033[93m'
NEGRITOAZUL = '\033[94m'
NEGRITOROSA = '\033[95m'
NEGRITOAZULCLARO = '\033[96m'
NEGRITOBRANCO = '\033[97m'
# Cores de fundo
FUNDO_PRETO   = "\033[40m"
FUNDO_VERMELHO = "\033[41m"
FUNDO_VERDE   = "\033[42m"
FUNDO_AMARELO = "\033[43m"
FUNDO_AZUL    = "\033[44m"
FUNDO_ROXO    = "\033[45m"
FUNDO_CIANO   = "\033[46m"
FUNDO_BRANCO  = "\033[47m"

# Formatações adicionais
OCULTO        = "\033[8m"   # Torna o texto invisível (útil para senhas)
RISCADO       = "\033[9m"   # Texto riscado (strike-through)
ITALICO       = "\033[3m"   # Itálico (nem todos os terminais suportam)
PISCANDO      = "\033[5m"   # Texto piscando (pouco suportado)
PISCANDO_RAPIDO = "\033[6m" # Piscando rápido (raro)
SEM_NEGRITO   = "\033[22m"  # Remove negrito
SEM_SUBLINHADO= "\033[24m"  # Remove sublinhado
SEM_REVERSO   = "\033[27m"  # Remove reverso


# Exemplo de uso:

print(NEGRITO + AZUL + "Texto azul em negrito" + RESET)
print(SUBLINHADO + VERMELHO + "Texto vermelho sublinhado" + RESET)
print(REVERSO + AMARELO + "Texto amarelo reverso" + RESET)