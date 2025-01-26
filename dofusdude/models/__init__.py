# coding: utf-8

# flake8: noqa
"""
    dofusdude

    # Open Ankama Developer Community The all-in-one toolbelt for your next Ankama related project.  ## Versions - [Dofus 2](https://docs.dofusdu.de/dofus2/) - [Dofus 3](https://docs.dofusdu.de/dofus3/)   - v1 [latest] (you are here)   ## Client SDKs - [Javascript](https://github.com/dofusdude/dofusdude-js) `npm i dofusdude-js --save` - [Typescript](https://github.com/dofusdude/dofusdude-ts) `npm i dofusdude-ts --save` - [Go](https://github.com/dofusdude/dodugo) `go get -u github.com/dofusdude/dodugo` - [Python](https://github.com/dofusdude/dofusdude-py) `pip install dofusdude` - [Java](https://github.com/dofusdude/dofusdude-java) Maven with GitHub packages setup  Everything, including this site, is generated out of the [Docs Repo](https://github.com/dofusdude/api-docs). Consider it the Single Source of Truth. If there is a problem with the SDKs, create an issue there.  Your favorite language is missing? Please let me know!  # Main Features - 🥷 **Seamless Auto-Update** load data in the background when a new Dofus version is released and serving it within 10 minutes with atomic data source switching. No downtime and no effects for the user, just always up-to-date.  - ⚡ **Blazingly Fast** all data in-memory, aggressive caching over short time spans, HTTP/2 multiplexing, written in Go, optimized for low latency, hosted on bare metal in 🇩🇪.  - 📨 **Almanax Discord Integration** Use the endpoints as a dev or the official [Web Client](https://discord.dofusdude.com) as a user.  - 🩸 **Dofus 3 Beta** from stable to bleeding edge by replacing /dofus3 with /dofus3beta.  - 🗣️ **Multilingual** supporting _en_, _fr_, _es_, _pt_, _de_.  - 🧠 **Search by Relevance** allowing typos in name and description, handled by language specific text analysis and indexing.  - 🕵️ **Official Sources** generated from actual data from the game.  ... and much more on the Roadmap on my [Discord](https://discord.gg/3EtHskZD8h). 

    The version of the OpenAPI document: 1.0.0
    Contact: stelzo@steado.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from dofusdude.models.almanax import Almanax
from dofusdude.models.almanax_bonus import AlmanaxBonus
from dofusdude.models.almanax_tribute import AlmanaxTribute
from dofusdude.models.almanax_tribute_item import AlmanaxTributeItem
from dofusdude.models.almanax_webhook import AlmanaxWebhook
from dofusdude.models.almanax_webhook_daily_settings import AlmanaxWebhookDailySettings
from dofusdude.models.condition import Condition
from dofusdude.models.condition_leaf import ConditionLeaf
from dofusdude.models.condition_node import ConditionNode
from dofusdude.models.condition_relation import ConditionRelation
from dofusdude.models.create_almanax_webhook import CreateAlmanaxWebhook
from dofusdude.models.create_almanax_webhook_daily_settings import CreateAlmanaxWebhookDailySettings
from dofusdude.models.create_almanax_webhook_mentions_value_inner import CreateAlmanaxWebhookMentionsValueInner
from dofusdude.models.create_rss_webhook import CreateRSSWebhook
from dofusdude.models.create_twitter_webhook import CreateTwitterWebhook
from dofusdude.models.effect import Effect
from dofusdude.models.effect_type import EffectType
from dofusdude.models.equipment import Equipment
from dofusdude.models.equipment_set import EquipmentSet
from dofusdude.models.error import Error
from dofusdude.models.game_search import GameSearch
from dofusdude.models.game_search_item import GameSearchItem
from dofusdude.models.game_search_type import GameSearchType
from dofusdude.models.get_meta_almanax_bonuses200_response_inner import GetMetaAlmanaxBonuses200ResponseInner
from dofusdude.models.get_meta_webhooks_twitter200_response import GetMetaWebhooksTwitter200Response
from dofusdude.models.images import Images
from dofusdude.models.item_subtype import ItemSubtype
from dofusdude.models.list_equipment_set import ListEquipmentSet
from dofusdude.models.list_equipment_sets import ListEquipmentSets
from dofusdude.models.list_item import ListItem
from dofusdude.models.list_item_general import ListItemGeneral
from dofusdude.models.list_items import ListItems
from dofusdude.models.list_mounts import ListMounts
from dofusdude.models.mount import Mount
from dofusdude.models.mount_family import MountFamily
from dofusdude.models.paged_links import PagedLinks
from dofusdude.models.put_almanax_webhook import PutAlmanaxWebhook
from dofusdude.models.put_rss_webhook import PutRSSWebhook
from dofusdude.models.put_twitter_webhook import PutTwitterWebhook
from dofusdude.models.range import Range
from dofusdude.models.recipe import Recipe
from dofusdude.models.resource import Resource
from dofusdude.models.rss_webhook import RssWebhook
from dofusdude.models.translated_id import TranslatedId
from dofusdude.models.twitter_webhook import TwitterWebhook
from dofusdude.models.version import Version
from dofusdude.models.weapon import Weapon
