import typing_extensions

from dofusdude.apis.tags import TagValues
from dofusdude.apis.tags.all_items_api import AllItemsApi
from dofusdude.apis.tags.almanax_api import AlmanaxApi
from dofusdude.apis.tags.consumables_api import ConsumablesApi
from dofusdude.apis.tags.cosmetics_api import CosmeticsApi
from dofusdude.apis.tags.equipment_api import EquipmentApi
from dofusdude.apis.tags.meta_api import MetaApi
from dofusdude.apis.tags.mounts_api import MountsApi
from dofusdude.apis.tags.quest_items_api import QuestItemsApi
from dofusdude.apis.tags.resources_api import ResourcesApi
from dofusdude.apis.tags.sets_api import SetsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ALL_ITEMS: AllItemsApi,
        TagValues.ALMANAX: AlmanaxApi,
        TagValues.CONSUMABLES: ConsumablesApi,
        TagValues.COSMETICS: CosmeticsApi,
        TagValues.EQUIPMENT: EquipmentApi,
        TagValues.META: MetaApi,
        TagValues.MOUNTS: MountsApi,
        TagValues.QUEST_ITEMS: QuestItemsApi,
        TagValues.RESOURCES: ResourcesApi,
        TagValues.SETS: SetsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ALL_ITEMS: AllItemsApi,
        TagValues.ALMANAX: AlmanaxApi,
        TagValues.CONSUMABLES: ConsumablesApi,
        TagValues.COSMETICS: CosmeticsApi,
        TagValues.EQUIPMENT: EquipmentApi,
        TagValues.META: MetaApi,
        TagValues.MOUNTS: MountsApi,
        TagValues.QUEST_ITEMS: QuestItemsApi,
        TagValues.RESOURCES: ResourcesApi,
        TagValues.SETS: SetsApi,
    }
)
