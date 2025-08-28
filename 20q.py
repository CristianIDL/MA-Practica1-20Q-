from base import database
from preguntas import questions

# Función para preguntas
# answer = "s/n", property = "propiedad clave de la lista questions" candidates="elementos de la base".
def preguntar(answer, property, candidates):
    # Filtra la base de datos según la respuesta del usuario.
    ans = True if answer == "s" else False
    # devuelve una lista con solo los objetos cuya propiedad clave coincide con la respuesta
    return [d for d in candidates if d[property] == ans]

def adivinar(database, questions, max_preguntas=20):
    # Asignamos los valores de nuestra base original a la variable candidatos.
    candidatos = database.copy()

    # i es el n. de pregunta, prop la propiedad clave, texto lo que se muestra.
    for i, (prop, texto) in enumerate(questions, start=1):
        if len(candidatos) <= 1 or i > max_preguntas:
            print("Se an alcanzado las 20 preguntas.")
            break

        ans = input(f"{i}. {texto} (s/n): ").lower() #normaliza uppercase y lowercase
        # Ejecutamosw la función que elimine candidatos que no coincidan con la respuesta
        candidatos = preguntar(ans, prop, candidatos)

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
