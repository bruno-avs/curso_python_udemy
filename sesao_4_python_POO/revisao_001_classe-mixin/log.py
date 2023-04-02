import pathlib


# my abstract class example
class Log:
    def _log(self, msg):
        raise NotImplementedError(
            f"Log method not implemented in {self.__class__.__name__}")

    def log_error(self, msg):
        return self._log(f"[ERROR]: {msg}")

    def log_info(self, msg):
        return self._log(f"[INFO]: {msg}")


class LogFileMixin(Log):
    def _log(self, msg):
        LOG_FILE_PATH = pathlib.Path(__file__).parent / "log_file.log"

        with open(LOG_FILE_PATH, "a", encoding="utf-8") as file:
            file.write(msg)
            file.write("\n")


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")


if __name__ == "__main__":
    lf = LogFileMixin()
    lf.log_error("an error has occurred")
    lf.log_info("successfully executed")

    lp = LogPrintMixin()
    lp.log_error("an error has occurred")
    lp.log_info("successfully executed")
