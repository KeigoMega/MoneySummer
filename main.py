import customtkinter as ctk
from time import time, sleep


moneys = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]


# 通貨タイプごとに生成されるクラス
class MoneyFrame(ctk.CTkFrame):
    def __init__(self, master, money_kingaku, money_image):
        super().__init__(master)
        self.money_label = ctk.CTkLabel(self, text=f"{money_kingaku}円")
        self.money_image = ctk.CTkImage(self, money_image)
        self.maisuu_input = ctk.CTkTextbox(self)

    def get_maisuu(self):
        return self.maisuu_input.get()


# メイン画面
class Main(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.living = True
        self.set_appearance_mode("dark")  # Modes: system(default), light, dark
        self.set_default_color_theme("green")  # Themes: blue(default), dark-blue, green
        self.title("おかね の けいさんアプリ")
        self.geometry("640x480")

        self.money_frames = {}
        for money in moneys:
            self.money_frames.setdefault(f"m{money}", MoneyFrame(self, money, f"images/{money}.png"))

        self.goukei_kingaku = ctk.CTkLabel(self, width=500, height=50, text="0円")

        self.keisan_button = ctk.CTkButton(self, width=500, height=50, text="けいさんする！", command=self.keisan)

    def goukei(self):
        goukei = 0
        for money in moneys:
            maisuu = self.money_frames[money].get_maisuu()
            if maisuu not in {0, None}:
                goukei += money * maisuu

        return goukei

    def keisan(self):
        goukei = self.goukei()
        self.goukei_label.







elv = elevator_controller.ElevatorController()


# button enablers

def disable_all_buttons():
    door_open_btn_enabler(0)
    door_close_btn_enabler(0)
    goto_floor_1_btn_enabler(0)
    goto_floor_2_btn_enabler(0)


def mode_selecter_enabler(go_en=0):
    if go_en:
        EV_mode_selector.configure(state="normal")
        EV_mode_selector.configure(text_color="white")
    else:
        EV_mode_selector.deselect()
        EV_mode_selector.configure(state="disable")
        EV_mode_selector.configure(text_color="gray")


def door_open_btn_enabler(go_en=0):
    if go_en:
        EV_door_open_btn.configure(state="normal")
        EV_door_open_btn.configure(text_color="white")
    else:
        EV_door_open_btn.configure(state="disable")
        EV_door_open_btn.configure(text_color="gray")


def door_close_btn_enabler(go_en=0):
    if go_en:
        EV_door_close_btn.configure(state="normal")
        EV_door_close_btn.configure(text_color="white")
    else:
        EV_door_close_btn.configure(state="disable")
        EV_door_close_btn.configure(text_color="gray")


def goto_floor_1_btn_enabler(go_en=0):
    if go_en:
        EV_goto_floor_1_btn.configure(state="normal")
        EV_goto_floor_1_btn.configure(text_color="white")
    else:
        EV_goto_floor_1_btn.configure(state="disable")
        EV_goto_floor_1_btn.configure(text_color="gray")


def goto_floor_2_btn_enabler(go_en=0):
    if go_en:
        EV_goto_floor_2_btn.configure(state="normal")
        EV_goto_floor_2_btn.configure(text_color="white")
    else:
        EV_goto_floor_2_btn.configure(state="disable")
        EV_goto_floor_2_btn.configure(text_color="gray")


# button functions

def mode_switched():
    if EV_mode_selector.get() and EV_mode_selector.cget("state") == "normal":
        elv.mode_switch_AGV(1)
    else:
        elv.mode_switch_AGV(0)
        elv.emergency_all_off()
        disable_all_buttons()


def door_open():
    if EV_door_open_btn.cget("state") == "normal":
        elv.door_open(1)


def door_close():
    if EV_door_close_btn.cget("state") == "normal":
        elv.door_close(1)


def goto_floor_1():
    if EV_goto_floor_1_btn.cget("state") == "normal":
        elv.goto_floor_1(1)


def goto_floor_2():
    if EV_goto_floor_2_btn.cget("state") == "normal":
        elv.goto_floor_2(1)


def check_inputs():
    elv.check_automation()
    elv.check_emergency()
    elv.check_error()
    elv.check_enable_ext_control()
    elv.check_rising()
    elv.check_falling()
    elv.check_running()
    elv.check_mode_agv()
    elv.check_mode_agv_working()
    elv.check_door_open()
    elv.check_door_close()
    elv.check_floor_1()
    elv.check_floor_2()


# 1列目の状態表示ランプです。

EV_automation = ctk.CTkLabel(master=app, width=118, height=58, text="全自動運転中", fg_color="gray")
EV_automation.place(x=20, y=20)

EV_running = ctk.CTkLabel(master=app, width=118, height=58, text="EV走行中", fg_color="gray")
EV_running.place(x=141, y=20)

EV_mode_AGV = ctk.CTkLabel(master=app, width=118, height=58, text="AGVモード", fg_color="gray")
EV_mode_AGV.place(x=262, y=20)

EV_mode_AGV_working = ctk.CTkLabel(master=app, width=118, height=58, text="AGV搬送モード", fg_color="gray")
EV_mode_AGV_working.place(x=383, y=20)

EV_enable_ext_control = ctk.CTkLabel(master=app, width=118, height=58, text="外部制御可能", fg_color="gray")
EV_enable_ext_control.place(x=504, y=20)

# 2列目の状態表示ランプです

EV_error = ctk.CTkLabel(master=app, width=118, height=28, text="EV異常", fg_color="gray")
EV_error.place(x=20, y=81)

EV_emergency = ctk.CTkLabel(master=app, width=118, height=28, text="EV非常時管制", fg_color="gray")
EV_emergency.place(x=20, y=111)

EV_floor_1 = ctk.CTkLabel(master=app, width=78, height=58, text="1階", fg_color="gray")
EV_floor_1.place(x=141, y=81)

EV_floor_2 = ctk.CTkLabel(master=app, width=78, height=58, text="2階", fg_color="gray")
EV_floor_2.place(x=222, y=81)

EV_rising = ctk.CTkLabel(master=app, width=78, height=58, text="上昇中", fg_color="gray")
EV_rising.place(x=302, y=81)

EV_falling = ctk.CTkLabel(master=app, width=78, height=58, text="下降中", fg_color="gray")
EV_falling.place(x=383, y=81)

EV_door_open = ctk.CTkLabel(master=app, width=78, height=58, text="戸全開", fg_color="gray")
EV_door_open.place(x=464, y=81)

EV_door_close = ctk.CTkLabel(master=app, width=78, height=58, text="戸全閉", fg_color="gray")
EV_door_close.place(x=544, y=81)

# 各種操作ボタンです

EV_mode_selector = ctk.CTkSwitch(master=app, text="運転モード切替(ON:AGV)", command=mode_switched)
EV_mode_selector.place(x=80, y=200)
EV_mode_selector.configure(state="disabled")

EV_door_open_btn = ctk.CTkButton(master=app, width=120, height=80, text="戸開ける", command=door_open)
EV_door_open_btn.place(x=40, y=300)
EV_door_open_btn.configure(state="disabled")

EV_door_close_btn = ctk.CTkButton(master=app, width=120, height=80, text="戸閉じる", command=door_close)
EV_door_close_btn.place(x=200, y=300)
EV_door_close_btn.configure(state="disabled")

EV_goto_floor_2_btn = ctk.CTkButton(master=app, width=50, height=100, corner_radius=50, text="2階へ", command=goto_floor_2)
EV_goto_floor_2_btn.place(x=440, y=170)
EV_goto_floor_2_btn.configure(state="disabled")

EV_goto_floor_1_btn = ctk.CTkButton(master=app, width=50, height=100, corner_radius=50, text="1階へ", command=goto_floor_1)
EV_goto_floor_1_btn.place(x=440, y=300)
EV_goto_floor_1_btn.configure(state="disabled")


while living:
    check_inputs()

    app.update_idletasks()
    app.update()

    if not elv.EV_automation or elv.EV_emergency or elv.EV_error:
        elv.emergency_all_off()
        mode_selecter_enabler(0)
        disable_all_buttons()
    else:
        mode_selecter_enabler(1)

        if not EV_mode_selector.get():
            disable_all_buttons()
        else:
            if not elv.EV_mode_AGV_working:
                elv.all_control_off()
                disable_all_buttons()
            else:
                if elv.EV_floor_1:
                    goto_floor_1_btn_enabler(0)
                    if not elv.EV_running:
                        if elv.EV_enable_ext_control:
                            goto_floor_2_btn_enabler(1)
                    else:
                        goto_floor_2_btn_enabler(0)

                if elv.EV_floor_2:
                    goto_floor_2_btn_enabler(0)
                    if not elv.EV_running:
                        if elv.EV_enable_ext_control:
                            goto_floor_1_btn_enabler(1)
                    else:
                        goto_floor_1_btn_enabler(0)

                if not elv.EV_running:
                    if elv.EV_door_close:
                        door_open_btn_enabler(1)
                        door_close_btn_enabler(0)
                    elif elv.EV_door_open:
                        door_open_btn_enabler(0)
                        door_close_btn_enabler(1)

    sleep(0.1)

    # 1列目の状態表示ランプ更新。

    if elv.EV_automation:
        EV_automation.configure(fg_color="yellow")
    else:
        EV_automation.configure(fg_color="gray")

    if elv.EV_running:
        EV_running.configure(fg_color="yellow")
    else:
        EV_running.configure(fg_color="gray")

    if elv.EV_mode_AGV:
        EV_mode_AGV.configure(fg_color="yellow")
    else:
        EV_mode_AGV.configure(fg_color="gray")

    if elv.EV_mode_AGV_working:
        EV_mode_AGV_working.configure(fg_color="yellow")
    else:
        EV_mode_AGV_working.configure(fg_color="gray")

    if elv.EV_enable_ext_control:
        EV_enable_ext_control.configure(fg_color="yellow")
    else:
        EV_enable_ext_control.configure(fg_color="gray")

    if elv.EV_enable_ext_control:
        EV_enable_ext_control.configure(fg_color="yellow")
    else:
        EV_enable_ext_control.configure(fg_color="gray")

    # 2列目の状態表示ランプ更新。

    if elv.EV_error:
        EV_error.configure(fg_color="red")
    else:
        EV_error.configure(fg_color="gray")

    if elv.EV_emergency:
        EV_emergency.configure(fg_color="red")
    else:
        EV_emergency.configure(fg_color="gray")

    if elv.EV_floor_1:
        EV_floor_1.configure(fg_color="yellow")
    else:
        EV_floor_1.configure(fg_color="gray")

    if elv.EV_floor_2:
        EV_floor_2.configure(fg_color="yellow")
    else:
        EV_floor_2.configure(fg_color="gray")

    if elv.EV_rising:
        EV_rising.configure(fg_color="yellow")
    else:
        EV_rising.configure(fg_color="gray")

    if elv.EV_falling:
        EV_falling.configure(fg_color="yellow")
    else:
        EV_falling.configure(fg_color="gray")

    if elv.EV_door_open:
        EV_door_open.configure(fg_color="yellow")
    else:
        EV_door_open.configure(fg_color="gray")

    if elv.EV_door_close:
        EV_door_close.configure(fg_color="yellow")
    else:
        EV_door_close.configure(fg_color="gray")


# app.mainloop()