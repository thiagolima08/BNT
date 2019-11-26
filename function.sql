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
    WHERE vei.renavam = ren;
END; $$
LANGUAGE plpgsql;
