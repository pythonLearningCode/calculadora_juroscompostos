from tkinter import *


def calcula_juros():
    try:
        capital = float(entrada_capital.get())
        taxa = float(entrada_taxa.get()) / 100
        periodo = float(entrada_periodo.get())
        mensalidade = float(entrada_mensalidade.get())
        montante = (capital * (1 + taxa) ** periodo) + (mensalidade * (((1 + taxa) ** periodo) - 1) / taxa)
        acumulado = mensalidade * periodo + capital
        juros = montante - acumulado
        label_montante['text'] = 'Montante: ' + str(f'{round(montante, 2)}')
        label_acumulado['text'] = 'Investido: ' + str(f'{round(acumulado, 2)}')
        label_juros['text'] = 'Juros: ' + str(f'{round(juros, 2)}')
    except ValueError:
        label_montante['text'] = 'Valor incorreto inserido'


root = Tk()

frame_mestre = Frame(root)

frame_capital = Frame(frame_mestre, pady='20')
label_capital = Label(frame_capital, text='Capital inicial:')
label_capital.pack(side='left')
entrada_capital = Entry(frame_capital)
entrada_capital.pack(side='left')
frame_capital.pack()


frame_taxa = Frame(frame_mestre, pady='20')
label_taxa = Label(frame_taxa, text='Taxa mensal(%):')
label_taxa.pack(side='left')
entrada_taxa = Entry(frame_taxa)
entrada_taxa.pack(side='left')
frame_taxa.pack()

frame_mensalidade = Frame(frame_mestre, pady='20')
label_mensalidade = Label(frame_mensalidade, text='Mensalidade:')
label_mensalidade.pack(side='left')
entrada_mensalidade = Entry(frame_mensalidade)
entrada_mensalidade.pack(side='left')
frame_mensalidade.pack()

frame_periodo = Frame(frame_mestre, pady='20')
label_periodo = Label(frame_periodo, text='Periodo(meses):')
label_periodo.pack(side='left')
entrada_periodo = Entry(frame_periodo)
entrada_periodo.pack(side='left')
frame_periodo.pack()

botao_calcular = Button(frame_mestre, text='CALCULAR', pady='10')
botao_calcular['command'] = calcula_juros
botao_calcular.pack()

frame_resultados = Frame(frame_mestre)
label_montante = Label(frame_resultados, text='Pressione o botão para calcular', pady='20')
label_montante.pack(side='left')

label_acumulado = Label(frame_resultados, text='', pady='20')
label_acumulado.pack(side='left')

label_juros = Label(frame_resultados, text='', pady='20')
label_juros.pack(side='left')
frame_resultados.pack()

frame_mestre.pack()
root.geometry('400x400+200+200')
root.title('CALCULADORA JUROS COMPOSTOS')
root.mainloop()
