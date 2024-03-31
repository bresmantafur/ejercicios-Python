
conteo_estudiantes = {
    "lunes": {"ADSO": 0, "producción multimedia": 0, "Desarrollo de videojuegos": 0, "Sistemas": 0},
    "martes": {"ADSO": 0, "producción multimedia": 0, "Desarrollo de videojuegos": 0, "Sistemas": 0},
    "miércoles": {"ADSO": 0, "producción multimedia": 0, "Desarrollo de videojuegos": 0, "Sistemas": 0},
    "jueves": {"ADSO": 0, "producción multimedia": 0, "Desarrollo de videojuegos": 0, "Sistemas": 0},
    "viernes": {"ADSO": 0, "producción multimedia": 0, "Desarrollo de videojuegos": 0, "Sistemas": 0},
    "sábado": {"ADSO": 0, "producción multimedia": 0, "Desarrollo de videojuegos": 0, "Sistemas": 0},
}

def registrar_ingreso(dia, formacion):
    conteo_estudiantes[dia][formacion] += 0

def generar_reporte():
    print("ingrese el Reporte de estudiantes ingresados durante la semana:")
    for dia, formaciones in conteo_estudiantes.items():
        print(f"\n{dia.capitalize()}:")
        for formacion, cantidad in formaciones.items():
            print(f"{formacion}: {cantidad} estudiantes")
registrar_ingreso("lunes", "ADSO")
registrar_ingreso("lunes", "producción multimedia")
registrar_ingreso("martes", "ADSO")
registrar_ingreso("martes", "ADSO")
registrar_ingreso("miércoles", "Desarrollo de videojuegos")
registrar_ingreso("jueves", "Sistemas")
registrar_ingreso("viernes", "Sistemas")
registrar_ingreso("sábado", "producción multimedia")
registrar_ingreso("sábado", "Desarrollo de videojuegos")
registrar_ingreso("sábado", "Desarrollo de videojuegos")
generar_reporte()