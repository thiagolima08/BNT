CREATE VIEW condutor_com_pontos AS
(
	SELECT con.idCadastro,con.nome,con.idcategoria_cnh,date_part('YEAR',mul.dataInfracao),inf.pontos
	FROM condutor con JOIN multa mul ON con.idCadastro = mul.idCondutor JOIN infracao inf ON inf.idinfracao = mul.idinfracao
	WHERE inf.pontos > 0
);

CREATE VIEW veiculos_proprietarios AS
(
	SELECT vei.renavam,vei.placa,con.nome,mod.denominacao,mar.nome,cid.nome,est.nome,tip.descricao
	FROM veiculo vei JOIN condutor con ON vei.idProprietario = con.idCadastro JOIN modelo mod ON mod.idModelo=vei.idModelo JOIN marca mar ON mar.idMarca=mod.idMarca JOIN cidade cid ON cid.idCidade=vei.idCidade JOIN estado est ON est.uf=cid.uf JOIN tipo tip ON tip.idTipo=mod.idTipo

);

CREATE VIEW num_infracoes_e_valores_multas AS
(
	SELECT COUNT(inf.idinfracao), SUM(mul.valor)
	FROM infracao inf JOIN multa mul ON inf.idinfracao = mul.idinfracao 
);
