import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import main

class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self)
        self.wm_title("Program do sprawdzania testów")
        container = tk.Frame(self, height=600, width=950)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.logic = args[0]

        self.logic.testing()

        self.frames = {}

        for F in (MainPage, AddTestPage):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.selected_folder = ""
        self.ans_values = []

        dropdown_values = list(controller.logic.config.keys())
        print(dropdown_values)
        
        check_test_window_button = ttk.Button(
            self, text="Sprawdź test", command=lambda: controller.show_frame(MainPage)
        )
        check_test_window_button.grid(row=0,column=0)
        add_test_window_button = ttk.Button(
            self, text="Dodaj test", command=lambda: controller.show_frame(AddTestPage)
        )
        add_test_window_button.grid(row=0, column=1)


        label = tk.Label(self, text="Sprawdź test", font=("Arial", 30))
        label.grid(row=1, column=0, columnspan=2,padx=10)

        clicked = StringVar()
        clicked.set(dropdown_values[0])

        dropdown_label = ttk.Label(
            self, text="Wybierz test:"
        )
        dropdown_label.grid(row=3, column=0,padx=10)
        option_choosen = StringVar()

        dropdown = ttk.OptionMenu(
            self, option_choosen, None, *dropdown_values
        )
        dropdown.grid(row=3, column=1, columnspan=1, padx=10)
        
        self.result_text = ScrolledText(self, )
        self.result_text.grid(row=2,column=8, columnspan=2, rowspan=5, padx=15)
        

        print(self.ans_values)
        #ans_dir_label = ttk.Label(
        #    self, text="Wybierz folder z odpowiedziami uczniów"
        #)
        #ans_dir_label.grid(row=4, column=0)

        
        #ans_dir_dialogue = ttk.Button(
        #    self, text="Wybierz", command=lambda: self.ask_directory()
        #)
        #ans_dir_dialogue.grid(row=4,column=1)

        check_test_button = ttk.Button(
            self, text="Sprawdź", command=lambda: self.check(option_choosen.get())
        )
        check_test_button.grid(row=4, column=0, columnspan=2)

    def ask_directory(self):
        self.selected_folder = filedialog.askdirectory()
        print(self.selected_folder)
        return self.selected_folder
    def check(self,filename):
        self.result_text.config(state=NORMAL)
        self.ans_values = (self.controller.logic.check_answers(filename))
        _counter = 1
        self.result_text.delete('1.0', END)
        for x in self.ans_values:
            self.result_text.insert('insert', "Odpowiedzi ucznia nr {} \n Ilość poprawnych odpowiedzi: {} \n Ilość niepoprawnych odpowiedzi: {} \n Procent poprawnych odpowiedzi: {} \n".format(str(_counter), x[0], x[1], x[2]))
            _counter += 1
        self.result_text.config(state=DISABLED)
        
class AddTestPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        check_test_window_button = ttk.Button(
            self, text="Sprawdź test", command=lambda: controller.show_frame(MainPage)
        )
        check_test_window_button.grid(row=0,column=0)
        add_test_window_button = ttk.Button(
            self, text="Dodaj test", command=lambda: controller.show_frame(AddTestPage)
        )
        add_test_window_button.grid(row=0, column=1)
        label = tk.Label(self, text="Dodaj test", font=("Arial", 30))
        label.grid(row=1, column=0, columnspan=2, padx=10)

        aa_label = tk.Label(self, text="Podaj nazwe testu")
        aa_label.grid(row=3, column=0)
        aa_entry = tk.Entry(self)
        aa_entry.grid(row=3,column=1)
        ab_label = tk.Label(self, text="Wybierz prawidłowe odpowiedzi")
        ab_label.grid(row=4, column=0)
        ab_dir = tk.Button(self, text="Wybierz", command=lambda: self.ask_file())
        ab_dir.grid(row=4,column=1)
        ac_label = tk.Label(self, text="Wybierz folder z odpowiedziami ucznia")
        ac_label.grid(row=5, column=0)
        ac_dir = tk.Button(self, text="Wybierz", command=lambda: self.ask_directory())
        ac_dir.grid(row=5, column=1)

        ad_button = tk.Button(self, text="Dodaj test", command=lambda: self.save_test())


    def ask_directory(self):
        self.selected_folder = filedialog.askdirectory()
        print(self.selected_folder)
        return self.selected_folder

    def ask_file(self):
        self.selected_file = filedialog.askopenfile()
        print(self.selected_file)
        return self.selected_file

    def save_test(self):
        

if __name__ == '__main__':
    logic = main.App()
    app = GUI(logic)
    app.geometry("950x600")
    app.mainloop()