CREATE DATABASE eco_system;

USE eco_system;

CREATE TABLE users(
    username varchar(20) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE logs( 
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE usuarios_eco( 
    id_usuario_eco int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre varchar(50) NOT NULL,
    descripcion text NOT NULL,
    imagen mediumblob null
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE guardado(
    id_guardado int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_usuario_eco  int     not null,
    FOREIGN KEY (id_usuario_eco) REFERENCES usuarios_eco(id_usuario_eco));
    

CREATE TABLE post(
    id_post int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Titulo  varchar(50) not null,
    descripcion text    not null,
    procedimiento   LONGTEXT   not null,
    link_video  varchar(100) null,
    imagen_p mediumblob,
    id_usuario_eco   int null,
    FOREIGN KEY (id_usuario_eco) REFERENCES usuarios_eco(id_usuario_eco));

CREATE TABLE comentarios(
    id_comentario int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_post int not null,
    fecha_comentario    timestamp NOT NULL default current_timestamp,
    comentario  text    not null,
    FOREIGN KEY (id_post) REFERENCES post(id_post));


INSERT INTO clientes(nombre,apellido_paterno,apellido_materno,telefono,email)VALUES(
    'Andres','Masel','Calamaro','7775912409','andy@gmail.com'),
    ('Alejandro','Lora','Serna','7710927169','Alex@gmail.com'));

INSERT INTO usuarios_eco(nombre,descripcion,imagen)VALUES(
    'Alejandro Lora Serna','Soy una persona dedicada y preocupada por la ecologia',0xffd8ffe1086a4578696600004d4d002a00000008000c0100000300000001021c000001010003000000010168000001020003000000030000009e010600030000000100020000011200030000000100010000011500030000000100030000011a000500000001000000a4011b000500000001000000ac012800030000000100020000013100020000001e000000b40132000200000014000000d28769000400000001000000e800000120000800080008000afc8000002710000afc800000271041646f62652050686f746f73686f7020435335204d6163696e746f736800323031323a30383a30392031393a35303a32370000000004900000070000000430323231a001000300000001ffff0000a00200040000000100000040a0030004000000010000002b0000000000000006010300030000000100060000011a0005000000010000016e011b0005000000010000017601280003000000010002000002010004000000010000017e0202000400000001000006e40000000000000048000000010000004800000001ffd8ffed000c41646f62655f434d0001ffee000e41646f626500648000000001ffdb0084000c08080809080c09090c110b0a0b11150f0c0c0f1518131315131318110c0c0c0c0c0c110c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c010d0b0b0d0e0d100e0e10140e0e0e14140e0e0e0e14110c0c0c0c0c11110c0c0c0c0c0c110c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0cffc0001108002b004003012200021101031101ffdd00040004ffc4013f0000010501010101010100000000000000030001020405060708090a0b0100010501010101010100000000000000010002030405060708090a0b1000010401030204020507060805030c33010002110304211231054151611322718132061491a1b14223241552c16233347282d14307259253f0e1f163733516a2b283264493546445c2a3743617d255e265f2b384c3d375e3f3462794a485b495c4d4e4f4a5b5c5d5e5f55666768696a6b6c6d6e6f637475767778797a7b7c7d7e7f711000202010204040304050607070605350100021103213112044151617122130532819114a1b14223c152d1f0332462e1728292435315637334f1250616a2b283072635c2d2449354a317644555367465e2f2b384c3d375e3f34694a485b495c4d4e4f4a5b5c5d5e5f55666768696a6b6c6d6e6f62737475767778797a7b7c7ffda000c03010002110311003f00a54be87580bac76f33b86d00c7f2bfac8ce18e319d6ed6c35a4c82396fc1131b07a77a3e83aa0c6ee364804ebf4366e10ef737feb6a36d5d0f1ded19b458d65c76b6c63b6b476d9608f63bdff491e304e96ae02059adbf96ed0fb55cda28b5d535a2d1bc03bb8d4782953664597b68156e2fafd4afbcb78fce5a2d387974bb130f1def3530b6bb7793ed07dbb7706b509dd3ebe94dc7ead65c2fac1734570edcdf59a766e73bd9b697fb93c4c51d2a5ad0ff00a2b0c48235b1a5ff00dd31a68cb74d81ad15b7e93b968207bf7b5a538c86319b3663bc1893b1ed718fe53dcdff00a28dd32ee99f688c6c92eb2c747a4e00469be6a6eddbb7dbf4f72b99b4630baa71b7640dbb3da18fe4359ed1bb7ee29867468ae1115a105c6df7ed7346350e8246e735c5c07943be8a8331ad226c0dda4c08246be5ee5af760e15a6c76ddd60d7731c43bf366bfe56cff00bfaa97b7a7575576b37bed7bc7a6d125cd046fd9639a7daed9fc84e196f651c63abfffd07a3270f2f65acb0d62802cc861dcfd5cd0e75564bb77b15db3a861558b4b5a583ed6f7d16003b0dc6a7be7f35ec1f9ca87d60c3cc7b6fcfaf662dad68634541ad0f692e18e2e2ff4fe96fdbbd6574ccff585bd3fa9543ed8c78a9d8ee90d702dfe73f7133878858fb3f482eba344f4d3b37d83170ae6b29c87575102c38cc87b9931ee67fc1e9fcdb969e464e337a26fb6a37b5f5b5b5b62497fd0668b987e574fbb3270f731eda5edc80f739e43c39ad9fd27e66d1ec6a9e7bf2fad74dc3a3a417d8fc4fe90f1fa3125a367b5c5bf9eddcc4fe1b96a6b6b258f8b4fa2560fb365df750c1b718df00f6896d7fcafe4aaf85f5ada72451d42bdce0f606130e6b0b493bffe92274de8b9b631f8d75be8656396beef5017176fdce6fb98f72e73a8d7663f5ac863dcd16d57c4b64374882d5246313609b35ba0c8f6a0f69d3fa874dcc6db98ec6b5cd25ed1e9b83b69d37643ab7b9beebbf91fe8d5839acaeb7f526d55306358c7565e1c6c2e8f477318c1ef633fc22e1f1337270732bc9a9eedcc3b8d24ccebb9cdfdd7fb9761d2faed3d4a8a4e4dada321a2cbedaab602e70acbbda777d16edfd27b93270e1d46a3f1a6412b1ae86bfc1b7fffd1d5a1981d4b02a731adb6ab36b83ad71dce2d3ea572c6ed6b1f5d8cfd237d8a966f4a073fedb5d5e85f706577b9846e73265a4d6e7bb6ed6b19ef6fbd55a3fe59ea3e9ef897eefb17f3130dfa5ebfbfd7ff004fe8a2f4cd9f6cafe8fa9bd91f4fd6edff00a0fb3f737a83d5fa36cc387ad39b81d16fb732acfe96cdae75c69cdc671f710d716dbb7d43fa3b7f3d6b5fd631ba7bc5592db31e496bee73496b1cd88fb43ab2e7377fe658a7d6b7fdb29f4bed3f44ff0045db31bfddfd27f33ff46ff34af667a9e99fe7776dd3ed3b3d388ff09fe0b6fef7f854f3763887d3f498f4ad3470326dcacacffb562d7564635803321ed3e9be46ddb67a8efa7ecfa1b556cdfab7937dacbb03d322d3fa76dcd61b19c01b2c6eeddf9df9cade2ef97eefb36cdbff0079db7d1981f4b67e9bd4ff00a0953b7edef9dbf419fd2b778ff818fcdff4a9c38ba7641aeba3996fd57bdcf73486b980fd3739a0ff0027d8d07e8ac1ea9d36ec2bdd55c3658676bd9c38100c31fa35ded7fd05df66fa5366fe37ba767a93c6bea7a5eef4bfaaa1f5923f615dbfec5b7f471ebcfa9c69fcd7e93ed1fd64f89c9a69616911e85fffd9ffed0f2650686f746f73686f7020332e30003842494d040400000000000f1c015a00031b25471c020000020000003842494d0425000000000010cdcffa7da8c7be09057076aeaf05c34e3842494d043a000000000093000000100000000100000000000b7072696e744f75747075740000000500000000436c7253656e756d00000000436c7253000000005247424300000000496e7465656e756d00000000496e746500000000496d6720000000004d70426c626f6f6c010000000f7072696e745369787465656e426974626f6f6c000000000b7072696e7465724e616d6554455854000000010000003842494d043b0000000001b200000010000000010000000000127072696e744f75747075744f7074696f6e7300000012000000004370746e626f6f6c0000000000436c6272626f6f6c00000000005267734d626f6f6c000000000043726e43626f6f6c0000000000436e7443626f6f6c00000000004c626c73626f6f6c00000000004e677476626f6f6c0000000000456d6c44626f6f6c0000000000496e7472626f6f6c000000000042636b674f626a630000000100000000000052474243000000030000000052642020646f7562406fe000000000000000000047726e20646f7562406fe0000000000000000000426c2020646f7562406fe000000000000000000042726454556e744623526c74000000000000000000000000426c6420556e744623526c7400000000000000000000000052736c74556e74462350786c40520000000000000000000a766563746f7244617461626f6f6c010000000050675073656e756d00000000506750730000000050675043000000004c656674556e744623526c74000000000000000000000000546f7020556e744623526c7400000000000000000000000053636c20556e74462350726340590000000000003842494d03ed000000000010004800000001000200480000000100023842494d042600000000000e000000000000000000003f8000003842494d040d0000000000040000001e3842494d04190000000000040000001e3842494d03f3000000000009000000000000000001003842494d271000000000000a000100000000000000023842494d03f5000000000048002f66660001006c66660006000000000001002f6666000100a1999a0006000000000001003200000001005a00000006000000000001003500000001002d000000060000000000013842494d03f80000000000700000ffffffffffffffffffffffffffffffffffffffffffff03e800000000ffffffffffffffffffffffffffffffffffffffffffff03e800000000ffffffffffffffffffffffffffffffffffffffffffff03e800000000ffffffffffffffffffffffffffffffffffffffffffff03e800003842494d0408000000000010000000010000024000000240000000003842494d041e000000000004000000003842494d041a00000000034b0000000600000000000000000000002b000000400000000b006d00610064007200690064002e006a0070006500670000000100000000000000000000000000000000000000010000000000000000000000400000002b00000000000000000000000000000000010000000000000000000000000000000000000010000000010000000000006e756c6c0000000200000006626f756e64734f626a6300000001000000000000526374310000000400000000546f70206c6f6e6700000000000000004c6566746c6f6e67000000000000000042746f6d6c6f6e670000002b00000000526768746c6f6e670000004000000006736c69636573566c4c73000000014f626a6300000001000000000005736c6963650000001200000007736c69636549446c6f6e67000000000000000767726f757049446c6f6e6700000000000000066f726967696e656e756d0000000c45536c6963654f726967696e0000000d6175746f47656e6572617465640000000054797065656e756d0000000a45536c6963655479706500000000496d672000000006626f756e64734f626a6300000001000000000000526374310000000400000000546f70206c6f6e6700000000000000004c6566746c6f6e67000000000000000042746f6d6c6f6e670000002b00000000526768746c6f6e67000000400000000375726c54455854000000010000000000006e756c6c54455854000000010000000000004d7367655445585400000001000000000006616c74546167544558540000000100000000000e63656c6c54657874497348544d4c626f6f6c010000000863656c6c546578745445585400000001000000000009686f727a416c69676e656e756d0000000f45536c696365486f727a416c69676e0000000764656661756c740000000976657274416c69676e656e756d0000000f45536c69636556657274416c69676e0000000764656661756c740000000b6267436f6c6f7254797065656e756d0000001145536c6963654247436f6c6f7254797065000000004e6f6e6500000009746f704f75747365746c6f6e67000000000000000a6c6566744f75747365746c6f6e67000000000000000c626f74746f6d4f75747365746c6f6e67000000000000000b72696768744f75747365746c6f6e6700000000003842494d042800000000000c000000023ff00000000000003842494d0414000000000004000000013842494d040c00000000070000000001000000400000002b000000c000002040000006e400180001ffd8ffed000c41646f62655f434d0001ffee000e41646f626500648000000001ffdb0084000c08080809080c09090c110b0a0b11150f0c0c0f1518131315131318110c0c0c0c0c0c110c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c010d0b0b0d0e0d100e0e10140e0e0e14140e0e0e0e14110c0c0c0c0c11110c0c0c0c0c0c110c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0cffc0001108002b004003012200021101031101ffdd00040004ffc4013f0000010501010101010100000000000000030001020405060708090a0b0100010501010101010100000000000000010002030405060708090a0b1000010401030204020507060805030c33010002110304211231054151611322718132061491a1b14223241552c16233347282d14307259253f0e1f163733516a2b283264493546445c2a3743617d255e265f2b384c3d375e3f3462794a485b495c4d4e4f4a5b5c5d5e5f55666768696a6b6c6d6e6f637475767778797a7b7c7d7e7f711000202010204040304050607070605350100021103213112044151617122130532819114a1b14223c152d1f0332462e1728292435315637334f1250616a2b283072635c2d2449354a317644555367465e2f2b384c3d375e3f34694a485b495c4d4e4f4a5b5c5d5e5f55666768696a6b6c6d6e6f62737475767778797a7b7c7ffda000c03010002110311003f00a54be87580bac76f33b86d00c7f2bfac8ce18e319d6ed6c35a4c82396fc1131b07a77a3e83aa0c6ee364804ebf4366e10ef737feb6a36d5d0f1ded19b458d65c76b6c63b6b476d9608f63bdff491e304e96ae02059adbf96ed0fb55cda28b5d535a2d1bc03bb8d4782953664597b68156e2fafd4afbcb78fce5a2d387974bb130f1def3530b6bb7793ed07dbb7706b509dd3ebe94dc7ead65c2fac1734570edcdf59a766e73bd9b697fb93c4c51d2a5ad0ff00a2b0c48235b1a5ff00dd31a68cb74d81ad15b7e93b968207bf7b5a538c86319b3663bc1893b1ed718fe53dcdff00a28dd32ee99f688c6c92eb2c747a4e00469be6a6eddbb7dbf4f72b99b4630baa71b7640dbb3da18fe4359ed1bb7ee29867468ae1115a105c6df7ed7346350e8246e735c5c07943be8a8331ad226c0dda4c08246be5ee5af760e15a6c76ddd60d7731c43bf366bfe56cff00bfaa97b7a7575576b37bed7bc7a6d125cd046fd9639a7daed9fc84e196f651c63abfffd07a3270f2f65acb0d62802cc861dcfd5cd0e75564bb77b15db3a861558b4b5a583ed6f7d16003b0dc6a7be7f35ec1f9ca87d60c3cc7b6fcfaf662dad68634541ad0f692e18e2e2ff4fe96fdbbd6574ccff585bd3fa9543ed8c78a9d8ee90d702dfe73f7133878858fb3f482eba344f4d3b37d83170ae6b29c87575102c38cc87b9931ee67fc1e9fcdb969e464e337a26fb6a37b5f5b5b5b62497fd0668b987e574fbb3270f731eda5edc80f739e43c39ad9fd27e66d1ec6a9e7bf2fad74dc3a3a417d8fc4fe90f1fa3125a367b5c5bf9eddcc4fe1b96a6b6b258f8b4fa2560fb365df750c1b718df00f6896d7fcafe4aaf85f5ada72451d42bdce0f606130e6b0b493bffe92274de8b9b631f8d75be8656396beef5017176fdce6fb98f72e73a8d7663f5ac863dcd16d57c4b64374882d5246313609b35ba0c8f6a0f69d3fa874dcc6db98ec6b5cd25ed1e9b83b69d37643ab7b9beebbf91fe8d5839acaeb7f526d55306358c7565e1c6c2e8f477318c1ef633fc22e1f1337270732bc9a9eedcc3b8d24ccebb9cdfdd7fb9761d2faed3d4a8a4e4dada321a2cbedaab602e70acbbda777d16edfd27b93270e1d46a3f1a6412b1ae86bfc1b7fffd1d5a1981d4b02a731adb6ab36b83ad71dce2d3ea572c6ed6b1f5d8cfd237d8a966f4a073fedb5d5e85f706577b9846e73265a4d6e7bb6ed6b19ef6fbd55a3fe59ea3e9ef897eefb17f3130dfa5ebfbfd7ff004fe8a2f4cd9f6cafe8fa9bd91f4fd6edff00a0fb3f737a83d5fa36cc387ad39b81d16fb732acfe96cdae75c69cdc671f710d716dbb7d43fa3b7f3d6b5fd631ba7bc5592db31e496bee73496b1cd88fb43ab2e7377fe658a7d6b7fdb29f4bed3f44ff0045db31bfddfd27f33ff46ff34af667a9e99fe7776dd3ed3b3d388ff09fe0b6fef7f854f3763887d3f498f4ad3470326dcacacffb562d7564635803321ed3e9be46ddb67a8efa7ecfa1b556cdfab7937dacbb03d322d3fa76dcd61b19c01b2c6eeddf9df9cade2ef97eefb36cdbff0079db7d1981f4b67e9bd4ff00a0953b7edef9dbf419fd2b778ff818fcdff4a9c38ba7641aeba3996fd57bdcf73486b980fd3739a0ff0027d8d07e8ac1ea9d36ec2bdd55c3658676bd9c38100c31fa35ded7fd05df66fa5366fe37ba767a93c6bea7a5eef4bfaaa1f5923f615dbfec5b7f471ebcfa9c69fcd7e93ed1fd64f89c9a69616911e85fffd93842494d042100000000005500000001010000000f00410064006f00620065002000500068006f0074006f00730068006f00700000001300410064006f00620065002000500068006f0074006f00730068006f0070002000430053003500000001003842494d04060000000000070003000000010100ffe10cdd687474703a2f2f6e732e61646f62652e636f6d2f7861702f312e302f003c3f787061636b657420626567696e3d22efbbbf222069643d2257354d304d7043656869487a7265537a4e54637a6b633964223f3e203c783a786d706d65746120786d6c6e733a783d2261646f62653a6e733a6d6574612f2220783a786d70746b3d2241646f626520584d5020436f726520352e302d633036302036312e3133343737372c20323031302f30322f31322d31373a33323a30302020202020202020223e203c7264663a52444620786d6c6e733a7264663d22687474703a2f2f7777772e77332e6f72672f313939392f30322f32322d7264662d73796e7461782d6e7323223e203c7264663a4465736372697074696f6e207264663a61626f75743d222220786d6c6e733a786d704d4d3d22687474703a2f2f6e732e61646f62652e636f6d2f7861702f312e302f6d6d2f2220786d6c6e733a73744576743d22687474703a2f2f6e732e61646f62652e636f6d2f7861702f312e302f73547970652f5265736f757263654576656e74232220786d6c6e733a64633d22687474703a2f2f7075726c2e6f72672f64632f656c656d656e74732f312e312f2220786d6c6e733a70686f746f73686f703d22687474703a2f2f6e732e61646f62652e636f6d2f70686f746f73686f702f312e302f2220786d6c6e733a786d703d22687474703a2f2f6e732e61646f62652e636f6d2f7861702f312e302f2220786d704d4d3a446f63756d656e7449443d2245334643464543453732313335423232343139393545354341313430433036412220786d704d4d3a496e7374616e636549443d22786d702e6969643a30313830313137343037323036383131383731464545423834464538373833412220786d704d4d3a4f726967696e616c446f63756d656e7449443d224533464346454345373231333542323234313939354535434131343043303641222064633a666f726d61743d22696d6167652f6a706567222070686f746f73686f703a436f6c6f724d6f64653d2233222070686f746f73686f703a49434350726f66696c653d2241646f626520524742202831393938292220786d703a437265617465446174653d22323031322d30382d30315430323a30303a30362b30323a30302220786d703a4d6f64696679446174653d22323031322d30382d30395431393a35303a32372b30323a30302220786d703a4d65746164617461446174653d22323031322d30382d30395431393a35303a32372b30323a3030223e203c786d704d4d3a486973746f72793e203c7264663a5365713e203c7264663a6c692073744576743a616374696f6e3d227361766564222073744576743a696e7374616e636549443d22786d702e6969643a3031383031313734303732303638313138373146454542383446453837383341222073744576743a7768656e3d22323031322d30382d30395431393a35303a32372b30323a3030222073744576743a736f6674776172654167656e743d2241646f62652050686f746f73686f7020435335204d6163696e746f7368222073744576743a6368616e6765643d222f222f3e203c2f7264663a5365713e203c2f786d704d4d3a486973746f72793e203c2f7264663a4465736372697074696f6e3e203c2f7264663a5244463e203c2f783a786d706d6574613e2020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020203c3f787061636b657420656e643d2277223f3effe202404943435f50524f46494c450001010000023041444245021000006d6e74725247422058595a2007cf00060003000000000000616373704150504c000000006e6f6e65000000000000000000000000000000000000f6d6000100000000d32d4144424500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a63707274000000fc0000003264657363000001300000006b777470740000019c00000014626b7074000001b00000001472545243000001c40000000e67545243000001d40000000e62545243000001e40000000e7258595a000001f4000000146758595a00000208000000146258595a0000021c000000147465787400000000436f7079726967687420313939392041646f62652053797374656d7320496e636f72706f726174656400000064657363000000000000001141646f62652052474220283139393829000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000058595a20000000000000f35100010000000116cc58595a200000000000000000000000000000000063757276000000000000000102330000637572760000000000000001023300006375727600000000000000010233000058595a200000000000009c1800004fa5000004fc58595a20000000000000348d0000a02c00000f9558595a2000000000000026310000102f0000be9cffee000e41646f626500640000000001ffdb0084000a07070708070a08080a0f0a080a0f120d0a0a0d1214101012101014110c0c0c0c0c0c110c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c010b0c0c15131522181822140e0e0e14140e0e0e0e14110c0c0c0c0c11110c0c0c0c0c0c110c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0cffc0001108002b004003011100021101031101ffdd00040008ffc401a20000000701010101010000000000000000040503020601000708090a0b0100020203010101010100000000000000010002030405060708090a0b1000020103030204020607030402060273010203110400052112314151061361227181143291a10715b14223c152d1e1331662f0247282f12543345392a2b26373c235442793a3b33617546474c3d2e2082683090a181984944546a4b456d355281af2e3f3c4d4e4f465758595a5b5c5d5e5f566768696a6b6c6d6e6f637475767778797a7b7c7d7e7f738485868788898a8b8c8d8e8f82939495969798999a9b9c9d9e9f92a3a4a5a6a7a8a9aaabacadaeafa110002020102030505040506040803036d0100021103042112314105511361220671819132a1b1f014c1d1e1234215526272f1332434438216925325a263b2c20773d235e2448317549308090a18192636451a2764745537f2a3b3c32829d3e3f38494a4b4c4d4e4f465758595a5b5c5d5e5f5465666768696a6b6c6d6e6f6475767778797a7b7c7d7e7f738485868788898a8b8c8d8e8f839495969798999a9b9c9d9e9f92a3a4a5a6a7a8a9aaabacadaeafaffda000c03010002110311003f00010c903480b484486bc87100d3fcaff5b2c36c452b38b716cd2d168aa4d411b95f61e382cda76a417d665586095a255128e601e5d371d69f672742cb03234dc125cc93ac021e4cf1fa9177e4bd2bf1626aad473a45c105e35640aa225fb4dd54103e2e614e44c83200b7f5a444e1c2de406956f4dd58d3fca72bff000b8ffa650a0249f8328b581c024726562c07b51bece4ac77c90627b94e3b698af2902f12682848dfdb7c3c6bc05fffd04edac74df43eaef1845e465e40126a2a9c390a37c4bff3cf22672bbb6c1100725b2c3a0dbba8beb7916398f149237e2a3b709053e06f8bed648191e4584a8730a8a6caf216b4b2b67731465639b9927883f095a855eb82c83654d114a6da747a425b6af24e2e22059562e2dc97d653c0b330e3489be2f8727c5c5e96baadd534a9b4bfac0fab5c932c8d4f49c014db9d635e3c78fc3f6f9642775bb6023a23afa0b613c27d5294057812a11fa854f868dcf91c88926baa8cf616329958af2906e591886e8b58f7fb5c3fe37c22642f082839d34d8e18e542ef33b8f4d16a59411cb848ca7e16e1fcc992049d91b747ffd1d05cd95e18e5494c4200b2dca1e4fbb282d1c956e5f0fd9cac8219096c984ba95843690aa98d4ddc925bcaa00fb239189debfb2ea3f6b23c3bff00553c5b24c82d2ca75586e1e284a891ad528ef1d69f12ff00c57b7f76d96137cc3007cd36b9bab55d079cd09b857895624a024c9f6136c1d57a31c8c1b6bcb89add071b633d14fecd2ab1f5f8bfc9c9f30a68143d8f9b97eb220d4632ec1d021346442a49e5f737fc264e58f6d987177a6fa6ea5a5de096f64b599d09703d260fc5b6e570c8ecbf14dfcc9fefbca8823625b86e2c0449bf8e38df5348628c5ac88d197e6652d4f4b92228f8d13fdd9fc98d0e4c4dd5bfffd2af31d95f482e3508f85acaaa111610aa1d58b0804c5bd3fb5cb8f3e395c25d0b3957449b4bbff5bd6d3f53847d7d1c44d6cd50ac0afdbebc3afed64cc3ac7e963c77b15392ef4d9af41b2e68eb03adc876672240eab5fde7ec711f02e19035bb00bf5092f35bd32c60d1cbc8f67fef4b8fdd2d59471f8491fb4acc9928d449b44b70bb4bd0efa447b59a5105ddb95926f54162c24e4cbf123b7fc361321cd14c5f538e4b6d6ee51dd44b14f4aad42d452857be580ecb4a9677d75617b1dd43237243c8c35ad77e44783fc5824011ba46dc99b695afc3a9dbc06ea6582e9564b89628d033b2c65be13cbecaf1f8fe2cc7946b936093ffd338b74d3f53d3e1645596193832bcae79b156f523aa2f15478e44fde2fc198d6416ca097dfe935d43ebd1c1f57b89824770c8c393a56aa4c6cedc78aa27c6bf1e1f10d532101cd26d3b43b89af21d434a8f8bb4c61bfb563f110ac449c799fddc9fb7f0e58662a8b5f0d6e9ccfad5b69ce22b9592d89251e7752c88c94005c3464b2f2fd8930463c5c904d25f752ddddea1f5bb58a2b8b49008ee5d4fa725471e2fea37dbf83ec71c9034374a16fbcb17571347369fe91598ff00a424e88d227403848bcb97ed7c5cb08c9dec4c7b90d2f952e19d948568c1fef19d41afecfc0a0fd9c90ca8e163bab6993595c34538f4e535e2f192030203511f60df0b7c4996c656821fffd4641ff1dcd4fd3e7c6afcfea1fef3d68bf6bd7f8fd6ff007ffa5944b906c0a9a57a7f5d8fecfabea253edfafdbfe8df87f273c816c45ebbcfebb07a5f5aa716ff007938569ea7c5fef47ec7f37fc5bfdd7c19645a51f7beafa47fbde7c76fadfa7e971a1fef3fdd5c7f9bfddb884b1eb4e7c9f97d57871ffa5671f46b41f6b87ef7d4ff0084c27f1c6c5d071fd20f5e3fddc7fef672fe6ff74d3f63fdf984f25475ff00a3ca4e7d3d46af0f56bd37f53d2f8bd2ff0057fd864024adf3353f404fcfea3c7f774f5ebeaf4dbfbafde7d63fd6ff0067861cd65c9fffd9);

INSERT INTO post(Titulo,descripcion,procedimiento,link_video,imagen_p,id_usuario_eco)VALUES(
    'Floreros de Pet','Solo utiliza botellas de pet y tus manos','Marca y corta la parte lisa de en medio de la botella para obtener un borde uniforme de aproximadamente 7.5 a 8cm (3") encima de donde quieres que vaya el borde estriado.
    Mide y haz cortes rectos, uniformes y del mismo tamaño en todo el rededor de la botella. Corta los segmentos a la mitad y luego vuélvelos a cortar a la mitad para obtener tiras uniformes y delgadas.
    Cuidadosamente presiona y dobla todas las tiras hacia afueracreando una orilla uniforme en todo el rededor.
    Presiona la botella boca abajo en una superficie plana y asegúrate de que la orilla esté uniforme.
    Teje la punta de una de las tiras sobre la siguiente y debajo de las siguientes dos.Dobla y haz un pliegue de manera que la punta quede en el lugar que se muestra aquí con una flecha.
    Dobla y haz un pliegue en la siguiente de la misma manera, pero esta téjela sobre dos y debajo de una.
    Dobla la tercera tira y téjela igual que con la primera..
    Continúa al rededor siguiendo este patrón hasta las últimas tres y mete cada una debajo de la siguiente hasta terminar de tejer.','https://www.youtube.com/watch?v=79NGnLiW5cU','234234234234',1);

INSERT INTO comentarios(nombre_usuario,apellido_p,comentario,fecha_comentario)VALUES(
    'Alejandro','Lora','Muy buena app!!!',now());

INSERT INTO users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('Edgar',MD5(concat('Edgar', 'kuorra_key')), 0, 1, 'Edgar', 'edgar@gmail.com','TIC:SI', MD5(concat('Edgar', 'kuorra_key', '2016/06/04')), 0),
('Abigail',MD5(concat('Abigail', 'kuorra_key')), 1, 1, 'Abigail', 'abita@gmail.com','TIC:SI', MD5(concat('Abigail', 'kuorra_key','2016/06/04')), 0);


SELECT * FROM users;
SELECT * FROM sessions;

CREATE USER 'eco_system'@'localhost' IDENTIFIED BY 'eco_system.2019';
GRANT ALL PRIVILEGES ON eco_system.* TO 'eco_system'@'localhost';
FLUSH PRIVILEGES;
