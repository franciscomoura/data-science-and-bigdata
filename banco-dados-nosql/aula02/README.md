##### Instruções:
* Copie e cole o código no shell do mongoDB;

##### 01) Insira no banco informações sobre você e seus colegas como nome, data de nascimento, disciplinas cursadas e em curso na PUC.

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

##### 02) Procure no banco a pessoa com a menor data de nascimento

```JavaScript
db.Alunos.find().sort ( {"data_nascimento": 1 }) .limit(1)
```

##### 03) Atualize a sua nota na disciplina NoSQL para 5

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

##### 04) Apague um de seus colegas
```JavaScript
db.Alunos.remove({
	"nome": /Willian/
})
```

###### Encontrar todos
```JavaScript
db.Alunos.find()
```
