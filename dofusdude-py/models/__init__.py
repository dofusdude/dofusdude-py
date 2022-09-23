# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from dofusdude-py.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from dofusdude-py.model.almanax_entry import AlmanaxEntry
from dofusdude-py.model.almanax_entry_bonus import AlmanaxEntryBonus
from dofusdude-py.model.almanax_entry_tribute import AlmanaxEntryTribute
from dofusdude-py.model.almanax_entry_tribute_item import AlmanaxEntryTributeItem
from dofusdude-py.model.condition_entry import ConditionEntry
from dofusdude-py.model.cosmetic import Cosmetic
from dofusdude-py.model.effects_entry import EffectsEntry
from dofusdude-py.model.effects_entry_type import EffectsEntryType
from dofusdude-py.model.equipment import Equipment
from dofusdude-py.model.equipment_parent_set import EquipmentParentSet
from dofusdude-py.model.equipment_set import EquipmentSet
from dofusdude-py.model.get_meta_almanax_bonuses200_response_inner import GetMetaAlmanaxBonuses200ResponseInner
from dofusdude-py.model.image_urls import ImageUrls
from dofusdude-py.model.item_list_entry import ItemListEntry
from dofusdude-py.model.items_list_entry_typed import ItemsListEntryTyped
from dofusdude-py.model.items_list_entry_typed_type import ItemsListEntryTypedType
from dofusdude-py.model.items_list_paged import ItemsListPaged
from dofusdude-py.model.links_paged import LinksPaged
from dofusdude-py.model.mount import Mount
from dofusdude-py.model.mount_list_entry import MountListEntry
from dofusdude-py.model.mounts_list_paged import MountsListPaged
from dofusdude-py.model.recipe_entry import RecipeEntry
from dofusdude-py.model.resource import Resource
from dofusdude-py.model.set_list_entry import SetListEntry
from dofusdude-py.model.sets_list_paged import SetsListPaged
from dofusdude-py.model.weapon import Weapon
from dofusdude-py.model.weapon_range import WeaponRange
