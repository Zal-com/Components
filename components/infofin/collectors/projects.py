import requests

from src.components import Collector


class InfofinProjectsCollector(Collector):
    def run(self):
        data = requests.get(
            "https://infofin.ulb.be/api/projects"
        ).json()

        return data