import tkinter as tk
from tkinter import ttk
from random import choice

READINGS = [
    {
        "sign": "The Aurora of Momentum",
        "title": "Action will open the door",
        "text": "Your next steps are not meant to be perfect. The cosmos favors courage, timing, and a willingness to move before certainty arrives.",
    },
    {
        "sign": "Moonlit Alignment",
        "title": "Trust the quiet signal",
        "text": "The answer is already present, but it speaks softly. Pause, listen, and follow the thread that brings calm instead of noise.",
    },
    {
        "sign": "The Crown of Renewal",
        "title": "A new chapter is forming",
        "text": "Release what has already finished its work. This cycle is ending so that a more luminous path can emerge with clarity.",
    },
    {
        "sign": "Solar Flame",
        "title": "Confidence will sharpen your direction",
        "text": "You do not need every answer before stepping forward. The next move becomes clear when your intention is sincere and steady.",
    },
    {
        "sign": "The Horizon Watcher",
        "title": "Patience is part of the magic",
        "text": "Some truths arrive only after the dust settles. Continue with integrity, and the right opportunity will reveal itself in its own season.",
    },
]


class CosmicOracleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cosmic-Oracle")
        self.root.geometry("820x620")
        self.root.minsize(760, 560)
        self.root.configure(bg="#060914")

        self._build_ui()
        self._set_default_reading()

    def _build_ui(self):
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        shell = tk.Frame(self.root, bg="#060914")
        shell.grid(row=0, column=0, sticky="nsew", padx=22, pady=22)
        shell.columnconfigure(0, weight=1)
        shell.rowconfigure(1, weight=1)

        title_bar = tk.Frame(shell, bg="#0b1128", bd=0)
        title_bar.grid(row=0, column=0, sticky="ew", pady=(0, 16))
        title_bar.columnconfigure(0, weight=1)

        title_label = tk.Label(
            title_bar,
            text="✦ Cosmic-Oracle",
            bg="#0b1128",
            fg="#f4d7ff",
            font=("Segoe UI", 18, "bold"),
            anchor="w",
            padx=18,
            pady=14,
        )
        title_label.grid(row=0, column=0, sticky="ew")

        inner = tk.Frame(shell, bg="#0d132b", bd=0)
        inner.grid(row=1, column=0, sticky="nsew")
        inner.columnconfigure(0, weight=1)
        inner.rowconfigure(0, weight=0)
        inner.rowconfigure(1, weight=1)

        intro = tk.Frame(inner, bg="#111a35", padx=20, pady=20)
        intro.grid(row=0, column=0, sticky="ew", pady=(0, 18))
        intro.columnconfigure(0, weight=1)

        intro_label = tk.Label(
            intro,
            text="Ask the stars for clarity.",
            bg="#111a35",
            fg="#ebecff",
            font=("Segoe UI", 22, "bold"),
            anchor="w",
        )
        intro_label.grid(row=0, column=0, sticky="ew")

        subtext = tk.Label(
            intro,
            text="Seek direction, trust your rhythm, and receive a glowing omen for your next step.",
            bg="#111a35",
            fg="#b9c4ff",
            font=("Segoe UI", 11),
            wraplength=660,
            justify="left",
            anchor="w",
        )
        subtext.grid(row=1, column=0, sticky="ew", pady=(8, 0))

        ask_section = tk.Frame(inner, bg="#0d132b")
        ask_section.grid(row=1, column=0, sticky="nsew")
        ask_section.columnconfigure(0, weight=1)

        question_label = tk.Label(
            ask_section,
            text="Your question",
            bg="#0d132b",
            fg="#e8dfff",
            font=("Segoe UI", 11, "bold"),
            anchor="w",
        )
        question_label.grid(row=0, column=0, sticky="w", padx=8, pady=(0, 6))

        self.question_var = tk.StringVar()
        self.question_entry = tk.Text(
            ask_section,
            width=1,
            height=4,
            bg="#171f3f",
            fg="#f3ecff",
            insertbackground="#f3ecff",
            bd=0,
            relief="flat",
            highlightthickness=1,
            highlightbackground="#3d4f93",
            wrap="word",
            font=("Segoe UI", 11),
        )
        self.question_entry.grid(row=1, column=0, sticky="ew", padx=8, pady=(0, 12))

        button_row = tk.Frame(ask_section, bg="#0d132b")
        button_row.grid(row=2, column=0, sticky="ew", padx=8)
        button_row.columnconfigure(0, weight=1)

        self.ask_button = ttk.Button(
            button_row,
            text="Consult the cosmos",
            command=self.ask_cosmos,
        )
        self.ask_button.grid(row=0, column=0, sticky="w")

        reading_panel = tk.Frame(inner, bg="#101935", padx=18, pady=18)
        reading_panel.grid(row=2, column=0, sticky="nsew", pady=(18, 0))
        reading_panel.columnconfigure(0, weight=1)
        reading_panel.rowconfigure(0, weight=1)

        self.sign_label = tk.Label(
            reading_panel,
            text="The Veil of Possibility",
            bg="#101935",
            fg="#7fe0ff",
            font=("Segoe UI", 10, "bold"),
            anchor="w",
        )
        self.sign_label.grid(row=0, column=0, sticky="w")

        self.title_label = tk.Label(
            reading_panel,
            text="Awaiting your question",
            bg="#101935",
            fg="#fef7ff",
            font=("Segoe UI", 20, "bold"),
            justify="left",
            anchor="w",
            wraplength=700,
        )
        self.title_label.grid(row=1, column=0, sticky="ew", pady=(10, 8))

        self.text_label = tk.Label(
            reading_panel,
            text="The stars are listening. Ask the cosmos a question and the oracle will reveal the next guiding thread.",
            bg="#101935",
            fg="#dfe6ff",
            font=("Segoe UI", 11),
            justify="left",
            anchor="w",
            wraplength=700,
        )
        self.text_label.grid(row=2, column=0, sticky="ew")

        self.question_entry.focus_set()

    def _set_default_reading(self):
        self.sign_label.config(text="The Veil of Possibility")
        self.title_label.config(text="Awaiting your question")
        self.text_label.config(
            text="The stars are listening. Ask the cosmos a question and the oracle will reveal the next guiding thread."
        )

    def ask_cosmos(self):
        question = self.question_entry.get("1.0", "end").strip()
        if not question:
            self.question_entry.focus_set()
            self.question_entry.delete("1.0", "end")
            self.question_entry.insert("1.0", "Ask a question before the stars answer.")
            return

        reading = choice(READINGS)
        focus_word = " ".join(question.split()[:2])
        self.sign_label.config(text=reading["sign"])
        self.title_label.config(text=f"{reading['title']} for {focus_word}")
        self.text_label.config(
            text=(
                f"{reading['text']} Your question, \"{question}\", is being carried by a current of possibility and personal growth."
            )
        )
        self.question_entry.delete("1.0", "end")


def main():
    root = tk.Tk()
    app = CosmicOracleApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
