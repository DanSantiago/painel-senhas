import FreeSimpleGUI as sg
import winsound
import time
from datetime import datetime
import os
import sys

#define o tema a ser utilizado e os padrões de fonte
sg.theme('Default1')
menu_fonte = ('Arial', 11)
titulo_jan1 = ('Helvetica', 30, 'bold')
input_jan1 = ('Helvetica', 45, 'bold')
botao_fonte = ('Arial', 15)
botao_cor = 'black on #f0f0f0'
botao_borda = 2
titulo_jan2 = ('Helvetica', 100, 'bold')
sub_titulo_jan2 = ('Helvetica', 40, 'bold')
show_princ_fonte = ('Helvetica', 220, 'bold')
show_sec_fonte = ('Helvetica', 125, 'bold')
cor_fundo = '#174478'
show_largura = (5,1)
nome_fonte = ('Helvetica', 50, 'bold')
largura_nome = (22,1)
relogio_fonte = ('Helvetica', 20, 'bold')

#imagens utilizadas em base64
logo = b'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'
proximo = b'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAATzaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjYtYzE0NSA3OS4xNjM0OTksIDIwMTgvMDgvMTMtMTY6NDA6MjIgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIiB4bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGhvdG9zaG9wLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE5IChXaW5kb3dzKSIgeG1wOkNyZWF0ZURhdGU9IjIwMjUtMDMtMDhUMTA6MDY6MTAtMDM6MDAiIHhtcDpNb2RpZnlEYXRlPSIyMDI1LTAzLTA4VDEwOjA3OjMwLTAzOjAwIiB4bXA6TWV0YWRhdGFEYXRlPSIyMDI1LTAzLTA4VDEwOjA3OjMwLTAzOjAwIiBkYzpmb3JtYXQ9ImltYWdlL3BuZyIgcGhvdG9zaG9wOkNvbG9yTW9kZT0iMyIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDplMzM3ZDM5NC05ZWYxLTU0NDUtYmY3OC0w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'
desfazer = b'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAATzaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjYtYzE0NSA3OS4xNjM0OTksIDIwMTgvMDgvMTMtMTY6NDA6MjIgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIiB4bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGhvdG9zaG9wLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE5IChXaW5kb3dzKSIgeG1wOkNyZWF0ZURhdGU9IjIwMjUtMDMtMDhUMTA6MDY6MDgtMDM6MDAiIHhtcDpNb2RpZnlEYXRlPSIyMDI1LTAzLTA4VDEwOjA3OjUwLTAzOjAwIiB4bXA6TWV0YWRhdGFEYXRlPSIyMDI1LTAzLTA4VDEwOjA3OjUwLTAzOjAwIiBkYzpmb3JtYXQ9ImltYWdlL3BuZyIgcGhvdG9zaG9wOkNvbG9yTW9kZT0iMyIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDplOWEzZTU3NS01Y2YxLWM3NGQtODU5MC05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'
chamar = b'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAAHYAAAB2AH6XKZyAAAE82lUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDUgNzkuMTYzNDk5LCAyMDE4LzA4LzEzLTE2OjQwOjIyICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHhtcDpDcmVhdGVEYXRlPSIyMDI1LTAzLTA4VDEwOjA2OjAyLTAzOjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAyNS0wMy0wOFQxMDowNzo1My0wMzowMCIgeG1wOk1ldGFkYXRhRGF0ZT0iMjAyNS0wMy0wOFQxMDowNzo1My0wMzowMCIgZGM6Zm9ybWF0PSJpbWFnZS9wbmciIHBob3Rvc2hvcDpDb2xvck1vZGU9IjMiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6Njk2ZmZlN2UtMWVjOS1kMTQ1LWI4MjAtMzE3ZmZkNjgwY2VlIiB4bXBNTTpEb2N1bWVudElE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'
repetir = b'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADdcAAA3XAUIom3gAAATzaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjYtYzE0NSA3OS4xNjM0OTksIDIwMTgvMDgvMTMtMTY6NDA6MjIgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIiB4bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGhvdG9zaG9wLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE5IChXaW5kb3dzKSIgeG1wOkNyZWF0ZURhdGU9IjIwMjUtMDMtMDhUMTA6MzA6MzMtMDM6MDAiIHhtcDpNb2RpZnlEYXRlPSIyMDI1LTAzLTA4VDEwOjMwOjU4LTAzOjAwIiB4bXA6TWV0YWRhdGFEYXRlPSIyMDI1LTAzLTA4VDEwOjMwOjU4LTAzOjAwIiBkYzpmb3JtYXQ9ImltYWdlL3BuZyIgcGhvdG9zaG9wOkNvbG9yTW9kZT0iMyIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo3MmMwZGJiYy0wZDVjLTNkNDYtOGRhNy1j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'

