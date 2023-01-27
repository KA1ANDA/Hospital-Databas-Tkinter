from tkinter import *
import sqlite3


#Funqciebi


#ganyofilebebshi gadanawilebis funqcia

def nervologia():
    for widgets in frame_name.winfo_children():
        widgets.destroy()

    for widgets in frame_email.winfo_children():
        widgets.destroy()

    for widgets in frame_tel.winfo_children():
        widgets.destroy()

    for widgets in frame_surati.winfo_children():
        widgets.destroy()

    for widgets in frame_gany.winfo_children():
        widgets.destroy()

    canvas_main_page.forget()

    eqimebi_satauri = Label(frame_main, text="სპეციალისტები", bg="white", font=("SYLFAEN", 20, "bold"))
    eqimebi_satauri.place(x=1050, y=10)
    for i in nervologia_array:
         Label(frame_name,text=f"{i[0]}",bg="#69C1E6",width=42,font=("SYLFAEN",10,"italic")).pack(padx=10,side=LEFT)
         Label(frame_email, text=f"Email: {i[2]}", bg="#69C1E6", width=42,font=("SYLFAEN",10,"italic")).pack(padx=10, side=LEFT)
         Label(frame_tel, text=f"Tel: {i[1]}", bg="#69C1E6", width=42,font=("SYLFAEN",10,"italic")).pack(padx=10, side=LEFT)
         Label(frame_gany, text=f"Departament: {i[4]}", bg="#69C1E6", width=42, font=("SYLFAEN", 10, "italic")).pack(padx=10,side=LEFT)
         for j in nev_img_array:
              canvas = Canvas(frame_surati, width=300, height=430, bg="#FFD889",relief=SOLID,bd=1)
              canvas.create_image(140, 230, image=j)
              canvas.pack(padx=10, side=LEFT, anchor=N)



def travmatologia():
   for widgets in frame_name.winfo_children():
        widgets.destroy()

   for widgets in frame_surati.winfo_children():
        widgets.destroy()

   for widgets in frame_email.winfo_children():
            widgets.destroy()

   for widgets in frame_tel.winfo_children():
            widgets.destroy()

   for widgets in frame_gany.winfo_children():
        widgets.destroy()

   canvas_main_page.forget()

   eqimebi_satauri = Label(frame_main, text="სპეციალისტები", bg="white", font=("SYLFAEN", 20, "bold"))
   eqimebi_satauri.place(x=1050, y=10)
   for i in travmatologia_array:
        Label(frame_name, text=f"{i[0]}",bg="#69C1E6", width=42).pack(padx=10, side=LEFT)
        Label(frame_email, text=f"Email:{i[2]}", bg="#69C1E6", width=42, font=("SYLFAEN", 10, "italic")).pack(padx=10, side=LEFT)
        Label(frame_tel, text=f"Tel:{i[1]}", bg="#69C1E6", width=42, font=("SYLFAEN", 10, "italic")).pack(padx=10, side=LEFT)
        Label(frame_gany, text=f"Departament: {i[4]}", bg="#69C1E6", width=42,font=("SYLFAEN", 10, "italic")).pack(padx=10, side=LEFT)
        for j in tra_img_array:
            canvas = Canvas(frame_surati, width=300, height=430, bg="#FFD889",relief=SOLID,bd=1)
            canvas.create_image(140, 230, image=j)
            canvas.pack(padx=10, side=LEFT, anchor=N)





