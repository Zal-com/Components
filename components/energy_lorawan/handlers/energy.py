from src.components import Handler
from src.data.retrieve import retrieve_first_row


class EnergyHandler(Handler):
    def run(self):
        datas = retrieve_first_row(self.get_table_by_name("energy_lorawan_energy"))

        if not datas:
            return {"error": "No data found"}

        return [item.data for item in datas]
