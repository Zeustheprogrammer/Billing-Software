from tkinter import *
from tkinter import filedialog,messagebox
import random
from datetime import datetime,timedelta
import sqlite3
import pyttsx3


root = Tk()        
root.geometry('1270x690+0+0')
root.title('Billing Software Using Python')
root.config(bg='firebrick4')
        
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)             

topFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Billing Software Using Python',font=('times new roman',30,'bold'),fg='yellow',bd=9,bg='red4',width=51)
labelTitle.grid(row=0,column=0)

#frames

itemFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
itemFrame.pack(side=LEFT)

costFrame=Frame(itemFrame,bd=4,relief=RIDGE,bg='firebrick4',pady=10)
costFrame.pack(side=BOTTOM)

phnFrame=Frame(itemFrame,bd=4,relief=RIDGE,bg='firebrick4',pady=10)
phnFrame.pack(side=BOTTOM)

cosmeticsFrame=LabelFrame(itemFrame,text='Cosmetics',font=('times new roman',19,'bold'),bd=10,relief=RIDGE,fg='red4',)
cosmeticsFrame.pack(side=LEFT)

groceryFrame=LabelFrame(itemFrame,text='Grocery',font=('times new roman',19,'bold'),bd=10,relief=RIDGE,fg='red4')
groceryFrame.pack(side=LEFT)

colddrinksFrame=LabelFrame(itemFrame,text='Cold Drinks',font=('times new roman',19,'bold'),bd=10,relief=RIDGE,fg='red4')
colddrinksFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='red4')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
buttonFrame.pack()

#Variables

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()

e_bathsoap = StringVar()
e_facecream = StringVar()
e_facewash = StringVar()
e_hairspray = StringVar()
e_hairgell = StringVar()
e_bodyloshan = StringVar()

e_rice = StringVar()
e_foodoil = StringVar()
e_daal = StringVar()
e_wheat = StringVar()
e_sugar = StringVar()
e_tea = StringVar()

e_maza=StringVar()
e_cococola = StringVar()
e_frooti = StringVar()
e_thumbsup = StringVar()
e_limbca = StringVar()
e_sprite = StringVar()
 
costofcosmeticsvar=StringVar()
costofgroceryvar=StringVar()
costofcolddrinksvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()
phnno=StringVar()

e_bathsoap.set('0')
e_facecream.set('0')
e_facewash.set('0')
e_hairspray.set('0')
e_hairgell.set('0')
e_bodyloshan.set('0')

e_rice.set('0')
e_foodoil.set('0')
e_daal.set('0')
e_wheat.set('0')
e_sugar.set('0')
e_tea.set('0')

e_maza.set('0')
e_cococola.set('0')
e_frooti.set('0')
e_thumbsup.set('0')
e_limbca.set('0')
e_sprite.set('0')

pricelist=list()

conn = sqlite3.connect("C:\\Users\\abboj\\OneDrive\\Desktop\\data.sqlite3")
c = conn.cursor()
c.execute("SELECT PRICE FROM StockDetails;")
tmplist = c.fetchall()
conn.commit()
conn.close()
for i in tmplist:
    pricelist.append(i[0])


#Functions

def reset():
    textReceipt.delete(1.0,END)
    e_bathsoap.set('0')
    e_facecream.set('0')
    e_facewash.set('0')
    e_hairspray.set('0')
    e_hairgell.set('0')
    e_bodyloshan.set('0')

    e_rice.set('0')
    e_foodoil.set('0')
    e_daal.set('0')
    e_wheat.set('0')
    e_sugar.set('0')
    e_tea.set('0')

    e_maza.set('0')
    e_cococola.set('0')
    e_frooti.set('0')
    e_thumbsup.set('0')
    e_limbca.set('0')
    e_sprite.set('0')

    textbathsoap.config(state=DISABLED)
    textfacecream.config(state=DISABLED)
    textfacewash.config(state=DISABLED)
    texthairspray.config(state=DISABLED)
    texthairgell.config(state=DISABLED)
    textbodyloshan.config(state=DISABLED)

    textrice.config(state=DISABLED)
    textfoodoil.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textwheat.config(state=DISABLED)
    textsugar.config(state=DISABLED)
    texttea.config(state=DISABLED)

    textmaza.config(state=DISABLED)
    textcococola.config(state=DISABLED)
    textfrooti.config(state=DISABLED)
    textthumbsup.config(state=DISABLED)
    textlimbca.config(state=DISABLED)
    textsprite.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)

    costofcosmeticsvar.set('')
    costofgroceryvar.set('')
    costofcolddrinksvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')
    phnno.set('')

