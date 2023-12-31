# cabaez_labs

 Este es un proyecto individual relacionado con Machine Learning Operations (MLOps) para la plataforma Steam, donde se  crea un sistema de recomendación de videojuegos para usuarios. Me enfrente a varios desafíos en la manipulación y limpieza de datos mal estructurados en archivos JSON.

Fundamentación del Proyecto MLOps para Steam

El proyecto MLOps desarrollado para Steam tiene como objetivo principal la creación de un sistema de recomendación de videojuegos personalizados para usuarios. Steam, una plataforma multinacional de videojuegos, se enfrenta al desafío de proporcionar a sus usuarios recomendaciones precisas y relevantes en un entorno con datos desafiantes, como archivos JSON mal estructurados, datos anidados y falta de procesos automatizados para la actualización de nuevos productos.

El proyecto se inicia con la adquisición de archivos JSON de gran tamaño que contienen información sobre usuarios, reseñas de videojuegos, detalles de juegos y más. Estos archivos presentan dificultades significativas en términos de estructura de datos y acceso a la información. Para abordar este problema, se utiliza Python y la biblioteca Pandas para llevar a cabo el proceso de Extracción, Transformación y Carga (ETL) de los datos.

Uno de los desafíos iniciales fue superar la dificultad de leer los archivos JSON debido a su estructura compleja y anidada. Se realizaron múltiples intentos de carga, lo que resultó en la creación de numerosos archivos CSV temporales con diferentes modificaciones y tamaños para explorar y comprender mejor los datos.

Una vez que se logró cargar los datos, se llevaron a cabo múltiples tareas de limpieza y transformación. Los datos se agruparon en columnas pertinentes, se eliminaron registros nulos o irrelevantes y se realizaron análisis de sentimientos sobre las reseñas de los usuarios.

La columna 'sentiment_analysis' se creó utilizando técnicas de Procesamiento de Lenguaje Natural (NLP) con TextBlob, asignando valores numéricos para describir el sentimiento general de las reseñas (0 para malo, 1 para neutral y 2 para positivo).

Además, se consolidaron los datos de varios archivos y se unieron mediante identificadores únicos para crear un conjunto de datos completo y coherente. Este conjunto de datos final contiene información esencial sobre usuarios, juegos, reseñas y detalles del juego, lo que lo convierte en la base para desarrollar un sólido sistema de recomendación.

En resumen, el proyecto MLOps para Steam abordó con éxito los desafíos de datos complejos y poco estructurados para crear un sistema de recomendación de videojuegos eficiente y preciso. El análisis de sentimientos añade un valor adicional al proporcionar una comprensión más profunda de las reseñas de los usuarios. Este proyecto demuestra la importancia de la limpieza de datos y la ingeniería de características en el desarrollo de soluciones de aprendizaje automático para problemas empresariales.

Esta fundamentación destaca la relevancia y el valor del proyecto MLOps para Steam al abordar desafíos reales relacionados con datos poco estructurados y proporcionar recomendaciones de calidad para los usuarios de la plataforma.

En  tal sentido tuve que poner en funcionamiento APIs utilizando el framework FastAPI que servirían como un medio para exponer y proporcionar acceso a datos específicos de la empresa a través de solicitudes HTTP. A continuación, se explica cada una de estas APIs en detalle:

userdata(User_id: str):

Propósito: Esta API tiene como objetivo proporcionar información detallada sobre un usuario en particular.
Parámetros: Se espera un único parámetro, User_id, que es una cadena que identifica de manera única al usuario.
Respuesta: La respuesta incluirá información relevante sobre el usuario, como la cantidad de dinero gastado por el usuario, el porcentaje de recomendación basado en las revisiones (posiblemente en función de reviews.recommend) y la cantidad de items relacionados con el usuario.
countreviews(YYYY-MM-DD: str, YYYY-MM-DD: str):

Propósito: Esta API permite contar la cantidad de usuarios que realizaron reseñas en un rango de fechas dado y calcular el porcentaje de recomendación basado en las revisiones realizadas en ese período.
Parámetros: Se esperan dos parámetros, que representan las fechas de inicio y fin del rango que se quiere analizar.
Respuesta: La respuesta incluirá la cantidad total de usuarios que realizaron reseñas dentro del rango de fechas especificado y el porcentaje de recomendación basado en esas revisiones.
genre(género: str):

Propósito: Esta API busca proporcionar información sobre la posición de un género de videojuegos en un ranking en función de las horas de juego acumuladas (PlayTimeForever).
Parámetros: Se espera un parámetro, género, que es una cadena que representa el género de videojuegos que se desea consultar.
Respuesta: La respuesta incluirá la posición en el ranking del género especificado en función de las horas de juego acumuladas.
userforgenre(género: str):

