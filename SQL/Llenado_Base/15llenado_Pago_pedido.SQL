REM INSERTING into Metodo_de_pago
SET DEFINE OFF;
--Metodo de pago PSE:
Insert into pago_pedido(K_PEDIDO,K_PAGO_PEDIDO, K_TIPOPAGO, F_PAGO,V_PAGO,I_ESTADO,N_OBSERVACION) values ('1',1,1,to_date('20/08/21','DD/MM/RR'),20000,'AUT',NULL);
Insert into pago_pedido(K_PEDIDO,K_PAGO_PEDIDO, K_TIPOPAGO, F_PAGO,V_PAGO,I_ESTADO,N_OBSERVACION)  values (2,1,1,to_date('21/08/21','DD/MM/RR'),6000,'AUT',NULL);
Insert into pago_pedido(K_PEDIDO,K_PAGO_PEDIDO, K_TIPOPAGO, F_PAGO,V_PAGO,I_ESTADO,N_OBSERVACION)  values (5,1,1,to_date('22/08/21','DD/MM/RR'),5000,'AUT',NULL);

--Metodo de pago Tarjeta de credito:
Insert into pago_pedido(K_PEDIDO,K_PAGO_PEDIDO, K_TIPOPAGO, F_PAGO,V_PAGO,I_ESTADO,N_OBSERVACION)  values ('3',1,2,to_date('22/08/21','DD/MM/RR'),1800,'AUT',NULL);
Insert into pago_pedido(K_PEDIDO,K_PAGO_PEDIDO, K_TIPOPAGO, F_PAGO,V_PAGO,I_ESTADO,N_OBSERVACION)  values (4,1,2,to_date('22/08/21','DD/MM/RR'),900,'AUT',NULL);