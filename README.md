# dofusdude
# A project for you - the developer.
The all-in-one toolbelt for your next Ankama related project.

## Client SDKs
- [Javascript](https://github.com/dofusdude/dofusdude-js) `npm i dofusdude-js --save`
- [Typescript](https://github.com/dofusdude/dofusdude-ts) `npm i dofusdude-ts --save`
- [Go](https://github.com/dofusdude/dodugo) `go get -u github.com/dofusdude/dodugo`
- [Python](https://github.com/dofusdude/dofusdude-py) `pip install dofusdude`
- [PHP](https://github.com/dofusdude/dofusdude-php)
- [Java](https://github.com/dofusdude/dofusdude-java) Maven with GitHub packages setup

Everything, including this site, is generated out of the [Docs Repo](https://github.com/dofusdude/api-docs). Consider it the Single Source of Truth. If there is a problem with the SDKs, create an issue there.

Your favorite language is missing? Please let me know!

# Main Features
- 🥷 **Seamless Auto-Update** load data in the background when a new Dofus version is released and serving it within 10 minutes with atomic data source switching. No downtime and no effects for the user, just always up-to-date.

- ⚡ **Blazingly Fast** all data in-memory, aggressive caching over short time spans, HTTP/2 multiplexing, written in Go, optimized for low latency, hosted on bare metal in 🇩🇪.

- 📨 **Discord Integration** Ankama related RSS and Almanax feeds to post to Discord servers with advanced features like filters or mentions. Use the endpoints as a dev or the official [Web Client](https://discord.dofusdude.com) as a user.

- 🩸 **Dofus 2 Beta** from stable to bleeding edge by replacing /dofus2 with /dofus2beta.

- 🗣️ **Multilingual** supporting _en_, _fr_, _es_, _pt_ including the dropped languages from the Dofus website _de_ and _it_.

- 🧠 **Search by Relevance** allowing typos in name and description, handled by language specific text analysis and indexing.

- 🕵️ **Complete** actual data from the game including items invisible to the encyclopedia like quest items.

- 🖼️ **HD Images** rendering game assets to high-res images with up to 800x800 px.

... and much more on the Roadmap on my [Discord](https://discord.gg/3EtHskZD8h).


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.9.3
- Package version: 0.9.3
- Generator version: 7.10.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://discord.gg/3EtHskZD8h](https://discord.gg/3EtHskZD8h)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/dofusdude/dofusdude-py.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/dofusdude/dofusdude-py.git`)

Then import the package:
```python
import dofusdude
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import dofusdude
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import dofusdude
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)



# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.AlmanaxApi(api_client)
    language = 'fr' # str | code
    var_date = 'Tue Jul 14 00:00:00 UTC 2020' # date | yyyy-mm-dd

    try:
        # Single Almanax Date
        api_response = api_instance.get_almanax_date(language, var_date)
        print("The response of AlmanaxApi->get_almanax_date:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlmanaxApi->get_almanax_date: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.dofusdu.de*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AlmanaxApi* | [**get_almanax_date**](docs/AlmanaxApi.md#get_almanax_date) | **GET** /dofus2/{language}/almanax/{date} | Single Almanax Date
*AlmanaxApi* | [**get_almanax_range**](docs/AlmanaxApi.md#get_almanax_range) | **GET** /dofus2/{language}/almanax | Almanax Range
*ConsumablesApi* | [**get_all_items_consumables_list**](docs/ConsumablesApi.md#get_all_items_consumables_list) | **GET** /{game}/{language}/items/consumables/all | List All Consumables
*ConsumablesApi* | [**get_items_consumables_list**](docs/ConsumablesApi.md#get_items_consumables_list) | **GET** /{game}/{language}/items/consumables | List Consumables
*ConsumablesApi* | [**get_items_consumables_search**](docs/ConsumablesApi.md#get_items_consumables_search) | **GET** /{game}/{language}/items/consumables/search | Search Consumables
*ConsumablesApi* | [**get_items_consumables_single**](docs/ConsumablesApi.md#get_items_consumables_single) | **GET** /{game}/{language}/items/consumables/{ankama_id} | Single Consumables
*CosmeticsApi* | [**get_all_cosmetics_list**](docs/CosmeticsApi.md#get_all_cosmetics_list) | **GET** /{game}/{language}/items/cosmetics/all | List All Cosmetics
*CosmeticsApi* | [**get_cosmetics_list**](docs/CosmeticsApi.md#get_cosmetics_list) | **GET** /{game}/{language}/items/cosmetics | List Cosmetics
*CosmeticsApi* | [**get_cosmetics_search**](docs/CosmeticsApi.md#get_cosmetics_search) | **GET** /{game}/{language}/items/cosmetics/search | Search Cosmetics
*CosmeticsApi* | [**get_cosmetics_single**](docs/CosmeticsApi.md#get_cosmetics_single) | **GET** /{game}/{language}/items/cosmetics/{ankama_id} | Single Cosmetics
*EquipmentApi* | [**get_all_items_equipment_list**](docs/EquipmentApi.md#get_all_items_equipment_list) | **GET** /{game}/{language}/items/equipment/all | List All Equipment
*EquipmentApi* | [**get_items_equipment_list**](docs/EquipmentApi.md#get_items_equipment_list) | **GET** /{game}/{language}/items/equipment | List Equipment
*EquipmentApi* | [**get_items_equipment_search**](docs/EquipmentApi.md#get_items_equipment_search) | **GET** /{game}/{language}/items/equipment/search | Search Equipment
*EquipmentApi* | [**get_items_equipment_single**](docs/EquipmentApi.md#get_items_equipment_single) | **GET** /{game}/{language}/items/equipment/{ankama_id} | Single Equipment
*GameApi* | [**get_game_search**](docs/GameApi.md#get_game_search) | **GET** /{game}/{language}/search | Game Search
*GameApi* | [**get_items_all_search**](docs/GameApi.md#get_items_all_search) | **GET** /{game}/{language}/items/search | Search All Items
*MetaApi* | [**get_game_search_types**](docs/MetaApi.md#get_game_search_types) | **GET** /dofus2/meta/search/types | Available Game Search Types
*MetaApi* | [**get_item_types**](docs/MetaApi.md#get_item_types) | **GET** /dofus2/meta/items/types | Available Item Types
*MetaApi* | [**get_meta_almanax_bonuses**](docs/MetaApi.md#get_meta_almanax_bonuses) | **GET** /dofus2/meta/{language}/almanax/bonuses | Available Almanax Bonuses
*MetaApi* | [**get_meta_almanax_bonuses_search**](docs/MetaApi.md#get_meta_almanax_bonuses_search) | **GET** /dofus2/meta/{language}/almanax/bonuses/search | Search Available Almanax Bonuses
*MetaApi* | [**get_meta_elements**](docs/MetaApi.md#get_meta_elements) | **GET** /dofus2/meta/elements | Effects and Condition Elements
*MetaApi* | [**get_meta_version**](docs/MetaApi.md#get_meta_version) | **GET** /dofus2/meta/version | Game Version
*MountsApi* | [**get_all_mounts_list**](docs/MountsApi.md#get_all_mounts_list) | **GET** /{game}/{language}/mounts/all | List All Mounts
*MountsApi* | [**get_mounts_list**](docs/MountsApi.md#get_mounts_list) | **GET** /{game}/{language}/mounts | List Mounts
*MountsApi* | [**get_mounts_search**](docs/MountsApi.md#get_mounts_search) | **GET** /{game}/{language}/mounts/search | Search Mounts
*MountsApi* | [**get_mounts_single**](docs/MountsApi.md#get_mounts_single) | **GET** /{game}/{language}/mounts/{ankama_id} | Single Mounts
*QuestItemsApi* | [**get_all_items_quest_list**](docs/QuestItemsApi.md#get_all_items_quest_list) | **GET** /{game}/{language}/items/quest/all | List All Quest Items
*QuestItemsApi* | [**get_item_quest_single**](docs/QuestItemsApi.md#get_item_quest_single) | **GET** /{game}/{language}/items/quest/{ankama_id} | Single Quest Items
*QuestItemsApi* | [**get_items_quest_list**](docs/QuestItemsApi.md#get_items_quest_list) | **GET** /{game}/{language}/items/quest | List Quest Items
*QuestItemsApi* | [**get_items_quest_search**](docs/QuestItemsApi.md#get_items_quest_search) | **GET** /{game}/{language}/items/quest/search | Search Quest Items
*ResourcesApi* | [**get_all_items_resources_list**](docs/ResourcesApi.md#get_all_items_resources_list) | **GET** /{game}/{language}/items/resources/all | List All Resources
*ResourcesApi* | [**get_items_resource_search**](docs/ResourcesApi.md#get_items_resource_search) | **GET** /{game}/{language}/items/resources/search | Search Resources
*ResourcesApi* | [**get_items_resources_list**](docs/ResourcesApi.md#get_items_resources_list) | **GET** /{game}/{language}/items/resources | List Resources
*ResourcesApi* | [**get_items_resources_single**](docs/ResourcesApi.md#get_items_resources_single) | **GET** /{game}/{language}/items/resources/{ankama_id} | Single Resources
*SetsApi* | [**get_all_sets_list**](docs/SetsApi.md#get_all_sets_list) | **GET** /{game}/{language}/sets/all | List All Sets
*SetsApi* | [**get_sets_list**](docs/SetsApi.md#get_sets_list) | **GET** /{game}/{language}/sets | List Sets
*SetsApi* | [**get_sets_search**](docs/SetsApi.md#get_sets_search) | **GET** /{game}/{language}/sets/search | Search Sets
*SetsApi* | [**get_sets_single**](docs/SetsApi.md#get_sets_single) | **GET** /{game}/{language}/sets/{ankama_id} | Single Sets
*WebhooksApi* | [**delete_webhooks_almanax_id**](docs/WebhooksApi.md#delete_webhooks_almanax_id) | **DELETE** /webhooks/almanax/{id} | Unregister Almanax Hook
*WebhooksApi* | [**delete_webhooks_rss_id**](docs/WebhooksApi.md#delete_webhooks_rss_id) | **DELETE** /webhooks/rss/{id} | Unregister RSS Hook
*WebhooksApi* | [**delete_webhooks_twitter_id**](docs/WebhooksApi.md#delete_webhooks_twitter_id) | **DELETE** /webhooks/twitter/{id} | Unregister Twitter Hook
*WebhooksApi* | [**get_meta_webhooks_almanax**](docs/WebhooksApi.md#get_meta_webhooks_almanax) | **GET** /meta/webhooks/almanax | Get Almanax Hook Metainfo
*WebhooksApi* | [**get_meta_webhooks_rss**](docs/WebhooksApi.md#get_meta_webhooks_rss) | **GET** /meta/webhooks/rss | Get RSS Hook Metainfo
*WebhooksApi* | [**get_meta_webhooks_twitter**](docs/WebhooksApi.md#get_meta_webhooks_twitter) | **GET** /meta/webhooks/twitter | Get Twitter Hook Metainfo
*WebhooksApi* | [**get_webhooks_almanax_id**](docs/WebhooksApi.md#get_webhooks_almanax_id) | **GET** /webhooks/almanax/{id} | Get Almanax Hook
*WebhooksApi* | [**get_webhooks_rss_id**](docs/WebhooksApi.md#get_webhooks_rss_id) | **GET** /webhooks/rss/{id} | Get RSS Hook
*WebhooksApi* | [**get_webhooks_twitter_id**](docs/WebhooksApi.md#get_webhooks_twitter_id) | **GET** /webhooks/twitter/{id} | Get Twitter Hook
*WebhooksApi* | [**post_webhooks_almanax**](docs/WebhooksApi.md#post_webhooks_almanax) | **POST** /webhooks/almanax | Register Almanax Hook
*WebhooksApi* | [**post_webhooks_rss**](docs/WebhooksApi.md#post_webhooks_rss) | **POST** /webhooks/rss | Register RSS Hook
*WebhooksApi* | [**post_webhooks_twitter**](docs/WebhooksApi.md#post_webhooks_twitter) | **POST** /webhooks/twitter | Register Twitter Hook
*WebhooksApi* | [**put_webhooks_almanax_id**](docs/WebhooksApi.md#put_webhooks_almanax_id) | **PUT** /webhooks/almanax/{id} | Update Almanax Hook
*WebhooksApi* | [**put_webhooks_rss_id**](docs/WebhooksApi.md#put_webhooks_rss_id) | **PUT** /webhooks/rss/{id} | Update RSS Hook
*WebhooksApi* | [**put_webhooks_twitter_id**](docs/WebhooksApi.md#put_webhooks_twitter_id) | **PUT** /webhooks/twitter/{id} | Update Twitter Hook


## Documentation For Models

 - [AlmanaxEntry](docs/AlmanaxEntry.md)
 - [AlmanaxEntryBonus](docs/AlmanaxEntryBonus.md)
 - [AlmanaxEntryTribute](docs/AlmanaxEntryTribute.md)
 - [AlmanaxEntryTributeItem](docs/AlmanaxEntryTributeItem.md)
 - [AlmanaxWebhook](docs/AlmanaxWebhook.md)
 - [AlmanaxWebhookDailySettings](docs/AlmanaxWebhookDailySettings.md)
 - [ConditionEntry](docs/ConditionEntry.md)
 - [ConditionTreeLeaf](docs/ConditionTreeLeaf.md)
 - [ConditionTreeNode](docs/ConditionTreeNode.md)
 - [ConditionTreeRelation](docs/ConditionTreeRelation.md)
 - [Cosmetic](docs/Cosmetic.md)
 - [CosmeticType](docs/CosmeticType.md)
 - [CreateAlmanaxWebhook](docs/CreateAlmanaxWebhook.md)
 - [CreateAlmanaxWebhookDailySettings](docs/CreateAlmanaxWebhookDailySettings.md)
 - [CreateAlmanaxWebhookMentionsValueInner](docs/CreateAlmanaxWebhookMentionsValueInner.md)
 - [CreateRSSWebhook](docs/CreateRSSWebhook.md)
 - [CreateTwitterWebhook](docs/CreateTwitterWebhook.md)
 - [EffectsEntry](docs/EffectsEntry.md)
 - [Equipment](docs/Equipment.md)
 - [EquipmentSet](docs/EquipmentSet.md)
 - [GetGameSearch200ResponseInner](docs/GetGameSearch200ResponseInner.md)
 - [GetMetaAlmanaxBonuses200ResponseInner](docs/GetMetaAlmanaxBonuses200ResponseInner.md)
 - [GetMetaVersion200Response](docs/GetMetaVersion200Response.md)
 - [GetMetaWebhooksTwitter200Response](docs/GetMetaWebhooksTwitter200Response.md)
 - [ImageUrls](docs/ImageUrls.md)
 - [ItemListEntry](docs/ItemListEntry.md)
 - [ItemListEntryParentSet](docs/ItemListEntryParentSet.md)
 - [ItemListEntryRange](docs/ItemListEntryRange.md)
 - [ItemsListEntryTyped](docs/ItemsListEntryTyped.md)
 - [ItemsListEntryTypedType](docs/ItemsListEntryTypedType.md)
 - [ItemsListPaged](docs/ItemsListPaged.md)
 - [LinksPaged](docs/LinksPaged.md)
 - [Mount](docs/Mount.md)
 - [MountListEntry](docs/MountListEntry.md)
 - [MountsListPaged](docs/MountsListPaged.md)
 - [PutAlmanaxWebhook](docs/PutAlmanaxWebhook.md)
 - [PutRSSWebhook](docs/PutRSSWebhook.md)
 - [PutTwitterWebhook](docs/PutTwitterWebhook.md)
 - [RecipeEntry](docs/RecipeEntry.md)
 - [Resource](docs/Resource.md)
 - [RssWebhook](docs/RssWebhook.md)
 - [SetEffectsEntry](docs/SetEffectsEntry.md)
 - [SetEffectsEntryType](docs/SetEffectsEntryType.md)
 - [SetListEntry](docs/SetListEntry.md)
 - [SetsListPaged](docs/SetsListPaged.md)
 - [TwitterWebhook](docs/TwitterWebhook.md)
 - [Weapon](docs/Weapon.md)
 - [WeaponRange](docs/WeaponRange.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

stelzo@steado.de


