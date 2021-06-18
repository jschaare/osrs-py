from bisect import bisect_left

from ..const import XP_PER_LEVEL


class Skill(object):
    def __init__(self, name: str, rank: int, xp: int) -> None:
        self.name = name
        self.rank = rank
        self.xp = xp

    @property
    def level(self) -> int:
        if self.xp == 0:
            return 1
        elif self.xp > XP_PER_LEVEL[-1]:
            return 99

        level = bisect_left(XP_PER_LEVEL, self.xp)
        if self.xp < XP_PER_LEVEL[level]:
            return level
        return level + 1

    def xp_to_level(self, level: int) -> int:
        curlvl = self.level
        if level < curlvl or level > 99:
            return 0
        return XP_PER_LEVEL[curlvl] - self.xp

    def __str__(self):
        return f"Skill(name={self.name}, rank={self.rank}, level={self.level}, xp={self.xp})"

    def __repr__(self):
        return self.__str__()
