CREATE OR REPLACE FUNCTION insertVeiculo()
RETURNS TRIGGER AS $$
BEGIN
    NEW.renavam := gerar_renavam(NEW.placa);
    RETURN NEW;
END; $$
LANGUAGE plpgsql;

CREATE TRIGGER tgInsertVeiculo
BEFORE INSERT ON veiculo
FOR EACH ROW
EXECUTE PROCEDURE insertVeiculo();