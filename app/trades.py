from models.models_main import Trade


class GeneratorTrades:
    def __init__(self, trade: Trade):
        self.active = trade.active
        self.repetition = trade.repetition

    def verify_if_active_exists(self, active: str) -> bool:
        list_active = active.split(",")

        for iten in list_active:
            with open("ativos.txt", "r") as arquive:
                if iten not in arquive:
                    return False
        return True
