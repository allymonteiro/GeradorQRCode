import qrcode
from colorama import Fore, Style, init

def gerar_qrcode():
    init(autoreset=True)
    print(Style.BRIGHT + Fore.CYAN + "--- GERADOR DE QR CODE ---")

    dados = input("Digite o texto ou link para o qual deseja criar o QR Code: ")
    nome_arquivo = input("Digite o nome do arquivo para salvar a imagem do QR Code: ")

    if not dados or not nome_arquivo:
        print(Fore.RED + "Os daods e o nome do arquivo não podem estar vazios.")
        return
    
    if not nome_arquivo.lower().endswith('.png'):
        nome_arquivo += '.png'

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(dados)
        qr.make(fit=True)

        try:
            imagem_qr = qr.make_image(fill_color="black", back_color="white")
            imagem_qr.save(nome_arquivo)
            print(Style.BRIGHT + Fore.GREEN + f"\nO QR Code foi salvo como '{nome_arquivo}' na pasta do projeto.")
            
        except Exception as e:
            print(Fore.RED + f"\nOcorreu um erro ao gerar a imagem: {e}")

if __name__ == "__main__":
    gerar_qrcode()
    input("\nPressione Enter para sair.")