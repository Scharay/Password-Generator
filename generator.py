import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import random
import string
import math
import threading
import time
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("")
    return os.path.join(base_path, relative_path)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

palettes = {
    "dark": {
        "bg": "#12151f", "panel": "#1a1e2e", "card": "#1f2437",
        "border": "#2a3050", "text": "#d0d8f0", "muted": "#5a6480",
        "accent": "#5b9cf6", "green": "#4ec994", "amber": "#e8a93a",
        "red": "#e05c6b", "purple": "#9d7fe8", "btn_bg": "#2d5fa6"
    },
    "light": {
        "bg": "#f4f5f8", "panel": "#e9ebf2", "card": "#ffffff",
        "border": "#d2d6e4", "text": "#2c303d", "muted": "#7a849e",
        "accent": "#1a73e8", "green": "#13804e", "amber": "#b06f00",
        "red": "#c53947", "purple": "#6b46c1", "btn_bg": "#1a73e8"
    }
}

translations = {
    "ru": {
        "title_app": "Генератор паролей",
        "config": "Конфигурация",
        "dark_mode": "Темная тема",
        "lang_label": "Язык",
        "len_lbl": "Длина пароля: ",
        "rec_lbl": "Рекомендуется: ≥ 12 символов",
        "count_lbl": "Количество паролей: ",
        "set_lbl": "Набор символов",
        "digits": "Цифры  0–9",
        "lower": "Строчные  a–z",
        "upper": "Заглавные  A–Z",
        "spec": "Спецсимволы  !@#$%",
        "similar": "Исключить похожие (0OolL1iI)",
        "memorable": "Запоминаемый режим",
        "hide": "Скрыть пароли  ***",
        "pin_lbl": "PIN-код",
        "pin_len": "Длина:",
        "btn_pin": "Создать PIN",
        "btn_copy_pin": "Копировать PIN",
        "warn_pin_empty": "Сначала создайте PIN",
        "pin_copied_msg": "ПИН-код успешно скопирован!",
        "pin_copied_title": "Успех",
        "title1": "Генератор",
        "title2": " паролей",
        "result": "Результат",
        "metric_str": "Надёжность",
        "metric_ent": "Энтропия",
        "metric_crack": "Взлом за",
        "metric_leak": "Утечки",
        "tpl_lbl": "Шаблон (пример: LLL-DD-S | L=буква, D=цифра, S=спец):",
        "words_lbl": "Встраиваемые слова (пример: coffee, cat):",
        "btn_gen": "Сгенерировать",
        "btn_copy": "Копировать",
        "btn_clear": "Очистить",
        "hist_lbl": "История сеанса (копирование: кнопка 'копировать')",
        "err_title": "Ошибка",
        "err_empty": "Пул символов пуст",
        "warn_title": "Внимание",
        "warn_gen": "Сначала сгенерируйте пароль.",
        "info_title": "Скопировано",
        "info_copied": "пароль скопирован",
        "info_copied_few": "пароля скопировано",
        "info_copied_many": "паролей скопировано",
        "copy_ctx": "Копировать",
        "instantly": "Мгновенно",
        "seconds": "сек.",
        "minutes": "мин.",
        "hours": "ч.",
        "days": "д.",
        "years": "л.",
        "crack_impossible": "Практически невозможно",
        "found": "Найден",
        "clean": "Чисто",
        "str_weak": "Слабый",
        "str_avg": "Средний",
        "str_good": "Хороший",
        "str_exc": "Отличный",
        "bits": "бит",
        "copied_selected": "Выделенные пароли скопированы!",
        "copied_generated": "паролей скопировано в буфер",
    },
    "en": {
        "title_app": "Password Generator",
        "config": "Configuration",
        "dark_mode": "Dark theme",
        "lang_label": "Language",
        "len_lbl": "Password length: ",
        "rec_lbl": "Recommended: ≥ 12 chars",
        "count_lbl": "Password count: ",
        "set_lbl": "Character set",
        "digits": "Digits 0–9",
        "lower": "Lowercase a–z",
        "upper": "Uppercase A–Z",
        "spec": "Special chars  !@#$%",
        "similar": "Exclude similar (0OolL1iI)",
        "memorable": "Memorable mode",
        "hide": "Hide passwords  ***",
        "pin_lbl": "PIN-code",
        "pin_len": "Length:",
        "btn_pin": "Create PIN",
        "btn_copy_pin": "Copy PIN",
        "warn_pin_empty": "Generate a PIN first",
        "pin_copied_msg": "PIN code copied successfully!",
        "pin_copied_title": "Success",
        "title1": "Password",
        "title2": " generator",
        "result": "Result",
        "metric_str": "Strength",
        "metric_ent": "Entropy",
        "metric_crack": "Crack time",
        "metric_leak": "Leaks",
        "tpl_lbl": "Template (example: LLL-DD-S | L=letter, D=digit, S=special):",
        "words_lbl": "Embedded words (example: coffee, cat):",
        "btn_gen": "Generate",
        "btn_copy": "Copy",
        "btn_clear": "Clear",
        "hist_lbl": "Session history (copying: 'copy' button)",
        "err_title": "Error",
        "err_empty": "Character pool is empty.",
        "warn_title": "Warning",
        "warn_gen": "Generate a password first.",
        "info_title": "Copied",
        "info_copied": "password copied to clipboard",
        "info_copied_few": "passwords copied to clipboard",
        "info_copied_many": "passwords copied to clipboard",
        "copy_ctx": "Copy",
        "instantly": "Instantly",
        "seconds": "sec.",
        "minutes": "min.",
        "hours": "h.",
        "days": "d.",
        "years": "y.",
        "crack_impossible": "Practically impossible",
        "found": "Found",
        "clean": "Clean",
        "str_weak": "Weak",
        "str_avg": "Average",
        "str_good": "Good",
        "str_exc": "Excellent",
        "bits": "bits",
        "copied_selected": "Selected passwords copied to clipboard!",
        "copied_generated": "passwords copied to clipboard",
    }
}

