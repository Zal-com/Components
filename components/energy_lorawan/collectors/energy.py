from src.components import Collector
import requests


class EnergyCollector(Collector):
    def run(self) -> dict:
        response = requests.get(
            "http://el-api.sc.ulb.ac.be/energy"
        )

        return response.json()