def kardioqirurgia():
    for widgets in frame_name.winfo_children():
        widgets.destroy()

    for widgets in frame_surati.winfo_children():
        widgets.destroy()

    for widgets in frame_email.winfo_children():
        widgets.destroy()

    for widgets in frame_tel.winfo_children():
        widgets.destroy()

    for widgets in frame_gany.winfo_children():
        widgets.destroy()

    canvas_main_page.forget()

    eqimebi_satauri = Label(frame_main, text="სპეციალისტები", bg="white", font=("SYLFAEN", 20, "bold"))
    eqimebi_satauri.place(x=1050, y=10)

    for i in kardioqirurgia_array:
         Label(frame_name, text=f"{i[0]}", bg="#69C1E6", width=42).pack(padx=10, side=LEFT)
         Label(frame_email, text=f"Email:{i[2]}", bg="#69C1E6", width=42, font=("SYLFAEN", 10, "italic")).pack(padx=10,side=LEFT)
         Label(frame_tel, text=f"Tel:{i[1]}", bg="#69C1E6", width=42, font=("SYLFAEN", 10, "italic")).pack(padx=10,side=LEFT)
         Label(frame_gany, text=f"Departament: {i[4]}", bg="#69C1E6", width=42,font=("SYLFAEN", 10, "italic")).pack(padx=10, side=LEFT)
         for j in kar_img_array:
              canvas = Canvas(frame_surati, width=300, height=430, bg="#FFD889",relief=SOLID,bd=1)
              canvas.create_image(140, 230, image=j)
              canvas.pack(padx=10, side=LEFT, anchor=N)





def qirurgia():
    for widgets in frame_name.winfo_children():
        widgets.destroy()

    for widgets in frame_surati.winfo_children():
        widgets.destroy()

    for widgets in frame_email.winfo_children():
        widgets.destroy()

    for widgets in frame_tel.winfo_children():
        widgets.destroy()

    for widgets in frame_gany.winfo_children():
        widgets.destroy()

    canvas_main_page.forget()

    eqimebi_satauri = Label(frame_main, text="სპეციალისტები", bg="white", font=("SYLFAEN", 20, "bold"))
    eqimebi_satauri.place(x=1050, y=10)

    for i in qirurgia_array:
         Label(frame_name, text=f"{i[0]}", bg="#69C1E6", width=42).pack(padx=10, side=LEFT)
         Label(frame_email, text=f"Email:{i[2]}", bg="#69C1E6", width=42, font=("SYLFAEN", 10, "italic")).pack(padx=10,  side=LEFT)
         Label(frame_tel, text=f"Tel:{i[1]}",bg="#69C1E6", width=42, font=("SYLFAEN", 10, "italic")).pack(padx=10,side=LEFT)
         Label(frame_gany, text=f"Departament: {i[4]}", bg="#69C1E6", width=42,font=("SYLFAEN", 10, "italic")).pack(padx=10, side=LEFT)
         for j in qir_img_array:
              canvas = Canvas(frame_surati, width=300, height=430, bg="#FFD889",relief=SOLID,bd=1)
              canvas.create_image(140, 230, image=j)
              canvas.pack(padx=10, side=LEFT, anchor=N)




def pedeatria():
    for widgets in frame_name.winfo_children():
        widgets.destroy()

    for widgets in frame_surati.winfo_children():
        widgets.destroy()

    for widgets in frame_email.winfo_children():
        widgets.destroy()

    for widgets in frame_tel.winfo_children():
        widgets.destroy()

    for widgets in frame_gany.winfo_children():
        widgets.destroy()

    canvas_main_page.forget()

    eqimebi_satauri = Label(frame_main, text="სპეციალისტები", bg="white", font=("SYLFAEN", 20, "bold"))
    eqimebi_satauri.place(x=1050, y=10)

    for i in pedeatria_array:
         Label(frame_name, text=f"{i[0]}", bg="#69C1E6", width=42).pack(padx=10, side=LEFT)
         Label(frame_email, text=f"Email:{i[2]}", bg="#69C1E6", width=42, font=("SYLFAEN", 10, "italic")).pack(padx=10,side=LEFT)
         Label(frame_tel, text=f"Tel:{i[1]}", bg="#69C1E6", width=42, font=("SYLFAEN", 10, "italic")).pack(padx=10, side=LEFT)
         Label(frame_gany, text=f"Departament: {i[4]}", bg="#69C1E6", width=42,font=("SYLFAEN", 10, "italic")).pack(padx=10, side=LEFT)
         for j in ped_img_array:
              canvas = Canvas(frame_surati, width=300, height=430, bg="#FFD889",relief=SOLID,bd=1)
              canvas.create_image(140, 230, image=j)
              canvas.pack(padx=10, side=LEFT, anchor=N)