FL = ("Segoe UI", 11)
FM = ("Consolas", 13)
FS = ("Segoe UI", 10)
FB = ("Segoe UI", 11, "bold")

spec_chars = "!@#$%"

weak_passwords = {
    "password","123456","12345678","qwerty","abc123","monkey","1234567",
    "letmein","trustno1","dragon","baseball","iloveyou","master","sunshine",
    "ashley","bailey","passw0rd","shadow","123123","654321","superman",
    "qazwsx","michael","football","password1","password123","admin","welcome",
    "login","hello","qwerty123","1q2w3e4r","1234","11111","000000","zxcvbnm",
    "qwertyuiop","987654321","pass","pass123","test","guest",
    "root","toor","alpine","changeme","default","secret","temp","temp123",
    "111111","222222","333333","444444","555555","666666","777777","888888",
    "999999","121212","696969","676767","7777777","123321","112233","445566",
    "password1!","password!","p@ssword","p@ssw0rd","passw0rd!","useruser",
    "admin123","administrator","root123","user","user123","qwerty1","qwerty12",
    "qweasd","zxcvbn","1q2w3e","1qaz2wsx","qazwsxedc","zaq12wsx","rootroot",
    "asdfgh","asdfghjkl","asdf1234","qwertyui","ytrewq","login123",
    "abc","abcd","abcde","abcdef","abcdefg","abcdefgh","abcdefghi","abcdefghij",
    "iloveyou1","iloveyou2","love","lovely","welcome1","welcome123",
    "letmein1","letmein123","monkey1","dragon1","football1","superman1",
    "0000000","00000000","123123123","321321","12341234","11223344","55667788",
    "password2","password3","password4","password5","password6","password7",
    "qwerty1234","qwerty2020","qwerty2021","qwerty2022","qwerty2023","qwerty2024",
    "test123","testtest","guest123","demo","demo123","changeme123","adminadmin",
    "qwerty2025","qwerty2026","password2025","password2026","admin2025","admin2026",
    "2025","2026","welcome2025","welcome2026","happynewyear","marrychristmas",
    "cisco","oracle","postgres","mysql","ubnt","mikrotik","huawei","zyxel",
    "manager","supervisor","service","support","operator","sysadmin",
    "mnbvcxz","poiuytrewq","lkjhgfdsa","asdf","zxc","qwer","qaz","wsx",
    "google","apple","microsoft","windows","android","iphone","samsung",
    "matrix","avatar","pokemon","starwars","batman","spiderman","warcraft",
    "cookie","coffee","chocolate","pizza","burger","banana","apple1"
}
weak_passwords_norm = {w.lower() for w in weak_passwords}


