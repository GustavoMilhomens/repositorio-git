
# 6. Biblioteca qrcode
# A biblioteca qrcode permite gerar facilmente códigos QR em Python.
#  * Não é uma biblioteca nativa.
#  * Para instalar, use: pip install qrcode
#  * Não possui um nome comumente atribuído na importação, geralmente importada como import qrcode.
# <!-- end list -->
import qrcode

# qrcode.make(dados)
# Cria um objeto QR code a partir dos dados fornecidos.
# Ele pode ser uma URL, texto, etc.
img = qrcode.make("https://www.google.com")

# img.save(nome_arquivo)
# Salva a imagem do QR code em um arquivo.
img.save("meu_qrcode.png")
print("QR Code para Google.com salvo como 'meu_qrcode.png'")

# Exemplo mais avançado (com ajustes de cor e erro):
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L, # Nível de correção de erro
    box_size=10, # Tamanho de cada "caixa" do QR
    border=4, # Espessura da borda
)
qr.add_data("Olá, mundo! Este é um QR Code personalizado.")
qr.make(fit=True)

img_personalizado = qr.make_image(fill_color="blue", back_color="white")
img_personalizado.save("qrcode_personalizado.png")
print("QR Code personalizado salvo como 'qrcode_personalizado.png'")

######################################################

# # link com mais informações
#  * qrcode:
#    https://pypi.org/project/qrcode/
#    https://python-qrcode.readthedocs.io/