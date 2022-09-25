# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from dofusdude.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ALL_ITEMS = "all items"
    ALMANAX = "almanax"
    CONSUMABLES = "consumables"
    COSMETICS = "cosmetics"
    EQUIPMENT = "equipment"
    META = "meta"
    MOUNTS = "mounts"
    QUEST_ITEMS = "quest items"
    RESOURCES = "resources"
    SETS = "sets"
