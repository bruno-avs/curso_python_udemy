def split(string: str, sep: str | None = None, maxsplit: int = -1) -> list[str]:
    if not isinstance(string, str):
        raise ValueError()

    separator: str = " "
    if sep is not None:
        if not isinstance(sep, str):
            raise ValueError()
        separator = sep

    counter: int = 0
    curr_index_value: str = ""
    splitted_value_list: list = []

    for c in string:
        if maxsplit != -1:
            if counter >= maxsplit:
                break

        if c == separator:
            splitted_value_list.append(curr_index_value)
            curr_index_value = ""
            continue

        curr_index_value += c

    if len(splitted_value_list) == 0:
        splitted_value_list.append(curr_index_value)

    return splitted_value_list


print(split("hello my name is Bruno."))
