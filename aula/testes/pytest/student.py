class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    # Metodo para adicionar uma nota
    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    # Metodo para verificar se o aluno passou
    def is_passing(self):
        average = self.calculate_average()
        return average >= 60