import unittest
from clases.horario import Horario

class TestSiglaHorarios(unittest.TestCase):
    def test_creacion_horario_instancia(self):
        """Verifica que la clase Horario inicialice correctamente sus atributos de POO."""
        h = Horario(1, "Lunes", "07:00", "09:00", "Activo", 1, "ASG01", "AULA101", "2026-S1")
        self.assertEqual(h._dia_semana, "Lunes")
        self.assertEqual(h._estado, "Activo")

if __name__ == '__main__':
    unittest.main()
