CREATE VIEW condutor_com_pontos AS
(
	SELECT
		con.idCadastro,
		con.nome "Nome do condutor",
		con.idcategoriacnh "Categoria",
		date_part('YEAR', mul.dataInfracao) "Ano da infração",
		SUM(inf.pontos) "Pontos"
	FROM condutor con
	INNER JOIN multa mul ON con.idCadastro = mul.idCondutor
	LEFT JOIN infracao inf ON inf.idinfracao = mul.idinfracao
	GROUP BY 
		date_part('YEAR', mul.dataInfracao),
		con.idCadastro
);

CREATE VIEW veiculos_proprietarios AS
(
	SELECT
		vei.renavam "Renavam",
		vei.placa "Placa",
		con.nome "Proprietário",
		mod.denominacao "Modelo",
		mar.nome "Marca",
		cid.nome "Cidade",
		est.nome "Estado",
		tip.descricao "Tipo"
	FROM veiculo vei
	LEFT JOIN condutor con ON vei.idProprietario = con.idCadastro
	LEFT JOIN modelo mod ON mod.idModelo=vei.idModelo
	LEFT JOIN marca mar ON mar.idMarca=mod.idMarca
	LEFT JOIN tipo tip ON tip.idTipo=mod.idTipo
	LEFT JOIN cidade cid ON cid.idCidade=vei.idCidade
	LEFT JOIN estado est ON est.uf=cid.uf
);

CREATE VIEW num_infracoes_e_valores_multas AS
(
	SELECT
		date_part('YEAR', mul.dataInfracao) "Ano",
		date_part('MONTH', mul.dataInfracao) "Mês",
		COUNT(inf.idinfracao) "Quantidade de infrações",
		SUM(mul.valor) "Valor total de multas"
	FROM multa mul
	LEFT JOIN infracao inf ON inf.idinfracao = mul.idinfracao
	GROUP BY 
		date_part('YEAR', mul.dataInfracao),
		date_part('MONTH', mul.dataInfracao)
);