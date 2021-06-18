from enum import Enum
from typing import List


class PlayerAccountType(Enum):
    NORMAL = "m=hiscore_oldschool/index_lite.ws"
    IRONMAN = "m=hiscore_oldschool_ironman/index_lite.ws"
    HARDCORE_IRONMAN = "m=hiscore_oldschool_hardcore_ironman/index_lite.ws"
    ULTIMATE_IRONMAN = "m=hiscore_oldschool_ultimate/index_lite.ws"
    DEADMAN = "m=hiscore_oldschool_deadman/index_lite.ws"
    SEASONAL = "m=hiscore_oldschool_seasonal/index_lite.ws"


SKILLS = [
    "attack",
    "defence",
    "strength",
    "hitpoints",
    "ranged",
    "prayer",
    "magic",
    "cooking",
    "woodcutting",
    "fletching",
    "fishing",
    "firemaking",
    "crafting",
    "smithing",
    "mining",
    "herblore",
    "agility",
    "thieving",
    "slayer",
    "farming",
    "runecrafting",
    "hunter",
    "construction",
]


def _gen_xp() -> List[int]:
    total = 0
    xp = [0]

    for i in range(1, 99):
        total += int(i + 300 * (2 ** (i / 7.0)))
        xp.append(total // 4)
    return xp


XP_PER_LEVEL = _gen_xp()
USER_AGENT = "osrs-py:dev"
OSRS_URL = "http://services.runescape.com"
OSRS_WIKI_URL = "https://oldschool.runescape.wiki/"
OSRS_WIKI_PRICES_API = "https://prices.runescape.wiki/api/v1/osrs"
