class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    def toString(self):
        return f"{self.nombre}: {self.telefono} -- {self.email}"

class Agenda:
    def __init__(self):
        self.contactos = []
                
    def nuevo(self):
        nombre = input("Nombre: ")
        telefono = int(input("Telefono: "))
        email = input("Email: ")            
        self.contactos.append(Contacto(nombre, telefono, email))
        print("Guardado!")
            
    def eliminar(self):
        nombre=input("Eliminar: ")
        for c in self.contactos:
            if nombre == c.nombre:
                self.contactos.remove(c)
                return
        print("No se encontró \"%s\"" % (nombre))
    def buscar(self):
        nombre = input("Buscar: ")
        for c in self.contactos:
            if c.nombre == nombre:
                print(c.toString())
                return
        print("No se encontró \"%s\"" % (nombre))
    def listar(self):
        texto = "Todos los contactos: %s\n" % (len(self.contactos))
        for i in self.contactos:
            texto += i.toString() + "\n"
        print(texto)
    def editar(self):
        nombre = input("Buscar: ")
        for c in self.contactos:
            if c.nombre == nombre:
                print("Deje en blanco para no modificar")
                n_nombre = input("Nombre(%s): " % (c.nombre))
                if len(n_nombre) > 0:
                    c.nombre = n_nombre
                n_telefono = input("Telefono(%s): " % (c.telefono))
                if len(n_telefono) > 0:
                    c.telefono = int(n_telefono)
                n_email = input("Email(%s): " % (c.email))
                if len(n_email) > 0:
                    c.email = n_email
                print("Actualizado: ", c.toString()) 
                return
        print("No se encontró \"%s\"" % (nombre))

class AgendaCLI:
    def __init__(self):
        self.running = True
        self.agenda = Agenda()
    def start(self):
        self.show_options()
        while(self.running):
            cmd = input(">_").lower()
            if cmd == "nuevo":
                self.agenda.nuevo()
            if cmd == "listar":
                self.agenda.listar()
            if cmd == "buscar":
                self.agenda.buscar()
            if cmd == "editar":
                self.agenda.editar()
            if cmd == "elimnar":
                self.elimnar()
            if cmd == "salir":
                print("Finalizar")
                self.running = False
    def show_options(self):
        print("*"*40)
        print("Agenda - Lista de comandos")
        print("*"*40)
        print("nuevo - Añadir contacto")
        print("listar - Lista de contactos")
        print("buscar - Buscar contacto ")
        print("editar - Editar contacto")
        print("salir - Cerrar agenda")
        print("*"*40)

cli = AgendaCLI()
cli.start()