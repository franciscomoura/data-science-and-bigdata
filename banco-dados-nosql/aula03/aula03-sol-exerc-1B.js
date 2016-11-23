/*
*   Exercício 1:
*   B) Utilizando as funções de mapReduce do mongo, conte o total de cada 
*   caracter existente no vocabulario. Por exemplo: aula -> a:2, u:1, l:1
*/

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
