from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hola_a_todos():
    return """
        <h1>hola_a_todos</h1>
        <a href="/novedades">¡Ver novedades!</a>
        <a href="/motivaciones">¡Ver motivaciones!</a>
        <a href="/monedas">¡Lansar moneda!</a>
    """

@app.route("/novedades")
def novedades():
    novedad = [
        "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
        "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones",
        "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
        "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
        "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
        "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
        "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos",
        "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"
    ]
    return f'<p>{random.choice(novedad)}</p>'

@app.route("/motivaciones")
def motivaciones():
    motivacion = [
        "El único modo de hacer un gran trabajo es amar lo que haces - Steve Jobs",
        "Nunca pienso en las consecuencias de fallar un gran tiro… cuando se piensa en las consecuencias se está pensando en un resultado negativo - Michael Jordan",
        "El dinero no es la clave del éxito; la libertad para poder crear lo es - Nelson Mandela",
        "Cuanto más duramente trabajo, más suerte tengo - Gary Player",
        "La inteligencia consiste no solo en el conocimiento, sino también en la destreza de aplicar los conocimientos en la práctica - Aristóteles",
        "El trabajo duro hace que desaparezcan las arrugas de la mente y el espíritu - Helena Rubinstein ",
        "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan - Elon Musk",
        "Escoge un trabajo que te guste, y nunca tendrás que trabajar ni un solo día de tu vida - Confucio",
        "Un sueño no se hace realidad por arte de magia, necesita sudor, determinación y trabajo duro - Colin Powell",
        "Cuéntamelo y me olvidaré. Enséñamelo y lo recordaré. Involúcrame y lo aprenderé - Benjamin Franklin ",
        "La lógica te llevará de la A a la Z. La imaginación te llevará a cualquier lugar - Albert Einstein",
        "A veces la adversidad es lo que necesitas encarar para ser exitoso - Zig Ziglar",
        "Nunca soñé con el éxito. Trabajé para conseguirlo - Estée Lauder",
        "Ejecuta tus conocimientos con la maestría del que sigue aprendiendo - Jonathan García-Allen",
        "Los clientes más insatisfechos deberían ser tu mayor inspiración para aprender - Bill Gates"
    ]
    return f'<p>{random.choice(motivacion)}</p>'

@app.route("/monedas")
def monedas():
    moneda = [
        "cara",
        "cruz"
    ]
    return f'<p>{random.choice(moneda)}</p>'

app.run(debug=True)
