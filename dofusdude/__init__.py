# coding: utf-8

# flake8: noqa

"""
    dofusdude

    # A project for you - the developer. The all-in-one toolbelt for your next Ankama related project.  ## Client SDKs - [Javascript](https://github.com/dofusdude/dofusdude-js) npm i dofusdude-js --save - [Typescript](https://github.com/dofusdude/dofusdude-ts) npm i dofusdude-ts --save - [Go](https://github.com/dofusdude/dodugo) go get -u github.com/dofusdude/dodugo - [Python](https://github.com/dofusdude/dofusdude-py) pip install dofusdude - [PHP](https://github.com/dofusdude/dofusdude-php)  Everything, including this site, is generated out of the [Docs Repo](https://github.com/dofusdude/api-docs). Consider it the Single Source of Truth. If there is a problem with the SDKs, create an issue there.  Your favorite language is missing? Please let me know!  # Main Features - 🥷 **Seamless Auto-Update** load data in the background when a new Dofus version is released and serving it within 2 minutes with atomic data source switching. No downtime and no effects for the user, just always up-to-date.  - ⚡ **Blazingly Fast** all data in-memory, aggressive caching over short time spans, HTTP/2 multiplexing, written in Go, optimized for low latency, hosted on bare metal in 🇩🇪.  - 📨 **Discord Integration** Ankama related RSS and Almanax feeds to post to Discord servers with advanced features like filters or mentions. Use the endpoints as a dev or the official [Web Client](https://discord.dofusdude.com) as a user.  - 🩸 **Dofus 2 Beta** from stable to bleeding edge by replacing /dofus2 with /dofus2beta.  - 🗣️ **Multilingual** supporting _en_, _fr_, _es_, _pt_ including the dropped languages from the Dofus website _de_ and _it_.  - 🧠 **Search by Relevance** allowing typos in name and description, handled by language specific text analysis and indexing.  - 🕵️ **Complete** actual data from the game including items invisible to the encyclopedia like quest items.  - 🖼️ **HD Images** rendering game assets to high-res images with up to 800x800 px.  ... and much more on the Roadmap on my Discord.   ## Deploy now. Use forever. Everything you see here on this site, you can use now and forever. Updates could introduce new fields, new paths or parameter but never break backwards compatibility.  There is one exception! **The API will _always_ choose being up-to-date over everything else**. So if Ankama decides to drop languages from the game like they did with their website, the API will loose support for them, too.  ## Thank you! I highly welcome everyone on my [Discord](https://discord.gg/3EtHskZD8h) to just talk about projects and use cases or give feedback of any kind.  The servers have a fixed monthly cost to provide very fast responses. If you want to help me keeping them running or simply donate to that cause, consider becoming a [GitHub Sponsor](https://github.com/sponsors/dofusdude).

    The version of the OpenAPI document: 0.8.1
    Contact: stelzo@steado.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.8.1"

# import apis into sdk package
from dofusdude.api.almanax_api import AlmanaxApi
from dofusdude.api.consumables_api import ConsumablesApi
from dofusdude.api.cosmetics_api import CosmeticsApi
from dofusdude.api.equipment_api import EquipmentApi
from dofusdude.api.game_api import GameApi
from dofusdude.api.meta_api import MetaApi
from dofusdude.api.mounts_api import MountsApi
from dofusdude.api.quest_items_api import QuestItemsApi
from dofusdude.api.resources_api import ResourcesApi
from dofusdude.api.sets_api import SetsApi
from dofusdude.api.webhooks_api import WebhooksApi

# import ApiClient
from dofusdude.api_response import ApiResponse
from dofusdude.api_client import ApiClient
from dofusdude.configuration import Configuration
from dofusdude.exceptions import OpenApiException
from dofusdude.exceptions import ApiTypeError
from dofusdude.exceptions import ApiValueError
from dofusdude.exceptions import ApiKeyError
from dofusdude.exceptions import ApiAttributeError
from dofusdude.exceptions import ApiException

# import models into sdk package
from dofusdude.models.almanax_entry import AlmanaxEntry
from dofusdude.models.almanax_entry_bonus import AlmanaxEntryBonus
from dofusdude.models.almanax_entry_tribute import AlmanaxEntryTribute
from dofusdude.models.almanax_entry_tribute_item import AlmanaxEntryTributeItem
from dofusdude.models.almanax_webhook import AlmanaxWebhook
from dofusdude.models.almanax_webhook_daily_settings import AlmanaxWebhookDailySettings
from dofusdude.models.condition_entry import ConditionEntry
from dofusdude.models.condition_tree_leaf import ConditionTreeLeaf
from dofusdude.models.condition_tree_node import ConditionTreeNode
from dofusdude.models.condition_tree_relation import ConditionTreeRelation
from dofusdude.models.cosmetic import Cosmetic
from dofusdude.models.cosmetic_type import CosmeticType
from dofusdude.models.create_almanax_webhook import CreateAlmanaxWebhook
from dofusdude.models.create_almanax_webhook_daily_settings import CreateAlmanaxWebhookDailySettings
from dofusdude.models.create_almanax_webhook_mentions_value_inner import CreateAlmanaxWebhookMentionsValueInner
from dofusdude.models.create_rss_webhook import CreateRSSWebhook
from dofusdude.models.create_twitter_webhook import CreateTwitterWebhook
from dofusdude.models.effects_entry import EffectsEntry
from dofusdude.models.effects_entry_type import EffectsEntryType
from dofusdude.models.equipment import Equipment
from dofusdude.models.equipment_parent_set import EquipmentParentSet
from dofusdude.models.equipment_set import EquipmentSet
from dofusdude.models.get_game_search200_response_inner import GetGameSearch200ResponseInner
from dofusdude.models.get_meta_almanax_bonuses200_response_inner import GetMetaAlmanaxBonuses200ResponseInner
from dofusdude.models.get_meta_webhooks_twitter200_response import GetMetaWebhooksTwitter200Response
from dofusdude.models.image_urls import ImageUrls
from dofusdude.models.item_list_entry import ItemListEntry
from dofusdude.models.items_list_entry_typed import ItemsListEntryTyped
from dofusdude.models.items_list_entry_typed_type import ItemsListEntryTypedType
from dofusdude.models.items_list_paged import ItemsListPaged
from dofusdude.models.links_paged import LinksPaged
from dofusdude.models.mount import Mount
from dofusdude.models.mount_list_entry import MountListEntry
from dofusdude.models.mounts_list_paged import MountsListPaged
from dofusdude.models.put_almanax_webhook import PutAlmanaxWebhook
from dofusdude.models.put_rss_webhook import PutRSSWebhook
from dofusdude.models.put_twitter_webhook import PutTwitterWebhook
from dofusdude.models.recipe_entry import RecipeEntry
from dofusdude.models.resource import Resource
from dofusdude.models.rss_webhook import RssWebhook
from dofusdude.models.set_list_entry import SetListEntry
from dofusdude.models.sets_list_paged import SetsListPaged
from dofusdude.models.twitter_webhook import TwitterWebhook
from dofusdude.models.weapon import Weapon
from dofusdude.models.weapon_range import WeaponRange