class passwordgenerator(ctk.CTk):
    def __init__(self):
        super().__init__()
        try:
            self.iconbitmap(resource_path("icon.ico"))
        except Exception:
            pass

        self.lang_var = tk.StringVar(value="ru")
        self.geometry("1060x760")
        self.minsize(980, 700)

        self._labels = []
        self._cards = []
        self._hlines = []
        self._entries = []
        self._tk_buttons = []
        self._checkbuttons = []

        self.history = []
        self.last_raw = []
        self._anim_running = False
        self._anim_chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%")
        self._hover_line = None

        self.words_pool = [
            "cyber","secure","shield","token","crypto","vertex","matrix",
            "pixel","nexus","omega","aegis","echo","prime","forge","vault",
            "core","quantum","rune","helix","phantom","synth","logic",
            "vector","daemon","packet","kernel","neural","binary","digital",
            "protocol","bastion","cipher","citadel","armor","mind","keygen",
            "proxy","subnet","firewall","entropy","bypass","access","breach",
            "detect","backup","script","shadow","static","compile","beacon",
            "hazard","vortex","hybrid","cobalt","method","lambda","syntax",
            "source","object","thread","buffer","render","system","server",
            "client","driver","engine","modulo","aspect","uplink","domain",
            "router","switch","cluster","gateway","anchor","signal","portal",
            "stream","octal","socket","remote","stdout","octane","tensor",
            "silicon","sensor","pulsar","cosmos","quasar","flux","quartz",
            "plasma","module","python","kotlin","golang","rust","process",
            "cache","runtime","library","ethernet","dns","latency","exploit",
            "sandbox","scanner","defender","decrypt","guardian","encrypt",
            "nebula","galaxy","meteor","comet","orbit","saturn","jupiter",
            "apollo","nova","stellar","lunar","solar","circuit","voltage",
            "frequency","analog","titan","valor","swift","blaze","spark",
            "surge","blade","crest","crown","drake","eagle","falcon","ghost",
            "halo","iron","knight","lance","noble","onyx","prism","quest",
            "raven","sigma","unity","ultra","wraith","xenon","alpha","bravo",
            "delta","foxtrot","hotel","india","juliet","kilo","lima","mike",
            "november","oscar","papa","quebec","romeo","sierra","tango",
            "uniform","victor","whiskey","yankee","zulu","frost","storm",
            "ember","cedar","coral","amber","stone","river","cloud","desert",
            "glacier","island","canyon","orbit","crater","aurora","zenith",
            "apex","dune","summit","ridge","tundra",
        ]

        self._build_ui()
        self.change_language()
        self.update_theme_styles()

    def _build_ui(self):
        self.grid_columnconfigure(0, minsize=280)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._build_sidebar()
        self._build_main()

    def _build_sidebar(self):
        self.sb = tk.Frame(self, width=280)
        self.sb.grid(row=0, column=0, sticky="nsew")
        self.sb.pack_propagate(False)

        self.lbl_config = tk.Label(self.sb, font=("Segoe UI", 13, "bold"))
        self.lbl_config.pack(pady=(24,6), padx=20, anchor="w")
        self._labels.append((self.lbl_config, "accent"))
        self._hline(self.sb)

        self.theme_var = tk.BooleanVar(value=True)
        self.cb_theme = tk.Checkbutton(self.sb, font=FS, variable=self.theme_var, command=self.toggle_theme)
        self.cb_theme.pack(anchor="w", padx=22, pady=(6,4))
        self._checkbuttons.append(self.cb_theme)

        self.lang_frame = tk.Frame(self.sb)
        self.lang_frame.pack(anchor="w", padx=22, pady=(4,6))
        self.lbl_lang = tk.Label(self.lang_frame, font=FS)
        self.lbl_lang.pack(side="left")
        self._labels.append((self.lbl_lang, "text"))
        self.lang_btn_ru = tk.Radiobutton(self.lang_frame, text="RU", font=FS, value="ru", variable=self.lang_var, command=self.change_language)
        self.lang_btn_ru.pack(side="left", padx=(10,5))
        self.lang_btn_en = tk.Radiobutton(self.lang_frame, text="EN", font=FS, value="en", variable=self.lang_var, command=self.change_language)
        self.lang_btn_en.pack(side="left", padx=5)
        self._checkbuttons.extend([self.lang_btn_ru, self.lang_btn_en])
        self._hline(self.sb)

        self.len_var = tk.IntVar(value=16)
        self.len_lbl = tk.Label(self.sb, font=FL)
        self.len_lbl.pack(pady=(12,2), padx=22, anchor="w")
        self._labels.append((self.len_lbl, "text"))
        self.len_scale = tk.Scale(self.sb, from_=4, to=64, orient="horizontal", variable=self.len_var, command=self._on_len_change, sliderrelief="flat", length=236, showvalue=False, highlightthickness=0, takefocus=0)
        self.len_scale.pack(padx=22)
        self.len_scale.set(16)
        self.lbl_rec = tk.Label(self.sb, font=("Segoe UI", 9, "italic"))
        self.lbl_rec.pack(padx=22, anchor="w", pady=(0,6))
        self._labels.append((self.lbl_rec, "muted"))

        self.count_var = tk.IntVar(value=1)
        self.count_lbl = tk.Label(self.sb, font=FL)
        self.count_lbl.pack(pady=(10,2), padx=22, anchor="w")
        self._labels.append((self.count_lbl, "text"))
        self.count_scale = tk.Scale(self.sb, from_=1, to=10, orient="horizontal", variable=self.count_var, highlightthickness=0, takefocus=0, sliderrelief="flat", length=236, showvalue=False, command=self._on_count_change)
        self.count_scale.pack(padx=22)
        self.count_scale.set(1)
        self._hline(self.sb)

        self.lbl_set = tk.Label(self.sb, font=("Segoe UI", 9, "bold"))
        self.lbl_set.pack(pady=(10,4), padx=22, anchor="w")
        self._labels.append((self.lbl_set, "muted"))

        self._cb_keys = ["digits","lower","upper","spec","similar","memorable","hide"]
        self._cb_defaults = [True, True, True, False, False, False, False]
        self._cb_widgets = {}
        self._cb = {}
        for key, default in zip(self._cb_keys, self._cb_defaults):
            var = tk.BooleanVar(value=default)
            cb  = tk.Checkbutton(self.sb, font=FS, variable=var)
            cb.pack(anchor="w", padx=22, pady=3)
            self._checkbuttons.append(cb)
            self._cb[key] = var
            self._cb_widgets[key] = cb

        self._cb_widgets["hide"].configure(command=self._on_hide_toggle)
        self._hline(self.sb)

        self.lbl_pin_title = tk.Label(self.sb, font=("Segoe UI", 9, "bold"))
        self.lbl_pin_title.pack(pady=(10,4), padx=22, anchor="w")
        self._labels.append((self.lbl_pin_title, "muted"))

        self.pin_row = tk.Frame(self.sb)
        self.pin_row.pack(padx=22, fill="x")
        self.lbl_plen = tk.Label(self.pin_row, font=FS)
        self.lbl_plen.pack(side="left")
        self._labels.append((self.lbl_plen, "text"))
        self.pin_len = tk.IntVar(value=6)
        self.pin_spin = tk.Spinbox(self.pin_row, from_=4, to=12, textvariable=self.pin_len, width=3, relief="flat", font=FS)
        self.pin_spin.pack(side="left", padx=8)
        self.btn_pin = tk.Button(self.pin_row, relief="flat", font=FS, cursor="hand2", command=self._gen_pin)
        self.btn_pin.pack(side="left")
        self._tk_buttons.append(self.btn_pin)

        self.pin_out = tk.Label(self.sb, text="", font=("Consolas", 14))
        self.pin_out.pack(pady=(6,4))
        self._labels.append((self.pin_out, "green"))

        self.btn_copy_pin = tk.Button(self.sb, relief="flat", font=FS, cursor="hand2", command=self.copy_pin_to_clipboard)
        self.btn_copy_pin.pack(fill="x", padx=22, pady=(0,10))
        self._tk_buttons.append(self.btn_copy_pin)

    def _build_main(self):
        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=0, column=1, padx=(16,20), pady=20, sticky="nsew")
        self.main_frame.columnconfigure(0, weight=1)

        self.hdr = tk.Frame(self.main_frame)
        self.hdr.grid(row=0, column=0, sticky="ew", pady=(0,12))
        self.lbl1 = tk.Label(self.hdr, font=("Segoe UI", 22, "bold"))
        self.lbl1.pack(side="left")
        self._labels.append((self.lbl1, "text"))
        self.lbl2 = tk.Label(self.hdr, font=("Segoe UI", 22, "bold"))
        self.lbl2.pack(side="left")
        self._labels.append((self.lbl2, "accent"))

        out = self._card(self.main_frame, row=1)
        self.lbl_res = tk.Label(out, font=FS)
        self.lbl_res.pack(anchor="w", padx=16, pady=(10,2))
        self._labels.append((self.lbl_res, "muted"))
        self.result_box = tk.Text(out, height=6, font=("Consolas", 14), relief="flat", wrap="none", padx=16, pady=8)
        self.result_box.pack(fill="both", expand=True)

        self.ctx_result = tk.Menu(self, tearoff=0)
        self.ctx_result.add_command(command=self._copy_selected_text)
        self.result_box.bind("<Button-3>",  self._show_ctx_result)
        self.result_box.bind("<Control-c>", self._copy_selected_text)
        self.result_box.bind("<Control-C>", self._copy_selected_text)

        met = self._card(self.main_frame, row=2)
        met.columnconfigure((0,1,2,3), weight=1)
        self.strength_bar = ctk.CTkProgressBar(met, height=8)
        self.strength_bar.set(0)
        self.strength_bar.grid(row=0, column=0, columnspan=4,
                               sticky="ew", padx=16, pady=(12,6))
        self._metric_widgets = {}
        self.str_lbl = self._metric(met, "metric_str", "-", 0)
        self.entropy_lbl = self._metric(met, "metric_ent", f"- {translations[self.lang_var.get()]['bits']}", 1)
        self.crack_lbl = self._metric(met, "metric_crack", "-", 2)
        self.leak_lbl = self._metric(met, "metric_leak", "-", 3)

        tpl = self._card(self.main_frame, row=3)
        cols = tk.Frame(tpl)
        cols.pack(fill="x", padx=16, pady=12)
        self._cards.append(cols)
        cols.columnconfigure((0,1), weight=1)
        lf = tk.Frame(cols)
        lf.grid(row=0, column=0, sticky="nsew", padx=(0,8))
        self._cards.append(lf)
        self.lbl_tpl = tk.Label(lf, font=FS)
        self.lbl_tpl.pack(anchor="w")
        self._labels.append((self.lbl_tpl, "muted"))
        self.tpl_entry = tk.Entry(lf, relief="flat", font=FM)
        self.tpl_entry.pack(fill="x", pady=4, ipady=4)
        self._entries.append(self.tpl_entry)
        rf = tk.Frame(cols)
        rf.grid(row=0, column=1, sticky="nsew", padx=(8,0))
        self._cards.append(rf)
        self.lbl_w = tk.Label(rf, font=FS)
        self.lbl_w.pack(anchor="w")
        self._labels.append((self.lbl_w, "muted"))
        self.words_entry = tk.Entry(rf, relief="flat", font=FM)
        self.words_entry.pack(fill="x", pady=4, ipady=4)
        self._entries.append(self.words_entry)

        btn = self._card(self.main_frame, row=4)
        bf = tk.Frame(btn)
        bf.pack(fill="x", padx=16, pady=12)
        self._cards.append(bf)
        bf.columnconfigure((0,1,2), weight=1)
        self.gen_btn = ctk.CTkButton(
            bf, height=44,
            font=ctk.CTkFont("Segoe UI", 13, weight="bold"),
            command=self.generate)
        self.gen_btn.grid(row=0, column=0, padx=(0,6), sticky="ew")
        self.btn_copy = tk.Button(bf, font=FB, relief="flat", cursor="hand2", command=self.copy_to_clipboard)
        self.btn_copy.grid(row=0, column=1, padx=3, ipady=10, sticky="ew")
        self._tk_buttons.append(self.btn_copy)
        self.btn_clear = tk.Button(bf, font=FB, relief="flat", cursor="hand2", command=self.clear_all)
        self.btn_clear.grid(row=0, column=2, padx=(6,0), ipady=10, sticky="ew")
        self._tk_buttons.append(self.btn_clear)

        self.hist_card = self._card(self.main_frame, row=5)
        self.lbl_hist = tk.Label(self.hist_card, font=FS)
        self.lbl_hist.pack(anchor="w", padx=16, pady=(10,2))
        self._labels.append((self.lbl_hist, "muted"))

        hist_wrap = tk.Frame(self.hist_card)
        hist_wrap.pack(fill="both", expand=True, padx=16, pady=(4,12))
        self._cards.append(hist_wrap)

        self.hist_box = tk.Text(hist_wrap, font=("Consolas", 11), 
                                relief="flat", wrap="none", 
                                cursor="xterm", exportselection=True,)
        self.hist_box.pack(fill="both", expand=True)
        self.hist_box.pack(side="left", fill="both", expand=True)

        self.hist_box.tag_config("hover", background="#2a3a5e")
        self.hist_box.bind("<Motion>", self._on_hist_hover)
        self.hist_box.bind("<Leave>", self._on_hist_leave)
        self.hist_box.bind("<Key>", self._block_keys_except_nav)

        self.main_frame.rowconfigure(5, weight=1)

    def _hline(self, parent):
        line = tk.Frame(parent, height=1)
        line.pack(fill="x", padx=16, pady=4)
        self._hlines.append(line)

    def _card(self, parent, row):
        c = tk.Frame(parent, highlightthickness=1)
        c.grid(row=row, column=0, sticky="nsew", pady=4)
        c.columnconfigure(0, weight=1)
        self._cards.append(c)
        return c

    def _metric(self, parent, lang_key, value, col):
        f = tk.Frame(parent)
        f.grid(row=1, column=col, padx=8, pady=(0,12), sticky="ew")
        self._cards.append(f)
        lbl_t = tk.Label(f, font=FS)
        lbl_t.pack()
        self._labels.append((lbl_t, "muted"))
        lbl_v = tk.Label(f, text=value, font=FB)
        lbl_v.pack()
        self._labels.append((lbl_v, "accent"))
        self._metric_widgets[lang_key] = (lbl_t, lbl_v)
        return lbl_v

    def _on_hist_hover(self, event):
        idx = self.hist_box.index(f"@{event.x},{event.y}")
        line_num = idx.split(".")[0]
        line_text = self.hist_box.get(f"{line_num}.0", f"{line_num}.end").strip()
        
        if not line_text:
            if self._hover_line:
                self.hist_box.tag_remove("hover", f"{self._hover_line}.0", f"{self._hover_line}.end+1c")
                self._hover_line = None
            return
        
        if line_num != self._hover_line:
            if self._hover_line:
                self.hist_box.tag_remove("hover", f"{self._hover_line}.0", f"{self._hover_line}.end+1c")
            self.hist_box.tag_add("hover", f"{line_num}.0", f"{line_num}.end+1c")
            self._hover_line = line_num

    def _on_hist_leave(self, event):
        if self._hover_line:
            self.hist_box.tag_remove("hover", f"{self._hover_line}.0", f"{self._hover_line}.end+1c")
            self._hover_line = None

    def _block_keys_except_nav(self, event):
        key = event.keysym.lower()
        char = event.char.lower()
        
        ctrl_pressed = (event.state & 0x4) != 0 or "control" in event.keysym.lower()
        if ctrl_pressed and (key in ("c", "a") or char in ("c", "с", "a", "ф")):
            return None

        if event.keysym in ("Up", "Down", "Left", "Right", "Home", "End", "Prior", "Next"):
            return None

        return "break"

    def _show_ctx_result(self, event):
        t = translations[self.lang_var.get()]
        self.ctx_result.entryconfigure(0, label=t["copy_ctx"])
        self.ctx_result.tk_popup(event.x_root, event.y_root)

    def _copy_selected_text(self, event=None):
        try:
            text = self.result_box.get("sel.first", "sel.last").strip()
        except tk.TclError:
            text = self.result_box.get("1.0", "end-1c").strip()
        if text:
            self.clipboard_clear()
            self.clipboard_append(text)
            self.update_idletasks()
            t = translations[self.lang_var.get()]
            messagebox.showinfo(t["info_title"], t["copied_selected"])
        return "break"

    def change_language(self):
        lang = self.lang_var.get()
        t    = translations[lang]

        self.title(t["title_app"])
        self.lbl1.configure(text=t["title1"])
        self.lbl2.configure(text=t["title2"])
        self.lbl_config.configure(text=t["config"])
        self.cb_theme.configure(text=t["dark_mode"])
        self.lbl_lang.configure(text=t["lang_label"])
        self.len_lbl.configure(text=f"{t['len_lbl']}{self.len_var.get()}")
        self.lbl_rec.configure(text=t["rec_lbl"])
        self.count_lbl.configure(text=f"{t['count_lbl']}{self.count_var.get()}")
        self.lbl_set.configure(text=t["set_lbl"])
        
        for key in self._cb_keys:
            self._cb_widgets[key].configure(text=f"  {t[key]}")
        self.lbl_pin_title.configure(text=t["pin_lbl"])
        self.lbl_plen.configure(text=t["pin_len"])
        self.btn_pin.configure(text=t["btn_pin"])
        self.btn_copy_pin.configure(text=t["btn_copy_pin"])
        self.lbl_res.configure(text=t["result"])
        
        for key, (lbl_t, _) in self._metric_widgets.items():
            lbl_t.configure(text=t[key])
        self.lbl_tpl.configure(text=t["tpl_lbl"])
        self.lbl_w.configure(text=t["words_lbl"])
        self.gen_btn.configure(text=t["btn_gen"])
        self.btn_copy.configure(text=t["btn_copy"])
        self.btn_clear.configure(text=t["btn_clear"])
        self.lbl_hist.configure(text=t["hist_lbl"])

        if not self.last_raw:
            self.entropy_lbl.configure(text=f"- {t['bits']}")

        if self.last_raw:
            self._update_metrics(self.last_raw[0])
        self._update_history()

    def update_theme_styles(self):
        mode = "dark" if self.theme_var.get() else "light"
        p    = palettes[mode]

        self.configure(fg_color=p["bg"])
        self.sb.configure(bg=p["panel"])
        self.pin_row.configure(bg=p["panel"])
        self.lang_frame.configure(bg=p["panel"])
        self.main_frame.configure(bg=p["bg"])
        self.hdr.configure(bg=p["bg"])

        for card in self._cards:
            card.configure(bg=p["card"])
            try:
                card.configure(highlightbackground=p["border"])
            except tk.TclError:
                pass

        for line in self._hlines:
            line.configure(bg=p["border"])

        for lbl, role in self._labels:
            try:
                lbl.configure(bg=lbl.master.cget("bg"), fg=p.get(role, p["text"]))
            except Exception:
                pass

        for entry in self._entries:
            entry.configure(bg=p["panel"], fg=p["accent"], insertbackground=p["accent"])

        self.pin_spin.configure(bg=p["card"], fg=p["accent"], buttonbackground=p["border"])

        for cb in self._checkbuttons:
            try:
                bg = cb.master.cget("bg")
                cb.configure(bg=bg, fg=p["text"], selectcolor=p["card"] if mode == "dark" else p["panel"], activebackground=bg, activeforeground=p["accent"])
            except Exception:
                pass

        for btn in self._tk_buttons:
            btn.configure(bg=p["card"], fg=p["accent"], highlightbackground=p["border"], activebackground=p["border"], activeforeground=p["accent"])

        self.result_box.configure(bg=p["card"], fg=p["green"], insertbackground=p["accent"], selectbackground=p["btn_bg"])
        self.result_box.tag_config("upper", foreground=p["purple"])
        self.result_box.tag_config("digit", foreground=p["amber"])
        self.result_box.tag_config("spec", foreground=p["red"])
        self.result_box.tag_config("lower", foreground=p["green"])

        hover_bg = "#2a3a5e" if mode == "dark" else "#c4d4f5"
        self.hist_box.configure(bg=p["card"], fg=p["text"], selectbackground=p["btn_bg"], insertbackground=p["accent"])
        self.hist_box.tag_config("hover", background=hover_bg)

        for scale in [self.len_scale, self.count_scale]:
            scale.configure(bg=p["panel"], fg=p["text"], troughcolor=p["border"], activebackground=p["accent"])

        self.strength_bar.configure(fg_color=p["border"])
        self.gen_btn.configure(fg_color=p["btn_bg"],
                               hover_color="#1e4a8a" if mode == "dark" else "#1557b0")

        if self.last_raw:
            self._update_metrics(self.last_raw[0])

    def toggle_theme(self):
        ctk.set_appearance_mode("dark" if self.theme_var.get() else "light")
        self.update_theme_styles()

    def _on_len_change(self, v):
        lang = self.lang_var.get()
        self.len_lbl.configure(
            text=f"{translations[lang]['len_lbl']}{int(float(v))}")

    def _on_count_change(self, v):
        lang = self.lang_var.get()
        self.count_lbl.configure(
            text=f"{translations[lang]['count_lbl']}{int(float(v))}")

    def _on_hide_toggle(self):
        if self._cb["hide"].get():
            self.hist_card.grid_remove()
            self.geometry(f"{self.winfo_width()}x{self.winfo_height() - 160}")
        else:
            self.hist_card.grid()
            self.geometry(f"{self.winfo_width()}x{self.winfo_height() + 160}")
        if self.last_raw:
            self._show_passwords(self.last_raw)

    def _make_password(self):
        tpl = self.tpl_entry.get().strip()
        if tpl:
            pw = ""
            for ch in tpl:
                if ch == 'L':
                    pw += random.choice(string.ascii_letters)
                elif ch == 'D':
                    pw += random.choice(string.digits)
                elif ch == 'S':
                    pw += random.choice(spec_chars)
                else:
                    pw += ch
            return pw

        if self._cb["memorable"].get():
            raw  = self.words_entry.get().strip()
            user_words = [w.strip() for w in raw.split(",") if w.strip()]
            pool = user_words if user_words else self.words_pool

            extra_words = [w for w in self.words_pool
                        if w.lower() not in {u.lower() for u in pool}]

            target_len = self.len_var.get()

            sep_pool = ""
            if self._cb["spec"].get():
                sep_pool += spec_chars
            if self._cb["digits"].get():
                sep_pool += string.digits[1:]
            if not sep_pool:
                sep_pool = "_"

            extra_pool = ""
            if self._cb["digits"].get():
                extra_pool += string.digits
            if self._cb["spec"].get():
                extra_pool += spec_chars
            if not extra_pool:
                extra_pool = string.digits

            def apply_case(w):
                if self._cb["upper"].get() and self._cb["lower"].get():
                    return w.capitalize()
                elif self._cb["upper"].get():
                    return w.upper()
                return w.lower()

            best_pw = None
            best_diff = 10**9

            for attempt in range(40):
                sep = random.choice(sep_pool)
                sep_len = len(sep)

                base = pool[:]
                random.shuffle(base)
                words = [apply_case(w) for w in base]

                base_candidate = sep.join(words)
                if len(base_candidate) > target_len:
                    words = []
                    used_len = 0
                    for w in base:
                        w2 = apply_case(w)
                        needed = len(w2) + (sep_len if words else 0)
                        if used_len + needed <= target_len:
                            words.append(w2)
                            used_len += needed
                        if used_len >= target_len:
                            break

                filler = random.sample(extra_words, min(10, len(extra_words)))
                for w in filler:
                    w2 = apply_case(w)
                    current = sep.join(words)

                    if len(current) + sep_len + len(w2) <= target_len:
                        words.append(w2)

                candidate = sep.join(words)

                while len(candidate) < target_len:
                    candidate += random.choice(extra_pool)

                candidate = candidate[:target_len]

                diff = abs(len(candidate) - target_len)
                if diff < best_diff:
                    best_diff = diff
                    best_pw = candidate
                if diff == 0:
                    break

            return best_pw

        pool = ""
        if self._cb["lower"].get():
            pool += string.ascii_lowercase
        if self._cb["upper"].get():
            pool += string.ascii_uppercase
        if self._cb["digits"].get():
            pool += string.digits
        if self._cb["spec"].get():
            pool += spec_chars
        if not pool:
            pool = string.ascii_lowercase + string.digits

        if self._cb["similar"].get():
            for c in "0OolL1iI":
                pool = pool.replace(c, "")
        if not pool:
            lang = self.lang_var.get()
            messagebox.showerror(translations[lang]["err_title"], translations[lang]["err_empty"])
            return None

        length = self.len_var.get()
        pw = list("".join(random.choice(pool) for _ in range(length)))

        required = []
        if self._cb["lower"].get():
            low_pool = string.ascii_lowercase
            if self._cb["similar"].get():
                low_pool = "".join(c for c in low_pool if c not in "0OolL1iI")
            if low_pool: required.append(random.choice(low_pool))

        if self._cb["upper"].get():
            up_pool = string.ascii_uppercase
            if self._cb["similar"].get():
                up_pool = "".join(c for c in up_pool if c not in "0OolL1iI")
            if up_pool: required.append(random.choice(up_pool))

        if self._cb["digits"].get():
            dig_pool = string.digits
            if self._cb["similar"].get():
                dig_pool = "".join(c for c in dig_pool if c not in "0OolL1iI")
            if dig_pool: required.append(random.choice(dig_pool))

        if self._cb["spec"].get():
            required.append(random.choice(spec_chars))

        positions = random.sample(range(length), min(len(required), length))
        for pos, ch in zip(positions, required):
            pw[pos] = ch

        return "".join(pw)

    def generate(self):
        passwords = []
        for _ in range(self.count_var.get()):
            pw = self._make_password()
            if pw is None:
                return
            passwords.append(pw)
            if pw not in self.history:
                self.history.append(pw)
        self.last_raw = passwords
        self._animate_then_show(passwords)

    def _animate_then_show(self, passwords):
        if self._anim_running:
            return
        target = passwords[0] if passwords else ""
        def run():
            self._anim_running = True
            for _ in range(8):
                fake = "".join(random.choice(self._anim_chars)
                               for _ in range(len(target)))
                self.after(0, lambda f=fake: self._write_fake(f))
                time.sleep(0.04)
            self.after(0, lambda: self._finalize(passwords))
        threading.Thread(target=run, daemon=True).start()

    def _write_fake(self, text):
        self.result_box.delete("1.0", "end")
        self.result_box.insert("end", text)

    def _finalize(self, passwords):
        self._anim_running = False
        self._show_passwords(passwords)
        self._update_metrics(passwords[0])
        self._update_history()

    def _show_passwords(self, passwords):
        self.result_box.delete("1.0", "end")
        for idx, pw in enumerate(passwords):
            if self._cb["hide"].get():
                self.result_box.insert("end", "*" * len(pw))
            else:
                for ch in pw:
                    if ch.isdigit():
                        tag = "digit"
                    elif ch in spec_chars+"_":
                        tag = "spec"
                    elif ch.isupper():
                        tag = "upper"
                    else:
                        tag = "lower"
                    self.result_box.insert("end", ch, tag)
            if idx < len(passwords) - 1:
                self.result_box.insert("end", "\n")

    def _update_history(self):
        self.hist_box.configure(state="normal")
        self.hist_box.delete("1.0", "end")
        for i, pw in enumerate(self.history, start=1):
            line = f"{i}. " + ("*" * len(pw) if self._cb["hide"].get() else pw)
            self.hist_box.insert("end", line + "\n")
        self.hist_box.configure(state="disabled")

    def _update_metrics(self, password):
        if not password:
            return
        lang = self.lang_var.get()
        t = translations[lang]
        mode = "dark" if self.theme_var.get() else "light"
        p = palettes[mode]

        pool_size = 0
        if any(c.islower() for c in password):
            pool_size += 26
        if any(c.isupper() for c in password):
            pool_size += 26
        if any(c.isdigit() for c in password):
            pool_size += 10
        if any(c in spec_chars for c in password):
            pool_size += len(spec_chars)
        if pool_size == 0:
            pool_size = 1

        entropy = len(password) * math.log2(pool_size)
        self.entropy_lbl.configure(text=f"{int(entropy)} {t['bits']}")

        is_weak = password.lower() in weak_passwords_norm
        if is_weak:
            self.strength_bar.set(0.1)
            self.strength_bar.configure(progress_color=p["red"])
            self.str_lbl.configure(text=t["str_weak"],  fg=p["red"])
            self.crack_lbl.configure(text=t["instantly"])
            self.leak_lbl.configure(text=t["found"],    fg=p["red"])
        else:
            self.leak_lbl.configure(text=t["clean"], fg=p["green"])
            if entropy < 40:
                self.strength_bar.set(0.25)
                self.strength_bar.configure(progress_color=p["red"])
                self.str_lbl.configure(text=t["str_weak"], fg=p["red"])
                self.crack_lbl.configure(text=f"~5 {t['minutes']}")
            elif entropy < 60:
                self.strength_bar.set(0.5)
                self.strength_bar.configure(progress_color=p["amber"])
                self.str_lbl.configure(text=t["str_avg"], fg=p["amber"])
                self.crack_lbl.configure(text=f"~2 {t['days']}")
            elif entropy < 80:
                self.strength_bar.set(0.75)
                self.strength_bar.configure(progress_color=p["accent"])
                self.str_lbl.configure(text=t["str_good"], fg=p["accent"])
                self.crack_lbl.configure(text=f"~12 {t['years']}")
            else:
                self.strength_bar.set(1.0)
                self.strength_bar.configure(progress_color=p["green"])
                self.str_lbl.configure(text=t["str_exc"], fg=p["green"])
                self.crack_lbl.configure(text=t["crack_impossible"])

    def copy_to_clipboard(self):
        lang = self.lang_var.get()
        t = translations[lang]

        try:
            selected = self.hist_box.get("sel.first", "sel.last").strip()
        except tk.TclError:
            selected = ""

        if selected:
            self.clipboard_clear()
            self.clipboard_append(selected)
            self.update_idletasks()
            messagebox.showinfo(t["info_title"], t["copied_selected"])
            return

        if not self.last_raw:
            messagebox.showwarning(t["warn_title"], t["warn_gen"])
            return

        text = "\n".join(self.last_raw)
        self.clipboard_clear()
        self.clipboard_append(text)
        self.update_idletasks()

        count = len(self.last_raw)
        if lang == "ru":
            if count % 10 == 1 and count % 100 != 11:
                key = "info_copied"
            elif 2 <= count % 10 <= 4 and (count % 100 < 10 or count % 100 >= 20):
                key = "info_copied_few"
            else:
                key = "info_copied_many"
            msg = f"{count} {t[key]}"
        else:
            key = "info_copied" if count == 1 else "info_copied_many"
            msg = f"{count} {t[key]}"
        messagebox.showinfo(t["info_title"], msg)

    def _gen_pin(self):
        n = self.pin_len.get()
        digits = "".join(random.choice(string.digits) for _ in range(n))
        if n == 4:
            formatted = digits[:2] + "-" + digits[2:]
        elif n == 6:
            formatted = digits[:3] + "-" + digits[3:]
        elif n == 8:
            formatted = digits[:4] + "-" + digits[4:]
        elif n == 10:
            formatted = digits[:5] + "-" + digits[5:]
        elif n == 12:
            formatted = digits[:6] + "-" + digits[6:]
        else:
            formatted = digits
        self.pin_out.configure(text=formatted)

    def copy_pin_to_clipboard(self):
        pin  = self.pin_out.cget("text").strip()
        lang = self.lang_var.get()
        t = translations[lang]
        if not pin:
            messagebox.showwarning(t["warn_title"], t["warn_pin_empty"])
            return
        self.clipboard_clear()
        self.clipboard_append(pin)
        self.update_idletasks()
        messagebox.showinfo(t["pin_copied_title"], t["pin_copied_msg"])

    def clear_all(self):
        self.result_box.delete("1.0", "end")
        self.history.clear()
        self.last_raw.clear()
        self._update_history()
        lang = self.lang_var.get()
        t = translations[lang]
        self.entropy_lbl.configure(text=f"- {t['bits']}")
        self.str_lbl.configure(text="-")
        self.crack_lbl.configure(text="-")
        self.leak_lbl.configure(text="-")
        self.strength_bar.set(0)
        self.pin_out.configure(text="")

if __name__ == "__main__":
    app = passwordgenerator()
    app.mainloop()