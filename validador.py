import re

def classifica_senha(senha):

    fraca = r"^[a-zA-Z]{1,5}$"
    moderada = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,7}$"
    forte = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,9}$"
    muito_forte = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#\$%\^&\*])[a-zA-Z\d!@#\$%\^&\*]{10}$"

    if re.fullmatch(fraca, senha):
        return "A senha informada é classificada como: Fraca"
    elif re.fullmatch(moderada, senha):
        return "A senha informada é classificada como: Moderada"
    elif re.fullmatch(forte, senha):
        return "A senha informada é classificada como: Forte"
    elif re.fullmatch(muito_forte, senha):
        return "A senha informada é classificada como: Muito Forte"
    else:
        return ("A senha precisa ser uma das seguintes opções:\n"
                "- Fraca: até 5 caracteres, com pelo menos 1 letra (qualquer tipo de letra).\n"
                "- Moderada: de 6 a 7 caracteres, com pelo menos 1 letra maiúscula, 1 letra minúscula e 1 número.\n"
                "- Forte: de 8 a 9 caracteres, com pelo menos 1 letra maiúscula, 1 letra minúscula e 1 número.\n"
                "- Muito Forte: exatamente 10 caracteres com letra maiúscula, minúscula, número e símbolo especial (!@#$%^&*).")

def main():
    print("=== Validador e Classificador Inteligente de Senhas ===")
    senha = input("Digite a senha para análise: ")
    categoria = classifica_senha(senha)
    print(f"{categoria}")

if __name__ == "__main__":
    main()
