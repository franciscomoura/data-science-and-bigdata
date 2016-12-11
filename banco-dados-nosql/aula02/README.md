### Aula 02 - Resolução de exercícios

#### Exercício 01
  * Escolha 3 colegas e:
    * Insira no banco informações sobre você e seus colegas como nome, data de nascimento, disciplinas cursadas e em curso na PUC;
    * Procure no banco a pessoa com a menor data de nascimento;
  * Atualize a sua nota na disciplina NoSQL para 5;
  * Apague um de seus colegas.
  
##### Solução:
* `a) Insira no banco informações sobre você e seus colegas como nome, data de nascimento, disciplinas cursadas e em curso na PUC:`

###### Aluno 1: Eu

```JavaScript
db.Alunos.insert({
	"nome": "Francisco Moura",
	"data_nascimento":ISODate("2001-01-14"),
	"disciplinas_cursadas": [
		{disciplina: "Introdução às linguagens estaíticas"},
		{disciplina: "Ciência de dados e big data em negócios"}
	],
	"disciplinas_em_curso": [
		{disciplina: "Banco de dados NoSQL"},
		{disciplina: "Arquitetura, qualidade e gestâo de dados"}
	]
})
```

###### Aluno 2: colega 1

```JavaScript
db.Alunos.insert({
	"nome": "Willian Hofner",
	"data_nascimento":ISODate("2000-01-09"),
	"disciplinas_cursadas": [
		{"disciplina": "Introdução às linguagens estaíticas"},
		{"disciplina": "Ciência de dados e big data em negócios"}
	],
	"disciplinas_em_curso": [
		{"disciplina": "Banco de dados NoSQL"},
		{"disciplina": "Arquitetura, qualidade e gestâo de dados"}
	]
})
```

###### Aluno 3: colega 2

```JavaScript
db.Alunos.insert({
	"nome": "João Henrique",
	"data_nascimento":ISODate("2001-01-09"),
	"disciplinas_cursadas": [
		{"disciplina": "Introdução às linguagens estaíticas"},
		{"disciplina": "Ciência de dados e big data em negócios"}
	],
	"disciplinas_em_curso": [
		{"disciplina": "Banco de dados NoSQL"},
		{"disciplina": "Arquitetura, qualidade e gestâo de dados"}
	]
})
```

###### Encontrar o aluno Francisco
```JavaScript
db.Alunos.find({
	"nome": /Francisco/
})
```

###### Encontrar todos os alunos
```JavaScript
db.Alunos.find()
```

* `b) Procure no banco a pessoa com a menor data de nascimento`

```JavaScript
db.Alunos.find().sort ( {"data_nascimento": 1 }) .limit(1)
```

* `c) Atualize a sua nota na disciplina NoSQL para 5`

```JavaScript
db.Alunos.updateOne(
	{"nome": "Francisco Moura"},
	{
		$set: {"disciplinas_em_curso": [
			{"disciplina": "Banco de dados NoSQL", nota: 5},
			{"disciplina": "Arquitetura, qualidade e gestâo de dados", nota: 10}
		]}
	}	
)
```

* `d) Apague um de seus colegas`

```JavaScript
db.Alunos.remove({
	"nome": /Willian/
})
```

###### Encontrar todos
```JavaScript
db.Alunos.find()
```

#### Exercício 02
##### Contando palavras
Complete o código do arquivo que está dentro de ~Aulas/nosql-class/aula2/ex2.py
* Liste as dez palavras com o maior valor no campos total e as imprima na tela.
* Encontre todas as palavras que são usuários do twitter, hashtags, urls e adicione um campo
informando o tipo da palavra.
* Conte o total de cada um dos tipos que você criou.

##### Solução
* `a) Liste as dez palavras com o maior valor no campos total e as imprima na tela.`
```Python
import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient('localhost', 27017)
    db = client.nosqlclass
    
    result = db.Vocabulary.find({}).sort("total", pymongo.DESCENDING).limit(10)
    print('{0:10} {1:10}'.format('Palavra', 'Total'))
    for word in result:
        print('{0:<10} {1:7,d}'.format(word['text'], word['total']).replace(',','.'))
```
`Resultado:`
```Bash
>>>
Palavra    Total
rt         202.375
e          189.464
no         164.138
de         160.927
casa       140.661
a          127.984
que        106.225
o           96.294
em          90.408
has         86.989
```
* `b) Encontre todas as palavras que são usuários do twitter, hashtags, urls e adicione um campo
informando o tipo da palavra` e
* `Conte o total de cada um dos tipos que você criou`
```Python
import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient('localhost', 27017)
    db = client.nosqlclass

    count_users = 0
    count_hastags = 0
    count_urls = 0

    result = db.Vocabulary.find({
        '$or' : [
            {'text': {'$regex' : '^@'}},
            {'text': {'$regex' : '^#'}},
            {'text': {'$regex' : '^http://'}},
            {'text': {'$regex' : '^www'}}
        ]
        })
    for word in result:
        if (word['text'].find('@') != -1):
            print('{0:<25s} {1:s}'.format(word['text'], 'Usuário'))
            count_users += 1
        elif (word['text'].find('#') != -1):
            print('{0:<25s} {1:s}'.format(word['text'], 'Hastag'))
            count_hastags += 1
        elif (word['text'].find('http://') != -1 or word['text'].find('www.') != -1):
            print('{0:<25s} {1:s}'.format(word['text'], 'URL'))
            count_urls += 1

    print('{0:20s} {1:7,d} '.format('Total usuários: ', count_users).replace(',','.'))
    print('{0:20s} {1:7,d} '.format('Total hastags: ', count_hastags).replace(',','.'))
    print('{0:20s} {1:7,d} '.format('Total URLs: ', count_urls).replace(',','.')) 
```
`Resultado`
```Bash
Total usuários:       89.813
Total hastags:        11.109
Total URLs:              113
```
