from tkinter import *
from tkinter import messagebox
import time
import datetime
import pygame,sys, random

pygame.init()
root = Tk()
root.title('SISTEMA DE VENDAS')
root.resizable(False,False)

root.configure(background='Khaki')

FrameABC =Frame(root, bg='black', bd=20, relief= RIDGE)
FrameABC.grid()

FrameABC1 =Frame(FrameABC, bg='Khaki', bd=10, relief= RIDGE)
FrameABC1.grid(row=0, column=0, columnspan=4, sticky=W)

FrameABC2 =Frame(FrameABC, bg='darkgrey', bd=10, relief= RIDGE)
FrameABC2.grid(row=1, column=0, sticky=W)

FrameABC3 =Frame(FrameABC, bg='darkgrey', bd=10, relief= RIDGE)
FrameABC3.grid(row=1, column=1, sticky=W)

FrameABC4 =Frame(FrameABC, bg='grey', bd=10, relief= RIDGE)
FrameABC4.grid(row=1, column=2, sticky=W)

FrameABC5 =Frame(FrameABC4, bg='darkgrey', bd=1, relief= RIDGE)
FrameABC5.grid(row=0, column=0, sticky=W)

FrameABC6 =Frame(FrameABC4, bg='darkgrey', bd=10, relief= RIDGE)
FrameABC6.grid(row=1, column=0, columnspan=4, sticky=W)

#Variaveis

Date1 = StringVar()
Time1 = StringVar()

Receipt_Ref = StringVar()
Tax = StringVar()
SubTotal = StringVar()
Total = StringVar()

Jeans_Jeggers = StringVar()
Coats_jackets = StringVar()
Sportwear = StringVar()
Dresses = StringVar()
Skirts = StringVar()
Swimwear = StringVar()
School_Uniform = StringVar()
Pyjamas = StringVar()

Jackets_Blazers = StringVar()
Formal_trousers = StringVar()
Formal_Shirts = StringVar()
Mens_Boots = StringVar()

Bed_Sheet = StringVar()
Pillows = StringVar()
Patterned_Bedding = StringVar()
Mattress_Protectors = StringVar()

Jeans_Jeggers.set('0')
Coats_jackets.set('0')
Sportwear.set('0')
Dresses.set('0')
Skirts.set('0')
Swimwear.set('0')
School_Uniform.set('0')
Pyjamas.set('0')
Jackets_Blazers.set('0')
Formal_trousers.set('0')
Formal_Shirts.set('0')
Mens_Boots.set('0')
Bed_Sheet.set('0')
Pillows.set('0')
Patterned_Bedding.set('0')
Mattress_Protectors.set('0')


Date1.set(time.strftime('%d/%m/%y'))
Time1.set(time.strftime('%H:%M:%S'))

#Funções

def Exit():
    result= messagebox.askquestion('Toque Requintado', 'Deseja realmente sair?')
    if result== 'yes':
        root.destroy()
        return
def Reset ():
    txtReceipt.delete('1.0', END)
    Jeans_Jeggers.set('0')
    Coats_jackets.set('0')
    Sportwear.set('0')
    Dresses.set('0')
    Skirts.set('0')
    Swimwear.set('0')
    School_Uniform.set('0')
    Pyjamas.set('0')
    Jackets_Blazers.set('0')
    Formal_trousers.set('0')
    Formal_Shirts.set('0')
    Mens_Boots.set('0')
    Bed_Sheet.set('0')
    Pillows.set('0')
    Patterned_Bedding.set('0')
    Mattress_Protectors.set('0')

