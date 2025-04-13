from unittest import TestCase

from aula.testes.unit_test.student import Student

# Cria a classe TestStudent que herda de TestCase
class TestStudent(TestCase):

    # Testa o metodo calculate_average da classe Student
    def test_calculate_average(self):
        # Cria instancias da classe Student com diferentes notas
        student1 = Student("Alice", [70, 80, 90])
        student2 = Student("Bob", [50, 70, 60])
        student3 = Student("Charlie", [])

        # Verifica se o metodo calculate_average retorna o valor correto
        # Se a instância student1 ao usar o metodo de calcular a media
        # O resultado deve ser 80
        self.assertEqual(student1.calculate_average(), 80)
        self.assertEqual(student2.calculate_average(), 60)
        self.assertEqual(student3.calculate_average(), 0)

    def test_is_passing(self):
        student1 = Student("Alice", [70, 80, 90])
        student2 = Student("Bob", [50, 70, 60])
        student3 = Student("Charlie", [])

        # Se retornar true, então o aluno passou
        self.assertTrue(student1.is_passing())
        self.assertTrue(student2.is_passing())

        #Neste caso é assertFalse, pois a media é 0, logo não passou
        self.assertFalse(student3.is_passing())


