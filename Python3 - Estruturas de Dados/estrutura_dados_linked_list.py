# Listas simplesmente encadeadas são estruturas de dados dinâmicas compostas por nós. Cada nó na lista contém um valor (ou valores) e um ponteiro para o próximo nó.
# O primeiro nó da lista é denominado de “head”, enquanto o último nó da lista é chamado de “tail”. Vale lembrar que você pode encontrar listas encadeadas 
# que possuem apenas sua implementação com o “head”, sem o “tail”.

# O desafio para o dia de hoje é implementar um sistema de gerenciamento de pacientes em um hospital usando listas simplesmente encadeadas.
# Cada paciente deve ter um nome, um número de identificação e o estado de saúde atual do paciente, como “estável”, “em tratamento intensivo”, 
# “em estado crítico”, entre outros. O sistema deve permitir adicionar novos pacientes, remover pacientes e listar todos os pacientes em ordem de chegada.

class Paciente:
    def __init__(self, paciente, estado):
        self.paciente = paciente
        self.estado = estado
        self.proximo = None
    

    def __str__(self):
        return f'Paciente: {self.paciente} | Estado de Saúde atual: {self.estado}'

class ListaDePacientes:
    ...