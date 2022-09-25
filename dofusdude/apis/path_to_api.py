import typing_extensions

from dofusdude.paths import PathValues
from dofusdude.apis.paths.game_language_items_search import GameLanguageItemsSearch
from dofusdude.apis.paths.game_language_mounts_search import GameLanguageMountsSearch
from dofusdude.apis.paths.game_language_sets_search import GameLanguageSetsSearch
from dofusdude.apis.paths.game_language_items_quest_search import GameLanguageItemsQuestSearch
from dofusdude.apis.paths.game_language_items_consumables_search import GameLanguageItemsConsumablesSearch
from dofusdude.apis.paths.game_language_items_resources_search import GameLanguageItemsResourcesSearch
from dofusdude.apis.paths.game_language_items_equipment_search import GameLanguageItemsEquipmentSearch
from dofusdude.apis.paths.game_language_items_cosmetics_search import GameLanguageItemsCosmeticsSearch
from dofusdude.apis.paths.game_language_items_cosmetics_ankama_id import GameLanguageItemsCosmeticsAnkamaId
from dofusdude.apis.paths.game_language_items_resources_ankama_id import GameLanguageItemsResourcesAnkamaId
from dofusdude.apis.paths.game_language_items_equipment_ankama_id import GameLanguageItemsEquipmentAnkamaId
from dofusdude.apis.paths.game_language_items_consumables_ankama_id import GameLanguageItemsConsumablesAnkamaId
from dofusdude.apis.paths.game_language_items_quest_ankama_id import GameLanguageItemsQuestAnkamaId
from dofusdude.apis.paths.game_language_mounts_ankama_id import GameLanguageMountsAnkamaId
from dofusdude.apis.paths.game_language_sets_ankama_id import GameLanguageSetsAnkamaId
from dofusdude.apis.paths.game_language_sets import GameLanguageSets
from dofusdude.apis.paths.game_language_mounts import GameLanguageMounts
from dofusdude.apis.paths.game_language_items_equipment import GameLanguageItemsEquipment
from dofusdude.apis.paths.game_language_items_resources import GameLanguageItemsResources
from dofusdude.apis.paths.game_language_items_consumables import GameLanguageItemsConsumables
from dofusdude.apis.paths.game_language_items_quest import GameLanguageItemsQuest
from dofusdude.apis.paths.game_language_items_cosmetics import GameLanguageItemsCosmetics
from dofusdude.apis.paths.dofus2_language_almanax import Dofus2LanguageAlmanax
from dofusdude.apis.paths.dofus2_language_almanax_date import Dofus2LanguageAlmanaxDate
from dofusdude.apis.paths.dofus2_meta_elements import Dofus2MetaElements
from dofusdude.apis.paths.dofus2_meta_language_almanax_bonuses import Dofus2MetaLanguageAlmanaxBonuses

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.GAME_LANGUAGE_ITEMS_SEARCH: GameLanguageItemsSearch,
        PathValues.GAME_LANGUAGE_MOUNTS_SEARCH: GameLanguageMountsSearch,
        PathValues.GAME_LANGUAGE_SETS_SEARCH: GameLanguageSetsSearch,
        PathValues.GAME_LANGUAGE_ITEMS_QUEST_SEARCH: GameLanguageItemsQuestSearch,
        PathValues.GAME_LANGUAGE_ITEMS_CONSUMABLES_SEARCH: GameLanguageItemsConsumablesSearch,
        PathValues.GAME_LANGUAGE_ITEMS_RESOURCES_SEARCH: GameLanguageItemsResourcesSearch,
        PathValues.GAME_LANGUAGE_ITEMS_EQUIPMENT_SEARCH: GameLanguageItemsEquipmentSearch,
        PathValues.GAME_LANGUAGE_ITEMS_COSMETICS_SEARCH: GameLanguageItemsCosmeticsSearch,
        PathValues.GAME_LANGUAGE_ITEMS_COSMETICS_ANKAMA_ID: GameLanguageItemsCosmeticsAnkamaId,
        PathValues.GAME_LANGUAGE_ITEMS_RESOURCES_ANKAMA_ID: GameLanguageItemsResourcesAnkamaId,
        PathValues.GAME_LANGUAGE_ITEMS_EQUIPMENT_ANKAMA_ID: GameLanguageItemsEquipmentAnkamaId,
        PathValues.GAME_LANGUAGE_ITEMS_CONSUMABLES_ANKAMA_ID: GameLanguageItemsConsumablesAnkamaId,
        PathValues.GAME_LANGUAGE_ITEMS_QUEST_ANKAMA_ID: GameLanguageItemsQuestAnkamaId,
        PathValues.GAME_LANGUAGE_MOUNTS_ANKAMA_ID: GameLanguageMountsAnkamaId,
        PathValues.GAME_LANGUAGE_SETS_ANKAMA_ID: GameLanguageSetsAnkamaId,
        PathValues.GAME_LANGUAGE_SETS: GameLanguageSets,
        PathValues.GAME_LANGUAGE_MOUNTS: GameLanguageMounts,
        PathValues.GAME_LANGUAGE_ITEMS_EQUIPMENT: GameLanguageItemsEquipment,
        PathValues.GAME_LANGUAGE_ITEMS_RESOURCES: GameLanguageItemsResources,
        PathValues.GAME_LANGUAGE_ITEMS_CONSUMABLES: GameLanguageItemsConsumables,
        PathValues.GAME_LANGUAGE_ITEMS_QUEST: GameLanguageItemsQuest,
        PathValues.GAME_LANGUAGE_ITEMS_COSMETICS: GameLanguageItemsCosmetics,
        PathValues.DOFUS2_LANGUAGE_ALMANAX: Dofus2LanguageAlmanax,
        PathValues.DOFUS2_LANGUAGE_ALMANAX_DATE: Dofus2LanguageAlmanaxDate,
        PathValues.DOFUS2_META_ELEMENTS: Dofus2MetaElements,
        PathValues.DOFUS2_META_LANGUAGE_ALMANAX_BONUSES: Dofus2MetaLanguageAlmanaxBonuses,
    }
)

