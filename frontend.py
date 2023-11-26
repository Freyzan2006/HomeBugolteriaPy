from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from backand import db, All_info, add_item
from backand import connection

db()

def add_transaction():
    if type_combobox.get() and amount_entry.get():
        try:
            transaction_type = type_combobox.get()
            amount = float(amount_entry.get())
            comment = comment_entry.get()


            add_item(transaction_type, amount, comment)

            type_combobox.set('')
            amount_entry.delete(0, END)
            comment_entry.delete(0, END)
            messagebox.showinfo("Успех", "Транзакция успешно добавлена !")

        except ValueError:
            messagebox.showerror('Ошибка', "Сумма введина некорректно !")
    else:
        messagebox.showinfo("Предпреждение", "Заполнены не все поля !")

def view_data():
    view_win = Toplevel(app)
    view_win.title("Просмотор транзакций")

    treeview = ttk.Treeview(view_win)
    treeview.pack()

    treeview["columns"] = ("type", "amount", "comment")
    treeview.column("#0", width = 0, stretch = NO)
    treeview.column("type", anchor = W, width = 100)
    treeview.column("amount", anchor = W, width = 100)
    treeview.column("comment", anchor = W, width = 200)

    treeview.heading("#0", text = "")
    treeview.heading("type", text = "Тип")
    treeview.heading("amount", text = "Cумма")
    treeview.heading("comment", text = "Комментарий")

    rows = All_info()

    for row in rows:
        treeview.insert("", END, text = "", values = row[1:])

app = Tk()
app.title("Домашняя бугалерия")
app.geometry("300x280")
app.resizable(False, False)

type_label = Label(app, text = "Тип:")
type_label.pack(pady = 10)
type_combobox = ttk.Combobox(app, values = ["Доход", "Расход"])
type_combobox.pack()

amount_label = Label(app, text = "Сумма:")
amount_label.pack(pady = 10)
amount_entry = Entry(app)
amount_entry.pack()

comment_label = Label(app, text = "Комментарий:")
comment_label.pack(pady = 10)
comment_entry = Entry(app)
comment_entry.pack()

add_button = Button(app, text = "Добавить транзакцию", command = add_transaction)
add_button.pack(pady = 10)

view_button = Button(app, text = "Просмотреть транзакции", command = view_data)
view_button.pack()