#função para lidar com o path dos sons
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#cria o layout da janela 1
def make_win1():

    menu_def = [
                 ['&Painel', ['&Abrir painel     F1', '&Zerar painel    F5']],
                 ['&Senhas', ['Informar cliente    F11', 'Limpar cliente']],
                 ['&Informações', ['Exibir número total de senhas chamadas']]
                ]

    layout = [
        [
         [sg.MenubarCustom(menu_def, pad=(0,0), key='MENU', font=menu_fonte, bar_font=menu_fonte)],
         sg.Text('SENHA', size=(6, 1), font=titulo_jan1, text_color='#174478'),
         sg.Input(key='senhainicial', size=(10, 1), font=input_jan1, text_color='yellow', background_color=cor_fundo, justification='right', enable_events = True), #criar limitação de 4 caracteres
         sg.Button('Chamar', font=botao_fonte, image_data=chamar, border_width=botao_borda, button_color = botao_cor, ),
         sg.Button('Repetir', font=botao_fonte, image_data=repetir, border_width=botao_borda, button_color= botao_cor, ),
         sg.Button('Desfazer', font=botao_fonte, image_data=desfazer, border_width=botao_borda, button_color= botao_cor, ),
         sg.Button('Próximo', font=botao_fonte, image_data=proximo, border_width=botao_borda, button_color=botao_cor, )
        ]]

    return sg.Window('Painel de senhas - v1.0', layout, finalize=True, icon='monitor.ico')

#cria o layout da janela 2
def make_win2():
    p_esquerda = [
               [sg.Text('                                                                     '),sg.Text('SENHA', font=titulo_jan2, text_color='#174478')],
               [sg.Text(justification='center', key='s1', text_color='yellow', background_color=cor_fundo, font=show_princ_fonte, size=show_largura)],
               [sg.Text(justification='center', key='name', text_color='white', background_color=cor_fundo, font=nome_fonte, size=largura_nome)],
               [sg.Text('', size=(53, 1), font=relogio_fonte, text_color='white', justification='center', key='hora', background_color=cor_fundo)],
             ]

    p_direita = [
               [sg.Text('                                                                     '),sg.Text('Anteriores', font=sub_titulo_jan2, text_color='#174478')],
               [sg.Text(justification='center', key='s2', text_color='yellow', background_color=cor_fundo, font=show_sec_fonte, size=show_largura)],
               [sg.Text(justification='center', key='s3', text_color='yellow', background_color=cor_fundo, font=show_sec_fonte, size=show_largura)],
               [sg.Text(justification='center', key='s4', text_color='yellow', background_color=cor_fundo, font=show_sec_fonte, size=show_largura)]
             ]

    layout = [
        [sg.Column(p_esquerda, element_justification='right'), sg.Text(''), sg.Column(p_direita, element_justification='right')]
    ]
    return sg.Window('Painel de senhas', layout, finalize=True, icon='monitor.ico')

