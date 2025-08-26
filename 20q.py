# Base de datos de ejemplo
# Tenemos una "base" llena de diccioionarios de datos que tienen las características de cada cosa
database = [
    {"name": "Lápiz", "oficina": True, "escuela": True, "electrónico": False, "juguete": False},
    {"name": "Computadora", "oficina": True, "escuela": True, "electrónico": True, "juguete": False},
    {"name": "Pelota", "oficina": False, "escuela": True, "electrónico": False, "juguete": True},
    {"name": "Labubu", "oficina": False, "escuela": False, "electrónico": False, "juguete": True},
]

# Lista de preguntas en orden
questions = [
    ("oficina", "¿Se usa en la oficina?"),
    ("escuela", "¿Se usa en la escuela?"),
    ("electrónico", "¿Es un objeto electrónico?"),
    ("juguete", "¿Es un juguete?"),
]

# Función para preguntas
# answer = "s/n", property = "propiedad clave de la lista questions" candidates="elementos de la base".
def take_chance(answer, property, candidates):
    # Filtra la base de datos según la respuesta del usuario.
    ans = True if answer == "y" else False
    # devuelve una lista con solo los objetos cuya propiedad clave coincide con la respuesta
    return [d for d in candidates if d[property] == ans]

def adivinar(database, questions, max_preguntas=20):
    # Asignamos los valores de nuestra base original a la variable candidatos.
    candidatos = database.copy()

    # i es el n. de pregunta, prop la propiedad clave, texto lo que se muestra.
    for i, (prop, texto) in enumerate(questions, start=1):
        if len(candidatos) <= 1 or i > max_preguntas:
            break

        ans = input(f"{i}. {texto} (y/n): ").lower() #normaliza uppercase y lowercase
        # Ejecutamosw la función que elimine candidatos que no coincidan con la respuesta
        candidatos = take_chance(ans, prop, candidatos)

        if len(candidatos) == 1:
            print(f"\n¡Tu objeto es: {candidatos[0]['name']}!")
            return

    # Si quedan varios o ninguno después de las preguntas
    if len(candidatos) > 1:
        print("\nNo estoy seguro... podrían ser:")
        for c in candidatos:
            print("-", c["name"])
    else:
        print("\nNo encontré ningún objeto que coincida.")

# Ejecutar
adivinar(database, questions)
