# dofusdude
# A project for you - the developer.
The free, always-up-to-date, low-latency, insert-buzzword-here Ankama API for your next cool project!

## Client SDKs
Don't write types or functions yourself - I already (kinda) did! 😉
- [Javascript](https://github.com/dofusdude/dofusdude-js) npm i dofusdude-js --save
- [Typescript](https://github.com/dofusdude/dofusdude-ts) npm i dofusdude-ts --save
- [Go](https://github.com/dofusdude/dodugo) go get -u github.com/dofusdude/dodugo
- [Python](https://github.com/dofusdude/dofusdude-py) pip install dofusdude
- [PHP](https://github.com/dofusdude/dofusdude-php)

Everything, including this site, is generated out of the [Docs Repo](https://github.com/dofusdude/api-docs). Consider it the Single Source of Truth. If there is a problem with the SDKs, create an issue there.

Your favorite language is missing? Please let me know!

# Main Features
- 🥷 **Seamless Auto-Update** load data in the background when a new Dofus version is released and serving it within 2 minutes with atomic data source switching. No downtime and no effects for the user, just always up-to-date.

- ⚡ **Blazingly Fast** all data in-memory, aggressive caching over short time spans, HTTP/2 multiplexing, written in Go, optimized for low latency, hosted on bare metal in 🇩🇪.

- 📨 **Discord Integration** Ankama related Twitter, RSS and Almanax feeds to post to Discord servers with advanced features like filters or mentions. Use the endpoints as a dev or the official [Web Client](https://discord.dofusdude.com) as a user.

- 🩸 **Dofus 2 Beta** from stable to bleeding edge by replacing /dofus2 with /dofus2beta.

- 🗣️ **Multilingual** supporting _en_, _fr_, _es_, _pt_ including the dropped languages from the Dofus website _de_ and _it_.

- 🧠 **Search by Relevance** allowing typos in name and description, handled by language specific text analysis and indexing by the powerful [Meilisearch](https://www.meilisearch.com) written in Rust.

- 🕵️ **Complete** actual data from the game including items invisible to the encyclopedia like quest items.

- 🖼️ **HD Images** rendering vector graphics into PNGs up to 800x800 px in the background.


## Current state
- Weapons ✅
- Equipment ✅
- Sets ✅
- Resources ✅
- Consumables ✅
- Pets ✅
- Mounts ✅
- Cosmetics/Ceremonial Items ✅
- Harnesses ✅
- Quest Items ✅
- Almanax ✅
- Monsters ❌
- Spells ❌

... and much more on the Roadmap on my Discord. 

## Deploy now. Use forever.
Everything you see here on this site, you can use now and forever. Updates could introduce new fields, new paths or parameter but never break backwards compatibility, so no field or parameter will be deleted.

There is one exception! **The API will _always_ choose being up-to-date over everything else**. So if Ankama decides to drop languages from the game like they did with their website, the API will loose support for them, too.

## Only the beginning... 🤯
I want this project to be useful and not just add plain GET-categories no one needs.

There is a long list of features I want to add (see the Roadmap on my [Discord](https://discord.gg/3EtHskZD8h)). But they are all focussed on you, the developers. So please let me know what you need. I will change the list based on demand.

# Get started! 🥳
Scroll down and try it for yourself!

Or see how these other awesome projects use it:
- [KaellyBot](https://github.com/Kaysoro/KaellyBot) by Kaysoro
- [Dofus Craftlist](https://dofuscraftlist-dev.netlify.app) by Lystina
- [AlmanaxApp](https://almanaxapp.netlify.app) by Lystina
- [DofuStuffSimulator](https://dofusstuffsimulator.netlify.app/)

I highly recommend using the SDKs for quick results. I use them myself for parts of the API.

## Thank you!
I highly welcome everyone on my [Discord](https://discord.gg/3EtHskZD8h) to just talk about projects and use cases or give feedback of any kind.

The servers have a fixed monthly cost to provide very fast responses. If you want to help me keeping them running or simply  donate, consider becoming a [GitHub Sponsor](https://github.com/sponsors/dofusdude).


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.7.2
- Package version: 0.7.2
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

import time
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
    api_instance = dofusdude.AllItemsApi(api_client)
    language = 'fr' # str | a valid language code
    game = 'dofus2' # str | 
    query = 'atcham' # str | case sensitive search query
    filter_type_name = 'Bottes' # str | only results with the translated type name across all item_subtypes (optional)
    filter_min_level = 190 # int | only results which level is equal or above this value (optional)
    filter_max_level = 200 # int | only results which level is equal or below this value (optional)
    limit = 8 # int | maximum number of returned results (optional) (default to 8)

    try:
        # Search All Items
        api_response = api_instance.get_items_all_search(language, game, query, filter_type_name=filter_type_name, filter_min_level=filter_min_level, filter_max_level=filter_max_level, limit=limit)
        print("The response of AllItemsApi->get_items_all_search:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AllItemsApi->get_items_all_search: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.dofusdu.de*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AllItemsApi* | [**get_items_all_search**](docs/AllItemsApi.md#get_items_all_search) | **GET** /{game}/{language}/items/search | Search All Items
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
*MetaApi* | [**get_meta_almanax_bonuses**](docs/MetaApi.md#get_meta_almanax_bonuses) | **GET** /dofus2/meta/{language}/almanax/bonuses | Available Almanax Bonuses
*MetaApi* | [**get_meta_elements**](docs/MetaApi.md#get_meta_elements) | **GET** /dofus2/meta/elements | Effects and Condition Elements
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
 - [ConditionEntryElement](docs/ConditionEntryElement.md)
 - [Cosmetic](docs/Cosmetic.md)
 - [CosmeticType](docs/CosmeticType.md)
 - [CreateAlmanaxWebhook](docs/CreateAlmanaxWebhook.md)
 - [CreateAlmanaxWebhookDailySettings](docs/CreateAlmanaxWebhookDailySettings.md)
 - [CreateAlmanaxWebhookMentionsValueInner](docs/CreateAlmanaxWebhookMentionsValueInner.md)
 - [CreateRSSWebhook](docs/CreateRSSWebhook.md)
 - [CreateTwitterWebhook](docs/CreateTwitterWebhook.md)
 - [EffectsEntry](docs/EffectsEntry.md)
 - [EffectsEntryType](docs/EffectsEntryType.md)
 - [Equipment](docs/Equipment.md)
 - [EquipmentParentSet](docs/EquipmentParentSet.md)
 - [EquipmentSet](docs/EquipmentSet.md)
 - [GetMetaAlmanaxBonuses200ResponseInner](docs/GetMetaAlmanaxBonuses200ResponseInner.md)
 - [GetMetaWebhooksTwitter200Response](docs/GetMetaWebhooksTwitter200Response.md)
 - [ImageUrls](docs/ImageUrls.md)
 - [ItemListEntry](docs/ItemListEntry.md)
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


