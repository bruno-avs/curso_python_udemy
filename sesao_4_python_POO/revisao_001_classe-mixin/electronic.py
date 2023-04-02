from log import LogPrintMixin


class Electronic:
    def __init__(self, name) -> None:
        self._name = name
        self._its_on = False

    def turn_on(self):
        if not self._its_on:
            self._its_on = True

    def turn_off(self):
        if self._its_on:
            self._its_on = False


class Smartphone(Electronic, LogPrintMixin):
    def turn_on(self):
        super().turn_on()

        if self._its_on:
            msg = f"the smartphone {self._name} has been turned on"
            self.log_info(msg)

    def turn_off(self):
        super().turn_off()

        if not self._its_on:
            msg = f"the smartphone {self._name} has been turned off"
            self.log_info(msg)
