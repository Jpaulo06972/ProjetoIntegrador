# Bloco de função para criptografia e descriptografia

def cripto(entrada):
    
    # Tabela de mapeamento de letras para números (A=1, ..., Z=26)
    T = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    texto_claro = entrada.upper()
    n = len(texto_claro)

    # Adiciona padding se o número de letras for ímpar
    if n % 2 != 0:
        texto_claro += 'X'
        n += 1

    # Converter texto para números
    I = [T.index(letra) + 1 for letra in texto_claro]

    # Criar pares de números
    P = [[I[i], I[i + 1]] for i in range(0, n, 2)]

    # Matriz de chave A
    A = [[4, 3], [1, 2]]

    # Criptografar (C = A * P mod 26)
    C = []
    for par in P:
        c1 = (A[0][0] * par[0] + A[0][1] * par[1]) % 26
        c2 = (A[1][0] * par[0] + A[1][1] * par[1]) % 26
        C.append([c1 if c1 != 0 else 26, c2 if c2 != 0 else 26])

    # Converter números de volta para letras
    texto_cifrado = ''.join(T[par[0] - 1] + T[par[1] - 1] for par in C)

    return texto_cifrado


def descriptografia(des):
    
    # Tabela de mapeamento de letras para números (A=1, ..., Z=26)
    T = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    des = des.upper()
    I = [T.index(letra) + 1 for letra in des]

    # Agrupar em pares
    pares = [[I[i], I[i + 1]] for i in range(0, len(I), 2)]

    # Matriz de chave A
    A = [[4, 3], [1, 2]]
    det = (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % 26

    # Inverso do determinante mod 26
    inv_det = None
    for i in range(1, 26):
        if (det * i) % 26 == 1:
            inv_det = i
            break

    if inv_det is None:
        return None

    # Matriz inversa A^-1 mod 26
    AI = [
        [(A[1][1] * inv_det) % 26, (-A[0][1] * inv_det) % 26],
        [(-A[1][0] * inv_det) % 26, (A[0][0] * inv_det) % 26]
    ]

    # Descriptografar (P = A^-1 * C mod 26)
    P_desc = []
    for par in pares:
        c1 = par[0] if par[0] != 26 else 0
        c2 = par[1] if par[1] != 26 else 0

        p1 = (AI[0][0] * c1 + AI[0][1] * c2) % 26
        p2 = (AI[1][0] * c1 + AI[1][1] * c2) % 26

        P_desc.append([p1 if p1 != 0 else 26, p2 if p2 != 0 else 26])

    # Converter números de volta para letras
    texto_desc = ''.join(T[par[0] - 1] + T[par[1] - 1] for par in P_desc)

    # Remove caractere de padding 'X' se estiver no final
    if texto_desc.endswith('X'):
        texto_desc = texto_desc[:-1]

    return texto_desc


criptografia = cripto("ALTA")
print(criptografia)

descript = descriptografia("NYEV")
print(descript)