
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from dofusdude.api.all_items_api import AllItemsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from dofusdude.api.all_items_api import AllItemsApi
from dofusdude.api.almanax_api import AlmanaxApi
from dofusdude.api.consumables_api import ConsumablesApi
from dofusdude.api.cosmetics_api import CosmeticsApi
from dofusdude.api.equipment_api import EquipmentApi
from dofusdude.api.meta_api import MetaApi
from dofusdude.api.mounts_api import MountsApi
from dofusdude.api.quest_items_api import QuestItemsApi
from dofusdude.api.resources_api import ResourcesApi
from dofusdude.api.sets_api import SetsApi