def nefrologia():
    for widgets in frame_name.winfo_children():
        widgets.destroy()

    for widgets in frame_surati.winfo_children():
        widgets.destroy()

    for widgets in frame_email.winfo_children():
        widgets.destroy()

    for widgets in frame_tel.winfo_children():
        widgets.destroy()

    for widgets in frame_gany.winfo_children():
        widgets.destroy()

    canvas_main_page.forget()

    eqimebi_satauri = Label(frame_main, text="სპეციალისტები", bg="white", font=("SYLFAEN", 20, "bold"))
    eqimebi_satauri.place(x=1050, y=10)

    for i in nefrologia_array:
         Label(frame_name, text=f"{i[0]}", bg="#69C1E6", width=42).pack(padx=10, side=LEFT)
         Label(frame_email, text=f"Email:{i[2]}",bg="#69C1E6", width=42, font=("SYLFAEN", 10, "italic")).pack(padx=10,side=LEFT)
         Label(frame_tel, text=f"Tel:{i[1]}", bg="#69C1E6", width=42, font=("SYLFAEN", 10, "italic")).pack(padx=10, side=LEFT)
         Label(frame_gany, text=f"Departament: {i[4]}", bg="#69C1E6", width=42,font=("SYLFAEN", 10, "italic")).pack(padx=10, side=LEFT)
         for j in nef_img_array:
              canvas = Canvas(frame_surati, width=300, height=430, bg="#FFD889",relief=SOLID,bd=1)
              canvas.create_image(140, 230, image=j)
              canvas.pack(padx=10, side=LEFT, anchor=N)

def onkologia():
    for widgets in frame_name.winfo_children():
        widgets.destroy()

    for widgets in frame_surati.winfo_children():
        widgets.destroy()

    for widgets in frame_email.winfo_children():
        widgets.destroy()

    for widgets in frame_tel.winfo_children():
        widgets.destroy()

    for widgets in frame_gany.winfo_children():
        widgets.destroy()

    canvas_main_page.forget()

    eqimebi_satauri = Label(frame_main, text="სპეციალისტები", bg="white", font=("SYLFAEN", 20, "bold"))
    eqimebi_satauri.place(x=1050, y=10)

    for i in onkologia_array:
         Label(frame_name, text=f"{i[0]}", bg="#69C1E6", width=42).pack(padx=10, side=LEFT)
         Label(frame_email, text=f"Email:{i[2]}", bg="#69C1E6", width=42, font=("SYLFAEN", 10, "italic")).pack(padx=10,side=LEFT)
         Label(frame_tel, text=f"Tel:{i[1]}", bg="#69C1E6", width=42, font=("SYLFAEN", 10, "italic")).pack(padx=10,side=LEFT)
         Label(frame_gany, text=f"Departament: {i[4]}", bg="#69C1E6", width=42,font=("SYLFAEN", 10, "italic")).pack(padx=10, side=LEFT)
         for j in onk_img_array:
              canvas = Canvas(frame_surati, width=300, height=430, bg="#FFD889",relief=SOLID,bd=1)
              canvas.create_image(140, 230, image=j)
              canvas.pack(padx=10, side=LEFT, anchor=N)






win = Tk()
win.geometry("1920x1080")
win.config(bg="#EFF1F2")
win.title("განყოფილებები და სპეციალისტები")
icon=PhotoImage(file="imgs/icon.png")
win.iconphoto(False,icon)

######################################################################################################################################################################################################################

