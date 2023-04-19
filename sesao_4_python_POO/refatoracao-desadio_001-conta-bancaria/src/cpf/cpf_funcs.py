from random import randint
from src.cpf.tax_region import Regions
import re


def generate_check_digit(CPF_sequence: str, start: int) -> str:
    total: int = 0
    for index, multiplier in enumerate(range(start, 1, -1)):
        total += multiplier * int(CPF_sequence[index])

    formula_result = 11 - (total % 11)
    return str(formula_result) if formula_result < 10 else "0"


def generate_first_check_digit(CPF_without_check_digits: str) -> str:
    return generate_check_digit(CPF_without_check_digits, start=10)


def generate_second_check_digit(CPF_with_first_digit: str) -> str:
    return generate_check_digit(CPF_with_first_digit, start=11)


def cpf_is_valid(CPF: str) -> bool:
    cpf_regex = re.compile(r"\D")

    cpf_under_review = cpf_regex.sub("", CPF)

    if len(cpf_under_review) != 11:
        return False

    if cpf_under_review == cpf_under_review[::-1]:
        return False

    first_nine_digits = cpf_under_review[:9]
    previous_first_check_digit = cpf_under_review[-2]
    previous_second_check_digit = cpf_under_review[-1]

    new_first_check_digit = generate_first_check_digit(cpf_under_review)

    if new_first_check_digit != previous_first_check_digit:
        return False

    cpf_with_first_check_digit = first_nine_digits + new_first_check_digit

    new_second_check_digit = generate_second_check_digit(
        cpf_with_first_check_digit)

    if new_second_check_digit != previous_second_check_digit:
        return False
    return True


def generate_cpf(tax_region: Regions) -> str:
    if not isinstance(tax_region, Regions):
        raise TypeError(
            'The "tax region" parameter must be an instance of regions')

    while True:
        first_nine_digits = str(randint(10000000, 99999999))

        if first_nine_digits != first_nine_digits[::-1]:
            break

    tax_region_digit = tax_region.value
    first_nine_digits = first_nine_digits + str(tax_region_digit)

    first_check_digits = generate_first_check_digit(first_nine_digits)

    cpf_with_first_check_digit = first_nine_digits + first_check_digits

    second_check_digit = generate_second_check_digit(
        cpf_with_first_check_digit)

    generated_cpf = cpf_with_first_check_digit + second_check_digit

    cpf_formatting_regex = re.compile(
        r"([0-9]{3})([0-9]{3})([0-9]{3})([0-9]{2})")

    cpf_formatting = cpf_formatting_regex.search(generated_cpf)

    if cpf_formatting is None:
        return generated_cpf

    generated_cpf = \
        f"{cpf_formatting.group(1)}." \
        f"{cpf_formatting.group(2)}." \
        f"{cpf_formatting.group(3)}-" \
        f"{cpf_formatting.group(4)}"

    return generated_cpf
