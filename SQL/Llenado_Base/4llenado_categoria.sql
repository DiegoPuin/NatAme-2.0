REM INSERTING into categoria
SET DEFINE OFF;
--Categorias
Insert into categoria(K_CATEGORIA,N_NOMCATEGORIA) values ('100','Hogar');
Insert into categoria(K_CATEGORIA,N_NOMCATEGORIA) values ('200','Nutricion');
Insert into categoria(K_CATEGORIA,N_NOMCATEGORIA) values ('300','Belleza');
Insert into categoria(K_CATEGORIA,N_NOMCATEGORIA) values ('400','Cuidado personal');

--Categoria Hogar
Insert into categoria(K_CATEGORIA,N_NOMCATEGORIA,K_CATEGORIA_PERTENECE) values ('101','Lavanderia','100');
Insert into categoria(K_CATEGORIA,N_NOMCATEGORIA,K_CATEGORIA_PERTENECE) values ('102','Limpieza de pisos','100');
Insert into categoria(K_CATEGORIA,N_NOMCATEGORIA,K_CATEGORIA_PERTENECE) values ('103','Desinfectantes','100');

--Categoria Nutricion
Insert into categoria(K_CATEGORIA,N_NOMCATEGORIA,K_CATEGORIA_PERTENECE) values ('201','Snacks','200');
Insert into categoria(K_CATEGORIA,N_NOMCATEGORIA,K_CATEGORIA_PERTENECE) values ('202','Bebidas','200');
Insert into categoria(K_CATEGORIA,N_NOMCATEGORIA,K_CATEGORIA_PERTENECE) values ('203','Confiteria','200');

--Categoria Belleza
Insert into categoria(K_CATEGORIA,N_NOMCATEGORIA,K_CATEGORIA_PERTENECE) values ('301','Perfumeria','300');
Insert into categoria(K_CATEGORIA,N_NOMCATEGORIA,K_CATEGORIA_PERTENECE) values ('302','Corte y peluqueria','300');
Insert into categoria(K_CATEGORIA,N_NOMCATEGORIA,K_CATEGORIA_PERTENECE) values ('303','Cosmeticos','300');

--Categoria Cuidado personal
Insert into categoria(K_CATEGORIA,N_NOMCATEGORIA,K_CATEGORIA_PERTENECE) values ('401','Salud','400');
Insert into categoria(K_CATEGORIA,N_NOMCATEGORIA,K_CATEGORIA_PERTENECE) values ('402','Vitaminas','400');