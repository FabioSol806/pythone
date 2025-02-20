# Definisci la classe principale 'Employee'
class Employee:
    def __init__(self, nome, cognome, salario):
        self._nome = nome
        self._cognome = cognome
        self._salario = salario

    def __repr__(self):
         return self._nome + " " + self._cognome + " Il suo salario è EUR: " + str(self._salario)
    

# Definisci la sottoclasse 'Manager' ereditata da 'Employee'
class Manager(Employee):
    def __init__(self, nome, cognome, salario, reparto):
        super().__init__(nome, cognome, salario)
        self._reparto = reparto
    

    def __repr__(self):
        return self._nome + " " + self._cognome + " Lavora al Reparto: " + self._reparto + " Il suo salario è di EUR " + str(self._salario)

# Esempio di creazione degli oggetti

impiegato = Employee('Luca', 'Verdi', 30000)
manager = Manager('Giulia', 'Bianchi', 50000, 'Risorse Umane')

# Stampa degli oggetti
print(impiegato)  # Luca Verdi, Salario: 30000 EUR
print(manager)    # Giulia Bianchi, Reparto: Risorse Umane, Salario: 50000 EUR