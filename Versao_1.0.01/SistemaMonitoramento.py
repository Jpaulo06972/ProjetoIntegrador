# Sistema de Monitoramento de Sustentabilidade
print("=============================================================")
print("                 Sistema de Monitoramento                    ")
print("                      Sustentavel                            ")
print("=============================================================")
# Coleta as informções do usuário sobre sua sustentabilidade
date = input("Digite a Data de Hoje: ")
qtdAgua = float(input("Digite seu consumo de água (Aprox. em Litros): ")) 
qtdEnergia = float(input("Digite seu consumo de energia (kWh): ")) 
qtdResiduo = float(input("Digite seu consumo de resíduos não reciclados (Kg): ")) 
porReciclado = int(input("Digite a porcentagem de resíduos reciclados (%): "))

print("Digite qual o meio de transporte você usou hoje? (S/N)")

publico = input("1. Transporte público(Ônibus, metrô, trem): ")
bicicleta = input("2. Bicicleta: ")
caminhada = input("3. Caminhada: ")
carro = input("4. Carro (Combustível fósseis): ")
carroEletrico = input("5. Carro elétrico: ")
carona = input("6. Carona compartilhada(Fósseies): ")
print("------------------------------------------------------")
print(f"Data: {date}")

# Classificão de sustentabilidade de água
if qtdAgua < 150:
    print("Consumo de água: Alta Sustentabilidade")

elif qtdAgua < 200:
    print("Consumo de água: Moderada Sustentabilidade")
    
else:
    print("Consumo de água: Baixa Sustentabilidade")

# Classificão de sustentabilidade de energia
if qtdEnergia < 5:
    print("Consumo de energia: Alta Sustentabilidade")

elif qtdAgua < 10:
    print("Consumo de energia: Moderada Sustentabilidade")

else:
    print("Consumo de energia: Baixa Sustentabilidade")

# Classificão de sustentabilidade dos resíduos
porNReciclado = (100 - porReciclado)

if porNReciclado > 50:
    print("Geração de Resíduos Não Recicláveis: Baixa Sustentabilidade")

elif porNReciclado > 20:
    print("Geração de Resíduos Não Recicláveis: Moderada Sustentabilidade")
    
else:
    print("Geração de Resíduos Não Recicláveis: Alta Sustentabilidade")

# Uso de transporte
if (publico == "S" or publico == "s") or (bicicleta == "S" or bicicleta == "s") or (caminhada == "S" or caminhada == "s") or (carroEletrico == "S" or carroEletrico == "s"):
    if (carro == "S" or carro == "s") or (carona == "S" or carona =="s"):  
        print("Uso de Transporte: Moderado Sustentabilidade")
    else:
        print("Uso de Transporte: Alta Sustentabilidade")

elif (carro == "S" or carro == "s") or (carona == "S" or carona == "s"):
        
    print("Uso de Transporte: Baixa Sustentabilidade")
