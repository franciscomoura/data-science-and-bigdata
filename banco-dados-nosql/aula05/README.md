### Resolução de exercícios
#### Instrções:
* Para cada uma das situações dos exercícios escolha a infraestrutura que você acha mais adequada e justifique sua escolha.

#### Exercício 01
Você e um grupo de amigos da faculdade decidem-se juntar e criar uma empresa de na área de IoT. Todos seus amigos são excelentes programadores porém estão em dúvida como montar a infraestrutura para suportar a grande quantidade de dados gerados pelos sensores da aplicação. O que vocês devem fazer?

##### Resposta:

* Infraestrutura:* componente gerenciador de fila de mensagens ingerindo os dados em um SGBD NoSQL.

* Justificativa:*
Pelo fato da frequência de geração e volume alto de dados, característico de sensores, o uso de gerenciadores de fila de mensagens se torna adequado, uma vez que estes componentes possuem a capacidade do recebimento garatindo da mensagem transmitida (os dados), permitindo a ingestão destes dados de forma assícrona, armazenando-os em um SGBD NoSQL que tem como característica inserção rápida e não há necessidade da existência prévia de um esquema de banco de dados (Schemaless - best: dynamically typed schema).
