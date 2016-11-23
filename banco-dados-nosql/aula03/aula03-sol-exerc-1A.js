/**
*   Aula 03 - Soluções do exercícios propostos
*   ------------------------------------------
*   Exercício 1:
*   A) Utilizando as funções de mapReduce do mongo, conte o número de palavras 
*   que terminam em ar, er, ir, or, ur.
*/

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
