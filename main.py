import customtkinter as ctk
from time import time, sleep
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

moneys = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]


# 通貨タイプごとに生成されるクラス
class MoneyFrame(ctk.CTkFrame):
    def __init__(self, master, money_kingaku, money_image):
        super().__init__(master)
        self.money_label = ctk.CTkLabel(self, text=f"{money_kingaku}円")
        self.money_label.pack()
        self.money_image = ctk.CTkImage(Image.open(money_image))
        self.money_image_label = ctk.CTkLabel(self, width=100, image=self.money_image)
        self.money_image_label.pack()
        self.maisuu_input = ctk.CTkTextbox(self)
        self.maisuu_input.pack()

    def get_maisuu(self):
        print(self.maisuu_input.get("0.0"))
        return self.maisuu_input.get("0.0")


# メイン画面
class Main(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.living = True
        self.title("おかね の けいさんアプリ")
        self.geometry("640x480")

        self.money_frames = {}
        for money in moneys:
            self.money_frames.setdefault(money, MoneyFrame(self, money, f"images/{money}.png"))
            self.money_frames[money].pack()

        self.goukei_kingaku = ctk.CTkLabel(self, width=500, height=50, text="0円")
        self.goukei_kingaku.pack()

        self.keisan_button = ctk.CTkButton(self, width=500, height=50, text="けいさんする！", command=self.keisan)
        self.keisan_button.pack()

    def goukei(self):
        goukei = 0
        for money in moneys:
            maisuu = self.money_frames[money].get_maisuu()
            if maisuu not in {0, None}:
                goukei += money * maisuu

        return goukei

    def keisan(self):
        goukei = self.goukei()
        self.goukei_kingaku.configure(text=f"{goukei}円")


app = Main()
app.mainloop()


# app.mainloop()