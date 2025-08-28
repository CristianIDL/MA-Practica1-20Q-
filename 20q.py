from base import database
from preguntas import questions

# Función para preguntas
# answer = "s/n", property = "propiedad clave de la lista questions" candidates="elementos de la base".
def preguntar(answer, property, candidates):
    # ans almacena True en el caso de que el usuario haya ingresado "s"
    ans = True if answer == "s" else False
    # Creamos un array vacío para agregar los elementos que coincidan
    baseFiltrada = []

    for d in candidates:
        # Si el atributo existe comparar
        if property in d:
            if d[property] == ans:
                baseFiltrada.append(d)
        else:
            # Si no existe asumimos False
            if not ans:
                baseFiltrada.append(d)
    return baseFiltrada


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
