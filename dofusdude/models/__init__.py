# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from dofusdude.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from dofusdude.model.almanax_entry import AlmanaxEntry
from dofusdude.model.almanax_webhook import AlmanaxWebhook
from dofusdude.model.condition_entry import ConditionEntry
from dofusdude.model.cosmetic import Cosmetic
from dofusdude.model.create_almanax_webhook import CreateAlmanaxWebhook
from dofusdude.model.create_rss_webhook import CreateRSSWebhook
from dofusdude.model.create_twitter_webhook import CreateTwitterWebhook
from dofusdude.model.effects_entry import EffectsEntry
from dofusdude.model.equipment import Equipment
from dofusdude.model.equipment_set import EquipmentSet
from dofusdude.model.image_urls import ImageUrls
from dofusdude.model.item_list_entry import ItemListEntry
from dofusdude.model.items_list_entry_typed import ItemsListEntryTyped
from dofusdude.model.items_list_paged import ItemsListPaged
from dofusdude.model.links_paged import LinksPaged
from dofusdude.model.mount import Mount
from dofusdude.model.mount_list_entry import MountListEntry
from dofusdude.model.mounts_list_paged import MountsListPaged
from dofusdude.model.put_almanax_webhook import PutAlmanaxWebhook
from dofusdude.model.put_rss_webhook import PutRSSWebhook
from dofusdude.model.put_twitter_webhook import PutTwitterWebhook
from dofusdude.model.recipe_entry import RecipeEntry
from dofusdude.model.resource import Resource
from dofusdude.model.rss_webhook import RssWebhook
from dofusdude.model.set_list_entry import SetListEntry
from dofusdude.model.sets_list_paged import SetsListPaged
from dofusdude.model.twitter_webhook import TwitterWebhook
from dofusdude.model.weapon import Weapon
