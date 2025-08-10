class FilaAtendimento:
    """
    Representa uma fila de atendimento que segue o princípio FIFO (First-In, First-Out).
    """
    def __init__(self):
        """Inicializa a fila como uma lista vazia."""
        self.fila = []

    def adicionar_chamado(self, chamado):
        """Adiciona um novo chamado ao final da fila."""
        self.fila.append(chamado)
        print(f"\n✅ Chamado '{chamado}' adicionado à fila.")

    def atender_chamado(self):
        """Atende o primeiro chamado da fila (o mais antigo)."""
        if self.fila:
            chamado_atendido = self.fila.pop(0)  # Remove o primeiro item da lista
            print(f"\n▶️ Atendendo chamado: '{chamado_atendido}'.")
        else:
            print("\nℹ️ Não há chamados na fila para atender.")

    def visualizar_chamados(self):
        """Visualiza todos os chamados pendentes na fila."""
        print("\n--- 👁️ Fila de Atendimento Atual ---")
        if self.fila:
            print("Chamados pendentes:")
            for i, chamado in enumerate(self.fila, start=1):
                print(f"{i}. {chamado}")
        else:
            print("A fila está vazia.")
        print("------------------------------------")

# Bloco principal que torna o programa interativo
if __name__ == "__main__":
    # Cria uma instância da nossa fila de atendimento
    fila_atendimento = FilaAtendimento()
    
    # Loop principal do menu
    while True:
        # Exibe o menu de opções para o usuário
        print("\n--- Sistema de Fila de Atendimento ---")
        print("Escolha uma opção:")
        print("1. Adicionar novo chamado")
        print("2. Atender próximo chamado")
        print("3. Visualizar fila")
        print("4. Sair")

        # Pede ao usuário para escolher uma opção
        escolha = input("Digite o número da sua opção: ")

        # Processa a escolha do usuário
        if escolha == '1':
            descricao_chamado = input("Digite a descrição do chamado: ")
            if descricao_chamado: # Garante que o usuário digitou algo
                fila_atendimento.adicionar_chamado(descricao_chamado)
            else:
                print("\n❌ Descrição inválida. O chamado não foi adicionado.")
        
        elif escolha == '2':
            fila_atendimento.atender_chamado()
        
        elif escolha == '3':
            fila_atendimento.visualizar_chamados()

        elif escolha == '4':
            print("\nSaindo do sistema. Até logo!")
            break  # Encerra o loop e o programa
        
        else:
            print("\n❌ Opção inválida! Por favor, escolha um número de 1 a 4.")
        
        # Pausa para o usuário ler a saída antes de mostrar o menu novamente
        input("\nPressione Enter para continuar...")
