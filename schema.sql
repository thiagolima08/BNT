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
    FOREIGN KEY (idTipo) REFERENCES marca (idTipo)
    FOREIGN KEY (idTipo) REFERENCES tipo (idTipo)
);
