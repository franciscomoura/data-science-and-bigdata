### Aula 05 - Resolução de exercícios
#### Instruções:
_Para cada uma das situações dos exercícios escolha a infraestrutura que você acha mais adequada e justifique sua escolha._

#### Exercício 01
_Você e um grupo de amigos da faculdade decidem-se juntar e criar uma empresa de na área de IoT. Todos seus amigos são excelentes programadores porém estão em dúvida como montar a infraestrutura para suportar a grande quantidade de dados gerados pelos sensores da aplicação. O que vocês devem fazer?_

##### Resposta:
__Infraestrutura:__ 
Componente gerenciador de fila de mensagens e um SGBD NoSQL.

__Justificativa:__
Pelo fato da frequência de geração e volume alto de dados, característico de sensores, o uso de gerenciadores de fila de mensagens se torna adequado, uma vez que estes componentes possuem a capacidade do recebimento garatindo da mensagem transmitida (os dados), permitindo que as mensagens recebidas sejam processadas de forma assícrona, assim, armazenando-as em um SGBD NoSQL que tem como característica inserção rápida e não há necessidade da existência de um esquema fixo de banco de dados (Schemaless - best: dynamically typed schema).

#### Exercício 02
Dentro de sua empresa certamente existem pontos que podem ser adaptados para uma arquitetura Big Data.
Explique a infraestrutura atual e o que você mudaria para melhorar a eficiência.

##### Resposta:
__Infraestrutura atual:__ Atualmente, o sistema de _harvest_ (coletor) dos dados sobre a biodiversidade brasileira [SiBBr](www.sibbr.gov.br) executa com dependências do Apache ActiveMQ, do banco de dados relacional PostgreSQL e do banco de dados espacial PostGIS. Necessariamente, nesta arquitetura, há a necessidade da definição fixa do esquema de banco de dados, uma necessidade imposta pelo tecnologia de banco de dados relacional. Estes bancos de dados são utilizados para armazenamento das ocorrências em formato RAW, ou seja, funciona apenas como um repositório de dados, para posterior processamento de indexação, dentro do fluxo de coleta, indexação e exibição da informação.

__Os problemas:__ Os dados coletados são compartilhados no formato do padrão [Darwin Core] (http://rs.tdwg.org/dwc/index.htm), um padrão utilizado para o compartilhamento de dados sobre a biodiversidade biológica. Em todas as atualizações de versões do padrão Darwin Core é necessário atualizar o esquema de banco de dados antes de persistir os dados compartilhados na nova versão. 
Outra desvantagem da persitência em bancos de dados relacionais dos dados compartilhados no formato Darwin Core é a incapacidade de se aproveitar a descrição do modelo de dados descrita pelos metados de forma dinâmica. Cada conjunto de dados é compartilhado com, no mínimo dois arquivos, sendo um arquivo de dados e um arquivo de metadados.
O esforço de persistir e recuperar tais dados em uma base de dados que utiliza o modelo relacional é maior se comparado com as mesmas operações no modelo de dados não-relacional. Somente no momento da leitura dos dados persistidos é que a aplicação faz uso dos metadados (o modelo dos dados), assim, duplicando os esforços de programação, pois há a necessidade da recuperação dos metadados e dos dados e realizar o mapeamento em memória.

__Solução:__ A arquitetura atual pode ser atualizada para utilizar a persistência em banco não-relacionais, eliminando o banco de dados relacional e o banco de dados espacial. Assim, a arquitetura atualizada tem como dependência o Apache ActiveMQ e um SGBD NoSQL, como o Cassandra, CouchDB ou MongoDB. Tanto os metadados quanto os dados podem ser persitidos e recuperados, sem preocupações com a versão do padrão, uma vez que os metadados já traz tal informação, eliminando alterações fixas no esquema de banco de dados. Os ganhos são maiores ainda, pois ocorre a redução ou até mesmo a eliminação de mapeamento dos objetos do banco em memória (eliminação do mapeamento ORM - Mapeamento Objeto Relacional). 
O ElasticSearch pode ser utilizado para substituir o banco espacial e prover maior velocidade de recuperação da informação espacial na fase de indexação e recuperação das informações.

__Conclusão:__ Assim, percebe-se a utilização correta da infraestrutura de big data. As ferramentas somente são utilizadas nas fases onde realmente se fazem necessárias, com o benefício da escalabilidade e recuperação rápida da informação.
