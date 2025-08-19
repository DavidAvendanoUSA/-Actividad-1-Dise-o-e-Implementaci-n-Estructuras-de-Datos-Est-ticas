class Calificacion:
    def __init__(self, actividad, nota):
        self.actividad = actividad
        self.nota = nota

    def __str__(self):
        return f"{self.actividad}: {self.nota}"

class Estudiante:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.calificaciones = []

    def __str__(self):
        return f"{self.id}: {self.nombre}: {self.calificaciones}"

class GestorNotas:
    
    @staticmethod
    def agregar_calificacion(actividad, nota, estudiante):
        estudiante.calificaciones.append(Calificacion(actividad, nota))
        print(f"Calificación añadida: {actividad} - {nota}")

    @staticmethod
    def eliminar_calificacion(estudiante, actividad):
        for i, cal in enumerate(estudiante.calificaciones):
            if cal.actividad == actividad:
                del estudiante.calificaciones[i]
                print(f"Calificación eliminada: {actividad}")
                return
        print(f"No se encontró la actividad '{actividad}' para eliminar.")

    @staticmethod
    def modificar_calificacion(estudiante, actividad, nueva_nota):
        for cal in estudiante.calificaciones:
            if cal.actividad == actividad:
                cal.nota = nueva_nota
                print(f"Calificación modificada: {actividad} - {nueva_nota}")
                return
        print(f"No se encontró la actividad '{actividad}' para modificar.")

    @staticmethod
    def calcular_promedio(estudiante):
        if not estudiante.calificaciones:
            return 0
        total = sum(cal.nota for cal in estudiante.calificaciones)
        promedio = total / len(estudiante.calificaciones)
        return promedio

    @staticmethod
    def mostrar_calificaciones(estudiante):
        if not estudiante.calificaciones:
            print("No hay calificaciones registradas.")
        else:
            print("Lista de Calificaciones:")
            for cal in estudiante.calificaciones:
                print(f" - {cal}")


if __name__ == "__main__":
    Est1 = Estudiante(1, "Pepe")
    
    GestorNotas.agregar_calificacion("Examen Parcial", 85, Est1)
    GestorNotas.agregar_calificacion("Tarea 1", 90, Est1)
    GestorNotas.agregar_calificacion("Proyecto Final", 95, Est1)

    GestorNotas.mostrar_calificaciones(Est1)

    GestorNotas.modificar_calificacion(Est1, "Tarea 1", 92)
    GestorNotas.eliminar_calificacion(Est1, "Examen Parcial")

    GestorNotas.mostrar_calificaciones(Est1)

    promedio = GestorNotas.calcular_promedio(Est1)
    print(f"Promedio de {Est1.nombre} con id {Est1.id}: {promedio:.2f}")

