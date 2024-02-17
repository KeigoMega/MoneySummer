import customtkinter as ctk
from time import time, sleep
from PIL import Image, ImageTk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

moneys = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]


class MoneyParent(ctk.CTkFrame):
    def __init__(self, master, font_normal, font_big):
        super().__init__(master)

        self.money_frames = {}

        offset = 0
        for money in moneys:
            self.money_frames.setdefault(
                money,
                MoneyFrame(
                    master=self,
                    money_kingaku=money,
                    money_image=f"images/{money}.png",
                    font_normal=font_normal,
                    font_big=font_big))

            self.money_frames[money].grid(row=0, column=offset)
            offset += 1


# 通貨タイプごとに生成されるクラス
class MoneyFrame(ctk.CTkFrame):
    def __init__(self, master, money_kingaku, money_image, font_normal, font_big):
        super().__init__(master)

        self.money_label = ctk.CTkLabel(self,
                                        text=f"{money_kingaku}円",
                                        font=font_normal)
        self.money_label.grid(row=0, column=0, sticky="ew")

        with Image.open(money_image) as im:
            im.thumbnail(size=(150, 100))
            self.money_image = ctk.CTkImage(
                light_image=im,
                dark_image=im,
                size=(im.width, im.height)
            )
            self.money_image_label = ctk.CTkLabel(self,
                                                  text="",
                                                  image=self.money_image)

        self.money_image_label.grid(row=1, column=0, sticky="ew")

        self.maisuu_input = ctk.CTkTextbox(self,
                                           width=80,
                                           height=55,
                                           font=font_big)
        self.maisuu_input.grid(row=2, column=0, sticky="ew")

        self.reset()

    def get_maisuu(self):
        maisuu = 0

        t = 0
        try:
            t = int(self.maisuu_input.get("0.0", "end"))
        except ValueError:
            t = 0
        finally:
            maisuu = t

        return maisuu

    def reset(self):
        self.maisuu_input.delete("0.0", "end")


class Goukei(ctk.CTkFrame):
    def __init__(self, master, money_parent, anzan_frame, hiragana_view, font_normal, font_big):
        super().__init__(master)

        self.money_parent = money_parent
        self.anzan_frame = anzan_frame
        self.hiragana_view = hiragana_view

        self.keisan_button = ctk.CTkButton(self,
                                           width=200, text="けいさんする！",
                                           command=self.keisan,
                                           font=font_normal)
        self.keisan_button.grid(row=0, column=0, sticky="wens")

        self.goukei_kingaku = ctk.CTkLabel(self,
                                           height=50,
                                           font=font_big)
        self.goukei_kingaku.grid(row=0, column=1, sticky="ew")

        self.reset()

    def goukei(self):
        goukei = 0
        for money in moneys:
            maisuu = self.money_parent.money_frames[money].get_maisuu()
            if maisuu not in {0, None}:
                goukei += money * maisuu

        return goukei

    def keisan(self):
        goukei = self.goukei()

        try:
            anzan = int(self.anzan_frame.anzan_input.get("0.0", "end"))
        except ValueError:
            self.anzan_frame.machigai()
        else:
            if anzan == goukei:
                self.anzan_frame.seikai()
            else:
                self.anzan_frame.machigai()

        self.hiragana_view.set_hiragana(goukei=goukei)
        self.goukei_kingaku.configure(text=f"{goukei}円")

    def reset(self):
        self.goukei_kingaku.configure(text="0円")


class Anzan(ctk.CTkFrame):
    def __init__(self, master, font_normal, font_big):
        super().__init__(master)

        self.anzan_title = ctk.CTkLabel(self,
                                        width=200,
                                        text="たしたら なんえん だと おもう？ ==> ",
                                        font=font_normal)
        self.anzan_title.grid(row=0, column=0)

        self.anzan_input = ctk.CTkTextbox(self,
                                          width=200,
                                          height=50,
                                          font=font_big)
        self.anzan_input.grid(row=0, column=1, sticky="ew")

        self.result_label = ctk.CTkLabel(self,
                                         width=200,
                                         height=50,
                                         font=font_big)
        self.result_label.grid(row=0, column=2, sticky="ns")

        self.reset()

    def seikai(self):
        self.anzan_input.configure(fg_color="green")
        self.result_label.configure(text="◎ せいかい！！")

    def machigai(self):
        self.anzan_input.configure(fg_color="red")
        self.result_label.configure(text="✕ ざんねん！！")

    def reset(self):
        self.anzan_input.delete("0.0", "end")
        self.anzan_input.configure(fg_color="white")
        self.result_label.configure(text="")


