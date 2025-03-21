# tecnicas-quiz
Quiz en una web para la asignatura Técnicas Artísticas

## Prompt usado

Por favor, genera un array en JSON con las siguientes características:

1. Cada elemento debe tener una pregunta extraída de esta fuente, y cuatro
   posibles respuestas.

2. Se debe marcar de alguna forma cuál es la respuesta correcta.

3. Para la respuesta correcta, se debe indicar, en una frase, por qué es
correcta; para las respuestas incorrectas, indicar por qué no lo son.

Genera al menos 50 preguntas de esta forma. En cada elemento del array, la
pregunta ocupará el campo "pregunta", las respuestas el campo "respuesta", y
cada respuesta debe tener los campos "texto" para el contenido, "correcto" si es
correcta o no, "justificacion" para explicar por qué es correcta o
incorrecta. En las descripciones de esta justificación, evitar expresiones del
tipo "la fuente indica que..."
