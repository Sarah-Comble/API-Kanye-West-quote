from tkinter import *
import requests

# on utilise les datas de l'api kanye west
def get_quote():
    reponse = requests.get(url="https://api.kanye.rest")
    reponse.raise_for_status()  # mettra un message d'erreur si la demande n'a pas de reponse
    data = reponse.json()
    # print(data["quote"])
    canvas.itemconfig(quote_text, text=data["quote"])

# UI Settings
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 25, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()