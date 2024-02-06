import customtkinter as ctk
from time import time, sleep
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

moneys = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]


# 通貨タイプごとに生成されるクラス
class MoneyFrame(ctk.CTkFrame):
    def __init__(self, master, money_kingaku, money_image, offset):
        super().__init__(master)
        self.money_label = ctk.CTkLabel(self, text=f"{money_kingaku}円")
        self.money_label.grid(row=0, column=0, sticky="ew")
        with Image.open(money_image) as im:
            im.thumbnail(size=(150, 100))
            self.money_image = ctk.CTkImage(
                light_image=im,
                dark_image=im,
                size=(im.width, im.height)
            )
            self.money_image_label = ctk.CTkLabel(self, text="", image=self.money_image)
        self.money_image_label.grid(row=1, column=0, sticky="ew")
        self.maisuu_input = ctk.CTkTextbox(self, width=100, height=20)
        self.maisuu_input.grid(row=2, column=0, sticky="ew")

    def get_maisuu(self):
        maisuu = 0
        try:
            t = int(self.maisuu_input.get("0.0"))
        except:
            t = 0
        finally:
            maisuu = t
        return maisuu


# メイン画面
class Main(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.living = True
        self.title("おかね の けいさんアプリ")
        self.geometry("1280x768")

        self.money_parent = ctk.CTkFrame(self)
        self.money_frames = {}
        offset = 0
        for money in moneys:
            self.money_frames.setdefault(money, MoneyFrame(self.money_parent, money, f"images/{money}.png", offset))
            self.money_frames[money].grid(row=0, column=offset)
            offset += 1
        self.money_parent.grid(row=0, column=0)

        self.goukei_parent = ctk.CTkFrame(self)

        self.keisan_button = ctk.CTkButton(self.goukei_parent, width=200, height=50, text="けいさんする！", command=self.keisan)
        self.keisan_button.grid(row=0, column=0, sticky="ew")

        self.goukei_kingaku = ctk.CTkLabel(self.goukei_parent, height=50, text="0円")
        self.goukei_kingaku.grid(row=0, column=1, sticky="ew")

        self.goukei_parent.grid(row=1, column=0, sticky="ew")

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