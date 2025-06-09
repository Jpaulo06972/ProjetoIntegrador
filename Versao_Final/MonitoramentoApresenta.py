#importação de bibliotecas
import mysql.connector
import os

#conexão com o Banco de Dados
conexao = mysql.connector.connect(
host="localhost", # IP ou hostname do servidor MySQL
user="root", # "login"
password="Jmr&012108", # senha
database="JoaoPaulo" # nome do banco (tem que existir)
)
cursor = conexao.cursor()

# Inicia com 1 para rodar a primeira vez
fim = 1 

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

# Condição para finalizar o sistema
while fim != 0: 
    
    # Tela Inicial
    print("=============================================================")
    print("                   Bem Vindo ao Sistema de                   ")
    print("                     Sustentabibilidade                      ")
    print("=============================================================")
     
    # Escolha do que será mostrado
    print("\n                     ESCOLHA UMA OPÇÃO      \n")
    print("1. Cadastro de Parâmetros Diários de Sustentabilidade.")
    print("2. Alteração de Parâmetros Diários de Sustentabilidade.")
    print("3. Exclusão de Parâmetros Diários de Sustentabilidade.")
    print("4. Classificação da Sustentabilidade.")
    print("5. Média de Sustentabilidade.")
    print("6. Sair do Sistema.\n")

    opcao = int(input("Digite a opção que você deseja (1-6): "))
    os.system('cls' if os.name == 'nt' else 'clear')

    # Caso o usuário escolha a opção que não existe ele faz o usuário escolher uma opção válida
    while opcao < 1 or opcao > 6:
        print("==========================================")
        print("             VALOR INVÁLIDO              ")
        print("       Digite um número entre 1 e 6      ")
        print("==========================================")

        print("\n           ESCOLHA UMA OPÇÃO      \n")
        print("1. Cadastro de Parâmetros Diários de Sustentabilidade.")
        print("2. Alteração de Parâmetros Diários de Sustentabilidade.")
        print("3. Exclusão de Parâmetros Diários de Sustentabilidade.")
        print("4. Classificação da Sustentabilidade.")
        print("5. Média de Sustentabilidade.")
        print("6. Sair do Sistema.\n")

        opcao = int(input("Digite a opção que você deseja (1-5): "))
        os.system('cls' if os.name == 'nt' else 'clear')

    # Condição de cadastro de sustentabilidade
    if opcao == 1: 
                
        # Tela Inicial
        print("=============================================================")
        print("                   Bem Vindo ao Cadastro de                  ")
        print("                      Sustentabibilidade                     ")
        print("=============================================================\n")
        print("O sistema calculará as informações de sustentabilidade\n")
        print("Para as perguntas sobre transporte responder com S (sim) ou N (não)\n")
        input('\n\t<< Tecle Enter para continuar >>')

        os.system('cls' if os.name == 'nt' else 'clear')

        # Sistema de Monitoramento de Sustentabilidade
        print("=============================================================")
        print("                 Sistema de Monitoramento                    ")
        print("                      Sustentável                            ")
        print("=============================================================\n")
        # Coleta as informções do usuário sobre sua sustentabilidade
        date = input("Digite a Data de Hoje (yyyy/mm/dd): ")
        qtdAgua = float(input("Digite seu consumo de água (Aprox. em Litros): ")) 
        qtdEnergia = float(input("Digite seu consumo de energia (kWh): ")) 
        qtdResiduo = float(input("Digite seu consumo de resíduos (Kg): ")) 
        porReciclado = int(input("Digite a porcentagem de resíduos reciclados (%): "))

        print("Digite qual o meio de transporte você usou hoje? (S/N)")

        # Coleta as informções do usuário sobre transporte
        publico = input("1. Transporte público(Ônibus, metrô, trem): ")
        bicicleta = input("2. Bicicleta: ")
        caminhada = input("3. Caminhada: ")
        carro = input("4. Carro (Combustível fósseis): ")
        carroEletrico = input("5. Carro elétrico: ")
        carona = input("6. Carona compartilhada(Fósseies): ")

        os.system('cls' if os.name == 'nt' else 'clear')

        # Comando de insert para o BD
        sqlConsumo = """
        INSERT INTO dadosConsumo (data, quantidadeAgua, quantidadeEnergia, quantidaderResiduos, porcentagemResiduos, publico, bicicleta, caminhada, carro, carroEletrico, carona) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Valores finais para inserção no BD
        valoresConsumo = (date, 
                          qtdAgua, 
                          qtdEnergia, 
                          qtdResiduo, 
                          porReciclado, 
                          publico, 
                          bicicleta, 
                          caminhada, 
                          carro, 
                          carroEletrico,
                          carona)

        # Executa o comando no Banco de dados 
        cursor.execute(sqlConsumo, valoresConsumo)
        # Salve o comando executado do banco de dados 
        conexao.commit()

        # Captura o ID inserido do relacionamento entre as tabelas 
        id_dado = cursor.lastrowid

        print("\nDados inseridos com sucesso no banco de dados!\n")
        print("=============================================================")
        print("                 Relatorio do Monitoramento                  ")
        print("                      de Sustentavel                         ")
        print("=============================================================\n")
        print(f"Data: {date}")

        # Classificão de sustentabilidade de água
        if qtdAgua < 150:
            print("Consumo de água: Alta Sustentabilidade")
            clfAguaC = "Alta"
            
        elif qtdAgua < 200:
            print("Consumo de água: Moderada Sustentabilidade")
            clfAguaC = "Moderada"
            
        else:
            print("Consumo de água: Baixa Sustentabilidade")
            clfAguaC = "Baixa"
        
        clfAgua = cripto(clfAguaC)
           
        # Classificão de sustentabilidade de energia
        if qtdEnergia < 5:
            print("Consumo de energia: Alta Sustentabilidade")
            clfEnergiaC = "Alta"
            
        elif qtdEnergia < 10:
            print("Consumo de energia: Moderada Sustentabilidade")
            clfEnergiaC = "Moderada"
            
        else:
            print("Consumo de energia: Baixa Sustentabilidade")
            clfEnergiaC = "Baixa"
        
        clfEnergia = cripto(clfEnergiaC)
           
        # Cálcula a quantidade de resíduos não reciclados 
        porNReciclado = (100 - porReciclado)

        # Classificão de sustentabilidade dos resíduos
        if porNReciclado > 50:
            print("Geração de Resíduos Não Recicláveis: Baixa Sustentabilidade")
            clfRecicladoC = "Baixa"
            
        elif porNReciclado > 20:
            print("Geração de Resíduos Não Recicláveis: Moderada Sustentabilidade")
            clfRecicladoC = "Moderada"
            
        else:
            print("Geração de Resíduos Não Recicláveis: Alta Sustentabilidade")
            clfRecicladoC = "Alta"

        clfReciclado = cripto(clfRecicladoC)
        
        # Classifica a sustentabilidade por meios de transportes utilizados 
        if (publico == "S" or publico == "s") or (bicicleta == "S" or bicicleta == "s") or (caminhada == "S" or caminhada == "s") or (carroEletrico == "S" or carroEletrico == "s"):
            if (carro == "S" or carro == "s") or (carona == "S" or carona =="s"):  
                print("Uso de Transporte: Moderado Sustentabilidade")
                clfTransporteC = "Moderada"
                
            else:
                print("Uso de Transporte: Alta Sustentabilidade")
                clfTransporteC = "Alta"
                
        elif (carro == "S" or carro == "s") or (carona == "S" or carona == "s"):
                
            print("Uso de Transporte: Baixa Sustentabilidade")
            clfTransporteC = "Baixa"
            
        else:
            print("Uso de Transporte: Baixa Sustentabilidade")
            clfTransporteC = "Alta"
        
        clfTransporte = cripto(clfTransporteC)
                
        input('\n\t<< Tecle Enter para continuar >>')
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Comando de insert para o BD
        sqlClassificao = """
        INSERT INTO classificacao (id, classificacaoAgua, classificacaoEnergia, classificacaoResiduo, classificacaoTransporte) 
        VALUES (%s, %s, %s, %s, %s)
        """

        # Valores finais para inserção no BD
        valoresClassificacao = (id_dado, clfAgua, clfEnergia, clfReciclado, clfTransporte)

        # Executa o comando no Banco de dados 
        cursor.execute(sqlClassificao, valoresClassificacao)
        # Salve o comando executado do banco de dados 
        conexao.commit()

    # Alteração dos Dados no Banco de Dados
    elif opcao == 2:
        
        # Coleta os dados dos registros
        cursor.execute("SELECT * FROM dadosConsumo")
        resultadoAlteracao = cursor.fetchall()
        
        # Exibe todos os registros do banco de Dados 
        print('\n========= Exibição dos Dados de Consumo =========\n')
        print('| ID | Data de registro | Consumo de água | Consumo de energia | Lixo não reciclável | % de resíduos recicláveis|')
        for linha in resultadoAlteracao:
            
            print(f'  {linha[0]:<4}', end='\t')
            print(f'  {linha[1]}', end='\t   ')
            print(f'  {linha[2]} L', end='\t\t')
            print(f'  {linha[3]} KwH', end='\t\t')
            print(f'{linha[4]} Kg', end='\t\t')
            print(f'{linha[5]}', end='\t\t\n')
        
            print('='*113)  

        # Escolhe o resgitro a ser alterado    
        idAltera = int(input("Digite o ID do registro que deseja alterar: "))
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Verificar se o ID existe
        cursor.execute("SELECT * FROM dadosConsumo WHERE ID = %s", (idAltera,))
        registro = cursor.fetchall()
        
        # verifica se exite o registro escolhido pelo usuário
        while not registro:    
            print("\nID não encontrado!")
            input('\n\t<< Tecle Algo para continuar >>')
            
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Exibe todos os registros novamente caso o cara digite a opção errada
            print('\n========= Exibição dos Dados de Consumo =========\n')
            print('| ID | Data de registro | Consumo de água | Consumo de energia | Lixo não reciclável | % de resíduos recicláveis|')
            for linha in resultadoAlteracao :
                print(f'  {linha[0]:<4}', end='\t')
                print(f'  {linha[1]}', end='\t   ')
                print(f'  {linha[2]} L', end='\t\t')
                print(f'  {linha[3]} KwH', end='\t\t')
                print(f'{linha[4]} Kg', end='\t\t')
                print(f'{linha[5]}', end='\t\t\n')
            
                print('='*113)   
            
            # Faz ele digitar sua nova escolha    
            idAltera = int(input("Digite o ID do registro que deseja alterar: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Verificar se o ID existe
            cursor.execute("SELECT * FROM dadosConsumo WHERE ID = %s", (idAltera,))
            registro = cursor.fetchall()
            
        # Mostra o dado que ele deseja alterar    
        print('\n========= Dado de Consumo que Desaja Alterar =========\n')
        print('| ID | Data de registro | Consumo de água | Consumo de energia | Lixo não reciclável | % de resíduos recicláveis|')
        for linha in registro:
            print(f'  {linha[0]:<4}', end='\t')
            print(f'  {linha[1]}', end='\t   ')
            print(f'  {linha[2]} L', end='\t\t')
            print(f'  {linha[3]} KwH', end='\t\t')
            print(f'{linha[4]} Kg', end='\t\t')
            print(f'{linha[5]}', end='\t\t\n')
        
        # Mostra para ele as opções para ele alterar os dados    
        print()
        print("=============================================================")
        print("                 Escolha o Tipo de Alteração                 ")
        print("=============================================================")
        print("                    ESCOLHA UMA OPÇÃO      \n")
        print("1. Alterar Tudo.")
        print("2. Alterar Apenas Um.")
        print("3. Cancelar Alteração.\n")
        
        tipoAlteracao = int(input("Digite a opção que você deseja (1-3): "))
        os.system('cls' if os.name == 'nt' else 'clear')
        
         # Caso o usuário escolha a opção que não existe ele faz o usuário escolher uma opção válida
        while tipoAlteracao < 1 or tipoAlteracao > 3:
            print("==========================================")
            print("             VALOR INVÁLIDO              ")
            print("       Digite um número entre 1 e 2      ")
            print("==========================================")

            print("\n           ESCOLHA UMA OPÇÃO      \n")
            print("1. Alterar Tudo.")
            print("2. Alterar Apenas Um.")
            print("3. Cancelar Alteração.\n")

            tipoAlteracao = int(input("Digite a opção que você deseja (1-3): "))
            os.system('cls' if os.name == 'nt' else 'clear')
        
        # Altera um dado especifico fazendo todas as perguntas novamente
        if tipoAlteracao == 1: 
            
            # Sistema de Monitoramento de Sustentabilidade
            print("=============================================================")
            print("               Alteração dos Dados no Sistema de             ")
            print("                  Monitoramento Sustentável                  ")
            print("=============================================================\n")
            # Coleta as informções do usuário sobre sua sustentabilidade
            novoDate = input("Digite a nova Data (yyyy/mm/dd): ")
            novoQtdAgua = float(input("Digite o novo valor do consumo de água (Aprox. em Litros): ")) 
            novoQtdEnergia = float(input("Digite o novo valor do consumo de energia (kWh): ")) 
            novoQtdResiduo = float(input("Digite o novo valor do consumo de resíduos (Kg): ")) 
            novoPorReciclado = int(input("Digite o novo valor da porcentagem de resíduos reciclados (%): "))

            print("Digite qual o meio de transporte você usou hoje? (S/N)")

            # Coleta as informções do usuário sobre transporte
            novoPublico = input("1. Transporte público(Ônibus, metrô, trem): ")
            novoBicicleta = input("2. Bicicleta: ")
            novoCaminhada = input("3. Caminhada: ")
            novoCarro = input("4. Carro (Combustível fósseis): ")
            novoCarroEletrico = input("5. Carro elétrico: ")
            novoCarona = input("6. Carona compartilhada(Fósseies): ")

            os.system('cls' if os.name == 'nt' else 'clear')

            sqlUpdate = """
            UPDATE dadosConsumo 
            SET data = %s,
                quantidadeAgua = %s,
                quantidadeEnergia = %s, 
                quantidaderResiduos = %s,
                porcentagemResiduos = %s,  
                publico = %s,
                bicicleta = %s,
                caminhada = %s,
                carro = %s,
                carroEletrico = %s, 
                carona = %s
            WHERE id = %s
            """
            # Valores finais do UPDATE no BD
            valoresUpdate = (novoDate,
                             novoQtdAgua, 
                             novoQtdEnergia,
                             novoQtdResiduo,
                             novoPorReciclado, 
                             novoPublico, 
                             novoBicicleta, 
                             novoCaminhada, 
                             novoCarro, 
                             novoCarroEletrico,
                             novoCarona,
                             idAltera)

            # Executa o comando no Banco de dados 
            cursor.execute(sqlUpdate, valoresUpdate)
            # Salve o comando executado do banco de dados 
            conexao.commit()

            print("\nDados Alterados com sucesso no banco de dados!\n")
            print("=============================================================")
            print("                 Relatorio do Monitoramento                  ")
            print("                      de Sustentavel                         ")
            print("=============================================================\n")
            print(f"Data: {novoDate}")

            # Classificão de sustentabilidade de água
            if novoQtdAgua < 150:
                print("Consumo de água: Alta Sustentabilidade")
                novoClfAguaC = "Alta"
                
            elif novoQtdAgua < 200:
                print("Consumo de água: Moderada Sustentabilidade")
                novoClfAguaC = "Moderada"
                
            else:
                print("Consumo de água: Baixa Sustentabilidade")
                novoClfAguaC = "Baixa"
            
            novoClfAgua = cripto(novoClfAguaC)
            
            # Classificão de sustentabilidade de energia
            if novoQtdEnergia < 5:
                print("Consumo de energia: Alta Sustentabilidade")
                novoClfEnergiaC = "Alta"
                
            elif novoQtdEnergia < 10:
                print("Consumo de energia: Moderada Sustentabilidade")
                novoClfEnergiaC = "Moderada"
                
            else:
                print("Consumo de energia: Baixa Sustentabilidade")
                novoClfEnergiaC = "Baixa"
            
            novoClfEnergia = cripto(novoClfEnergiaC)
             
            # Cálcula a quantidade de resíduos não reciclados 
            novoPorNReciclado = (100 - novoPorReciclado)

            # Classificão de sustentabilidade dos resíduos
            if novoPorNReciclado > 50:
                print("Geração de Resíduos Não Recicláveis: Baixa Sustentabilidade")
                novoClfRecicladoC = "Baixa"
                
            elif novoPorNReciclado > 20:
                print("Geração de Resíduos Não Recicláveis: Moderada Sustentabilidade")
                novoClfRecicladoC = "Moderada"
                
            else:
                print("Geração de Resíduos Não Recicláveis: Alta Sustentabilidade")
                novoClfRecicladoC = "Alta"

            novoClfReciclado = cripto(novoClfRecicladoC)
            
            # Classifica a sustentabilidade por meios de transportes utilizados 
            if (novoPublico == "S" or novoPublico == "s") or (novoBicicleta == "S" or novoBicicleta == "s") or (novoCaminhada == "S" or novoCaminhada == "s") or (novoCarroEletrico == "S" or novoCarroEletrico == "s"):
                if (novoCarro == "S" or novoCarro == "s") or (novoCarona == "S" or novoCarona =="s"):  
                    print("Uso de Transporte: Moderado Sustentabilidade")
                    novoClfTransporteC = "Moderado"
                    
                else:
                    print("Uso de Transporte: Alta Sustentabilidade")
                    novoClfTransporteC = "Alta"
                    
            elif (novoCarro == "S" or novoCarro == "s") or (novoCarona == "S" or novoCarona == "s"):
                    
                print("Uso de Transporte: Baixa Sustentabilidade")
                novoClfTransporteC = "Baixa"
            else:
                print("Uso de Transporte: Baixa Sustentabilidade")
                novoClfTransporteC  = "Alta"
            
            
            novoClfTransporte = cripto(novoClfTransporteC)
            
            # Comando de insert para o BD
            sqlClassificaoAlterado = """
            UPDATE classificacao 
            SET classificacaoAgua = %s,
                classificacaoEnergia = %s, 
                classificacaoResiduo = %s,
                classificacaoTransporte = %s
            WHERE id = %s
            """
            # Valores finais para inserção no BD
            valoresClassificacaoAlterado = (novoClfAgua, novoClfEnergia, novoClfReciclado, novoClfTransporte, idAltera)

            # Executa o comando no Banco de dados 
            cursor.execute(sqlClassificaoAlterado, valoresClassificacaoAlterado)
            # Salve o comando executado do banco de dados 
            conexao.commit()
            
            input('\n\t<< Tecle Enter para continuar >>')
            os.system('cls' if os.name == 'nt' else 'clear')
            
        # Alteração por dado especifico    
        if tipoAlteracao == 2: 
            # Mostra o dado que ele deseja alterar    
            print('\n========= Dado de Consumo que Desaja Alterar =========\n')
            print('| ID | Data de registro | Consumo de água | Consumo de energia | Lixo não reciclável | % de resíduos recicláveis|')
            for linha in registro:
                print(f'  {linha[0]:<4}', end='\t')
                print(f'  {linha[1]}', end='\t   ')
                print(f'  {linha[2]} L', end='\t\t')
                print(f'  {linha[3]} KwH', end='\t\t')
                print(f'{linha[4]} Kg', end='\t\t')
                print(f'{linha[5]}', end='\t\t\n')
                
            # Mostra para ele as opções para ele alterar o dado especifico    
            print()
            print("=============================================================")
            print("                 Escolha o Tipo de Alteração                 ")
            print("=============================================================")
            print("                    ESCOLHA UMA OPÇÃO      \n")
            print("1. Data.")
            print("2. Consumo de Água.")
            print("3. Consumo de Energia.")
            print("4. Dados dos Resíduos Gerados.")
            print("5. Dados dos Transportes.")

            qualAlteracao = int(input("Digite a opção que você deseja (1-5): "))
            os.system('cls' if os.name == 'nt' else 'clear')

            # Caso o usuário escolha a opção que não existe ele faz o usuário escolher uma opção válida
            while qualAlteracao < 1 or qualAlteracao > 5:
                print("==========================================")
                print("             VALOR INVÁLIDO              ")
                print("       Digite um número entre 1 e 5      ")
                print("==========================================")

                print("\n           ESCOLHA UMA OPÇÃO      \n")
                print("1. Data.")
                print("2. Consumo de Água.")
                print("3. Consumo de Energia.")
                print("4. Dados dos Resíduos Gerados.")
                print("5. Dados dos Transportes.")
                
                qualAlteracao = int(input("Digite a opção que você deseja (1-5): "))

                os.system('cls' if os.name == 'nt' else 'clear')
                
            # Alteração da data
            if qualAlteracao == 1:
                # Alteração da data 
                print("=============================================================")
                print("               Alteração do Dado no Sistema de             ")
                print("                  Monitoramento Sustentável                  ")
                print("=============================================================\n")
                # Coleta as informções do usuário sobre sua sustentabilidade
                novoDate = input("Digite a nova Data (yyyy/mm/dd): ")
                sqlUpdate = "UPDATE dadosConsumo SET data = %s WHERE id = %s"
                
                # Valores finais do UPDATE no BD
                valoresUpdate = (novoDate,idAltera)

                # Executa o comando no Banco de dados 
                cursor.execute(sqlUpdate, valoresUpdate)
                # Salve o comando executado do banco de dados 
                conexao.commit()
                
                print("\nDado Alterado com sucesso no banco de dados!\n")
                
                input('\n\t<< Tecle Enter para continuar >>')
                os.system('cls' if os.name == 'nt' else 'clear')
                
            #Alteração no consumo de água       
            elif qualAlteracao == 2:
                # Alteração do consumo de água
                print("=============================================================")
                print("               Alteração do Dado no Sistema de             ")
                print("                  Monitoramento Sustentável                  ")
                print("=============================================================\n")
                # Coleta as informções do usuário sobre sua sustentabilidade
                novoQtdAgua = float(input("Digite o novo valor do consumo de água (Aprox. em Litros): ")) 
                sqlUpdate = "UPDATE dadosConsumo SET quantidadeAgua = %s WHERE id = %s"
                
                # Valores finais do UPDATE no BD
                valoresUpdate = (novoQtdAgua,idAltera)

                # Executa o comando no Banco de dados 
                cursor.execute(sqlUpdate, valoresUpdate)
                # Salve o comando executado do banco de dados 
                conexao.commit()
                
                # Classificão de sustentabilidade de água
                if novoQtdAgua < 150:
                    novoClfAguaC = "Alta"
                    
                elif novoQtdAgua < 200:
                    novoClfAguaC = "Moderada"
                    
                else:
                    novoClfAguaC = "Baixa"
                
                novoClfAgua = cripto(novoClfAguaC)
                
                # Comando para executar o UPDATE
                sqlClassificaoAlterado = "UPDATE classificacao SET classificacaoAgua = %s WHERE id = %s"
                
                # Valores finais para inserção no BD
                valoresClassificacaoAlterado = (novoClfAgua,idAltera)
                
                # Executa o comando no Banco de dados 
                cursor.execute(sqlClassificaoAlterado, valoresClassificacaoAlterado)
                
                # Salve o comando executado do banco de dados 
                conexao.commit()   
                
                print("\nDado Alterado com sucesso no banco de dados!\n")
                
                input('\n\t<< Tecle Enter para continuar >>')
                os.system('cls' if os.name == 'nt' else 'clear')
            
            #Alteração no consumo de energia       
            elif qualAlteracao == 3:
                # Alteração do consumo de água
                print("=============================================================")
                print("               Alteração do Dado no Sistema de             ")
                print("                  Monitoramento Sustentável                  ")
                print("=============================================================\n")
                # Coleta as informções do usuário sobre sua sustentabilidade
                novoQtdEnergia = float(input("Digite o novo valor do consumo de energia (kWh): "))
                sqlUpdate = "UPDATE dadosConsumo SET quantidadeEnergia = %s WHERE id = %s"
                
                # Valores finais do UPDATE no BD
                valoresUpdate = (novoQtdEnergia,idAltera)

                # Executa o comando no Banco de dados 
                cursor.execute(sqlUpdate, valoresUpdate)
                # Salve o comando executado do banco de dados 
                conexao.commit()
                
                # Classificão de sustentabilidade de energia
                if novoQtdEnergia < 5:
                    novoClfEnergiaC = "Alta"
                    
                elif novoQtdEnergia < 10:
                    novoClfEnergiaC = "Moderada"
                    
                else:
                    novoClfEnergiaC = "Baixa"
                
                novoClfEnergia = cripto(novoClfEnergiaC)
                
                # Comando para executar o UPDATE
                sqlClassificaoAlterado = "UPDATE classificacao SET classificacaoEnergia = %s WHERE id = %s"
                
                # Valores finais para inserção no BD
                valoresClassificacaoAlterado = (novoClfEnergia,idAltera)
                
                # Executa o comando no Banco de dados 
                cursor.execute(sqlClassificaoAlterado, valoresClassificacaoAlterado)
                
                # Salve o comando executado do banco de dados 
                conexao.commit()   
                
                print("\nDado Alterado com sucesso no banco de dados!\n")
                input('\n\t<< Tecle Enter para continuar >>')
                os.system('cls' if os.name == 'nt' else 'clear')
                
            #Alteração dos dados de resíduos gerados      
            elif qualAlteracao == 4:
                # Alteração do nos dados de resíduos gerados
                print("=============================================================")
                print("               Alteração do Dado no Sistema de             ")
                print("                  Monitoramento Sustentável                  ")
                print("=============================================================\n")
                # Coleta as informções do usuário sobre sua sustentabilidade
                novoQtdResiduo = float(input("Digite o novo valor do consumo de resíduos (Kg): ")) 
                novoPorReciclado = int(input("Digite o novo valor da porcentagem de resíduos reciclados (%): "))
                
                sqlUpdate = "UPDATE dadosConsumo SET quantidaderResiduos = %s, porcentagemResiduos = %s WHERE id = %s"
                
                # sqlUpdate = "UPDATE dadosConsumo SET quantidaderResiduos = %s WHERE id = %s"
                
                # Valores finais do UPDATE no BD
                valoresUpdate = (novoQtdResiduo, novoPorReciclado, idAltera)

                # Executa o comando no Banco de dados 
                cursor.execute(sqlUpdate, valoresUpdate)
                # Salve o comando executado do banco de dados 
                conexao.commit()
                
                # Cálcula a quantidade de resíduos não reciclados 
                novoPorNReciclado = (100 - novoPorReciclado)

                # Classificão de sustentabilidade dos resíduos
                if novoPorNReciclado > 50:
                    novoClfRecicladoC = "Baixa"
                    
                elif novoPorNReciclado > 20:
                    novoClfRecicladoC = "Moderada"
                    
                else:
                    novoClfRecicladoC = "Alta"
                
                novoClfReciclado = cripto(novoClfRecicladoC)
                
                # Comando para executar o UPDATE
                sqlClassificaoAlterado = "UPDATE classificacao SET classificacaoResiduo = %s WHERE id = %s"
                
                # Valores finais para inserção no BD
                valoresClassificacaoAlterado = (novoClfReciclado, idAltera)
                
                # Executa o comando no Banco de dados 
                cursor.execute(sqlClassificaoAlterado, valoresClassificacaoAlterado)
                
                # Salve o comando executado do banco de dados 
                conexao.commit()   
                
                print("\nDado Alterado com sucesso no banco de dados!\n")
                input('\n\t<< Tecle Enter para continuar >>')
                os.system('cls' if os.name == 'nt' else 'clear')   
                
            #Alteração dos dados de transporte 
            elif qualAlteracao == 5:
                
                cursor.execute("SELECT * FROM dadosConsumo WHERE ID = %s", (idAltera,))
                consumo = cursor.fetchall()
                
                print('\n========= Exibição dos Dados de Transporte: =========\n')
                print('ID | Público | Bicicleta | Caminhada | Carro | Carro Elétrico | Carona |')
                for linha in consumo:
                        print(f'{linha[0]:<4}', end='\t')
                        print(f'{linha[6]}', end='\t')
                        print(f'   {linha[7]}', end='\t')
                        print(f'       {linha[8]}', end='\t')
                        print(f' {linha[9]}', end='\t')
                        print(f'     {linha[10]}', end='\t\t')
                        print(f'   {linha[11]}', end='\t\t\t\n')
                
                print()
                
                # Alteração do nos dados de transporte
                print("=============================================================")
                print("               Alteração do Dado no Sistema de             ")
                print("                  Monitoramento Sustentável                  ")
                print("=============================================================\n")
                # Coleta as informções do usuário sobre transporte
                novoPublico = input("1. Transporte público(Ônibus, metrô, trem): ")
                novoBicicleta = input("2. Bicicleta: ")
                novoCaminhada = input("3. Caminhada: ")
                novoCarro = input("4. Carro (Combustível fósseis): ")
                novoCarroEletrico = input("5. Carro elétrico: ")
                novoCarona = input("6. Carona compartilhada(Fósseies): ")
                
                sqlUpdate = "UPDATE dadosConsumo SET publico = %s, bicicleta = %s, caminhada = %s, carro = %s, carroEletrico = %s, carona = %s WHERE id = %s"
                
                # Valores finais do UPDATE no BD
                valoresUpdate = (novoPublico, novoBicicleta, novoCaminhada, novoCarro, novoCarroEletrico, novoCarona, idAltera)

                # Executa o comando no Banco de dados 
                cursor.execute(sqlUpdate, valoresUpdate)
                # Salve o comando executado do banco de dados 
                conexao.commit()
                
                # Classifica a sustentabilidade por meios de transportes utilizados 
                if (novoPublico == "S" or novoPublico == "s") or (novoBicicleta == "S" or novoBicicleta == "s") or (novoCaminhada == "S" or novoCaminhada == "s") or (novoCarroEletrico == "S" or novoCarroEletrico == "s"):
                    if (novoCarro == "S" or novoCarro == "s") or (novoCarona == "S" or novoCarona =="s"):  
                        novoClfTransporteC = "Moderado"
                        
                    else:
                        novoClfTransporteC = "Alta"
                        
                elif (novoCarro == "S" or novoCarro == "s") or (novoCarona == "S" or novoCarona == "s"):
                    novoClfTransporteC = "Baixa"
                    
                else:
                    novoClfTransporteC  = "Alta"
                
                novoClfTransporte  = cripto(novoClfTransporteC)
                
                # Comando para executar o UPDATE
                sqlClassificaoAlterado = "UPDATE classificacao SET classificacaoTransporte = %s WHERE id = %s"
                
                # Valores finais para inserção no BD
                valoresClassificacaoAlterado = (novoClfTransporte, idAltera)
                
                # Executa o comando no Banco de dados 
                cursor.execute(sqlClassificaoAlterado, valoresClassificacaoAlterado)
                
                # Salve o comando executado do banco de dados 
                conexao.commit()   
                
                print("\nDado Alterado com sucesso no banco de dados!\n")
                input('\n\t<< Tecle Enter para continuar >>')
                os.system('cls' if os.name == 'nt' else 'clear')    
                
    # Opção que exclui um dado das tabelas     
    elif opcao == 3:
        
        # Coleta os dados dos registros
        cursor.execute("SELECT * FROM dadosConsumo")
        resultadoAlteracao = cursor.fetchall()
        
        # Exibe todos os registros do banco de Dados 
        print('\n========= Exibição dos Dados de Consumo =========\n')
        print('| ID | Data de registro | Consumo de água | Consumo de energia | Lixo não reciclável | % de resíduos recicláveis|')
        for linha in resultadoAlteracao:
            print(f'  {linha[0]:<4}', end='\t')
            print(f'  {linha[1]}', end='\t   ')
            print(f'  {linha[2]} L', end='\t\t')
            print(f'  {linha[3]} KwH', end='\t\t')
            print(f'{linha[4]} Kg', end='\t\t')
            print(f'{linha[5]}', end='\t\t\n')
        
            print('='*113)  

        # Escolhe o resgitro a ser excluido    
        idExclui = int(input("Digite o ID do registro que deseja Excluir: "))
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Verificar se o ID existe
        cursor.execute("SELECT * FROM dadosConsumo WHERE ID = %s", (idExclui,))
        registro = cursor.fetchall()
        
        # verifica se exite o registro escolhido pelo usuário
        while not registro:    
            print("\nID não encontrado!")
            input('\n\t<< Tecle Algo para continuar >>')
            
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Exibe todos os registros novamente caso o cara digite a opção errada
            print('\n========= Exibição dos Dados de Consumo =========\n')
            print('| ID | Data de registro | Consumo de água | Consumo de energia | Lixo não reciclável | % de resíduos recicláveis|')
            for linha in resultadoAlteracao :
                print(f'  {linha[0]:<4}', end='\t')
                print(f'  {linha[1]}', end='\t   ')
                print(f'  {linha[2]} L', end='\t\t')
                print(f'  {linha[3]} KwH', end='\t\t')
                print(f'{linha[4]} Kg', end='\t\t')
                print(f'{linha[5]}', end='\t\t\n')
            
                print('='*113)   
            
            # Faz ele digitar sua nova escolha    
            idExclui = int(input("Digite o ID do registro que deseja Excluir: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Verificar se o ID existe
            cursor.execute("SELECT * FROM dadosConsumo WHERE ID = %s", (idExclui,))
            registro = cursor.fetchall()
            
        # Mostra o dado que ele deseja alterar    
        print('\n========= Dado de Consumo que Desaja Excluir =========\n')
        print('| ID | Data de registro | Consumo de água | Consumo de energia | Lixo não reciclável | % de resíduos recicláveis|')
        for linha in registro:
            print(f'  {linha[0]:<4}', end='\t')
            print(f'  {linha[1]}', end='\t   ')
            print(f'  {linha[2]} L', end='\t\t')
            print(f'  {linha[3]} KwH', end='\t\t')
            print(f'{linha[4]} Kg', end='\t\t')
            print(f'{linha[5]}', end='\t\t\n')
            
        # Mostra para ele as opções para ele alterar os dados    
        print()
        print("=============================================================")
        print("        Escolha se Deseja Realmente Excluir esse Dado        ")
        print("=============================================================")
        print("                    ESCOLHA UMA OPÇÃO      \n")
        print("1. Sim.")
        print("2. Não.\n")
        
        exclui = int(input("Digite a opção que você deseja (1-2): "))
        os.system('cls' if os.name == 'nt' else 'clear')
        
         # Caso o usuário escolha a opção que não existe ele faz o usuário escolher uma opção válida
        while exclui < 1 or exclui > 2:
            print("==========================================")
            print("             VALOR INVÁLIDO              ")
            print("       Digite um número entre 1 e 2      ")
            print("==========================================\n")

            print("=============================================================")
            print("        Escolha se Deseja Realmente Excluir esse Dado        ")
            print("=============================================================")
            print("                    ESCOLHA UMA OPÇÃO      \n")
            print("1. Sim.")
            print("2. Não.\n")

            exclui = int(input("Digite a opção que você deseja (1-2): "))
            os.system('cls' if os.name == 'nt' else 'clear')          
            
        if exclui == 1:
            
            try:
                cursor.execute("DELETE FROM classificacao  WHERE id = %s", (idExclui,)) 
                
                cursor.execute("DELETE FROM dadosConsumo WHERE id = %s", (idExclui,))
            
                conexao.commit() 
                print("\nRegistro apagado com sucesso!")
                      
            except mysql.connector.Error as err:
                    conexao.rollback()
                    print(f"\nErro ao apagar registro: {err}")
                    
        else: 
            # Comando Cancelado
            print("COMANDO DE EXCLUSÃO CANSELADO")
            input('\n\t<< Tecle Enter para continuar >>')
            os.system('cls' if os.name == 'nt' else 'clear')
            
    elif opcao == 4:
        # Coleta os dados dos registros
        cursor.execute("SELECT * FROM dadosConsumo")
        consumo = cursor.fetchall()
        
        cursor.execute("SELECT * FROM classificacao")
        classifcacao = cursor.fetchall()
        
        # Exibe todos os registros do banco de Dados 
        print('\n========= Exibição dos Dados de Consumo =========\n')
        print('| ID | Data de registro | Consumo de água | Consumo de energia | Lixo não reciclável | % de resíduos recicláveis|')
        for linha in consumo:
            print(f'  {linha[0]:<4}', end='\t')
            print(f'  {linha[1]}', end='\t   ')
            print(f'  {linha[2]} L', end='\t\t')
            print(f'  {linha[3]} KwH', end='\t\t')
            print(f'{linha[4]} Kg', end='\t\t')
            print(f'{linha[5]}', end='\t\t\n')
        
            print('='*113)  
            
        print('\n========= Exibição dos Dados de Transporte: =========\n')
        print('ID | Público | Bicicleta | Caminhada | Carro | Carro Elétrico | Carona |')
        for linha in consumo:
                print(f'{linha[0]:<4}', end='\t')
                print(f'{linha[6]}', end='\t')
                print(f'   {linha[7]}', end='\t')
                print(f'       {linha[8]}', end='\t')
                print(f' {linha[9]}', end='\t')
                print(f'     {linha[10]}', end='\t\t')
                print(f'   {linha[11]}', end='\t\t\t\n')
                
                print('='*72)   
        # Exibe todos os registros do banco de dados da tabela de classificacao
        print('\n========= Exibição da Classificação de Sustentabilidade =========\n')
        print('ID  | Consumo de água | Consumo de energia | Lixo não reciclável | % de resíduos recicláveis |')
        print('-' * 95)  # Linha separadora do cabeçalho

        for linha in classifcacao:
            linha1  = descriptografia(linha[1])
            linha2  = descriptografia(linha[2])
            linha3  = descriptografia(linha[3])
            linha4  = descriptografia(linha[4])
            print(f'{str(linha[0]):<4}|      {linha1}       |        {linha2}        |        {linha3}         |            {linha4}       |')
            print('-' * 95)  # Linha separadora entre registros       
                 
        input('\n\t<< Tecle Enter para continuar >>')
        os.system('cls' if os.name == 'nt' else 'clear')   
        
    # Opção de que gera a média dos registros no banco de dados
    elif opcao == 5:
        print("=============================================================")
        print("                Relatorio da Média dos dados                 ")
        print("               Registrados no Banco de Dados                 ")
        print("=============================================================\n")

        # Puxa a média de todos os dados de água registrados na tabela
        cursor.execute("SELECT AVG(quantidadeAgua) FROM dadosConsumo")
        media_agua = cursor.fetchone()[0]
            
        # Classificão de sustentabilidade de água
        if media_agua < 150:
            print("Consumo de água: Alta Sustentabilidade")

        elif media_agua < 200:
            print("Consumo de água: Moderada Sustentabilidade")
                
        else:
            print("Consumo de água: Baixa Sustentabilidade")

        # Exibe a média de consumo água         
        print(f'Média do consumo de água: {media_agua:.2f} L\n') 

        # Puxa a média de todos os dados de energia registrados na tabela    
        cursor.execute("SELECT AVG(quantidadeEnergia) FROM dadosConsumo")
        mediaEnergia = cursor.fetchone()[0]
            
        # Classificão de sustentabilidade de energia
        if mediaEnergia < 5:
            print("Consumo de energia: Alta Sustentabilidade")
                
        elif mediaEnergia < 10:
            print("Consumo de energia: Moderada Sustentabilidade")
                
        else:
            print("Consumo de energia: Baixa Sustentabilidade")

        # Exibe a média de consumo energia     
        print(f'Média do consumo de energia: {mediaEnergia:.2f} kWh\n')

        # Puxa a média de todos os dados de lixo gerado
        cursor.execute("SELECT AVG(quantidaderResiduos) FROM dadosConsumo")
        mediaResiduo = cursor.fetchone()[0]

        # Puxa a média de todos os dados de porcentagem dos lixo reclicado    
        cursor.execute("SELECT AVG(quantidaderResiduos) FROM dadosConsumo")
        mediaPorcentagem = cursor.fetchone()[0]

        # Cálcula a porcentagem de lixos não reciclados   
        mediaNReciclado = (100 - mediaPorcentagem)

        # Classificão de sustentabilidade de residuos 
        if mediaNReciclado > 50:
            print("Geração de Resíduos Não Recicláveis: Baixa Sustentabilidade")
        
        elif mediaNReciclado > 20:
            print("Geração de Resíduos Não Recicláveis: Moderada Sustentabilidade")
                
        else:
            print("Geração de Resíduos Não Recicláveis: Alta Sustentabilidade")
        
        print(f'Média da porcentagem de resíduos recicláveis: {mediaNReciclado:.2f} %\n')

        # Puxa a média de todos os dados de porcentagem dos lixo reclicado    
        cursor.execute("SELECT publico, bicicleta, caminhada, carro, carroEletrico, carona FROM dadosConsumo")
        transporte = cursor.fetchall()

        countS = 0
        countN = 0
        countM = 0
        
        # Condição para verificar se a maioria dos transportes foram sustentáveis ou não
        for linha in transporte:
            if (linha[0] == "S" or linha[0] == "s") or (linha[1] == "S" or linha[1] == "s") or (linha[2] == "S" or linha[2] == "s") or (linha[4] == "S" or linha[4] == "s"):       
                if (linha[3] == "S" or linha[3] == "s") or (linha[5] == "S" or linha[5] == "s"):
                    countM += 1 
                else:
                    countS += 1
                    
            elif (linha[3] == "S" or linha[3] == "s") or (linha[5] == "S" or linha[5] == "s"):
                    countN += 1 
            else:
                countS += 1
        
        # Fala qual foi a maior parte dos transporte poluentes            
        if countS > countN:
            print(f'Maior uso de transporte: Transporte não sustentável')
            
        elif countS < countN:
            print(f'Maior uso de transporte: Transporte sustentável')    
            
        else: 
            print(f'Maior uso de transporte: Transporte moderado')  
              
        input('\n\t<< Tecle Enter para continuar >>')
        os.system('cls' if os.name == 'nt' else 'clear')      
                 
    elif opcao == 6:
        fim = 0