def Total():

    Item1 = float(Jeans_Jeggers.get())
    Item2 = float(Coats_jackets.get())
    Item3 = float(Sportwear.get())
    Item4 = float(Dresses.get())
    Item5 = float(Skirts.get())
    Item6 = float(Swimwear.get())
    Item7 = float(School_Uniform.get())
    Item8 = float(Pyjamas.get())
    Item9 = float(Jackets_Blazers.get())
    Item10 = float(Formal_trousers.get())
    Item11 = float(Formal_Shirts.get())
    Item12 = float(Mens_Boots.get())
    Item13 = float(Bed_Sheet.get())
    Item14 = float(Pillows.get())
    Item15 = float(Patterned_Bedding.get())
    Item16 = float(Mattress_Protectors.get())

    Priceofitem1 = ('R$') + str('%.2f'% (Item1 * 20.00))
    Priceofitem2 = ('R$') + str('%.2f' % (Item2 * 50.00))
    Priceofitem3 = ('R$') + str('%.2f' % (Item3 * 30.00))
    Priceofitem4 = ('R$') + str('%.2f' % (Item4 * 9.00))
    Priceofitem5 = ('R$') + str('%.2f' % (Item5 * 35.00))
    Priceofitem6 = ('R$') + str('%.2f' % (Item6 * 37.00))
    Priceofitem7 = ('R$') + str('%.2f' % (Item7 * 78.00))
    Priceofitem8 = ('R$') + str('%.2f' % (Item8 * 24.00))
    Priceofitem9 = ('R$') + str('%.2f' % (Item9 * 29.00))
    Priceofitem10 = ('R$') + str('%.2f' % (Item10 * 30.00))
    Priceofitem11= ('R$') + str('%.2f' % (Item11 * 27.00))
    Priceofitem12 = ('R$') + str('%.2f' % (Item12 * 50.00))
    Priceofitem13 = ('R$') + str('%.2f' % (Item13 * 60.00))
    Priceofitem14 = ('R$') + str('%.2f' % (Item14 * 40.00))
    Priceofitem15 = ('R$') + str('%.2f' % (Item15 * 80.00))
    Priceofitem16 = ('R$') + str('%.2f' % (Item16 * 23.00))

    Feminino = (Item1 * 20.00) + (Item2 * 50.00) + (Item3 * 30.00)  + (Item4 * 9.00)
    Crianca = (Item5 * 35.00) + (Item6 * 37.00) + (Item7 * 78.00) + (Item8 * 24.00)
    Masculino = (Item9 * 29.00) + (Item10 * 30.00) + (Item11 * 27.00) + (Item12 * 50.00)
    Cama = (Item13 * 60.00) + (Item14 * 40.00) + (Item15 * 80.00) + (Item16 * 23.00)

    SubTotalofITENS = ('R$') + str('%.2f'% (Feminino + Crianca + Masculino + Cama))
    Tax = ('R$') + str('%.2f'% (Feminino + Crianca + Masculino + Cama) * 15)

    TT = (Feminino + Crianca + Masculino + Cama)
    TC = ((Feminino + Crianca + Masculino + Cama) * 15/100)

    TotalCost =  ('R$') + str('%.2f'% (TT + TC))

    txtReceipt.delete('1.0', END)
    x = random.randint(10747, 5000298)
    randomRef = str(x)
    Receipt_Ref.set('CUPOM'+randomRef)
    txtReceipt.insert(END, 'cupom Ref:\t\t\t' + Receipt_Ref.get() + '\n' + Date1.get() + '\t\t\t' + Time1.get() + '\n')
    txtReceipt.insert(END, '---------------------------------------------------------' + '\n')
    txtReceipt.insert(END, 'Item:\t\t' + 'Preço do item:' + '\n')
    txtReceipt.insert(END, '---------------------------------------------------------' + '\n')

    txtReceipt.insert(END, 'Blusa jeans:\t\t\t' + Priceofitem1 + '\n')
    txtReceipt.insert(END, 'Casaco:\t\t\t' + Priceofitem2 + '\n')
    txtReceipt.insert(END, 'Roupa Sport:\t\t\t' + Priceofitem3 + '\n')
    txtReceipt.insert(END, 'Vestido:\t\t\t' + Priceofitem4 + '\n')
    txtReceipt.insert(END, 'Saias:\t\t\t' + Priceofitem5 + '\n')
    txtReceipt.insert(END, 'Natação:\t\t\t' + Priceofitem6 + '\n')
    txtReceipt.insert(END, 'Uniforme:\t\t\t' + Priceofitem7 + '\n')
    txtReceipt.insert(END, 'Pijamas:\t\t\t' + Priceofitem8 + '\n')
    txtReceipt.insert(END, 'Casaco Masculino:\t\t\t' + Priceofitem9 + '\n')
    txtReceipt.insert(END, 'Calças:\t\t\t' + Priceofitem10 + '\n')
    txtReceipt.insert(END, 'Camisas:\t\t\t' + Priceofitem11 + '\n')
    txtReceipt.insert(END, 'Calçados:\t\t\t' + Priceofitem12 + '\n')
    txtReceipt.insert(END, 'Lençois:\t\t\t' + Priceofitem13 + '\n')
    txtReceipt.insert(END, 'Travesseiros:\t\t\t' + Priceofitem14 + '\n')
    txtReceipt.insert(END, 'Roupa de cama:\t\t\t' + Priceofitem15 + '\n')
    txtReceipt.insert(END, 'Colchão:\t\t\t' + Priceofitem16 + '\n')

lblDate=Label(FrameABC1,width=16, textvariable=Date1, font=('arial',30,'bold'), padx=9, pady=9, bd=14, bg='grey', fg='Cornsilk',
               justify=CENTER).grid(row=0, column=0)

