import os
import subprocess
import random
from datetime import datetime

# Define o diretório base
base_directory = os.path.join(os.path.expanduser('~'), 'Documents', 'wandistudio', 'wandicode')

def create_sketch(sketch_name):
    """Cria um novo esboço com o nome fornecido."""
    sketch_path = os.path.join(base_directory, sketch_name)
    if not os.path.exists(sketch_path):
        os.makedirs(sketch_path)
        command = f'arduino-cli sketch new "{sketch_path}"'
        subprocess.run(command, shell=True)
        print(f"Esboço criado em: {sketch_path}")
    else:
        print(f"Esboço com o nome '{sketch_name}' já existe.")

def list_sketches():
    """Lista todos os esboços existentes no diretório base."""
    print("Esboços existentes:")
    for folder in os.listdir(base_directory):
        folder_path = os.path.join(base_directory, folder)
        if os.path.isdir(folder_path):
            creation_time = os.path.getctime(folder_path)
            formatted_time = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
            print(f"- {folder} (Criado em: {formatted_time})")

def delete_sketch(sketch_name):
    """Exclui o esboço com o nome fornecido."""
    sketch_path = os.path.join(base_directory, sketch_name)
    if os.path.exists(sketch_path):
        subprocess.run(f'rmdir /s /q "{sketch_path}"', shell=True)
        print(f"Esboço '{sketch_name}' excluído.")
    else:
        print(f"Esboço '{sketch_name}' não encontrado.")

def main():
    while True:
        print("\nGerenciador de Esboços")
        print("1. Criar Novo Esboço")
        print("2. Listar Esboços")
        print("3. Excluir Esboço")
        print("4. Sair")

        choice = input("Escolha uma opção: ").strip()

        if choice == '1':
            sketch_name = input("Digite o nome do esboço (deixe em branco para nome automático): ").strip()
            if not sketch_name:
                random_number = random.randint(10, 99)
                sketch_name = f"wandicode{random_number}"
            create_sketch(sketch_name)
        elif choice == '2':
            list_sketches()
        elif choice == '3':
            sketch_name = input("Digite o nome do esboço a ser excluído: ").strip()
            delete_sketch(sketch_name)
        elif choice == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Abre o diretório no Explorador de Arquivos
    open_directory_command = f'explorer "{base_directory}"'
    subprocess.run(open_directory_command, shell=True)

if __name__ == "__main__":
    main()
