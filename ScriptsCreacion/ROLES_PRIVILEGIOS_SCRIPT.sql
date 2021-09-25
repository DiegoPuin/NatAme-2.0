
-- CREACIÓN DE ROLES 

--Rol Cliente
CREATE ROLE rol_cliente;
GRANT CONNECT TO rol_cliente;
GRANT select ON natame.representante_cliente TO rol_cliente;
GRANT select,insert,update ON natame.metodo_de_pago TO rol_cliente;
GRANT select,insert ON natame.pedido TO rol_cliente;
GRANT select,insert ON natame.item TO rol_cliente;
GRANT select,insert,update ON natame.cliente TO rol_cliente;
GRANT select ON natame.producto TO rol_cliente;
GRANT select ON natame.categoria TO rol_cliente;


--Rol Representante
CREATE ROLE rol_representante;
GRANT CONNECT TO rol_representante;
GRANT select ON natame.cliente TO rol_representante;
GRANT select ON natame.representante_cliente TO rol_representante;
GRANT select ON natame.pedido TO rol_representante;
GRANT select ON natame.categoria_representante TO rol_representante;
GRANT select ON natame.representante TO rol_representante;
GRANT select ON natame.pais TO rol_representante;
GRANT select ON natame.region TO rol_representante;
GRANT select ON natame.producto TO rol_representante;
GRANT select ON natame.categoria TO rol_representante;

--Rol Representante_Master
CREATE ROLE rol_representante_master;
GRANT CONNECT TO rol_representante_master;
GRANT CREATE USER TO rol_representante_master;
GRANT ALTER USER TO rol_representante_master;
GRANT select,insert,update ON natame.cliente TO rol_representante_master;
GRANT select,insert ON natame.representante_cliente TO rol_representante_master;
GRANT select,insert,update ON natame.pedido TO rol_representante_master;
GRANT select,insert,update ON natame.categoria_representante TO rol_representante_master;
GRANT select,insert,update ON natame.representante TO rol_representante_master;
GRANT select,insert,update ON natame.pais TO rol_representante_master;
GRANT select,insert,update ON natame.region TO rol_representante_master;
GRANT select,insert,update ON natame.producto TO rol_representante_master;
GRANT select,insert,update ON natame.categoria TO rol_representante_master;

--Rol DBA
CREATE ROLE dba_natame;
GRANT ALL PRIVILEGES TO dba_natame ;


--CREACIÓN USUARIOS:

-- Table Space de clientes
CREATE TABLESPACE natameCli DATAFILE 'C:\oraclexe\app\oracle\oradata\XE\natameCli.dbf' SIZE 3m AUTOEXTEND ON;
CREATE TEMPORARY TABLESPACE natameCliTmp TEMPFILE 'C:\oraclexe\app\oracle\oradata\XE\natameCliTMP.DBF' SIZE 2M AUTOEXTEND ON;


--representantes
CREATE USER jrod IDENTIFIED BY 1234 DEFAULT TABLESPACE natameCli TEMPORARY TABLESPACE natameCliTMP QUOTA 2M ON natamedef PASSWORD EXPIRE;
CREATE USER jrig IDENTIFIED BY 1234 DEFAULT TABLESPACE natameCli TEMPORARY TABLESPACE natameCliTMP QUOTA 2M ON natamedef PASSWORD EXPIRE;
CREATE USER Eherr IDENTIFIED BY 1234 DEFAULT TABLESPACE natameCli TEMPORARY TABLESPACE natameCliTMP QUOTA 2M ON natamedef PASSWORD EXPIRE;

GRANT rol_representante TO jrod ;
GRANT rol_representante TO jrig ;
GRANT rol_representante TO Eherr ;

--clientes
CREATE USER clop IDENTIFIED BY 1234 DEFAULT TABLESPACE natameCli TEMPORARY TABLESPACE natameCliTMP QUOTA 2M ON natamedef PASSWORD EXPIRE;
CREATE USER dtorr IDENTIFIED BY 1234 DEFAULT TABLESPACE natameCli TEMPORARY TABLESPACE natameCliTMP QUOTA 2M ON natamedef PASSWORD EXPIRE;
CREATE USER drio IDENTIFIED BY 1234 DEFAULT TABLESPACE natameCli TEMPORARY TABLESPACE natameCliTMP QUOTA 2M ON natamedef PASSWORD EXPIRE;

GRANT rol_cliente TO clop;
GRANT rol_cliente TO dtorr;
GRANT rol_cliente TO drio;

--cliente que se vuelve representante:
--GRANT rol_representante TO jrod ;  (Forma de hacerlo, no correr comando)

--representantes que se vuelve Master
--GRANT rol_representante TO jrod ; -- (no es master aún, no correr)



