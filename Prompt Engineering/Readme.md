# Prompting Principles
- **Principle 1: Write clear and specific instructions**
- **Principle 2: Give the model time to “think”**

Estas tácticas se muestran en el archivo guideline.py

## Tácticas

### Táctica 1: Usar delimitadores para indicar claramente las partes distintas de la entrada
- Los delimitadores pueden ser algo como: ```, """, < >, `<tag> </tag>`, `:`

### Táctica 2: Pedir un resultado estructurado
- Por ejemplo pedir que el resultado se entregue en un archivo JSON
- o en un archivo HTML
### Táctica 3: Pedir al modelo que compruebe si se cumplen las condiciones
(Usar condicionales)

    Se le proporcionará un texto delimitado por comillas triples. 
    Si contiene una secuencia de instrucciones, reescriba esas 
    instrucciones en el siguiente formato: 
    Paso 1 - ... 
    Paso 2 - … … 
    Paso N - … 
    Si el texto no contiene una secuencia de instrucciones,
    simplemente escriba "No se proporcionan pasos".

    \"\"\"{text_1}\"\"\"

### Táctica 4: "Few-shot" prompting
Técnica de indicación que permite que un modelo procese ejemplos antes de intentar una tarea.
El problema de hacer predicciones basadas en un número limitado de muestras.


### Táctica 5: Especificar los pasos requeridos para completar una tarea

También se puede pedir que su salida se dé en un formato específico

    ... Realice las siguientes acciones: 
    1 - Resuma el siguiente texto delimitado por triple backticks con 1 frase. 
    2 - Traducir el resumen al francés. 
    3 - Enumere cada nombre en el resumen en francés. 
    4 - Muestra un objeto json que contiene las siguientes claves: 
        french_summary, num_names. 
    
    Separe sus respuestas con saltos de línea.
    
    Use el siguiente formato:
    Text: <text to summarize>
    Summary: <summary>
    Translation: <summary translation>
    Names: <list of names in Italian summary>
    Output JSON: <json with summary and num_names>


### Táctica 6: Indicar al modelo que encuentre su propia solución antes de apresurarse a llegar a una conclusión.

    determinar si la respuesta es correcta
    primero trabaja en tu propia solución
    luego compare las soluciones
    No determine si la solución es correcta hasta tu hayas resuelto el problema

    luego se divide por secciones usando delimitadores