#suratebi
nev_img_1 = PhotoImage(file="imgs/dato.png")
nev_img_2 = PhotoImage(file="imgs/mari.png")
nev_img_3 = PhotoImage(file="imgs/nikoloz.png")
nev_img_4 = PhotoImage(file="imgs/qeti.png")
nev_img_array = [nev_img_1,nev_img_2,nev_img_3,nev_img_4]

tra_img_1 = PhotoImage(file="imgs/qetevan.png")
tra_img_2 = PhotoImage(file="imgs/mamuka.png")
tra_img_3 = PhotoImage(file="imgs/tamta.png")
tra_img_4 = PhotoImage(file="imgs/beso.png")
tra_img_array = [tra_img_1,tra_img_2,tra_img_3,tra_img_4]

kar_img_1 = PhotoImage(file="imgs/nino.png")
kar_img_2 = PhotoImage(file="imgs/ana.png")
kar_img_3 = PhotoImage(file="imgs/nana.png")
kar_img_4 = PhotoImage(file="imgs/levani.png")
kar_img_array = [kar_img_1,kar_img_2,kar_img_3,kar_img_4]


qir_img_1 = PhotoImage(file="imgs/natia.png")
qir_img_2 = PhotoImage(file="imgs/nino.png")
qir_img_3 = PhotoImage(file="imgs/zurab.png")
qir_img_4 = PhotoImage(file="imgs/ana.png")
qir_img_array = [qir_img_1,qir_img_2,qir_img_3,qir_img_4]


ped_img_1 = PhotoImage(file="imgs/zurab.png")
ped_img_2 = PhotoImage(file="imgs/mamuka.png")
ped_img_3 = PhotoImage(file="imgs/natia.png")
ped_img_4 = PhotoImage(file="imgs/beso.png")
ped_img_array = [ped_img_1,ped_img_2,ped_img_3,ped_img_4]


nef_img_1 = PhotoImage(file="imgs/ana.png")
nef_img_2 = PhotoImage(file="imgs/zurab.png")
nef_img_3 = PhotoImage(file="imgs/nino.png")
nef_img_4 = PhotoImage(file="imgs/nana.png")
nef_img_array = [nef_img_1,nef_img_2,nef_img_3,nef_img_4]

onk_img_1 = PhotoImage(file="imgs/mamuka.png")
onk_img_2 = PhotoImage(file="imgs/levani.png")
onk_img_3 = PhotoImage(file="imgs/ana.png")
onk_img_4 = PhotoImage(file="imgs/natia.png")
onk_img_array = [onk_img_1,onk_img_2,onk_img_3,onk_img_4]

#monacemta baza

db = sqlite3.connect('hosbitalData.db')