Propósito: Esta API tiene como objetivo identificar a los 5 usuarios que han jugado más horas en un género específico y proporcionar información detallada sobre ellos, incluyendo su URL de usuario y su identificación de usuario (user_id).
Parámetros: Se espera un parámetro, género, que es una cadena que representa el género de videojuegos que se desea consultar.
Respuesta: La respuesta incluirá una lista de los 5 usuarios principales que han jugado más horas en el género especificado, junto con su URL de usuario y su user_id.
developer(desarrollador: str):

Propósito: Esta API busca proporcionar información sobre la cantidad de items (videojuegos) y el porcentaje de contenido gratuito (Free) por año según la empresa desarrolladora especificada.
Parámetros: Se espera un parámetro, desarrollador, que es una cadena que representa la empresa desarrolladora cuya información se desea consultar.
Respuesta: La respuesta incluirá una tabla que enumera los años y la cantidad de contenido gratuito lanzado por la empresa desarrolladora especificada en cada año.
sentiment_analysis(año: int):

Propósito: Esta API se centra en el análisis de sentimiento de las reseñas de usuarios en función del año de lanzamiento de los videojuegos.
Parámetros: Se espera un parámetro, año, que es un número entero que representa el año para el cual se desea realizar el análisis de sentimiento.
Respuesta: La respuesta incluirá una lista con la cantidad de registros de reseñas de usuarios categorizados en función del análisis de sentimiento para el año especificado.
Estas APIs se diseñan para permitir a los usuarios obtener información específica de la empresa de manera fácil y eficiente a través de solicitudes HTTP. Cada una de ellas proporciona una funcionalidad distinta para el análisis y consulta de datos relacionados con videojuegos y usuarios en la plataforma Steam.

Las csv utilizado para las APIs, luegod e la limpieza, transformaciones, recortes y uniones de datos son las siguientes resultado_sin_nulos.csv, resultado_union_actualizado_csv y usuario_reviews_sinfechas_nulos.csv, que fueron cargados al Repositorio de GitHub.

EDA
Diagrama de dispersión entre dos variables numéricas
Relacion muy dispareja entre las variables "playtime_forever" y "metascore"
La justificación de que hay una relación muy dispareja entre las variables "playtime_forever" y "metascore" se basa en la observación de un diagrama de dispersión entre estas dos variables. En este caso, se supone que "playtime_forever" representa la cantidad de tiempo de juego de un juego y "metascore" representa la puntuación otorgada por Metacritic a ese juego. Veamos cómo se puede llegar a esta conclusión:

Distribución de los Puntos: Después de crear el diagrama de dispersión con "playtime_forever" en el eje X y "metascore" en el eje Y, se observa que los puntos están dispersos de manera irregular a lo largo del gráfico. Esto significa que no hay una tendencia clara de agrupación de puntos en una dirección específica.

Ausencia de Correlación Lineal: La dispersión aleatoria de puntos sugiere que no existe una correlación lineal significativa entre estas dos variables. En otras palabras, no se puede trazar una línea recta que represente una relación lineal entre la cantidad de tiempo de juego y la puntuación de Metacritic.

Puntuaciones Metacríticas Variables para Juegos con Diferentes Tiempos de Juego: Se observa que juegos con una amplia gama de tiempos de juego tienen puntuaciones de Metacritic variadas. Algunos juegos con bajos tiempos de juego tienen altas puntuaciones, mientras que otros con altos tiempos de juego tienen puntuaciones bajas. Esto indica que la puntuación de Metacritic no está directamente relacionada con la cantidad de tiempo de juego.

Puntos Atípicos: Es posible que en el diagrama de dispersión se observen puntos atípicos, es decir, juegos que se alejan significativamente de la tendencia general. Estos puntos atípicos refuerzan la idea de que no hay una relación clara entre las dos variables.

En resumen, la forma en que los puntos se distribuyen en el diagrama de dispersión, la falta de una tendencia clara y la variabilidad en las puntuaciones de Metacritic para juegos con diferentes tiempos de juego indican que no hay una relación sólida y predecible entre "playtime_forever" y "metascore". Esto justifica la afirmación de que la relación entre estas dos variables es muy dispareja y que no se puede establecer una conexión lineal clara entre ellas en base a los datos observados.

![image](https://github.com/carlosab2021/cabaez_labs/assets/86332466/6080c2de-8181-4e48-8ac4-e7450c868140)

Identificación de Outliers
# Diagramas de caja (box plots) para variables numéricas
![image](https://github.com/carlosab2021/cabaez_labs/assets/86332466/49ced886-2712-4bd6-bd50-c9bcd7378458)
![image](https://github.com/carlosab2021/cabaez_labs/assets/86332466/a320f9e1-eafe-4086-81a7-682830227ebb)

links Render: https://cabaez-labs.onrender.com/docs Video: https://youtu.be/BNlYJqtDFxI
