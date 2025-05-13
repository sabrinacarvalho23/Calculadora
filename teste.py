import unittest

# Funções da calculadora
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Erro: divisão por zero."
    return n1 / n2

def power(n1, n2):
    return n1 ** n2


class TestCalculadoraSimples(unittest.TestCase):

    def test_adicao(self):
        # Testa a adição simples
        resultado = add(2, 3)
        self.assertEqual(resultado, 5)  # Espera 5 como resultado

    def test_subtracao(self):
        # Testa a subtração simples
        resultado = subtract(5, 3)
        self.assertEqual(resultado, 2)  # Espera 2 como resultado

    def test_multiplicacao(self):
        # Testa a multiplicação simples
        resultado = multiply(2, 3)
        self.assertEqual(resultado, 6)  # Espera 6 como resultado

    def test_divisao(self):
        # Testa a divisão simples
        resultado = divide(6, 3)
        self.assertEqual(resultado, 2)  # Espera 2 como resultado

    def test_divisao_por_zero(self):
        # Testa a divisão por zero
        resultado = divide(1, 0)
        self.assertEqual(resultado, "Erro: divisão por zero.")  # Espera erro

    def test_potenciacao(self):
        # Testa a potenciação simples
        resultado = power(2, 3)
        self.assertEqual(resultado, 8)  # Espera 8 como resultado


if __name__ == '__main__':
    unittest.main()