def printf():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:
            bill_data=textReceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information','Your Bill Is Succesfully Printed')

        conn = sqlite3.connect("C:\\Users\\abboj\\OneDrive\\Desktop\\data.sqlite3")
        c = conn.cursor()
        c.execute("INSERT INTO data (billnumber,date,priceofCosmetics,priceofGrocery,priceofColddrinks,subtotalofItems,servicetaxvarofitems,Total,phnno) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                (billnumber,date,priceofCosmetics,priceofGrocery,priceofColddrinks,subtotalofItems,servicetaxvarofitems,subtotalofItems+servicetaxvarofitems,phnno.get()))            
        if e_bathsoap.get()!='0':
            sql = "UPDATE StockDetails SET stock = stock-? WHERE item = ?"
            val = (int(e_bathsoap.get()), "bathsoap")
            c.execute(sql, val)

        if e_facecream.get()!='0':
            sql = "UPDATE StockDetails SET stock = stock-? WHERE item = ?"
            val = (int(e_facecream.get()), "facecream")
            c.execute(sql, val)

        if e_facewash.get()!='0':
            sql = "UPDATE StockDetails SET stock = stock-? WHERE item = ?"
            val = (int(e_facewash.get()), "facewash")
            c.execute(sql, val)

        if e_hairspray.get() != '0':
            sql = "UPDATE StockDetails SET stock = stock-? WHERE item = ?"
            val = (int(e_hairspray.get()), "hairspray")
            c.execute(sql, val)
        if e_hairgell.get() != '0':
            sql = "UPDATE StockDetails SET stock = stock-? WHERE item = ?"
            val = (int(e_hairgell.get()), "hairgell")
            c.execute(sql, val)
            
        if e_bodyloshan.get() != '0':
            sql = "UPDATE StockDetails SET stock = stock-? WHERE item = ?"
            val = (int(e_bodyloshan.get()), "bodyloshan")
            c.execute(sql, val)

        if e_rice.get() != '0':
            sql = "UPDATE StockDetails SET stock = stock-? WHERE item = ?"
            val = (int(e_rice.get()), "rice")
            c.execute(sql, val)

        if e_foodoil.get() != '0':
            sql = "UPDATE StockDetails SET stock = stock-? WHERE item = ?"
            val = (int(e_foodoil.get()), "foodoil")
            c.execute(sql, val)

        if e_daal.get() != '0':
            sql = "UPDATE StockDetails SET stock = stock-? WHERE item = ?"
            val = (int(e_daal.get()), "daal")
            c.execute(sql, val)
            
        if e_wheat.get() != '0':
            sql = "UPDATE StockDetails SET stock = stock-? WHERE item = ?"
            val = (int(e_wheat.get()), "wheat")
            c.execute(sql, val)

        if e_sugar.get() != '0':
            sql = "UPDATE StockDetails SET stock = stock-? WHERE item = ?"
            val = (int(e_sugar.get()), "sugar")
            c.execute(sql, val)

        if e_tea.get() != '0':
            sql = "UPDATE StockDetails SET stock = stock-? WHERE item = ?"
            val = (int(e_tea.get()), "tea")
            c.execute(sql, val)

        if e_maza.get() != '0':
            sql = "UPDATE StockDetails SET stock = stock-? WHERE item = ?"
            val = (int(e_maza.get()), "maza")
            c.execute(sql, val)

        if e_cococola.get() != '0':
            sql = "UPDATE StockDetails SET stock = stock-? WHERE item = ?"
            val = (int(e_cococola.get()), "cococola")
            c.execute(sql, val)

        if e_frooti.get() != '0':
            sql = "UPDATE StockDetails SET stock = stock-? WHERE item = ?"
            val = (int(e_frooti.get()), "frooti")
            c.execute(sql, val)

        if e_thumbsup.get() != '0':
            sql = "UPDATE StockDetails SET stock = stock-? WHERE item = ?"
            val = (int(e_thumbsup.get()), "thumbsup")
            c.execute(sql, val)

        if e_limbca.get() != '0':
            sql = "UPDATE StockDetails SET stock = stock-? WHERE item = ?"
            val = (int(e_limbca.get()), "limbca")
            c.execute(sql, val)

        if e_sprite.get() != '0':
            sql = "UPDATE StockDetails SET stock = stock-? WHERE item = ?"
            val = (int(e_sprite.get()), "sprite")
            c.execute(sql, val)
        if  var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0:
            c.execute("Insert Into OrderDetailsOfCosmetics values (?,?,?,?,?,?,?,?)",(billnumber,date,int(e_bathsoap.get()),int(e_facecream.get()),int(e_facewash.get()),int(e_hairspray.get()),int(e_hairgell.get()),int(e_bodyloshan.get())))
        if var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0:
            c.execute("Insert Into OrderDetailsOfGrocery values (?,?,?,?,?,?,?,?)",(billnumber,date,int(e_rice.get()),int(e_foodoil.get()),int(e_daal.get()),int(e_wheat.get()),int(e_sugar.get()),int(e_tea.get())))
        if var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or var16.get() != 0 or var17.get() != 0 or var18.get() != 0 :
            c.execute("Insert Into OrderDetailsOfColdDrinks values (?,?,?,?,?,?,?,?)",(billnumber,date,int(e_maza.get()),int(e_cococola.get()),int(e_frooti.get()),int(e_thumbsup.get()),int(e_limbca.get()),int(e_sprite.get())))
        conn.commit()
        conn.close()
        reset()

def totalcost():
    global priceofCosmetics,priceofGrocery,priceofColddrinks,subtotalofItems,servicetaxvarofitems,billnumber,date
    if  var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
    var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
    var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
    var16.get() != 0 or var17.get() != 0 or var18.get() != 0 :
            
        item1 = int(e_bathsoap.get())*pricelist[0] if e_bathsoap.get() else 0
        item2 = int(e_facecream.get())*pricelist[1] if e_facecream.get() else 0
        item3 = int(e_facewash.get())*pricelist[2] if e_facewash.get() else 0
        item4 = int(e_hairspray.get())*pricelist[3] if e_hairspray.get() else 0
        item5 = int(e_hairgell.get())*pricelist[4] if e_hairgell.get() else 0
        item6 = int(e_bodyloshan.get())*pricelist[5] if e_bodyloshan.get() else 0
        item7 = int(e_rice.get())*pricelist[6] if e_rice.get() else 0
        item8 = int(e_foodoil.get())*pricelist[7] if e_foodoil.get() else 0
        item9 = int(e_daal.get())*pricelist[8] if e_daal.get() else 0
        item10 = int(e_wheat.get())*pricelist[9] if e_wheat.get() else 0
        item11 = int(e_sugar.get())*pricelist[10] if e_sugar.get() else 0
        item12 = int(e_tea.get())*pricelist[11] if e_tea.get() else 0
        item13 = int(e_maza.get())*pricelist[12]    if e_maza.get() else 0
        item14 = int(e_cococola.get())*pricelist[13] if e_cococola.get() else 0
        item15 = int(e_frooti.get())*pricelist[14] if e_frooti.get() else 0
        item16 = int(e_thumbsup.get())*pricelist[15] if e_thumbsup.get() else 0
        item17 = int(e_limbca.get())*pricelist[16] if e_limbca.get() else 0
        item18 = int(e_sprite.get())*pricelist[17] if e_sprite.get() else 0
        priceofCosmetics=item1+item2+item3+item4+item5+item6
        priceofGrocery=item7+item8+item9+item10+item11+item12 
        priceofColddrinks=item13+item14+item15+item16+item17+item18
                           
        costofcosmeticsvar.set(str(priceofCosmetics)+ ' Rs')
        costofgroceryvar.set(str(priceofGrocery)+ ' Rs')
        costofcolddrinksvar.set(str(priceofColddrinks)+ ' Rs')

        subtotalofItems=priceofCosmetics+priceofGrocery+priceofColddrinks
        subtotalvar.set(str(subtotalofItems)+' Rs')

        servicetaxvarofitems=subtotalofItems*0.05
        servicetaxvar.set(str(servicetaxvarofitems)+' Rs')

        tottalcost=subtotalofItems+servicetaxvarofitems
        totalcostvar.set(str(tottalcost)+' Rs')

        text = f"Total cost is {tottalcost} rupees"
        engine.say(text)
        engine.runAndWait()
        
        if costofcosmeticsvar.get() != '' or costofgroceryvar.get() != '' or costofcolddrinksvar != '':
            textReceipt.delete(1.0,END)
            x=random.randint(100,10000)
            billnumber='BILL'+str(x)
            now = datetime.now()
            date=now.strftime("%d/%m/%Y, %H:%M:%S")
            textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
            textReceipt.insert(END,'***************************************************************\n')
            textReceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
            textReceipt.insert(END,'***************************************************************\n')
            
            if e_bathsoap.get()!='0':
                textReceipt.insert(END,f'Bath Soap\t\t\t{item1}\n\n')

            if e_facecream.get()!='0':
                textReceipt.insert(END,f'Face Cream\t\t\t{item2}\n\n')

            if e_facewash.get()!='0':
                textReceipt.insert(END,f'Face Wash\t\t\t{item3}\n\n')

            if e_hairspray.get() != '0':
                textReceipt.insert(END, f'Hair Spray:\t\t\t{item4}\n\n')

            if e_hairgell.get() != '0':
                textReceipt.insert(END, f'Hair Gell:\t\t\t{item5}\n\n')
            
            if e_bodyloshan.get() != '0':
                textReceipt.insert(END, f'Body Loshan:\t\t\t{item6}\n\n')

            if e_rice.get() != '0':
                textReceipt.insert(END, f'Rice:\t\t\t{item7}\n\n')

            if e_foodoil.get() != '0':
                textReceipt.insert(END, f'Food Oil:\t\t\t{item8}\n\n')

            if e_daal.get() != '0':
                textReceipt.insert(END, f'Daal:\t\t\t{item9}\n\n')
            
            if e_wheat.get() != '0':
                textReceipt.insert(END, f'Wheat:\t\t\t{item10}\n\n')

            if e_sugar.get() != '0':
                textReceipt.insert(END, f'Sugar:\t\t\t{item11}\n\n')

            if e_tea.get() != '0':
                textReceipt.insert(END, f'Tea:\t\t\t{item12}\n\n')

            if e_maza.get() != '0':
                textReceipt.insert(END, f'Mazaa:\t\t\t{item13}\n\n')

            if e_cococola.get() != '0':
                textReceipt.insert(END, f'Coco Cola:\t\t\t{item14}\n\n')

            if e_frooti.get() != '0':
                textReceipt.insert(END, f'Frooti:\t\t\t{item15}\n\n')

            if e_thumbsup.get() != '0':
                textReceipt.insert(END, f'Thumbs Up:\t\t\t{item16}\n\n')

            if e_limbca.get() != '0':
                textReceipt.insert(END, f'Limbca:\t\t\t{item17}\n\n')

            if e_sprite.get() != '0':
                textReceipt.insert(END, f'Sprite:\t\t\t{item18}\n\n')

            textReceipt.insert(END,'***************************************************************\n')
            if costofcosmeticsvar.get()!='0 Rs':
                textReceipt.insert(END,f'Cost Of Cosmetics\t\t\t{priceofCosmetics}Rs\n\n')
            if costofgroceryvar.get() != '0 Rs':
                textReceipt.insert(END,f'Cost Of Grocery\t\t\t{priceofGrocery}Rs\n\n')
            if costofcolddrinksvar.get() != '0 Rs':
                textReceipt.insert(END,f'Cost Of Cold Drinks\t\t\t{priceofColddrinks}Rs\n\n')

            textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
            textReceipt.insert(END, f'Service Tax\t\t\t{servicetaxvarofitems}Rs\n\n')
            textReceipt.insert(END, f'Total Cost\t\t\t{tottalcost}Rs\n\n')
            textReceipt.insert(END,'***************************************************************\n')

    else:
        messagebox.showerror('Error','No Item Is selected')

def update():
    conn = sqlite3.connect("C:\\Users\\abboj\\OneDrive\\Desktop\\data.sqlite3")
    c = conn.cursor()
    if  var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
    var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
    var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
    var16.get() != 0 or var17.get() != 0 or var18.get() != 0 :
        
        sql = "UPDATE StockDetails SET stock = stock + ? WHERE item = ?"
        val = (int(e_bathsoap.get()),"bathsoap",)
        c.execute(sql, val)
        
        sql = "UPDATE StockDetails SET stock = stock + ? WHERE item = ?"
        val = (int(e_facecream.get()),"facecream",)
        c.execute(sql, val)
        
        sql = "UPDATE StockDetails SET stock = stock + ? WHERE item = ?"
        val = (int(e_facewash.get()),"facewash",)
        c.execute(sql, val)
        
        sql = "UPDATE StockDetails SET stock = stock + ? WHERE item = ?"
        val = (int(e_hairspray.get()),"hairspray",)
        c.execute(sql, val)

        sql = "UPDATE StockDetails SET stock = stock + ? WHERE item = ?"
        val = (int(e_hairgell.get()), "hairgell",)
        c.execute(sql, val)
        
        sql = "UPDATE StockDetails SET stock = stock + ? WHERE item = ?"
        val = (int(e_bodyloshan.get()),"bodyloshan",)
        c.execute(sql, val)
        
        sql = "UPDATE StockDetails SET stock = stock + ? WHERE item = ?"
        val = (int(e_rice.get()),"rice",)
        c.execute(sql, val)

        sql = "UPDATE StockDetails SET stock = stock + ? WHERE item = ?"
        val = (int(e_foodoil.get()),"foodoil",)
        c.execute(sql, val)
        
        sql = "UPDATE StockDetails SET stock = stock + ? WHERE item = ?"
        val = (int(e_daal.get()),"daal",)
        c.execute(sql, val)
        e_daal
        sql = "UPDATE StockDetails SET stock = stock + ? WHERE item = ?"
        val = (int(e_wheat.get()),"wheat",)
        c.execute(sql, val)
       
        sql = "UPDATE StockDetails SET stock = stock + ? WHERE item = ?"
        val = (int(e_sugar.get()),"sugar",)
        c.execute(sql, val)
        
        sql = "UPDATE StockDetails SET stock = stock + ? WHERE item = ?"
        val = (int(e_tea.get()),"tea",)
        c.execute(sql, val)
        
        sql = "UPDATE StockDetails SET stock = stock + ? WHERE item = ?"
        val = (int(e_maza.get()),"maza",)
        c.execute(sql, val)
        
        sql = "UPDATE StockDetails SET stock = stock + ? WHERE item = ?"
        val = (int(e_cococola.get()),"cococola",)
        c.execute(sql, val)

        sql = "UPDATE StockDetails SET stock =stock + ? WHERE item = ?"
        val = (int(e_frooti.get()), "frooti",)
        c.execute(sql, val)

        sql = "UPDATE StockDetails SET stock = stock + ? WHERE item = ?"
        val = (int(e_thumbsup.get()),"thumbsup",)
        c.execute(sql, val)

        sql = "UPDATE StockDetails SET stock = stock + ? WHERE item = ?"
        val = (int(e_limbca.get()), "limbca",)
        c.execute(sql, val)

        sql = "UPDATE StockDetails SET stock = stock + ? WHERE item = ?"
        val = (int(e_sprite.get()),"sprite",)
        c.execute(sql, val)
        conn.commit()
        conn.close()
        messagebox.showinfo('Information','Stock is updated successfully')
        reset()
    else:    
        c.execute("SELECT stock from StockDetails;")
        tmplist = c.fetchall()
        stocklist = list()
        for i in tmplist:
            stocklist.append(i[0])
        e_bathsoap.set(stocklist[0])
        e_facecream.set(stocklist[1])
        e_facewash.set(stocklist[2])
        e_hairspray.set(stocklist[3])
        e_hairgell.set(stocklist[4])
        e_bodyloshan.set(stocklist[5])
        e_rice.set(stocklist[6])
        e_foodoil.set(stocklist[7])
        e_daal.set(stocklist[8])
        e_wheat.set(stocklist[9])
        e_sugar.set(stocklist[10])
        e_tea.set(stocklist[11])
        e_maza.set(stocklist[12])
        e_cococola.set(stocklist[13])
        e_frooti.set(stocklist[14])
        e_thumbsup.set(stocklist[15])
        e_limbca.set(stocklist[16])
        e_sprite.set(stocklist[17])
        conn.close()

def count():
    conn = sqlite3.connect("C:\\Users\\abboj\\OneDrive\\Desktop\\data.sqlite3")
    c = conn.cursor()
    now = datetime.now()
    start_date = datetime(now.year, now.month, 1).strftime("%d/%m/%Y, %H:%M:%S")
    end_date = (datetime(now.year, now.month+1, 1) - timedelta(days=1)).strftime("%d/%m/%Y, %H:%M:%S")
    query = "SELECT sum(maza),sum(cococola),sum(frooti),sum(thumbsup),sum(limbca),sum(sprite) FROM OrderDetailsOfColdDrinks WHERE date BETWEEN ? AND ?"
    c.execute(query, (start_date, end_date))
    tmp = c.fetchall()
    e_maza.set(tmp[0][0])
    e_cococola.set(tmp[0][1])
    e_frooti.set(tmp[0][2])
    e_thumbsup.set(tmp[0][3])
    e_limbca.set(tmp[0][4])
    e_sprite.set(tmp[0][5])
    query = "SELECT sum(bathsoap),sum(facecream),sum(facewash),sum(hairspray),sum(hairgell),sum(bodyloshan) FROM OrderDetailsOfCosmetics WHERE date BETWEEN ? AND ?"
    c.execute(query, (start_date, end_date))
    tmp = c.fetchall()
    e_bathsoap.set(tmp[0][0])
    e_facecream.set(tmp[0][1])
    e_facewash.set(tmp[0][2])
    e_hairspray.set(tmp[0][3])
    e_hairgell.set(tmp[0][4])
    e_bodyloshan.set(tmp[0][5])
    query = "SELECT sum(rice),sum(foodoil),sum(daal),sum(wheat),sum(sugar),sum(tea) FROM OrderDetailsOfGrocery WHERE date BETWEEN ? AND ?"
    c.execute(query, (start_date, end_date))
    tmp = c.fetchall()
    e_rice.set(tmp[0][0])
    e_foodoil.set(tmp[0][1])
    e_daal.set(tmp[0][2])
    e_wheat.set(tmp[0][3])
    e_sugar.set(tmp[0][4])
    e_tea.set(tmp[0][5])

def bathsoap():
    if var1.get()==1:
        textbathsoap.config(state=NORMAL)
        textbathsoap.focus()
        textbathsoap.delete(0,END)
    else:
        textbathsoap.config(state=DISABLED)
        e_bathsoap.set('0')

def facecream():
    if var2.get()==1:
        textfacecream.config(state=NORMAL)
        textfacecream.focus()
        textfacecream.delete(0,END)
    else:
        textfacecream.config(state=DISABLED)
        e_facecream.set('0')

def facewash():
    if var3.get()==1:
        textfacewash.config(state=NORMAL)
        textfacewash.delete(0,END)
        textfacewash.focus()

    else:
        textfacewash.config(state=DISABLED)
        e_facewash.set('0')

def hairspray():
    if var4.get() == 1:
        texthairspray.config(state=NORMAL)
        texthairspray.focus()
        texthairspray.delete(0, END)
    else:
        texthairspray.config(state=DISABLED)
        e_hairspray.set('0')

def hairgell():
    if var5.get() == 1:
        texthairgell.config(state=NORMAL)
        texthairgell.focus()
        texthairgell.delete(0, END)
    else:
        texthairgell.config(state=DISABLED)
        e_hairgell.set('0')


def bodyloshan():
    if var6.get() == 1:
        textbodyloshan.config(state=NORMAL)
        textbodyloshan.focus()
        textbodyloshan.delete(0, END)
    else:
        textbodyloshan.config(state=DISABLED)
        e_bodyloshan.set('0')

def rice():
    if var7.get() == 1:
        textrice.config(state=NORMAL)
        textrice.focus()
        textrice.delete(0, END)
    else:
        textrice.config(state=DISABLED)
        e_rice.set('0')


def foodoil():
    if var8.get() == 1:
        textfoodoil.config(state=NORMAL)
        textfoodoil.focus()
        textfoodoil.delete(0, END)
    else:
        textfoodoil.config(state=DISABLED)
        e_foodoil.set('0')


def daal():
    if var9.get() == 1:
        textdaal.config(state=NORMAL)
        textdaal.focus()
        textdaal.delete(0, END)
    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')


def wheat():
    if var10.get() == 1:
        textwheat.config(state=NORMAL)
        textwheat.focus()
        textwheat.delete(0, END)
    else:
        textwheat.config(state=DISABLED)
        e_wheat.set('0')


def sugar():
    if var11.get() == 1:
        textsugar.config(state=NORMAL)
        textsugar.focus()
        textsugar.delete(0, END)
    else:
        textsugar.config(state=DISABLED)
        e_sugar.set('0')


def tea():
    if var12.get() == 1:
        texttea.config(state=NORMAL)
        texttea.focus()
        texttea.delete(0, END)
    else:
        texttea.config(state=DISABLED)
        e_tea.set('0')


def maza():
    if var13.get() == 1:
        textmaza.config(state=NORMAL)
        textmaza.focus()
        textmaza.delete(0, END)
    else:
        textmaza.config(state=DISABLED)
        e_maza.set('0')


def cococola():
    if var14.get() == 1:
        textcococola.config(state=NORMAL)
        textcococola.focus()
        textcococola.delete(0, END)
    else:
        textcococola.config(state=DISABLED)
        e_cococola.set('0')


def frooti():
    if var15.get() == 1:
        textfrooti.config(state=NORMAL)
        textfrooti.focus()
        textfrooti.delete(0, END)
    else:
        textfrooti.config(state=DISABLED)
        e_frooti.set('0')

def thumbsup():
    if var16.get() == 1:
        textthumbsup.config(state=NORMAL)
        textthumbsup.focus()
        textthumbsup.delete(0, END)
    else:
        textthumbsup.config(state=DISABLED)
        e_thumbsup.set('0')


def limbca():
    if var17.get() == 1:
        textlimbca.config(state=NORMAL)
        textlimbca.focus()
        textlimbca.delete(0, END)
    else:
        textlimbca.config(state=DISABLED)
        e_limbca.set('0')


def sprite():
    if var18.get() == 1:
        textsprite.config(state=NORMAL)
        textsprite.delete(0, END)
        textsprite.focus()
    else:
        textsprite.config(state=DISABLED)
        e_sprite.set('0')

 
#Cosmetics

bathsoap=Checkbutton(cosmeticsFrame,text='Bath Soap',font=('times new roman',18,'bold'),onvalue=1,offvalue=0,variable=var1,command=bathsoap)
bathsoap.grid(row=0,column=0,sticky=W)
 
facecream=Checkbutton(cosmeticsFrame,text='Face Cream',font=('times new roman',18,'bold'),onvalue=1,offvalue=0,variable=var2,command=facecream)
facecream.grid(row=1,column=0,sticky=W)

facewash=Checkbutton(cosmeticsFrame,text='Face Wash',font=('times new roman',18,'bold'),onvalue=1,offvalue=0,variable=var3,command=facewash)
facewash.grid(row=2,column=0,sticky=W)

hairspray=Checkbutton(cosmeticsFrame,text='Hair Spray',font=('times new roman',18,'bold'),onvalue=1,offvalue=0,variable=var4,command=hairspray)
hairspray.grid(row=3,column=0,sticky=W)

hairgell=Checkbutton(cosmeticsFrame,text='Hair Gell',font=('times new roman',18,'bold'),onvalue=1,offvalue=0,variable=var5,command=hairgell)
hairgell.grid(row=4,column=0,sticky=W)

bodyloshan=Checkbutton(cosmeticsFrame,text='Body Loshan',font=('times new roman',18,'bold'),onvalue=1,offvalue=0,variable=var6,command=bodyloshan)
bodyloshan.grid(row=5,column=0,sticky=W)

#Entry Fields for Cosmetics

textbathsoap=Entry(cosmeticsFrame,font=('times new roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_bathsoap)
textbathsoap.grid(row=0,column=1)

textfacecream=Entry(cosmeticsFrame,font=('times new roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_facecream)
textfacecream.grid(row=1,column=1)

textfacewash=Entry(cosmeticsFrame,font=('times new roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_facewash)
textfacewash.grid(row=2,column=1)

texthairspray = Entry(cosmeticsFrame, font=('times new roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_hairspray)
texthairspray.grid(row=3, column=1)

texthairgell = Entry(cosmeticsFrame, font=('times new roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_hairgell)
texthairgell.grid(row=4, column=1)

textbodyloshan = Entry(cosmeticsFrame, font=('times new roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_bodyloshan)
textbodyloshan.grid(row=5, column=1)

#Grocery

rice=Checkbutton(groceryFrame,text='Rice',font=('times new roman',18,'bold'),onvalue=1,offvalue=0,variable=var7,command=rice)
rice.grid(row=0,column=0,sticky=W)

foodoil=Checkbutton(groceryFrame,text='Food Oil',font=('times new roman',18,'bold'),onvalue=1,offvalue=0,variable=var8,command=foodoil)
foodoil.grid(row=1,column=0,sticky=W)

daal=Checkbutton(groceryFrame,text='Daal',font=('times new roman',18,'bold'),onvalue=1,offvalue=0,variable=var9,command=daal)
daal.grid(row=2,column=0,sticky=W)

wheat=Checkbutton(groceryFrame,text='Wheat',font=('times new roman',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=wheat)
wheat.grid(row=3,column=0,sticky=W)

sugar=Checkbutton(groceryFrame,text='Sugar',font=('times new roman',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=sugar)
sugar.grid(row=4,column=0,sticky=W)

tea=Checkbutton(groceryFrame,text='Tea',font=('times new roman',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=tea)
tea.grid(row=5,column=0,sticky=W)

#entry fields for Grocery

textrice = Entry(groceryFrame, font=('times new roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_rice)
textrice.grid(row=0, column=1)

textfoodoil = Entry(groceryFrame, font=('times new roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_foodoil)
textfoodoil.grid(row=1, column=1)

textdaal = Entry(groceryFrame, font=('times new roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_daal)
textdaal.grid(row=2, column=1)

textwheat = Entry(groceryFrame, font=('times new roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_wheat)
textwheat.grid(row=3, column=1)
              
textsugar = Entry(groceryFrame, font=('times new roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_sugar)
textsugar.grid(row=4, column=1)

texttea = Entry(groceryFrame, font=('times new roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_tea)
texttea.grid(row=5, column=1)

#Cold Drinks

maza=Checkbutton(colddrinksFrame,text='Mazaa',font=('times new roman',18,'bold'),onvalue=1,offvalue=0,variable=var13,command=maza)
maza.grid(row=0,column=0,sticky=W)

cococola=Checkbutton(colddrinksFrame,text='Coco Cola',font=('times new roman',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=cococola)
cococola.grid(row=1,column=0,sticky=W)

frooti=Checkbutton(colddrinksFrame,text='Frooti',font=('times new roman',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=frooti)
frooti.grid(row=2,column=0,sticky=W)

thumbsup=Checkbutton(colddrinksFrame,text='Thumbs Up',font=('times new roman',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=thumbsup)
thumbsup.grid(row=3,column=0,sticky=W)

limbca=Checkbutton(colddrinksFrame,text='Limbca',font=('times new roman',18,'bold'),onvalue=1,offvalue=0,variable=var17,command=limbca)
limbca.grid(row=4,column=0,sticky=W)

sprite=Checkbutton(colddrinksFrame,text='Sprite',font=('times new roman',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=sprite)
sprite.grid(row=5,column=0,sticky=W)
       
#entry fields for Cold drinks

textmaza = Entry(colddrinksFrame, font=('times new roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_maza)
textmaza.grid(row=0, column=1)

textcococola = Entry(colddrinksFrame, font=('times new roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_cococola)
textcococola.grid(row=1, column=1)

textfrooti = Entry(colddrinksFrame, font=('times new roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_frooti)
textfrooti.grid(row=2, column=1)

textthumbsup = Entry(colddrinksFrame, font=('times new roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_thumbsup)
textthumbsup.grid(row=3, column=1)

textlimbca = Entry(colddrinksFrame, font=('times new roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_limbca)
textlimbca.grid(row=4, column=1)

textsprite = Entry(colddrinksFrame, font=('times new roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_sprite)
textsprite.grid(row=5, column=1)

#costlabels & entry fields

labelCostofCosmetics=Label(costFrame,text='Cost of Cosmetics',font=('times new roman',16,'bold'),bg='firebrick4',fg='white')
labelCostofCosmetics.grid(row=0,column=0)

textCostofCosmetics=Entry(costFrame,font=('times new roman',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcosmeticsvar)
textCostofCosmetics.grid(row=0,column=1,padx=41)

labelCostofGrocery=Label(costFrame,text='Cost of Grocery',font=('times new roman',16,'bold'),bg='firebrick4',fg='white')
labelCostofGrocery.grid(row=1,column=0)

textCostofGrocery=Entry(costFrame,font=('times new roman',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofgroceryvar)
textCostofGrocery.grid(row=1,column=1,padx=41)

labelCostofColdDrinks=Label(costFrame,text='Cost of Cold Drinks',font=('times new roman',16,'bold'),bg='firebrick4',fg='white')
labelCostofColdDrinks.grid(row=2,column=0)

textCostofColdDrinks=Entry(costFrame,font=('times new roman',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcolddrinksvar)
textCostofColdDrinks.grid(row=2,column=1,padx=41)

labelSubTotal=Label(costFrame,text='Sub Total',font=('times new roman',16,'bold'),bg='firebrick4',fg='white')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(costFrame,font=('times new roman',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

labelServiceTax=Label(costFrame,text='Service Tax',font=('times new roman',16,'bold'),bg='firebrick4',fg='white')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(costFrame,font=('times new roman',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=41)

labelTotalCost=Label(costFrame,text='Total Cost',font=('times new roman',16,'bold'),bg='firebrick4',fg='white')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('times new roman',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=41)

labelphnno=Label(phnFrame,text='Enter the mobile number',font=('times new roman',16,'bold'),bg='firebrick4',fg='white')
labelphnno.grid(row=0,column=0)

textphnno=Entry(phnFrame,font=('times new roman',16,'bold'),bd=6,width=14,textvariable=phnno)
textphnno.grid(row=0,column=1,padx=41)

#Buttons

buttonTotal=Button(buttonFrame,text='Total',font=('times new roman',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Print',font=('times new roman',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=printf)
buttonReceipt.grid(row=0,column=1)

buttonReceipt=Button(buttonFrame,text='Update',font=('times new roman',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=update)
buttonReceipt.grid(row=0,column=2)

buttonReset=Button(buttonFrame,text='Count',font=('times new roman',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=count)
buttonReset.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('times new roman',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=reset)
buttonReset.grid(row=0,column=4)

#textarea for receipt

textReceipt=Text(recieptFrame,font=('times new roman',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

#Calculator

operator='' #7+9
def buttonClick(numbers): #9
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''



calculatorField=Entry(calculatorFrame,font=('times new roman',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('times new roman',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                    command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('times new roman',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                    command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('times new roman',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                    ,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('times new roman',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                        ,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('times new roman',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                    ,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('times new roman',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                    ,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('times new roman',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                    ,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('times new roman',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                        ,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('times new roman',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                    ,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('times new roman',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                    ,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('times new roman',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                    ,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('times new roman',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                        ,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font=('times new roman',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                        command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('times new roman',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                        ,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('times new roman',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                    ,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('times new roman',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                        command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)


root.mainloop()