lblTitle=Label(FrameABC1,width=16, text='\tToque Requintado\t', font=('consolas',30,'bold'), padx=9, pady=9, bd=14, bg='grey', fg='Cornsilk',
               justify=CENTER).grid(row=0, column=1)

lblTime=Label(FrameABC1,width=15, textvariable=Time1, font=('arial',30,'bold'), padx=9, pady=9, bd=14, bg='Grey', fg='Cornsilk',
               justify=CENTER).grid(row=0, column=2)

#LabelFeminino

lblFeminino=Label(FrameABC2, text='Feminino', font=('arial',20,'bold'), padx=8, bd=14, bg='grey', fg='Khaki',width=25,
               justify=CENTER).grid(row=0, column=0, columnspan=4)

lblJeansBlusa=Label(FrameABC2, text='Jeans Blusa:', font=('arial',15,'bold'), bg='darkgrey', fg='Khaki',
               justify=LEFT).grid(row=1, column=0)

lblCoatsjackets=Label(FrameABC2, text='Casaco:', font=('arial',15,'bold'), bg='darkgrey', fg='Khaki',
               justify=LEFT).grid(row=2, column=0)

lblSportwear=Label(FrameABC2, text='roupa Sport:', font=('arial',15,'bold'), bg='darkgrey', fg='Khaki',
               justify=LEFT).grid(row=3, column=0)

lblDresses=Label(FrameABC2, text='Vestidos:', font=('arial',15,'bold'), bg='darkgrey', fg='Khaki',
               justify=LEFT).grid(row=4, column=0)

#CAIXA DE TEXTO FEMININO

txtJeansBlusa=Entry(FrameABC2, textvariable=Jeans_Jeggers, font=('arial', 15, 'bold'),
                    bd=2, bg='white', fg='black', justify=CENTER).grid(row=1, column=1, pady=1)

txtJeansCoatsjackets=Entry(FrameABC2,textvariable=Coats_jackets, font=('arial', 15, 'bold'),
                    bd=2, bg='white', fg='black', justify=CENTER).grid(row=2, column=1, pady=1)

txtJeansSportwear=Entry(FrameABC2, textvariable=Sportwear, font=('arial', 15, 'bold'),
                    bd=2, bg='white', fg='black', justify=CENTER).grid(row=3, column=1, pady=1)

txtJeansDresses=Entry(FrameABC2,textvariable=Dresses, font=('arial', 15, 'bold'),
                    bd=2, bg='white', fg='black', justify=CENTER).grid(row=4, column=1, pady=1)

#Labelcriança

lblCrianca=Label(FrameABC2, text='Criança', font=('arial',20,'bold'), padx=8, bd=14, bg='grey', fg='Khaki', width=25,
               justify=CENTER).grid(row=5, column=0, columnspan=4)

lblSkirts=Label(FrameABC2, text='Saias:', font=('arial',15,'bold'), bg='darkgrey', fg='Khaki',
               justify=LEFT).grid(row=6, column=0)

lblSwimwear=Label(FrameABC2, text='Natação:', font=('arial',15,'bold'),bg='darkgrey', fg='Khaki',
               justify=LEFT).grid(row=7, column=0)

lblSchoolUniform=Label(FrameABC2, text='Uniforme:', font=('arial',15,'bold'), bg='darkgrey', fg='Khaki',
               justify=LEFT).grid(row=8, column=0)

lblPyjamas=Label(FrameABC2, text='Pijama:', font=('arial',15,'bold'), bg='darkgrey', fg='Khaki',
               justify=LEFT).grid(row=9, column=0)

#CAIXA DE TEXTO CRIANÇA

txtSkirts=Entry(FrameABC2,textvariable=Skirts, font=('arial', 15, 'bold'),
                    bd=2, bg='white', fg='black', justify=CENTER).grid(row=6, column=1, pady=1)

txtSwimwear=Entry(FrameABC2,textvariable=Swimwear, font=('arial', 15, 'bold'),
                    bd=2, bg='white', fg='black', justify=CENTER).grid(row=7, column=1, pady=1)

txtSchoolUniform=Entry(FrameABC2,textvariable=School_Uniform, font=('arial', 15, 'bold'),
                    bd=2, bg='white', fg='black', justify=CENTER).grid(row=8, column=1, pady=1)

txtPyjamas=Entry(FrameABC2,textvariable=Pyjamas, font=('arial', 15, 'bold'),
                    bd=2, bg='white', fg='black', justify=CENTER).grid(row=9, column=1, pady=1)


#Labelmasculino

lblMasculino=Label(FrameABC3, text='Masculino', font=('arial',20,'bold'), padx=8, bd=14, bg='grey', fg='Khaki',width=25,
               justify=CENTER).grid(row=0, column=0, columnspan=4)