#função principal
def main():
    #cria o objeto da janela 1 e define a janela 2 como vazia
    window1, window2 = make_win1(), None

    #cria a lista das senhas e a variável de nome do cliente
    valores = []
    cliente = ''

    #organiza as imagens dos botões de forma alinhada a esquerda do texto
    for key in ('Chamar', 'Repetir', 'Desfazer', 'Próximo'):
        window1[key].block_focus()
        window1[key].widget.configure(compound="left", width=0, height=0)

    #vincula as teclas de atalho com os botões respectivos
    window1.bind('<F1>', 'Abrir painel     F1')
    window1.bind('<F5>', 'Zerar painel    F5')
    window1.bind('<F11>', 'Informar cliente    F11')

    #loop de eventos
    while True:

        #define a leitura de eventos para todas as janelas e com um timeout (para atualizar o relógio)
        window, event, values = sg.read_all_windows(timeout=50)

        #checa se o tamanho da senha é maior que 5 caracteres, e se for, bloqueia
        if window == window1 and len(values['senhainicial']) > 5:
            window1['senhainicial'].update(values['senhainicial'][:-1])

        #checa se o caractere digitado é um número e se não for, bloqueia
        if window == window1 and event == 'senhainicial' and len(values['senhainicial']) and values['senhainicial'][-1] not in ('0123456789'):
            window1['senhainicial'].update(values['senhainicial'][:-1])

        #valida o fechamento das janelas (se for a janela 2, volta o foco para a 1 e se for a 1, fecha o programa
        if event == sg.WIN_CLOSED:
            window.close()
            if window == window2:
                window2 = None
            elif window == window1:
                break

        #uso do botão de chamada
        elif event == 'Chamar' and len(values['senhainicial']):

            if not window2:
                window2 = make_win2()
                window2.Maximize()

            if len(valores) > 0:
                if valores[-1] != values['senhainicial']:
                    valores.append(values['senhainicial'])
                    window2['s1'].update(text_color='yellow')
                    window2['s1'].update(values['senhainicial'])
                    ch = resource_path("Chamada.wav")
                    winsound.PlaySound(ch, winsound.SND_FILENAME + winsound.SND_ASYNC)
                    data_e_hora_atuais = datetime.now()
                    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
                    with open('log.txt', 'a') as arquivo:
                        arquivo.write(f'Data: {data_e_hora_em_texto}  |  Senha: {valores[-1]}\n')
                    if cliente != '':
                        window2['name'].update(cliente)
                        cliente = ''
                    else:
                        window2['name'].update(cliente)
            else:
                valores.append(values['senhainicial'])
                window2['s1'].update(text_color='yellow')
                window2['s1'].update(values['senhainicial'])
                ch = resource_path("Chamada.wav")
                winsound.PlaySound(ch, winsound.SND_FILENAME + winsound.SND_ASYNC)
                data_e_hora_atuais = datetime.now()
                data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
                with open('log.txt', 'a') as arquivo:
                    arquivo.write(f'Data: {data_e_hora_em_texto}  |  Senha: {valores[-1]}\n')
                if cliente != '':
                    window2['name'].update(cliente)
                    cliente = ''
                else:
                    window2['name'].update(cliente)
            if int(valores[-1]) <= 99999:
                if len(valores) > 1:
                    window2['s2'].update(valores[len(valores) - 2])
                if len(valores) > 2:
                    window2['s3'].update(valores[len(valores) - 3])
                if len(valores) > 3:
                    window2['s4'].update(valores[len(valores) - 4])

        # uso do botão de repetir
        elif event == 'Repetir' and window2:
            if len(valores) > 0:
                window2['s1'].update(valores[-1])
                window2['s1'].update(text_color='orangered')
                ch = resource_path("Repetir.wav")
                winsound.PlaySound(ch, winsound.SND_FILENAME + winsound.SND_ASYNC)

        # uso do botão de próximo
        elif event == 'Próximo' and window2:
            if len(valores) > 0:
                if int(valores[-1]) < 99999:
                    novo_valor = int(valores[-1]) + 1
                    window['senhainicial'].update(str(novo_valor))
                    valores.append(str(novo_valor))
                    window2['s1'].update(text_color='yellow')
                    window2['s1'].update(valores[-1])
                    ch = resource_path("Chamada.wav")
                    winsound.PlaySound(ch, winsound.SND_FILENAME + winsound.SND_ASYNC)
                    data_e_hora_atuais = datetime.now()
                    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
                    with open('log.txt', 'a') as arquivo:
                        arquivo.write(f'Data: {data_e_hora_em_texto}  |  Senha: {valores[-1]}\n')
                    if cliente != '':
                        window2['name'].update(cliente)
                        cliente = ''
                    else:
                        window2['name'].update(cliente)
                else:
                    pass

                if int(valores[-1]) <= 99999:
                    if len(valores) > 1:
                        window2['s2'].update(valores[len(valores) - 2])
                    if len(valores) > 2:
                        window2['s3'].update(valores[len(valores) - 3])
                    if len(valores) > 3:
                        window2['s4'].update(valores[len(valores) - 4])

        # uso do botão de desfazer
        elif event == 'Desfazer' and window2:
            if len(valores) > 1:
                valores.pop()
                window['senhainicial'].update(valores[-1])
                window2['s1'].update(text_color='yellow')
                window2['s1'].update(valores[-1])
                data_e_hora_atuais = datetime.now()
                data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
                with open('log.txt', 'a') as arquivo:
                    arquivo.write(f'Data: {data_e_hora_em_texto}  |  Senha: {valores[-1]}\n')
                if len(valores) == 1:
                    window2['s2'].update('')
                elif len(valores) > 1:
                    window2['s2'].update(valores[len(valores) - 2])
                if len(valores) == 2:
                    window2['s3'].update('')
                elif len(valores) > 2:
                    window2['s3'].update(valores[len(valores) - 3])
                if len(valores) == 3:
                    window2['s4'].update('')
                elif len(valores) > 3:
                    window2['s4'].update(valores[len(valores) - 4])
            else:
                pass

        # uso da opção de zerar painel
        elif event == 'Zerar painel    F5' and window2:
            while True:
                senha = ''
                senha = sg.popup_get_text('Informe a senha de liberação: ', title='Liberação', icon='monitor.ico', password_char='*')
                if senha == 'adminadmin':
                    valores.clear()
                    window2['s1'].update('')
                    window2['s2'].update('')
                    window2['s3'].update('')
                    window2['s4'].update('')
                    break
                elif not senha:
                    break
                else:
                    sg.popup('Senha incorreta!', title='Erro', icon='monitor.ico')

        # uso da opção de abrir painel
        elif event == 'Abrir painel     F1' and not window2:
            if len(valores) == 0:
                window2 = make_win2()
                window2.Maximize()
            else:
                window2 = make_win2()
                window2.Maximize()
                window['senhainicial'].update(valores[-1])
                window2['s1'].update(text_color='yellow')
                window2['s1'].update(valores[-1])
                if len(valores) == 1:
                    window2['s2'].update('')
                elif len(valores) > 1:
                    window2['s2'].update(valores[len(valores) - 2])
                if len(valores) == 2:
                    window2['s3'].update('')
                elif len(valores) > 2:
                    window2['s3'].update(valores[len(valores) - 3])
                if len(valores) == 3:
                    window2['s4'].update('')
                elif len(valores) > 3:
                    window2['s4'].update(valores[len(valores) - 4])

        # uso da opção de informar nome do cliente
        elif event == 'Informar cliente    F11':
            cliente = sg.popup_get_text('Informe o nome do cliente: ', title='Definir cliente', icon='monitor.ico')

        # uso da opção de limpar cliente
        elif event == 'Limpar cliente':
            cliente = ''

        # uso da opção de exibir total de senhas chamadas
        elif event == 'Exibir número total de senhas chamadas':
            sg.popup(f'Total de senhas chamadas: {len(valores)}', title='Relatório', icon='monitor.ico')
        # checa o timeout caso nada tenha sido realizado
        elif window2 and sg.TIMEOUT_EVENT:
            window2['hora'].update(time.strftime('%H:%M:%S'))

    window.close()

if __name__ == '__main__':
    main()