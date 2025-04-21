import re

def classifica_senha(senha):
    if len(senha) < 6:
        return "Fraca"
    
    moderada = r"^(?=.*[a-zA-Z])(?=.*[0-9]).{6,}$"
    forte = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$"
    muito_forte = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*]).{10,}$"

    if re.match(muito_forte, senha):
        return "Muito Forte"
    elif re.match(forte, senha):
        return "Forte"
    elif re.match(moderada, senha):
        return "Moderada"
    else:
        return "Fraca"

def main():
    print("=== Validador e Classificador Inteligente de Senhas ===")
    senha = input("Digite a senha para análise: ")
    categoria = classifica_senha(senha)
    print(f"A senha informada é classificada como: {categoria}")

if __name__ == "__main__":
    main()
