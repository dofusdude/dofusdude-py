# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from dofusdude.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    GAME_LANGUAGE_ITEMS_SEARCH = "/{game}/{language}/items/search"
    GAME_LANGUAGE_MOUNTS_SEARCH = "/{game}/{language}/mounts/search"
    GAME_LANGUAGE_SETS_SEARCH = "/{game}/{language}/sets/search"
    GAME_LANGUAGE_ITEMS_QUEST_SEARCH = "/{game}/{language}/items/quest/search"
    GAME_LANGUAGE_ITEMS_CONSUMABLES_SEARCH = "/{game}/{language}/items/consumables/search"
    GAME_LANGUAGE_ITEMS_RESOURCES_SEARCH = "/{game}/{language}/items/resources/search"
    GAME_LANGUAGE_ITEMS_EQUIPMENT_SEARCH = "/{game}/{language}/items/equipment/search"
    GAME_LANGUAGE_ITEMS_COSMETICS_SEARCH = "/{game}/{language}/items/cosmetics/search"
    GAME_LANGUAGE_ITEMS_COSMETICS_ANKAMA_ID = "/{game}/{language}/items/cosmetics/{ankama_id}"
    GAME_LANGUAGE_ITEMS_RESOURCES_ANKAMA_ID = "/{game}/{language}/items/resources/{ankama_id}"
    GAME_LANGUAGE_ITEMS_EQUIPMENT_ANKAMA_ID = "/{game}/{language}/items/equipment/{ankama_id}"
    GAME_LANGUAGE_ITEMS_CONSUMABLES_ANKAMA_ID = "/{game}/{language}/items/consumables/{ankama_id}"
    GAME_LANGUAGE_ITEMS_QUEST_ANKAMA_ID = "/{game}/{language}/items/quest/{ankama_id}"
    GAME_LANGUAGE_MOUNTS_ANKAMA_ID = "/{game}/{language}/mounts/{ankama_id}"
    GAME_LANGUAGE_SETS_ANKAMA_ID = "/{game}/{language}/sets/{ankama_id}"
    GAME_LANGUAGE_SETS = "/{game}/{language}/sets"
    GAME_LANGUAGE_MOUNTS = "/{game}/{language}/mounts"
    GAME_LANGUAGE_ITEMS_EQUIPMENT = "/{game}/{language}/items/equipment"
    GAME_LANGUAGE_ITEMS_RESOURCES = "/{game}/{language}/items/resources"
    GAME_LANGUAGE_ITEMS_CONSUMABLES = "/{game}/{language}/items/consumables"
    GAME_LANGUAGE_ITEMS_QUEST = "/{game}/{language}/items/quest"
    GAME_LANGUAGE_ITEMS_COSMETICS = "/{game}/{language}/items/cosmetics"
    DOFUS2_LANGUAGE_ALMANAX = "/dofus2/{language}/almanax"
    DOFUS2_LANGUAGE_ALMANAX_DATE = "/dofus2/{language}/almanax/{date}"
    DOFUS2_META_ELEMENTS = "/dofus2/meta/elements"
    DOFUS2_META_LANGUAGE_ALMANAX_BONUSES = "/dofus2/meta/{language}/almanax/bonuses"
