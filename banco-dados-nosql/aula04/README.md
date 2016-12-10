### Resolução de exercícios
#### Instruções:
* Execute o código na base de dados que contém a collection Vocabulary.
* Copie e cole o código no shell do mongoDB.

#### Faça uma pesquisa simples na coleção *Vocabulary* pelo termo “feliz” no campo *text* e responda:
* A) Número de documentos que foi escaneado
* B) Tempo que levou para fazer a consulta
* C) Crie um índice simples no campo text
* D) Número de documentos que foi escaneado
* E) Tempo que levou para fazer a consulta
  
  #####   Soluções
  ##### Consulta com explain, sem índice no campo *text*
  ```JavaScript
  db.Vocabulary.find({text: "feliz"}).explain({"executionStats":1})
  ```
  ###### A) Número de documentos que foi escaneado
  ```JSON
  "totalDocsExamined" : 291214
  ```
  ###### B) Tempo que levou para fazer a consulta
  ```JSON
  "executionTimeMillis" : 99
  ``` 
  ###### C) Crie um índice simples no campo *text* e re-execute a consulta
  ```JavaScript
  db.Vocabulary.createIndex({"text": 1}, {expireAfterSeconds: 3600})
  ```
  ###### D) Número de documentos que foi escaneado
  ```JSON
  "docsExamined" : 1
  ```
  ###### E) Tempo que levou para fazer a consulta
  ```JSON
  "executionTimeMillis" : 4
  ```  
  
