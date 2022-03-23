from models.models_main import Trade


class GeneratorTrades:
    def __init__(self, trade: Trade):
        self.active = trade.active
        self.repetition = trade.repetition

    def verify_if_active_exists(self, active: str) -> bool:
        try:
            list_active: list = active.replace(" ", "").split(",")

            list_formatted = []

            with open("ativos.txt", "r") as arquive:
                actives_txt = arquive.readlines()
            for iten_txt in actives_txt:
                list_formatted.append(iten_txt.replace("\n", ""))

            print(list_formatted)

            for iten in list_active:
                if iten not in list_formatted:
                    return False
            return True
        except AttributeError:
            return False
