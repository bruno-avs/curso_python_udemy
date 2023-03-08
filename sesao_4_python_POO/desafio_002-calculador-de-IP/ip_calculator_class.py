from sub_class import IPConfig
from typing import Union
import re


class IPCalculator:
    def __init__(self) -> None:
        self.__method_access_modifier = False

    @staticmethod
    def _converter_to_binary(ip: str) -> str:
        ip_sets = ip.split(".")

        ip_in_binary = ""
        for ip_set in ip_sets:
            binary = ''
            ip_set = int(ip_set)

            while ip_set > 0:
                binary += str(ip_set % 2)
                ip_set //= 2

            ip_in_binary += f"{binary:0<8}"[::-1]
        return ip_in_binary

    @staticmethod
    def _converter_to_decimal(binary_sequence: str):

        binary_conversion_table = (128, 64, 32, 16, 8, 4, 2, 1)
        decimal_sequence = ''
        decimal = 0
        counter = 0
        for bi in binary_sequence:
            if int(bi) == 1:
                decimal += binary_conversion_table[counter]
                counter += 1

            elif int(bi) == 0:
                decimal += 0
                counter += 1

            if counter == 8:
                decimal_sequence += str(decimal) + "."
                counter = 0
                decimal = 0
        return decimal_sequence[0:-1]

    @staticmethod
    def _calc_mask_in_binary(prefix: str) -> str:
        mask_in_binary = f"{'1' * int(prefix):0<32s}"
        return mask_in_binary

    @staticmethod
    def _calc_n_ips(mask_in_binary: str) -> str:
        bits_for_hosts = mask_in_binary.count("0")
        return str((2 ** bits_for_hosts) - 2)

    @staticmethod
    def _calc_network_ip_in_binary(
            ip_in_binary: str,
            mask_in_binary: str
    ) -> str:
        bits_for_hosts = mask_in_binary.count("0")

        ip_without_host_bits = ip_in_binary[0:-bits_for_hosts]
        new_host_bits = "0" * bits_for_hosts

        return ip_without_host_bits + new_host_bits

    @staticmethod
    def _calc_broadcast_in_binary(ip_in_binary: str, mask_in_binary: str):
        bits_for_hosts = mask_in_binary.count("0")

        ip_without_host_bits = ip_in_binary[0:-bits_for_hosts]
        new_host_bits = "1" * bits_for_hosts

        return ip_without_host_bits + new_host_bits

    @staticmethod
    def _calc_first_ip(network_ip: str) -> str:
        key = network_ip.rfind(".")

        net_address = network_ip[:key]

        host_address = network_ip[(key + 1):]

        first_ip = f"{net_address}.{int(host_address) + 1}"

        return first_ip

    @staticmethod
    def _calc_last_ip(broadcast_ip: str) -> str:
        key = broadcast_ip.rfind(".")

        net_address = broadcast_ip[:key]
        host_address = broadcast_ip[(key + 1):]

        last_ip = f"{net_address}.{int(host_address) - 1}"

        return last_ip

    @staticmethod
    def _check_values(
            ip: str,
            mask: Union[str] = "",
            prefix: Union[str, int] = ""
    ):
        regex_check = re.compile(r"^([\d]{1,3}).([\d]{1,3}).([\d]{1,3}).([\d]{1,3})$")
        is_ip = regex_check.search(ip)
        is_mask = regex_check.search(mask)

        if not is_ip:
            print(f'{ip} não é um IPv4 valido!!.')
            return False

        if not mask and not prefix:
            print("Por favor informe a mascara ou o prefixo")
            return False

        if not prefix.isnumeric():
            print(f"{prefix} não é um prefixo valido!!.")
            return False

        if not is_mask and not mask:
            print(f"{mask} não é um mascara valido!!.")
            return False

        return True

    def calculate_ip(
            self,
            ip: str,
            mask: Union[str] = "",
            prefix: Union[str, int] = ""
    ):
        if self._check_values(ip, mask, prefix):
            return

        self.__method_access_modifier = True

        ip_in_binary = self._converter_to_binary(ip)

        mask_in_binary = self._calc_mask_in_binary(prefix)
        rede_in_binary = self._calc_network_ip_in_binary(ip_in_binary, mask_in_binary)
        broadcast_in_binary = self._calc_broadcast_in_binary(ip_in_binary, mask_in_binary)

        mask = self._converter_to_decimal(mask_in_binary)
        rede_ip = self._converter_to_decimal(rede_in_binary)
        broadcast = self._converter_to_decimal(broadcast_in_binary)

        n_ips = self._calc_n_ips(mask_in_binary)
        first_ip = self._calc_first_ip(rede_ip)
        last_ip = self._calc_last_ip(broadcast)

        self.__method_access_modifier = False

        return IPConfig(ip, prefix, mask, rede_ip, broadcast, first_ip, last_ip, n_ips)
