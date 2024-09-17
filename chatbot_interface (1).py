import tkinter as tk
from tkinter import scrolledtext
from chatbot_logic import chatbot_response

# Função para enviar a mensagem no chat
def send_message():
    user_input = input_field.get()

    if user_input.strip() != "":
        # Insere a mensagem do usuário à direita
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "\n" + " " * 30 + user_input + "\n", "right")
        chat_window.tag_configure("right", justify="right")

        # Obtém a resposta do chatbot
        response = chatbot_response(user_input)

        # Insere a resposta do chatbot à esquerda
        chat_window.insert(tk.END, response + '\n\n', "left")
        chat_window.tag_configure("left", justify="left")

        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)
        input_field.delete(0, tk.END)

# Função para criar botões arredondados
def create_rounded_button(parent, text, command, bg="#007bff", fg="white"):
    return tk.Button(parent, text=text, command=command, font=("Helvetica", 10, "bold"), bg=bg, fg=fg, 
                     relief="flat", bd=0, highlightthickness=0)

# Interface gráfica
root = tk.Tk()

root.title("TOP-AI")

root.geometry("600x500")
root.resizable(0, 0)

# Área de chat
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, font=("Helvetica", 12))
chat_window.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.75)

# Campo de entrada de texto
input_field = tk.Entry(root, font=("Helvetica", 12))
input_field.place(relx=0.02, relwidth=0.76, relheight=0.1, rely=0.8)

# Botão de envio de mensagem (arredondado)
send_button = create_rounded_button(root, "Enviar", send_message)
send_button.place(relx=0.8, rely=0.8, relwidth=0.18, relheight=0.1)

# Configurar o campo de entrada para focar automaticamente
input_field.focus_set()

# Loop principal da interface gráfica
root.mainloop()
