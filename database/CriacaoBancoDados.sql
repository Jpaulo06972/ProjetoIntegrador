CREATE DATABASE ProjetoIntegrador;
USE ProjetoIntegrador;

CREATE TABLE dadosConsumo(
	id INT AUTO_INCREMENT PRIMARY KEY,
    data VARCHAR(50) NOT NULL,
    quantidadeAgua DECIMAL(10, 2) NOT NULL,
    quantidadeEnergia DECIMAL(10, 2) NOT NULL,
	quantidaderResiduos DECIMAL(10, 2) NOT NULL,
    porcentagemResiduos DECIMAL(10, 2) NOT NULL,
    publico VARCHAR(5) NOT NULL,
    bicicleta VARCHAR(5) NOT NULL,
    caminhada VARCHAR(5) NOT NULL,
    carro VARCHAR(5) NOT NULL,
    carroEletrico VARCHAR(5) NOT NULL,
    carona VARCHAR(5) NOT NULL
);
SELECT * FROM dadosConsumo;

CREATE TABLE classificacao(
	id INT PRIMARY KEY,
    classificacaoAgua VARCHAR(100) NOT NULL,
    classificacaoEnergia VARCHAR(100) NOT NULL,
	classificacaoResiduo VARCHAR(100) NOT NULL,
    classificacaoTransporte VARCHAR(100) NOT NULL,
    FOREIGN KEY (id) REFERENCES dadosConsumo(id)
);

SELECT * FROM classificacao;
