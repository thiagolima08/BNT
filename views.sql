CREATE VIEW condutor_com_pontos AS
(
	SELECT con.idCadastro,con.nome "Nome do condutor",con.idcategoria_cnh "Categoria", date_part('YEAR',mul.dataInfracao) "Ano da infração", inf.pontos "Pontos"
	FROM condutor con JOIN multa mul ON con.idCadastro = mul.idCondutor JOIN infracao inf ON inf.idinfracao = mul.idinfracao
	WHERE inf.pontos > 0
);

CREATE VIEW veiculos_proprietarios AS
(
	SELECT vei.renavam Renavam,vei.placa Placa,con.nome Proprietário,mod.denominacao Modelo,mar.nome Marca,cid.nome Cidade,est.nome Estado,tip.descricao Tipo
	FROM veiculo vei JOIN condutor con ON vei.idProprietario = con.idCadastro JOIN modelo mod ON mod.idModelo=vei.idModelo JOIN marca mar ON mar.idMarca=mod.idMarca JOIN cidade cid ON cid.idCidade=vei.idCidade JOIN estado est ON est.uf=cid.uf JOIN tipo tip ON tip.idTipo=mod.idTipo
);

CREATE VIEW num_infracoes_e_valores_multas AS
(
	SELECT COUNT(inf.idinfracao) "Quantidade de infrações", SUM(mul.valor) "Valor total de multas"
	FROM infracao inf JOIN multa mul ON inf.idinfracao = mul.idinfracao 
);
