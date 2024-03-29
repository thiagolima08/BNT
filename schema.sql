DROP TABLE IF EXISTS estado CASCADE;
DROP TABLE IF EXISTS cidade CASCADE;
DROP TABLE IF EXISTS tipo CASCADE;
DROP TABLE IF EXISTS marca CASCADE;
DROP TABLE IF EXISTS modelo CASCADE;
DROP TABLE IF EXISTS categoria_cnh CASCADE;
DROP TABLE IF EXISTS condutor CASCADE;
DROP TABLE IF EXISTS especie CASCADE;
DROP TABLE IF EXISTS categoria_veiculo CASCADE;
DROP TABLE IF EXISTS veiculo CASCADE;
DROP TABLE IF EXISTS licenciamento CASCADE;
DROP TABLE IF EXISTS transferencia CASCADE;
DROP TABLE IF EXISTS infracao CASCADE;
DROP TABLE IF EXISTS multa CASCADE;

CREATE TABLE estado (
    uf   CHAR (2)     NOT NULL,
    nome VARCHAR (40) NOT NULL,

    PRIMARY KEY (uf)
);

CREATE TABLE cidade (
    idCidade CHAR (3)     NOT NULL,
    nome     VARCHAR (50) NOT NULL,
    uf       CHAR (2)     NOT NULL,

    PRIMARY KEY (idCidade),
    FOREIGN KEY (uf)       REFERENCES estado (uf)
);

CREATE TABLE tipo (
    idTipo    INTEGER      NOT NULL,
    descricao VARCHAR (30) NOT NULL,

    PRIMARY KEY (idTipo)
);

CREATE TABLE marca (
    idMarca INTEGER      NOT NULL,
    nome    VARCHAR (40) NOT NULL,
    origem  VARCHAR (40) NOT NULL,

    PRIMARY KEY (idMarca)
);

CREATE TABLE modelo (
    idModelo    INTEGER      NOT NULL,
    denominacao VARCHAR (40) NOT NULL,
    idMarca     INTEGER      NOT NULL,
    idTipo      INTEGER      NOT NULL,

    PRIMARY KEY (idModelo),
    FOREIGN KEY (idMarca)  REFERENCES marca (idMarca),
    FOREIGN KEY (idTipo)   REFERENCES tipo (idTipo)
);


CREATE TABLE categoria_cnh (
    idCategoriaCNH CHAR (4) NOT NULL,
    descricao      TEXT     NOT NULL,

    PRIMARY KEY (idCategoriaCNH)
);

CREATE TABLE condutor (
    idCadastro     INTEGER   NOT NULL,
    cpf            CHAR (11) NOT NULL,
    nome           CHAR (50) NOT NULL,
    dataNasc       DATE      NOT NULL CHECK (extract(year from age(dataNasc)) >= 18),
    idCategoriaCNH CHAR (3)  NOT NULL,
    endereco       CHAR (50) NOT NULL,
    bairro         CHAR (50) NOT NULL,
    idCidade       CHAR (3)  NOT NULL,
    situacaoCNH    CHAR (1)  NOT NULL DEFAULT 'R' CHECK (situacaoCNH = 'R' OR situacaoCNH = 'S'),

    PRIMARY KEY (idCadastro),
    FOREIGN KEY (idCategoriaCNH) REFERENCES categoria_cnh (idCategoriaCNH),
    FOREIGN KEY (idCidade)       REFERENCES cidade (idCidade)
);

CREATE TABLE especie (
    idEspecie INTEGER      NOT NULL,
    descricao VARCHAR (30) NOT NULL,

    PRIMARY KEY (idEspecie)
);

CREATE TABLE categoria_veiculo (
    idCategoria INTEGER     NOT NULL,
    descricao   VARCHAR(30) NOT NULL,
    idEspecie   INTEGER     NOT NULL,

    PRIMARY KEY (idCategoria),
    FOREIGN KEY (idEspecie)  REFERENCES especie (idEspecie)
);

CREATE TABLE veiculo (
    renavam        CHAR (13) NOT NULL,
    placa          CHAR (7)  NOT NULL,
    ano            INTEGER   NOT NULL,
    idCategoria    INTEGER   NOT NULL,
    idProprietario INTEGER   NOT NULL,
    idModelo       INTEGER   NOT NULL,
    idCidade       CHAR (3)  NOT NULL,
    dataCompra     DATE      NOT NULL,
    dataAquisicao  DATE      NOT NULL,
    valor          FLOAT     NOT NULL,
    situacao       CHAR (1)  NOT NULL DEFAULT 'R' CHECK (situacao = 'R' OR situacao = 'I' OR situacao = 'B'),

    PRIMARY KEY (renavam),
    FOREIGN KEY (idCategoria)    REFERENCES categoria_veiculo(idCategoria),
    FOREIGN KEY (idProprietario) REFERENCES condutor(idCadastro),
    FOREIGN KEY (idModelo)       REFERENCES modelo(idModelo),
    FOREIGN KEY (idCidade)       REFERENCES cidade(idCidade)
);

CREATE TABLE licenciamento (
    ano      INTEGER   NOT NULL,
    renavam  CHAR (13) NOT NULL,
    dataVenc DATE      NOT NULL,
    pago     CHAR (1)  NOT NULL DEFAULT 'N' CHECK (pago = 'S' OR pago = 'N'),

    PRIMARY KEY (ano, renavam),
    FOREIGN KEY (renavam)      REFERENCES veiculo(renavam)
);

CREATE TABLE transferencia (
    idHistorico    INTEGER   NOT NULL,
    renavam        CHAR (13) NOT NULL,
    idProprietario INTEGER   NOT NULL,
    dataCompra     DATE      NOT NULL,
    dataVenda      DATE      NULL,

    PRIMARY KEY (idHistorico),
    FOREIGN KEY (renavam)        REFERENCES veiculo(renavam),
    FOREIGN KEY (idProprietario) REFERENCES condutor(idCadastro)
);

CREATE TABLE infracao (
    idInfracao INTEGER       NOT NULL,
    descricao  VARCHAR (150) NOT NULL,
    valor      NUMERIC       NOT NULL,
    pontos     INTEGER       NOT NULL,

    PRIMARY KEY (idInfracao)
);

CREATE TABLE multa (
    idMulta        INTEGER   NOT NULL,
    renavam        CHAR (13) NOT NULL,
    idInfracao     INTEGER   NOT NULL,
    idCondutor     INTEGER   NOT NULL,
    dataInfracao   DATE      NOT NULL,
    dataVencimento DATE      NOT NULL,
    dataPagamento  DATE      NULL,
    valor          NUMERIC   NOT NULL,
    juros          NUMERIC   NOT NULL DEFAULT 0.0,
    valorFinal     NUMERIC   NOT NULL DEFAULT 0.0,
    pago           CHAR (1)  NOT NULL DEFAULT 'N' CHECK (pago = 'S' OR pago = 'N'),

    PRIMARY KEY (idMulta),
    FOREIGN KEY (renavam)    REFERENCES veiculo(renavam),
    FOREIGN KEY (idInfracao) REFERENCES infracao(idInfracao),
    FOREIGN KEY (idCondutor) REFERENCES condutor(idCadastro)
);
