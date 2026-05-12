# ══════════════════════════════════════════════════════════════
# proyecto.py · Ficha 3236582 · SENA CTM Itagüí
# Completá con los datos reales de tu proyecto
# ══════════════════════════════════════════════════════════════

nombre_proyecto = "brans prubea2"           # nombre de tu proyecto
descripcion     = "resuelve dudas de git"           # qué problema resuelve
tecnologias     = ['python','git','github','git bash']           # ["HTML", "Python", "MySQL"]
integrantes     = ['brandon','silva','jurado']           # ["Nombre 1", "Nombre 2"]
funcionalidades = ['prueba','git','commit','certificados']           # ["Login", "Registro", "Reportes"]


def mostrar_info():
    print(f"Proyecto:      {nombre_proyecto}")
    print(f"Descripción:   {descripcion}")
    print(f"Equipo:        {', '.join(integrantes)}")
    print(f"Tecnologías:   {', '.join(tecnologias)}")
    print(f"Funcionalidades:")
    for f in funcionalidades:
        print(f"  - {f}")


mostrar_info()