c = db.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS nervologia(
   name TEXT,
   tel INTEGER,
   email TEXT,
   img BLOB,
   engname TEXT,
   departament TEXT
)""")

# c.execute("INSERT INTO onkologia VALUES ('მაია ბოლქვაძე',599-20-11-65,'maia@gmail.com',NULL,'maia bolqvadze','ონკოლოგია')")




c.execute("SELECT name,tel,email,engname,departament FROM nervologia ")
nervologia_array = c.fetchall()
c.execute("SELECT name,tel,email,engname,departament FROM travmatologia ")
travmatologia_array = c.fetchall()
c.execute("SELECT name,tel,email,engname,departament FROM kardioqirurgia ")
kardioqirurgia_array = c.fetchall()
c.execute("SELECT name,tel,email,engname,departament FROM qirurgia ")
qirurgia_array = c.fetchall()
c.execute("SELECT name,tel,email,engname,departament FROM pedeatria ")
pedeatria_array = c.fetchall()
c.execute("SELECT name,tel,email,engname,departament FROM nefrologia ")
nefrologia_array = c.fetchall()
c.execute("SELECT name,tel,email,engname,departament FROM onkologia ")
onkologia_array = c.fetchall()




db.commit()





######################################################################################################################################################################################################################




#Headeri
frame_header=Frame(win,bg="#69C1E6",width=4000,height=80)
frame_header.pack()

#Mtavari
frame_main=Frame(win,bg="white",width=2000,height=4000,bd=4,relief=RIDGE)
frame_main.pack(pady=50,padx=30)

gany_satauri = Label(frame_main,text="განყოფილებები:",bg="white",font=("SYLFAEN",20,"bold"))
gany_satauri.pack(anchor=NW,padx=40,pady=10)




#side bar GANYOFILEBA

frame_ganyofileba =Frame(frame_main,bg="white",width=300,height=4000)
frame_ganyofileba.pack(side=LEFT,padx=40)

gany1 = Button(frame_ganyofileba,text=" ნევროლოგია",width=15,bg="#81EE97",fg="white",font=("SYLFAEN",30,"bold"),command=nervologia)
gany1.pack(pady=15)
gany2 = Button(frame_ganyofileba,text="ტრავმატოლოგია ",width=15,bg="#81EE97",fg="white",font=("SYLFAEN",30,"bold"),command=travmatologia)
gany2.pack(pady=15)
gany3 = Button(frame_ganyofileba,text="კარდიოქირურგია ",width=15,bg="#81EE97",fg="white",font=("SYLFAEN",30,"bold"),command=kardioqirurgia)
gany3.pack(pady=15)
gany4 = Button(frame_ganyofileba,text="ქირურგია",bg="#81EE97",width=15,fg="white",font=("SYLFAEN",30,"bold"),command=qirurgia)
gany4.pack(pady=15)
gany5 = Button(frame_ganyofileba,text="პედეატრია",bg="#81EE97",width=15,fg="white",font=("SYLFAEN",30,"bold"),command=pedeatria)
gany5.pack(pady=15)
gany6 = Button(frame_ganyofileba,text="ნეფროლოგია",bg="#81EE97",width=15,fg="white",font=("SYLFAEN",30,"bold"),command=nefrologia)
gany6.pack(pady=15)
gany7 = Button(frame_ganyofileba,text="ონკოლოგია",bg="#81EE97",width=15,fg="white",font=("SYLFAEN",30,"bold"),command=onkologia)
gany7.pack(pady=15)



# Frame Eqimebi

frame_eqimebi = Frame(frame_main,bg="#EFF1F2",bd=2,relief=RIDGE,width=1300,height=650)
frame_eqimebi.pack(side=LEFT,padx=40)

#frame fiqsirdeba zomebi
frame_eqimebi.pack_propagate(False)

#mtavari bg
mainBg=PhotoImage(file="imgs/mainBG.png")
wamlebiBg = PhotoImage(file="imgs/wamlebi.png")

canvas_main_page = Canvas(frame_eqimebi, width=1300, height=650, bg="#A2E2E9")
canvas_main_page.create_image(500, 320, image=mainBg)
canvas_main_page.create_image(980, 500, image=wamlebiBg)
canvas_main_page.create_text(900,280,text="Making a Difference\nTogether",fill="black",font=("ARIAL", 52, "bold"))
canvas_main_page.create_text(690,420,text="Feel Better",fill="green",font=("SYLFAEN", 35, "italic"))
canvas_main_page.pack()


#eqimebis info framebi
frame_surati =Frame(frame_eqimebi)
frame_surati.pack(side=TOP,pady=(30,40))

frame_gany = Frame(frame_eqimebi)
frame_gany.pack(side=BOTTOM,pady=(0,30))

frame_tel = Frame(frame_eqimebi)
frame_tel.pack(side=BOTTOM)

frame_email = Frame(frame_eqimebi)
frame_email.pack(side=BOTTOM)

frame_name = Frame(frame_eqimebi)
frame_name.pack(side=BOTTOM)







win.mainloop()