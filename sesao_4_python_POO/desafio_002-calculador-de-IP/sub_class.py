class IPConfig:
    def __init__(
            self,
            ip: str,
            prefix: str,
            mask: str,
            rede_ip: str,
            broadcast: str,
            first_ip: str,
            last_ip: str,
            n_ips: str,
    ) -> None:
        self.IP = ip
        self.prefix = prefix
        self.mask = mask
        self.rede_ip = rede_ip
        self.broadcast = broadcast
        self.first_ip = first_ip
        self.last_ip = last_ip
        self.n_ips = n_ips



