
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from dofusdude-py.api.all_items_api import AllItemsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from dofusdude-py.api.all_items_api import AllItemsApi
from dofusdude-py.api.almanax_api import AlmanaxApi
from dofusdude-py.api.consumables_api import ConsumablesApi
from dofusdude-py.api.cosmetics_api import CosmeticsApi
from dofusdude-py.api.equipment_api import EquipmentApi
from dofusdude-py.api.meta_api import MetaApi
from dofusdude-py.api.mounts_api import MountsApi
from dofusdude-py.api.quest_items_api import QuestItemsApi
from dofusdude-py.api.resources_api import ResourcesApi
from dofusdude-py.api.sets_api import SetsApi
