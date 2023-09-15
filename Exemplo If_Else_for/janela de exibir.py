def main():
    nome = input("Digite seu nome: ")
    print("Bom dia, " + nome)

if __name__ == "__main__":
    main()
    import tkinter as tk
from tkinter import messagebox

def mostrar_mensagem():
    nome = entrada.get()
    if nome:
        mensagem = "Bom dia, " + nome
        messagebox.showinfo("Mensagem", mensagem)
    else:
        messagebox.showwarning("Aviso", "Digite seu nome!")

# Configuração da janela
janela = tk.Tk()
janela.title("Saudação")

# Criação e posicionamento dos elementos
rotulo = tk.Label(janela, text="Digite seu nome:")
rotulo.pack(pady=10)

entrada = tk.Entry(janela)
entrada.pack(pady=5)

botao = tk.Button(janela, text="Saudar", command=mostrar_mensagem)
botao.pack(pady=10)

# Inicia o loop da interface
janela.mainloop()