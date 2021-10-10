REM INSERTING into pedido
SET DEFINE OFF;
--pedido:
Insert into pedido(K_PEDIDO, F_PEDIDO, F_LLEGADA, I_ESTADO, Q_VALORT, K_TIPOID, K_IDENTIFICACION ) values ('1',to_date('20/08/21','DD/MM/RR'),to_date('23/08/21','DD/MM/RR'),'ENT','20000','CC','21111');
Insert into pedido(K_PEDIDO, F_PEDIDO, F_LLEGADA, I_ESTADO, Q_VALORT, K_TIPOID, K_IDENTIFICACION ) values ('2',to_date('21/08/21','DD/MM/RR'),to_date('23/08/21','DD/MM/RR'),'ENT','6000','CC','21112');
Insert into pedido(K_PEDIDO, F_PEDIDO, F_LLEGADA, I_ESTADO, Q_VALORT, K_TIPOID, K_IDENTIFICACION ) values ('3',to_date('22/08/21','DD/MM/RR'),to_date('23/08/21','DD/MM/RR'),'ENT','1800','CC','21113');
Insert into pedido(K_PEDIDO, F_PEDIDO, F_LLEGADA, I_ESTADO, Q_VALORT,K_TIPOID, K_IDENTIFICACION ) values ('4',to_date('22/08/21','DD/MM/RR'),to_date('23/08/21','DD/MM/RR'),'ENT','900','CC','21111');
Insert into pedido(K_PEDIDO, F_PEDIDO, F_LLEGADA, I_ESTADO, Q_VALORT, K_TIPOID, K_IDENTIFICACION ) values ('5',to_date('22/08/21','DD/MM/RR'),'','PAG','5000','CC','21112');