import customtkinter as ctk

#Configuração aparencia
ctk.set_appearance_mode('dark')

#Criação das funções de funcionalidade

def validar_login():
    usuario =campo_usuario.get()
    senha = campo_senha.get()

    #Verificar se o usuario é igual a joao e senha 1234

    if usuario =='joao' and senha == '1234':
        resultado_login.configure(text='Login feito com sucesso', text_color ='green')

    else:
        resultado_login.configure(text='Login incorreto', text_color='red')

#criação da janela principal
app = ctk.CTk()
app.title('Tela de login')
app.geometry('400x500')

#Criação dos campos
#lable

label_usuario = ctk.CTkLabel(app, text='Usuário')
label_usuario.pack(pady=10)

#entry

campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)
#lable

label_senha  = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=10)

#entry

campo_senha = ctk.CTkEntry(app, placeholder_text='Digite seu senha')
campo_senha.pack(pady=10)

#button

botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=10)
#Campo feedback de login

resultado_login =ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)

app.mainloop()