from typing import NamedTuple, Callable, Dict, List, Optional
from BaseClasses import CollectionState


class RegionExit(NamedTuple):
    region: str
    access_rule: Callable[[CollectionState, int], bool] = lambda state, player: True
    breakable_wall: bool = False


region_table: Dict[str, List[str]] = {
    "Menu": ["Dungeon Mirror"],
    "Dungeon Mirror": ["Dungeon Slide"],
    "Dungeon Slide": ["Dungeon Mirror", "Dungeon Strong Eyes", "Dungeon Escape Lower"],
    "Dungeon Strong Eyes": ["Dungeon Slide", "Dungeon => Castle"],
    "Dungeon => Castle": ["Dungeon Mirror", "Dungeon Strong Eyes", "Castle Main"],
    "Dungeon Escape Lower": ["Dungeon Slide", "Dungeon Escape Upper", "Underbelly Main"],
    "Dungeon Escape Upper": ["Dungeon Escape Lower", "Theatre Outside Scythe Corridor"],
    "Castle Main": ["Dungeon => Castle", "Library Main", "Keep Main", "Empty Bailey", "Theatre Pillar", "Castle Spiral Climb",],
    "Castle Spiral Climb": ["Castle Main", "Castle High Climb", "Castle By Scythe Corridor",],
    "Castle High Climb": [],
    "Castle By Scythe Corridor": ["Castle Spiral Climb", "Castle High Climb", "Castle => Theatre (Front)",],
    "Castle => Theatre (Front)": ["Castle By Scythe Corridor", "Castle Moon Room", "Theatre Main",],
    "Castle Moon Room": [],
    "Library Main": ["Library Locked", "Library Greaves", "Library Top"],
    "Library Locked": [],
    "Library Greaves": ["Library Top"],
    "Library Top": ["Library Greaves"],
    "Keep Main": ["Keep Locked Room", "Keep Sunsetter", "Keep Path To Throne", "Keep => Underbelly", "Theatre Outside Scythe Corridor",],
    "Keep Locked Room": ["Keep Sunsetter"],
    "Keep Sunsetter": [],
    "Keep => Underbelly": ["Keep Main", "Underbelly Hole"],
    "Empty Bailey": ["Castle Main", "Tower Remains", "Theatre Pillar",],
    "Tower Remains": ["Underbelly Main", "The Great Door",],
    "Underbelly Main Lower": ["Underbelly Little Guy", "Underbelly By Heliacal", "Underbelly Hole", "Underbelly Main Upper"],
    "Underbelly Main Upper": ["Underbelly Main Lower", "Underbelly Light Pillar", "Underbelly By Heliacal"],
    "Underbelly Little Guy": ["Empty Bailey", "Underbelly Main Lower", "Underbelly Main Upper"],
    "Underbelly By Heliacal": ["Underbelly Main Upper"],
    "Underbelly Hole": ["Underbelly Main Lower", "Underbelly => Keep"],
    "Underbelly Light Pillar": ["Underbelly Ascendant Light", "Underbelly => Dungeon"],
    "Underbelly Ascendant Light": ["Underbelly Light Pillar", "Underbelly => Dungeon"],
    "Underbelly => Keep": ["Keep => Underbelly", "Underbelly Hole"],
    "Underbelly => Dungeon": ["Dungeon Escape Lower", "Underbelly Light Pillar", "Underbelly Ascendant Light"],
    "Theatre Main": ["Keep Main",],
    "Theatre Pillar": ["Theatre Main",],
    "Theatre Outside Scythe Corridor": ["Theatre Main"],
    "The Great Door": [],
}