class HiraganaView(ctk.CTkFrame):
    def __init__(self, master, font_normal, font_big):
        super().__init__(master)

        self.hiragana_label = ctk.CTkLabel(self,
                                           height=50,
                                           font=font_big)
        self.hiragana_label.grid(row=0, column=0, sticky="ew")

        self.reset()

    def set_hiragana(self, goukei):
        goukei_hiragana = self.goukei_to_hiragana(goukei)
        self.hiragana_label.configure(text=f"{goukei_hiragana} えん")

    def goukei_to_hiragana(self, goukei):
        goukei_str = reversed([i for i in str(goukei)])
        goukei_hiragana = []
        man = []
        for i, num in enumerate(goukei_str):
            if i == 0:
                if num in {"0"}:
                    pass
                else:
                    goukei_hiragana.append(f"{num}")
            elif i == 1:
                if num in {"0"}:
                    pass
                elif num in {"1"}:
                    goukei_hiragana.append(" じゅう")
                else:
                    goukei_hiragana.append(f"{num}じゅう")
            elif i == 2:
                if num in {"2", "4", "5", "7", "9"}:
                    goukei_hiragana.append(f"{num}ひゃく")
                elif num in {"3"}:
                    goukei_hiragana.append(f"{num}びゃく")
                elif num in {"6", "8"}:
                    goukei_hiragana.append(f"{num}ぴゃく")
                elif num in {"1"}:
                    goukei_hiragana.append(" ひゃく")
                else:
                    pass
            elif i == 3:
                if num in {"2", "4", "5", "6", "7", "8", "9"}:
                    goukei_hiragana.append(f"{num}せん")
                elif num in {"3"}:
                    goukei_hiragana.append(f"{num}ぜん")
                elif num in {"1"}:
                    goukei_hiragana.append(" せん")
                else:
                    pass
            elif i in {4, 5, 6, 7}:
                man.append(num)

        if man:
            str_man = ""
            for t in reversed(man):
                str_man += t
            res = self.goukei_to_hiragana(int(str_man))
            goukei_hiragana.append(f"{res}まん")

        renketu = ""
        for hiragana in reversed(goukei_hiragana):
            renketu += hiragana + " "

        return renketu

    def reset(self):
        self.hiragana_label.configure(text="ここ に ひらがな での きんがく を ひょうじ します")


# メイン画面
class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.font_normal = ctk.CTkFont(family="Rounded Mplus 1c", size=16)
        self.font_big = ctk.CTkFont(family="Rounded Mplus 1c", size=24)

        self.living = True
        self.title("おかね の けいさんアプリ Ver1.0")
        self.geometry("1023x400")

        self.money_parent = MoneyParent(self,
                                        font_normal=self.font_normal,
                                        font_big=self.font_big)

        self.anzan_frame = Anzan(self,
                                 font_normal=self.font_normal,
                                 font_big=self.font_big)

        self.hiragana_view = HiraganaView(self,
                                          font_normal=self.font_normal,
                                          font_big=self.font_big)

        self.goukei_frame = Goukei(self,
                                   money_parent=self.money_parent,
                                   anzan_frame=self.anzan_frame,
                                   hiragana_view=self.hiragana_view,
                                   font_normal=self.font_normal,
                                   font_big=self.font_big)

        self.reset_button = ctk.CTkButton(self,
                                          height=50,
                                          text="ぜんぶ けします",
                                          command=self.reset_all,
                                          font=self.font_big)

        self.money_parent.grid(row=0, column=0, sticky="ew")
        self.anzan_frame.grid(row=1, column=0, sticky="ew")
        self.goukei_frame.grid(row=2, column=0, sticky="ew")
        self.hiragana_view.grid(row=3, column=0, sticky="ew")
        self.reset_button.grid(row=4, column=0, sticky="ew")

    def reset_all(self):
        for money_frame in self.money_parent.money_frames.values():
            money_frame.reset()
        self.anzan_frame.reset()
        self.goukei_frame.reset()
        self.hiragana_view.reset()


app = Main()
app.mainloop()
