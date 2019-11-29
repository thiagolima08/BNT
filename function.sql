DROP FUNCTION IF EXISTS historico_transacao;
CREATE OR REPLACE FUNCTION historico_transacao (ren CHAR(13))
RETURNS TABLE (
    "Renavam"        CHAR(13),
    "Modelo"         VARCHAR(40),
    "Marca"          VARCHAR(40),
    "Ano"            INTEGER,
    "Proprietário"   CHAR(50),
    "Data de compra" DATE,
    "Data de Venda"  DATE
)
AS $$
BEGIN
    RETURN QUERY SELECT
        vei.renavam "Renavam",
        mod.denominacao "Modelo",
        mar.nome "Marca",
        vei.ano "Ano",
        con.nome "Proprietário",
        tra.dataCompra "Data de compra",
        tra.dataVenda "Data de Venda"
    from transferencia tra
    LEFT JOIN veiculo vei ON vei.renavam = tra.renavam
    LEFT JOIN condutor con ON tra.idProprietario = con.idCadastro
    LEFT JOIN modelo mod ON mod.idModelo=vei.idModelo
    LEFT JOIN marca mar ON mar.idMarca=mod.idMarca
    WHERE vei.renavam = ren
    UNION
    SELECT
        vei.renavam "Renavam",
        mod.denominacao "Modelo",
        mar.nome "Marca",
        vei.ano "Ano",
        con.nome "Proprietário",
        vei.dataCompra "Data de compra",
        vei.dataAquisicao "Data de Venda"
    FROM veiculo vei
    LEFT JOIN condutor con ON vei.idProprietario = con.idCadastro
    LEFT JOIN modelo mod ON mod.idModelo=vei.idModelo
    LEFT JOIN marca mar ON mar.idMarca=mod.idMarca
    WHERE vei.renavam = ren
    ORDER BY "Data de Venda";
END; $$
LANGUAGE plpgsql;

DROP FUNCTION IF EXISTS gerar_dv;
CREATE OR REPLACE FUNCTION gerar_dv (num CHAR(10))
RETURNS CHAR(1)
AS $$
DECLARE
    somador  INTEGER := 0;
    n        INTEGER := 0;
    m        INTEGER := 0;
    contador INTEGER := 1;
BEGIN
    LOOP 
        EXIT WHEN contador > 10;
        n := CAST(SUBSTRING(num, contador, 1) AS INTEGER);
        m := CAST(SUBSTRING('3298765432', contador, 1) AS INTEGER);
        somador := somador + (n * m);
        contador := contador + 1 ; 
    END LOOP ; 

    RETURN CAST(((somador * 10) % 11) % 10 AS CHAR(1));
END; $$
LANGUAGE plpgsql;

DROP FUNCTION IF EXISTS gerar_renavam;
CREATE OR REPLACE FUNCTION gerar_renavam (pla CHAR(7))
RETURNS CHAR(13)
AS $$
DECLARE
    acumulador  char(10);
BEGIN
    acumulador := CONCAT(
        CAST(ASCII(UPPER(SUBSTRING(pla, 1, 1))) AS CHAR(2)),
        CAST(ASCII(UPPER(SUBSTRING(pla, 2, 1))) AS CHAR(2)),
        CAST(ASCII(UPPER(SUBSTRING(pla, 3, 1))) AS CHAR(2)),
        SUBSTRING(PLA, 4, 4)
    );
    RETURN CONCAT(acumulador, gerar_dv(acumulador));
END; $$
LANGUAGE plpgsql;

DROP FUNCTION IF EXISTS gerar_data_licenciamento;
CREATE OR REPLACE FUNCTION gerar_data_licenciamento (pla CHAR(7), ano CHAR(4))
RETURNS DATE
AS $$
BEGIN
    CASE SUBSTRING(pla, 7, 1)
        WHEN '1' THEN
            RETURN CONCAT(ano, '-03-31');
        WHEN '2' THEN
            RETURN CONCAT(ano, '-04-30');
        WHEN '3' THEN
            RETURN CONCAT(ano, '-05-31');
        WHEN '4' THEN
            RETURN CONCAT(ano, '-06-30');
        WHEN '5' THEN
            RETURN CONCAT(ano, '-07-31');
        WHEN '6' THEN
            RETURN CONCAT(ano, '-08-31');
        WHEN '7' THEN
            RETURN CONCAT(ano, '-09-30');
        WHEN '8' THEN
            RETURN CONCAT(ano, '-10-31');
        WHEN '9' THEN
            RETURN CONCAT(ano, '-11-30');
        WHEN '0' THEN
            RETURN CONCAT(ano, '-12-31');
    END CASE;
END; $$
LANGUAGE plpgsql;