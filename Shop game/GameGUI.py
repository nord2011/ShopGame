from itertools import product
from tkinter import *
import shop


player = shop.Player(name="Игрок", initial_balance=1000, max_storage=500)

apple = shop.Product(name="Яблоко", purchase_price=50, sell_price=30, quantity=2, stak=True)
Arbyz = shop.Product(name="Арбуз", purchase_price=100, sell_price=80, quantity=5, stak=True)
Sword = shop.Product(name="Меч Хуже", purchase_price=200, sell_price=160, stak=False)

Shop = shop.Shop(name="Магазин")

player.inventory.append(apple)
player.inventory.append(Arbyz)
player.inventory.append(Sword)

def update_balance():
    balance.config(text=f"${player.balance}")

def update_inventory():
    inventory_list.delete(0, END)


    for product in player.inventory:
        inventory_list.insert(END, f"{product.name} // Стоимость продажи: {product.sell_price} // Количество: {product.quantity}")



def update_Shop_list():
    buy_list.delete(0, END)

    for shop in player.shop.shop_list:
        buy_list.insert(END,f"{shop.name} // Стоимость покупки: {shop.purchase_price}// Стоимость продажи: {shop.sell_price} // Количество: {shop.quantity}")



def more_button_click():
    buy_button.pack_forget()
    sell_button.pack_forget()
    exit_button.pack_forget()
    more_button.pack_forget()

    back_button.pack(side="bottom", fill="x", padx=0, pady=0)
    add_button.pack(side="bottom", fill="x", padx=0, pady=20)
    del_button.pack(side="bottom", fill="x", padx=0, pady=0)

def sell_button_click():
    del_prod = inventory_list.curselection()
    del_prod_idx = del_prod[0]
    """if player.inventory[del_prod_idx].stak:
        player.inventory[del_prod_idx].quantity -= 1
        player.balance += player.inventory[del_prod_idx].sell_price
    else:
        player.balance += player.inventory[del_prod_idx].sell_price
        player.inventory.pop(del_prod_idx)"""
    player.sell(del_prod_idx)



    update_balance()
    update_inventory()
    update_Shop_list()

def buy_button_click():
    add_prod = buy_list.curselection()
    add_prod_idx = add_prod[0]
    player.buy(add_prod_idx, quantity_to_buy=1)

    update_balance()
    update_inventory()
    update_Shop_list()

def add_button_click():
    pass

def del_button_click():
    pass

def back_button_click():
    back_button.pack_forget()
    add_button.pack_forget()
    del_button.pack_forget()

    exit_button.pack(side="bottom",fill="x", padx=0, pady=0)
    buy_button.pack(side="bottom", fill="x", padx=0, pady=20)
    sell_button.pack(side="bottom", fill="x", padx=0, pady=20)
    more_button.pack(side="bottom", fill="x", padx=0, pady=20)


window = Tk()
window.title("Game")
window.geometry("730x640")
window.configure(bg="orange")

more_button_image = PhotoImage(file="more_button.png")
buy_button_image = PhotoImage(file="buy_button.png")
sell_button_image = PhotoImage(file="sell_button.png")
exit_button_image = PhotoImage(file="exit_button.png")

right_panel = Frame(window, bg="black", width=200, bd=6)
right_panel.pack(side="right", fill="y")

balance = Label(
    right_panel,
    text=f"$0",
    bg="black",
    fg="green",
    font=("Comic Sans MS", 20, "bold"),
    bd=6
)
balance.pack(pady=8, padx=5)

exit_button = Button(right_panel,
                     text="Exit",
                     bg="black",
                     fg="white",
                     font=("Comic Sans MS", 20, "bold"),
                     bd=6,
                     command=window.quit,
                     image=exit_button_image,
                     compound="right"
                    )
exit_button.pack(side="bottom",fill="x", padx=0, pady=0)

buy_button = Button(right_panel,
                    text="Buy",
                    bg="black",
                    fg="green",
                    font=("Comic Sans MS", 20, "bold"),
                    bd=6,
                    image=buy_button_image,
                    compound="right",
                    command=buy_button_click
                    )
buy_button.pack(side="bottom", fill="x", padx=0, pady=20)

sell_button = Button(right_panel,
                     text="Sell",
                     bg="black",
                     fg="red",
                     font=("Comic Sans MS", 20, "bold"),
                     bd=6,
                     image=sell_button_image,
                    compound="right",
                     command=sell_button_click)
sell_button.pack(side="bottom", fill="x", padx=0, pady=20)

more_button = Button(right_panel,
                     text="More",
                     bg="black",
                     fg="purple",
                     font=("Comic Sans MS", 20, "bold"),
                     bd=6,
                     image=more_button_image,
                     compound="right",
                     command=more_button_click
                     )
more_button.pack(side="bottom", fill="x", padx=0, pady=20)

add_button = Button(right_panel,
                    text="Add",
                    bg="black",
                    fg="green",
                    font=("Comic Sans MS", 20, "bold"),
                    bd=6)

del_button = Button(right_panel,
                    text="Del",
                    bg="black",
                    fg="red",
                    font=("Comic Sans MS", 20, "bold"),
                    bd=6)

back_button = Button(right_panel,
                     text="Back",
                     bg="black",
                     fg="white",
                     font=("Comic Sans MS", 20, "bold"),
                     bd=6,
                     command=back_button_click)

main_area = Frame(window, bg="yellow")
main_area.pack(expand=True, fill="both")

bottom_area = Frame(main_area, bg="black", bd=6, height=170)
bottom_area.pack(fill="x", side="bottom")

list_frame = Frame(main_area,
                   bg="black",)
list_frame.pack(fill="x")

inventory_label = Label(list_frame,
                        text="Инвентарь",
                        bg="black",
                        fg="white",
                        font=("Comic Sans MS", 20, "bold"))
inventory_label.pack()

inventory_list = Listbox(list_frame,
                         height=5,
                         bg="black",
                         fg="white")
inventory_list.pack(fill="x")

buy_list_label = Label(bottom_area,
                       text="Купить:",
                       bg="black",
                       fg="white",
                       font=("Comic Sans MS", 20, "bold"))
buy_list_label.pack(fill="x", side="top")

buy_list = Listbox(bottom_area,
                         height=5,
                         bg="black",
                         fg="white")
buy_list.pack(fill="x", side="bottom")





update_balance()
update_inventory()
update_Shop_list()

window.mainloop()