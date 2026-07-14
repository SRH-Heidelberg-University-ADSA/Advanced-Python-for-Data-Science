import requests


class Stackoverflow:

    BASE_URL = "https://api.stackexchange.com/2.3"

    def get_questions(self, tag: str, count: int = 5) -> list[dict]:

        url = f"{self.BASE_URL}/questions"
        params = {
            "order": "desc",
            "sort": "votes",
            "tagged": tag,
            "site": "stackoverflow",
            "pagesize": count,
        }

        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        return response.json()["items"]


st = Stackoverflow()
print(st.get_questions("python"))
