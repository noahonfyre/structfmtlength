def main():
    print("Not all types are currently supported.")
    print("Please check the source code for a detailed list of supported types.")
    print()
    print("Byte order and pad bytes can be omitted in the input, they are ignored nevertheless.")
    data: str = input("Enter format: ")

    length: int = 0
    str_length_var_string: str = ""

    for char in data:
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
                length += int(str_length_var_string)
                str_length_var_string = ""
            case _:
                if char.isdigit():
                    str_length_var_string += char
                else:
                    length += 0

    print(f"Length: {length}")


if __name__ == "__main__":
    main()