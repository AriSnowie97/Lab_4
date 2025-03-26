import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.expression = ""
        self.entry = tk.Entry(master, width=20, font=("Arial", 16), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        buttons = [
            '7',  '8',  '9',  '/',
            '4',  '5',  '6',  '*',
            '1',  '2',  '3',  '-',
            'C',  '0',  '=',  '+'
        ]
        row = 1
        col = 0
        for button_text in buttons:
            tk.Button(master, text=button_text, width=5, font=("Arial", 16), command=lambda x=button_text: self.on_button(x)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button(self, button):
        if button == '=':
            try:
                result = eval(self.expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                self.expression = str(result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
        elif button == 'C':
            self.expression = ""
            self.entry.delete(0, tk.END)
        else:
            self.expression += button
            self.entry.insert(tk.END, button)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
