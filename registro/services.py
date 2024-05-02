from registro.models import Curso, Estudiante, Profesor, Direccion

def crear_curso(codigo, nombre, version):
    curso = Curso(codigo=codigo,nombre=nombre,version=version)
    curso.save()
    return curso


def crear_profesor(rut,nombre,apellido,activo,creado_por):
    profesor = Profesor(rut=rut,nombre=nombre,apellido=apellido,activo=activo,creado_por=creado_por)
    profesor.save()
    return profesor


def crear_estudiante(rut,nombre,apellido,fecha_nac,activo,creado_por):
    alumno = Estudiante(rut=rut,nombre=nombre,apellido=apellido,fecha_nac=fecha_nac,activo=activo,creado_por=creado_por)
    alumno.save()
    return alumno


def crear_direccion(calle,numero,dpto,comuna,ciudad,region,estudiante_id,pk_id):
    estudiante_id = Estudiante.objects.get(rut=pk_id)
    direccion = Direccion(calle=calle,numero=numero,dpto=dpto,comuna=comuna,ciudad=ciudad,region=region,estudiante_id=estudiante_id)
    direccion.save()
    return direccion


def obtiene_estudiante(pk_id):    
    try:
        estudiante = Estudiante.objects.get(rut=pk_id)
        return estudiante
    except:
        print("error en obtiene estudiante")


def obtiene_profesor(pk_id):    
    try:
        profe = Profesor.objects.get(rut=pk_id)
        return profe
    except:
        print("error en obtiene profesor")


def obtiene_curso(pk_id):    
    try:
        curso = Curso.objects.get(codigo=pk_id)
        return curso
    except:
        print("error en obtiene curso")


def agrega_profesor_a_curso(pk_id_profe, pk_id_curso):
    try:
        profe = Profesor.objects.get(rut=pk_id_profe)
        curso = Curso.objects.get(codigo=pk_id_curso)
        profe.cursos.add(curso)
        return True
    except:
        print("error en agregar profe a curso")


def agrega_cursos_a_estudiante(pk_id_curso, pk_id_estudiante):
    try:
        estudiante = Estudiante.objects.get(rut=pk_id_estudiante)
        curso = Curso.objects.get(codigo=pk_id_curso)
        estudiante.cursos.add(curso)
        return True
    except:
        print("error en agregar curso a estudiante")


def imprimir_estudiante_cursos():
    estudiantes = Estudiante.objects.all()
    for estudiante in estudiantes:
        for curso in estudiante.cursos.all():
            print(f"{curso.nombre}")