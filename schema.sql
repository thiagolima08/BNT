DROP TABLE IF EXISTS proprietario;
DROP TABLE IF EXISTS categoria_cnh;
DROP TABLE IF EXISTS especie;
DROP TABLE IF EXISTS modelo;
DROP TABLE IF EXISTS marca;
DROP TABLE IF EXISTS tipo;
DROP TABLE IF EXISTS cidade;
DROP TABLE IF EXISTS estado;

CREATE TABLE estado (
    uf       CHAR 	 (2)  NOT NULL,
    nome     VARCHAR (50) NOT NULL,
    PRIMARY KEY (uf)
);

CREATE TABLE cidade (
    idCidade CHAR 	 (3)  NOT NULL,
    nome     VARCHAR (50) NOT NULL,
    uf       CHAR 	 (2)  NOT NULL,
    PRIMARY KEY (idCidade),
    FOREIGN KEY (uf) REFERENCES estado (uf)
);

CREATE TABLE tipo (
    idTipo    INTEGER      NOT NULL,
    descricao VARCHAR (30) NOT NULL,
    PRIMARY KEY (idTipo)
);

CREATE TABLE marca (
    idMarca   INTEGER      NOT NULL,
    nome      VARCHAR (40) NOT NULL,
    origem    VARCHAR (40) NOT NULL,
    PRIMARY KEY (idMarca)
);

CREATE TABLE modelo (
    idModelo    INTEGER      NOT NULL,
    denominacao VARCHAR (40) NOT NULL,
    idMarca     INTEGER      NOT NULL,
    idTipo      INTEGER      NOT NULL,
    PRIMARY KEY (idModelo),
    FOREIGN KEY (idMarca) REFERENCES marca (idMarca),
    FOREIGN KEY (idTipo) REFERENCES tipo (idTipo)
);

CREATE TABLE especie (
    idEspecie INTEGER      NOT NULL,
    descricao VARCHAR (30) NOT NULL,
    PRIMARY KEY (idEspecie)
);

CREATE TABLE categoria_cnh (
    idCategoriaCNH CHAR (3) NOT NULL,
    descricao      TEXT     NOT NULL,
    PRIMARY KEY (idCategoriaCNH)
);

CREATE TABLE proprietario (
    idCadastro     INTEGER   NOT NULL,
    cpf            CHAR (11) NOT NULL,
    nome           CHAR (50) NOT NULL,
    dataNasc       DATE      NOT NULL,
    idCategoriaCNH CHAR (3)  NOT NULL,
    endereco       CHAR (50) NOT NULL,
    bairro         CHAR (30) NOT NULL,
    idCidade       CHAR (3)  NOT NULL,
    situacaoCNH    CHAR (1)  NOT NULL,
    PRIMARY KEY(idCadastro),
    FOREIGN KEY (idCategoriaCNH) REFERENCES categoria_cnh (idCategoriaCNH),
    FOREIGN KEY (idCidade) REFERENCES cidade (idCidade)
);
