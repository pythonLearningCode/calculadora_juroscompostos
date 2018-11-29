from tkinter import *


def calcula_juros():
    capital = float(entrada_capital.get())
    taxa = float(entrada_taxa.get())
    periodo = float(entrada_periodo.get())
    mensalidade = float(entrada_mensalidade.get())
    montante = (capital * (1 + taxa) ** periodo) + (mensalidade * (((1 + taxa) ** periodo) - 1) / taxa)
    label_montante['text'] = str(montante)


root = Tk()

frame_mestre = Frame(root)

frame_capital = Frame(frame_mestre, pady='20')
label_capital = Label(frame_capital, text='Capital inicial:')
label_capital.pack(side='left')
entrada_capital = Entry(frame_capital)
entrada_capital.pack(side='left')
frame_capital.pack()

frame_taxa = Frame(frame_mestre, pady='20')
label_taxa = Label(frame_taxa, text='Taxa mensal(decimal):')
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


label_montante = Label(frame_mestre, text='Pressione o botão para calcular', pady='20')
label_montante.pack()

frame_mestre.pack()
root.geometry('400x400+200+200')
root.title('CALCULADORA JUROS COMPOSTOS')
root.mainloop()