path_to_api = PathToApi(
    {
        PathValues.GAME_LANGUAGE_ITEMS_SEARCH: GameLanguageItemsSearch,
        PathValues.GAME_LANGUAGE_MOUNTS_SEARCH: GameLanguageMountsSearch,
        PathValues.GAME_LANGUAGE_SETS_SEARCH: GameLanguageSetsSearch,
        PathValues.GAME_LANGUAGE_ITEMS_QUEST_SEARCH: GameLanguageItemsQuestSearch,
        PathValues.GAME_LANGUAGE_ITEMS_CONSUMABLES_SEARCH: GameLanguageItemsConsumablesSearch,
        PathValues.GAME_LANGUAGE_ITEMS_RESOURCES_SEARCH: GameLanguageItemsResourcesSearch,
        PathValues.GAME_LANGUAGE_ITEMS_EQUIPMENT_SEARCH: GameLanguageItemsEquipmentSearch,
        PathValues.GAME_LANGUAGE_ITEMS_COSMETICS_SEARCH: GameLanguageItemsCosmeticsSearch,
        PathValues.GAME_LANGUAGE_ITEMS_COSMETICS_ANKAMA_ID: GameLanguageItemsCosmeticsAnkamaId,
        PathValues.GAME_LANGUAGE_ITEMS_RESOURCES_ANKAMA_ID: GameLanguageItemsResourcesAnkamaId,
        PathValues.GAME_LANGUAGE_ITEMS_EQUIPMENT_ANKAMA_ID: GameLanguageItemsEquipmentAnkamaId,
        PathValues.GAME_LANGUAGE_ITEMS_CONSUMABLES_ANKAMA_ID: GameLanguageItemsConsumablesAnkamaId,
        PathValues.GAME_LANGUAGE_ITEMS_QUEST_ANKAMA_ID: GameLanguageItemsQuestAnkamaId,
        PathValues.GAME_LANGUAGE_MOUNTS_ANKAMA_ID: GameLanguageMountsAnkamaId,
        PathValues.GAME_LANGUAGE_SETS_ANKAMA_ID: GameLanguageSetsAnkamaId,
        PathValues.GAME_LANGUAGE_SETS: GameLanguageSets,
        PathValues.GAME_LANGUAGE_MOUNTS: GameLanguageMounts,
        PathValues.GAME_LANGUAGE_ITEMS_EQUIPMENT: GameLanguageItemsEquipment,
        PathValues.GAME_LANGUAGE_ITEMS_RESOURCES: GameLanguageItemsResources,
        PathValues.GAME_LANGUAGE_ITEMS_CONSUMABLES: GameLanguageItemsConsumables,
        PathValues.GAME_LANGUAGE_ITEMS_QUEST: GameLanguageItemsQuest,
        PathValues.GAME_LANGUAGE_ITEMS_COSMETICS: GameLanguageItemsCosmetics,
        PathValues.DOFUS2_LANGUAGE_ALMANAX: Dofus2LanguageAlmanax,
        PathValues.DOFUS2_LANGUAGE_ALMANAX_DATE: Dofus2LanguageAlmanaxDate,
        PathValues.DOFUS2_META_ELEMENTS: Dofus2MetaElements,
        PathValues.DOFUS2_META_LANGUAGE_ALMANAX_BONUSES: Dofus2MetaLanguageAlmanaxBonuses,
    }
)
