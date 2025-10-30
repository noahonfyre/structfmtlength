import tkinter as tk


def calculate(fmt: str) -> int:
    var_sizes: set[str] = {"s", "p"}
    sizes: dict[str, int] = {
        "c": 1,
        "b": 1,
        "B": 1,
        "?": 1,
        "h": 2,
        "H": 2,
        "e": 2,
        "i": 4,
        "I": 4,
        "l": 4,
        "L": 4,
        "f": 4,
        "q": 8,
        "Q": 8,
        "d": 8,
        "F": 8,
        "D": 16,
    }

    length: int = 0
    buffer: str = ""

    for char in fmt:
        if char.isdigit():
            buffer += char
            continue

        if char in var_sizes:
            length += int(buffer or 0)
            buffer = ""
        elif char in sizes:
            length += sizes[char]

    return length


def update(*_) -> None:
    fmt: str = input_variable.get()
    text: str = str(calculate(fmt))
    output_variable.set(text)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("structformatlength")
    root.resizable(False, False)

    root.option_add("*font", "Arial 16")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    input_variable = tk.StringVar()
    input_entry = tk.Entry(root, justify="center", textvariable=input_variable)
    input_entry.grid(sticky="nsew", ipadx=20, ipady=10)

    input_variable.trace("w", update)

    output_variable = tk.StringVar()
    output_entry = tk.Entry(root, justify="center", state="readonly", textvariable=output_variable)
    output_entry.grid(sticky="nsew", ipadx=20, ipady=10)

    output_variable.set("0")

    root.mainloop()
