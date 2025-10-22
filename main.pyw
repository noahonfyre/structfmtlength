import tkinter as tk


def calculate(fmt: str) -> int:
    length: int = 0
    n: str = ""

    for char in fmt:
        match char:
            case "c": length += 1
            case "b": length += 1
            case "B": length += 1
            case "?": length += 1
            case "h": length += 2
            case "H": length += 2
            case "i": length += 4
            case "I": length += 4
            case "l": length += 4
            case "L": length += 4
            case "q": length += 8
            case "Q": length += 8
            case "e": length += 2
            case "f": length += 4
            case "d": length += 8
            case "F": length += 8
            case "D": length += 16
            case "s":
                length += int(n)
                n = ""
            case _:
                if char.isdigit():
                    n += char
                else:
                    length += 0

    return length


def update(*_) -> None:
    fmt = input_variable.get()
    output_variable.set(str(calculate(fmt)))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("structformatlength")
    root.resizable(False, False)

    root.option_add("*font", "Arial 18")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    input_variable = tk.StringVar()
    input_entry = tk.Entry(root, justify="center", textvariable=input_variable)
    input_entry.grid(sticky="ew", ipadx=20, ipady=10)

    input_variable.trace("w", update)

    output_variable = tk.StringVar()
    output_entry = tk.Entry(root, justify="center", state="readonly", textvariable=output_variable)
    output_entry.grid(sticky="ew", ipadx=20, ipady=10)

    output_variable.set("0")

    root.mainloop()
