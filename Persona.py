class Persona:
    def __init__ (self, name, lastname):
        self.name = name
        self.lastname = lastname
        print(self)
persona = Persona("joe", "Doe")

print(persona)
