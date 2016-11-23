#### Intruções:
* Copie e cole o código no shell do mongoDB; ou 
* Execute os arquivos .js usando a função load diretamento no shell do mongoDB:
```Bash
load("path/arquivo.js")
```

##### Exercício 1
###### A) Utilizando as funções de mapReduce do mongo, conte o número de palavras que terminam em ar, er, ir, or, ur.
```JavaScript

// função de mapeamento - map
var map_fn = function(){
    emit(this.text.substring(this.text.length - 2, this.text.length), 1);
}

// função de redução - reduce
var reduce_fn = function(key, values){
    return Array.sum(values);
}

print("Aula 03 - Exercício 01 \nExecutando map-reduce questão A...");
// aplicando a função mapRedude na collection Vocabulary
var result = db.Vocabulary.mapReduce(
        map_fn, 
        reduce_fn,
        {
            query: {text:  /((ar)|(er)|(ir)|(or)|(ur))$/},
            out: "conta_palavras"
        }
    );

// imprimindo as saídas
print("Resultado do processamento:");
printjson(result);

print("Contagem das palavras:")
var cursor = db.conta_palavras.find({});
while (cursor.hasNext()) {
    printjson(cursor.next())
}

// fechar cursor
cursor.close();

```

###### B) Utilizando as funções de mapReduce do mongo, conte o total de cada caracter existente no vocabulario. Por exemplo: aula -> a:2, u:1, l:1
```JavaScript

// função de mapeamento - map
var map_fn = function() {
    if (this.text == undefined) return;

    for (var i = 0; i < this.text.length; i++) {
        emit(this.text[i], 1);
    }
};

// função de redução - reduce
var reduce_fn = function(key, value) {
    return Array.sum(value);
};

print("Aula 03 - Exercício 01 \nExecutando map-reduce questão B...");
// aplicando a função mapRedude na collection Vocabulary
var result = db.Vocabulary.mapReduce(
        map_fn, // map
        reduce_fn, // reduce
        {
            query: {},
            out: "conta_caracteres"
        }
    );

// imprimindo as saídas
print("Resultado do processamento:");
printjson(result);

print("Contagem dos caracteres:")
var cursor = db.conta_caracteres.find({});
while (cursor.hasNext()) {
    printjson(cursor.next())
}

// fechar cursor
cursor.close();

```    

##### Exercício 2
###### Utilizando a função de agregação contar quantos itens cujo o campo total seja maior do que 1000, agrupando-os por tipo, (campo type) e exiba o resultado em ordem crescente.

```JavaScript
var result_cursor = db.Vocabulary.aggregate([
        { $match: { total: { $gt: 1000 } } },
        {
            $group: {
                _id: { type: "$type" },
                qty: { $sum: 1 }
            }
        },
        { $sort: { "_id.type": 1 } }
    ]);

result_cursor.pretty();

while (result_cursor.hasNext()) {
    printjson(result_cursor.next());
}

result_cursor.close();

```