lblCoats=Label(FrameABC3, text='Casacos:', font=('arial',15,'bold'), bg='darkgrey', fg='Khaki',
               justify=LEFT).grid(row=1, column=0)

lblPants=Label(FrameABC3, text='Calças:', font=('arial',15,'bold'), bg='darkgrey', fg='Khaki',
               justify=LEFT).grid(row=2, column=0)

lblShirt=Label(FrameABC3, text='Camisas:', font=('arial',15,'bold'), bg='darkgrey', fg='Khaki',
               justify=LEFT).grid(row=3, column=0)

lblShoes=Label(FrameABC3, text='Calçados:', font=('arial',15,'bold'), bg='darkgrey', fg='Khaki',
               justify=LEFT).grid(row=4, column=0)

#CAIXA DE TEXTO MASCULINO

txtCoats=Entry(FrameABC3,textvariable=Jackets_Blazers, font=('arial', 15, 'bold'),
                    bd=2, bg='white', fg='black', justify=CENTER).grid(row=1, column=1, pady=1)

txtPants=Entry(FrameABC3,textvariable=Formal_trousers, font=('arial', 15, 'bold'),
                    bd=2, bg='white', fg='black', justify=CENTER).grid(row=2, column=1, pady=1)

txtShirt=Entry(FrameABC3,textvariable=Formal_Shirts, font=('arial', 15, 'bold'),
                    bd=2, bg='white', fg='black', justify=CENTER).grid(row=3, column=1, pady=1)

txtShoes=Entry(FrameABC3,textvariable=Mens_Boots, font=('arial', 15, 'bold'),
                    bd=2, bg='white', fg='black', justify=CENTER).grid(row=4, column=1, pady=1)

#LabelRoupas

lblRoupas=Label(FrameABC3, text='Cama', font=('arial',20,'bold'), padx=8, bd=14, bg='grey', fg='Khaki', width=25,
               justify=CENTER).grid(row=5, column=0, columnspan=4)

lblBed_Sheet=Label(FrameABC3, text='Lençois:', font=('arial',15,'bold'), bg='darkgrey', fg='Khaki',
               justify=LEFT).grid(row=6, column=0)

lblPillows=Label(FrameABC3, text='Travesseiros:', font=('arial',15,'bold'),bg='darkgrey', fg='Khaki',
               justify=LEFT).grid(row=7, column=0)

lblPatterned_Bedding=Label(FrameABC3, text='Roupa de cama:', font=('arial',15,'bold'), bg='darkgrey', fg='Khaki',
               justify=LEFT).grid(row=8, column=0)

lblMattress_Protectors=Label(FrameABC3, text='Colchão:', font=('arial',15,'bold'), bg='darkgrey', fg='Khaki',
               justify=LEFT).grid(row=9, column=0)

#CAIXA DE TEXTO ROUPAS

txtBed_Sheet=Entry(FrameABC3,textvariable=Bed_Sheet, font=('arial', 15, 'bold'),
                    bd=2, bg='white', fg='black', justify=CENTER).grid(row=6, column=1, pady=1)

txtPillows=Entry(FrameABC3,textvariable=Pillows, font=('arial', 15, 'bold'),
                    bd=2, bg='white', fg='black', justify=CENTER).grid(row=7, column=1, pady=1)

txtPatterned_Bedding=Entry(FrameABC3,textvariable=Patterned_Bedding, font=('arial', 15, 'bold'),
                    bd=2, bg='white', fg='black', justify=CENTER).grid(row=8, column=1, pady=1)

txtMattress_Protectors=Entry(FrameABC3,textvariable=Mattress_Protectors, font=('arial', 15, 'bold'),
                    bd=2, bg='white', fg='black', justify=CENTER).grid(row=9, column=1, pady=1)

#Recibo

txtReceipt = Text(FrameABC5, height=19, width=33, bd=12, font=('arial', 9, 'bold'))
txtReceipt.grid(row=0, column=0)

#Botões

btnTotal = Button(FrameABC6, padx=1, pady=1, bd=4, fg='black',command=Total, font=('arial', 16, 'bold'),
                  width=5, bg='gold', text='Total').grid(row=0, column=0)

btnLimpar = Button(FrameABC6, padx=1, pady=1, bd=4, fg='black',command=Reset, font=('arial', 16, 'bold'),
                  width=5, bg='khaki', text='Limpar').grid(row=0, column=1)

btnSair = Button(FrameABC6, padx=1, pady=1, bd=4, fg='black',command=Exit, font=('arial', 16, 'bold'),
                  width=5, bg='red', text='Sair').grid(row=0, column=2)



root.mainloop()
















