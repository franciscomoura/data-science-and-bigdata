#####Exercício 1
######A) Utilizando as funções de mapReduce do mongo, conte o número de palavras que terminam em ar, er, ir, or, ur.
```JavaScript
db.Vocabulary.mapReduce(
        function() { emit(this.text, 1);}, // map
        function(key, value) { return Array.sum(value)}, // reduce
        {
            query: {$or: [{text: /ar$/}, {text: /er$/}, {text: /ir$/}, {text: /or$/}, {text: /ur$/}]},
            out: "resultado"
        }
    )
```

######B) Utilizando as funções de mapReduce do mongo, conte o total de cada caracter existente no vocabulario. Por exemplo: aula -> a:2, u:1, l:1
```JavaScript
var map_fn = function() {
    if (this.text == undefined) return;

    for (var i = 0; i < this.text.length; i++) {
        emit(this.text[i], 1);
    }
};

var reduce_fn = function(key, value) {
    return Array.sum(value);
};

db.Vocabulary.mapReduce(
        map_fn, // map
        reduce_fn, // reduce
        {
            query: {},
            out: "saida"
        }
    )
```    
