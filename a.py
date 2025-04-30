import random
import string

print("==========Gerador de senhas==========")
print("Tipos:\n"
      "1) Letras minúsculas\n"
      "2) Letras maiúsculas\n"
      "3) Caracteres especiais\n"
      "4) Dígitos\n"
      "5) Todos os anteriores (recomendado)\n")
      
tipo_de_senha: int = int(input("Digite o tipo de senha escolhido: "))
tamanho_da_senha: int = int(input("Digite o tamanho desejado para a senha: "))

def gerar_senha(tamanho: int, usar_minusculas: bool = False, usar_maiusculas: bool = False,
                usar_numeros: bool = False, usar_especiais: bool = False) -> str:
    if tamanho < 1:
        return "O tamanho da senha deve ser maior que 0."
    
    # Conjuntos 
    caracteres = ""
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiais:
        caracteres += "@#!&$#%*/ç.;:?¨()[]{}|,^~+-¨'_=°ªº"

    if not caracteres:
        return "Nenhum tipo de caractere selecionado."

    # Garante que tem pelomenos um de cada tipo selecionado
    senha = []
    if usar_minusculas:
        senha.append(random.choice(string.ascii_lowercase))
    if usar_maiusculas:
        senha.append(random.choice(string.ascii_uppercase))
    if usar_numeros:
        senha.append(random.choice(string.digits))
    if usar_especiais:
        senha.append(random.choice("@#!&$#%*/ç.;:?¨()[]{}|,^~+-¨'_=°ªº"))

    # Preenche o restante da senha
    senha += [random.choice(caracteres) for _ in range(tamanho - len(senha))]
    
    # Embaralha a senha para evitar previsibilidade
    random.shuffle(senha)

    return "".join(senha)

# Lógica pra /determinar os tipos de caracteres com base na escolha do usuário
if tipo_de_senha == 1:
    print("============== SENHA ==============\n"
          "Copie sua senha: " + gerar_senha(tamanho_da_senha, usar_minusculas=True))
elif tipo_de_senha == 2:
    print("============== SENHA ==============\n"
          "Copie sua senha: " + gerar_senha(tamanho_da_senha, usar_maiusculas=True))
elif tipo_de_senha == 3:
    print("============== SENHA ==============\n"
          "Copie sua senha: " + gerar_senha(tamanho_da_senha, usar_especiais=True))
elif tipo_de_senha == 4:
    print("============== SENHA ==============\n"
          "Copie sua senha: " + gerar_senha(tamanho_da_senha, usar_numeros=True))
elif tipo_de_senha == 5:
    print("============== SENHA ==============\n"
          "Copie sua senha: " + gerar_senha(tamanho_da_senha, usar_minusculas=True,
                                           usar_maiusculas=True, usar_numeros=True, usar_especiais=True))
else:
    print("Tipo de senha inválido, tente novamente...")
