import requests
from yarl import URL
from typing import Optional

from ..const import OSRS_URL, PlayerAccountType, SKILLS
from .skill import Skill

# TODO: add bosses and stuff


class Player(object):
    def __init__(self, username: str) -> None:
        self.username = username
        self.rank = -1
        self.total_level = -1
        self.total_xp = -1
        self.account_url = None
        self.account_type = self._get_account_type()
        self.skills = {}
        self.update()

    def update(self) -> None:
        blob = self._get_data()
        self._set_data(blob)

    def _get_data(self) -> str:
        try:
            resp = requests.get(self.account_url)
            resp.raise_for_status()
            return resp.text
        except requests.HTTPError as e:
            raise e

    def _set_data(self, blob: str) -> None:
        data = blob.split("\n")
        self.rank, self.total_level, self.total_xp = map(int, data[0].split(","))

        skills = {}
        for i, name in enumerate(SKILLS, start=1):
            skill_data = list(map(int, data[i].split(",")))
            skills[name] = Skill(name, skill_data[0], skill_data[2])
        self.skills = skills
        return

    def _get_account_type(self) -> Optional[PlayerAccountType]:
        for acctype in PlayerAccountType:
            try:
                acc_url = URL(OSRS_URL) / acctype.value % {"player": self.username}
                resp = requests.get(acc_url)
                resp.raise_for_status()
                self.account_url = acc_url
                return acctype
            except requests.HTTPError as e:
                raise e
        return None

    def __str__(self) -> str:
        return (
            self.__repr__() + "\n" + "\n".join(str(sk) for _, sk in self.skills.items())
        )

    def __repr__(self) -> str:
        return (
            "Player("
            f"username={self.username},"
            f"account_type={self.account_type.name},"
            f"rank={self.rank},"
            f"total_level={self.total_level},"
            f"total_xp={self.total_xp}"
            ")"
        )
