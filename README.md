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

I highly recommend using the SDKs for quick results. I use them myself for microservices for the API.

## Thank you!
I highly welcome everyone on my [Discord](https://discord.gg/3EtHskZD8h) to just talk about projects and use cases or give feedback of any kind.

The servers have a fixed monthly cost to provide very fast responses. If you want to help me keeping them running or simply  donate, consider becoming a [GitHub Sponsor](https://github.com/sponsors/dofusdude).


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.7.1
- Package version: 0.7.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://discord.gg/3EtHskZD8h](https://discord.gg/3EtHskZD8h)

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


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

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import dofusdude
from pprint import pprint
from dofusdude.apis.tags import all_items_api
from dofusdude.model.items_list_entry_typed import ItemsListEntryTyped
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_items_api.AllItemsApi(api_client)
    language = "fr" # str | a valid language code
game = "dofus2" # str | 
query = "atcham" # str | case sensitive search query
filter_type_name = "Bottes" # str | only results with the translated type name across all item_subtypes (optional)
filter_min_level = 190 # int | only results which level is equal or above this value (optional)
filter_max_level = 200 # int | only results which level is equal or below this value (optional)
limit = 8 # int | maximum number of returned results (optional) (default to CodegenParameter{isFormParam=false, isQueryParam=true, isPathParam=false, isHeaderParam=false, isCookieParam=false, isBodyParam=false, isContainer=false, isCollectionFormatMulti=false, isPrimitiveType=true, isModel=false, isExplode=true, baseName='limit', paramName='limit', dataType='int', datatypeWithEnum='null', dataFormat='null', collectionFormat='null', description='maximum number of returned results', unescapedDescription='maximum number of returned results', baseType='null', defaultValue='8', enumDefaultValue='null', enumName='null', style='FORM', deepObject='false', allowEmptyValue='false', example='8', jsonSchema='{
  "name" : "limit",
  "in" : "query",
  "description" : "maximum number of returned results",
  "required" : false,
  "style" : "form",
  "explode" : true,
  "schema" : {
    "maximum" : 100,
    "minimum" : 1,
    "type" : "integer",
    "example" : 8,
    "default" : 8
  }
}', isString=false, isNumeric=false, isInteger=true, isShort=false, isLong=false, isUnboundedInteger=true, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isFreeFormObject=false, isAnyType=false, isArray=false, isMap=false, isFile=false, isEnum=false, _enum=null, allowableValues=null, items=null, mostInnerItems=null, additionalProperties=null, vars=[], requiredVars=[], vendorExtensions={}, hasValidation=true, maxProperties=null, minProperties=null, isNullable=false, isDeprecated=false, required=false, maximum='100', exclusiveMaximum=false, minimum='1', exclusiveMinimum=false, maxLength=null, minLength=null, pattern='null', maxItems=null, minItems=null, uniqueItems=false, uniqueItemsBoolean=null, contentType=null, multipleOf=null, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, schema=CodegenProperty{openApiType='integer', baseName='LimitSchema', complexType='null', getter='getLimit', setter='setLimit', description='null', dataType='int', datatypeWithEnum='int', dataFormat='null', name='limit', min='null', max='null', defaultValue='8', defaultValueWithParam=' = data.limit;', baseType='int', containerType='null', title='null', unescapedDescription='null', maxLength=null, minLength=null, pattern='null', example='8', jsonSchema='{
  "maximum" : 100,
  "minimum" : 1,
  "type" : "integer",
  "example" : 8,
  "default" : 8
}', minimum='1', maximum='100', exclusiveMinimum=false, exclusiveMaximum=false, required=false, deprecated=false, hasMoreNonReadOnly=false, isPrimitiveType=true, isModel=false, isContainer=false, isString=false, isNumeric=false, isInteger=true, isShort=false, isLong=false, isUnboundedInteger=true, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isFile=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isFreeFormObject=false, isArray=false, isMap=false, isEnum=false, isInnerEnum=false, isEnumRef=false, isAnyType=false, isReadOnly=false, isWriteOnly=false, isNullable=false, isSelfReference=false, isCircularReference=false, isDiscriminator=false, _enum=null, allowableValues=null, items=null, additionalProperties=null, vars=[], requiredVars=[], mostInnerItems=null, vendorExtensions={}, hasValidation=true, isInherited=false, discriminatorValue='null', nameInCamelCase='Limit', nameInSnakeCase='null', enumName='null', maxItems=null, minItems=null, maxProperties=null, minProperties=null, uniqueItems=false, uniqueItemsBoolean=null, multipleOf=null, isXmlAttribute=false, xmlPrefix='null', xmlName='null', xmlNamespace='null', isXmlWrapped=false, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false, isBooleanSchemaTrue=false, isBooleanSchemaFalse=false, format=null, dependentRequired=null, contains=null}, content=null, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false})

    try:
        # Search All Items
        api_response = api_instance.get_items_all_search(languagegamequeryfilter_type_name=filter_type_namefilter_min_level=filter_min_levelfilter_max_level=filter_max_levellimit=limit)
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling AllItemsApi->get_items_all_search: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.dofusdu.de*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AllItemsApi* | [**get_items_all_search**](docs/apis/tags/AllItemsApi.md#get_items_all_search) | **get** /{game}/{language}/items/search | Search All Items
*AlmanaxApi* | [**get_almanax_date**](docs/apis/tags/AlmanaxApi.md#get_almanax_date) | **get** /dofus2/{language}/almanax/{date} | Single Almanax Date
*AlmanaxApi* | [**get_almanax_range**](docs/apis/tags/AlmanaxApi.md#get_almanax_range) | **get** /dofus2/{language}/almanax | Almanax Range
*ConsumablesApi* | [**get_all_items_consumables_list**](docs/apis/tags/ConsumablesApi.md#get_all_items_consumables_list) | **get** /{game}/{language}/items/consumables/all | List All Consumables
*ConsumablesApi* | [**get_items_consumables_list**](docs/apis/tags/ConsumablesApi.md#get_items_consumables_list) | **get** /{game}/{language}/items/consumables | List Consumables
*ConsumablesApi* | [**get_items_consumables_search**](docs/apis/tags/ConsumablesApi.md#get_items_consumables_search) | **get** /{game}/{language}/items/consumables/search | Search Consumables
*ConsumablesApi* | [**get_items_consumables_single**](docs/apis/tags/ConsumablesApi.md#get_items_consumables_single) | **get** /{game}/{language}/items/consumables/{ankama_id} | Single Consumables
*CosmeticsApi* | [**get_all_cosmetics_list**](docs/apis/tags/CosmeticsApi.md#get_all_cosmetics_list) | **get** /{game}/{language}/items/cosmetics/all | List All Cosmetics
*CosmeticsApi* | [**get_cosmetics_list**](docs/apis/tags/CosmeticsApi.md#get_cosmetics_list) | **get** /{game}/{language}/items/cosmetics | List Cosmetics
*CosmeticsApi* | [**get_cosmetics_search**](docs/apis/tags/CosmeticsApi.md#get_cosmetics_search) | **get** /{game}/{language}/items/cosmetics/search | Search Cosmetics
*CosmeticsApi* | [**get_cosmetics_single**](docs/apis/tags/CosmeticsApi.md#get_cosmetics_single) | **get** /{game}/{language}/items/cosmetics/{ankama_id} | Single Cosmetics
*EquipmentApi* | [**get_all_items_equipment_list**](docs/apis/tags/EquipmentApi.md#get_all_items_equipment_list) | **get** /{game}/{language}/items/equipment/all | List All Equipment
*EquipmentApi* | [**get_items_equipment_list**](docs/apis/tags/EquipmentApi.md#get_items_equipment_list) | **get** /{game}/{language}/items/equipment | List Equipment
*EquipmentApi* | [**get_items_equipment_search**](docs/apis/tags/EquipmentApi.md#get_items_equipment_search) | **get** /{game}/{language}/items/equipment/search | Search Equipment
*EquipmentApi* | [**get_items_equipment_single**](docs/apis/tags/EquipmentApi.md#get_items_equipment_single) | **get** /{game}/{language}/items/equipment/{ankama_id} | Single Equipment
*MetaApi* | [**get_meta_almanax_bonuses**](docs/apis/tags/MetaApi.md#get_meta_almanax_bonuses) | **get** /dofus2/meta/{language}/almanax/bonuses | Available Almanax Bonuses
*MetaApi* | [**get_meta_elements**](docs/apis/tags/MetaApi.md#get_meta_elements) | **get** /dofus2/meta/elements | Effects and Condition Elements
*MountsApi* | [**get_all_mounts_list**](docs/apis/tags/MountsApi.md#get_all_mounts_list) | **get** /{game}/{language}/mounts/all | List All Mounts
*MountsApi* | [**get_mounts_list**](docs/apis/tags/MountsApi.md#get_mounts_list) | **get** /{game}/{language}/mounts | List Mounts
*MountsApi* | [**get_mounts_search**](docs/apis/tags/MountsApi.md#get_mounts_search) | **get** /{game}/{language}/mounts/search | Search Mounts
*MountsApi* | [**get_mounts_single**](docs/apis/tags/MountsApi.md#get_mounts_single) | **get** /{game}/{language}/mounts/{ankama_id} | Single Mounts
*QuestItemsApi* | [**get_all_items_quest_list**](docs/apis/tags/QuestItemsApi.md#get_all_items_quest_list) | **get** /{game}/{language}/items/quest/all | List All Quest Items
*QuestItemsApi* | [**get_item_quest_single**](docs/apis/tags/QuestItemsApi.md#get_item_quest_single) | **get** /{game}/{language}/items/quest/{ankama_id} | Single Quest Items
*QuestItemsApi* | [**get_items_quest_list**](docs/apis/tags/QuestItemsApi.md#get_items_quest_list) | **get** /{game}/{language}/items/quest | List Quest Items
*QuestItemsApi* | [**get_items_quest_search**](docs/apis/tags/QuestItemsApi.md#get_items_quest_search) | **get** /{game}/{language}/items/quest/search | Search Quest Items
*ResourcesApi* | [**get_all_items_resources_list**](docs/apis/tags/ResourcesApi.md#get_all_items_resources_list) | **get** /{game}/{language}/items/resources/all | List All Resources
*ResourcesApi* | [**get_items_resource_search**](docs/apis/tags/ResourcesApi.md#get_items_resource_search) | **get** /{game}/{language}/items/resources/search | Search Resources
*ResourcesApi* | [**get_items_resources_list**](docs/apis/tags/ResourcesApi.md#get_items_resources_list) | **get** /{game}/{language}/items/resources | List Resources
*ResourcesApi* | [**get_items_resources_single**](docs/apis/tags/ResourcesApi.md#get_items_resources_single) | **get** /{game}/{language}/items/resources/{ankama_id} | Single Resources
*SetsApi* | [**get_all_sets_list**](docs/apis/tags/SetsApi.md#get_all_sets_list) | **get** /{game}/{language}/sets/all | List All Sets
*SetsApi* | [**get_sets_list**](docs/apis/tags/SetsApi.md#get_sets_list) | **get** /{game}/{language}/sets | List Sets
*SetsApi* | [**get_sets_search**](docs/apis/tags/SetsApi.md#get_sets_search) | **get** /{game}/{language}/sets/search | Search Sets
*SetsApi* | [**get_sets_single**](docs/apis/tags/SetsApi.md#get_sets_single) | **get** /{game}/{language}/sets/{ankama_id} | Single Sets
*WebhooksApi* | [**delete_webhooks_almanax_id**](docs/apis/tags/WebhooksApi.md#delete_webhooks_almanax_id) | **delete** /webhooks/almanax/{id} | Unregister Almanax Hook
*WebhooksApi* | [**delete_webhooks_rss_id**](docs/apis/tags/WebhooksApi.md#delete_webhooks_rss_id) | **delete** /webhooks/rss/{id} | Unregister RSS Hook
*WebhooksApi* | [**delete_webhooks_twitter_id**](docs/apis/tags/WebhooksApi.md#delete_webhooks_twitter_id) | **delete** /webhooks/twitter/{id} | Unregister Twitter Hook
*WebhooksApi* | [**get_meta_webhooks_almanax**](docs/apis/tags/WebhooksApi.md#get_meta_webhooks_almanax) | **get** /meta/webhooks/almanax | Get Almanax Hook Metainfo
*WebhooksApi* | [**get_meta_webhooks_rss**](docs/apis/tags/WebhooksApi.md#get_meta_webhooks_rss) | **get** /meta/webhooks/rss | Get RSS Hook Metainfo
*WebhooksApi* | [**get_meta_webhooks_twitter**](docs/apis/tags/WebhooksApi.md#get_meta_webhooks_twitter) | **get** /meta/webhooks/twitter | Get Twitter Hook Metainfo
*WebhooksApi* | [**get_webhooks_almanax_id**](docs/apis/tags/WebhooksApi.md#get_webhooks_almanax_id) | **get** /webhooks/almanax/{id} | Get Almanax Hook
*WebhooksApi* | [**get_webhooks_rss_id**](docs/apis/tags/WebhooksApi.md#get_webhooks_rss_id) | **get** /webhooks/rss/{id} | Get RSS Hook
*WebhooksApi* | [**get_webhooks_twitter_id**](docs/apis/tags/WebhooksApi.md#get_webhooks_twitter_id) | **get** /webhooks/twitter/{id} | Get Twitter Hook
*WebhooksApi* | [**post_webhooks_almanax**](docs/apis/tags/WebhooksApi.md#post_webhooks_almanax) | **post** /webhooks/almanax | Register Almanax Hook
*WebhooksApi* | [**post_webhooks_rss**](docs/apis/tags/WebhooksApi.md#post_webhooks_rss) | **post** /webhooks/rss | Register RSS Hook
*WebhooksApi* | [**post_webhooks_twitter**](docs/apis/tags/WebhooksApi.md#post_webhooks_twitter) | **post** /webhooks/twitter | Register Twitter Hook
*WebhooksApi* | [**put_webhooks_almanax_id**](docs/apis/tags/WebhooksApi.md#put_webhooks_almanax_id) | **put** /webhooks/almanax/{id} | Update Almanax Hook
*WebhooksApi* | [**put_webhooks_rss_id**](docs/apis/tags/WebhooksApi.md#put_webhooks_rss_id) | **put** /webhooks/rss/{id} | Update RSS Hook
*WebhooksApi* | [**put_webhooks_twitter_id**](docs/apis/tags/WebhooksApi.md#put_webhooks_twitter_id) | **put** /webhooks/twitter/{id} | Update Twitter Hook

## Documentation For Models

 - [AlmanaxEntry](docs/models/AlmanaxEntry.md)
 - [AlmanaxWebhook](docs/models/AlmanaxWebhook.md)
 - [ConditionEntry](docs/models/ConditionEntry.md)
 - [Cosmetic](docs/models/Cosmetic.md)
 - [CreateAlmanaxWebhook](docs/models/CreateAlmanaxWebhook.md)
 - [CreateRSSWebhook](docs/models/CreateRSSWebhook.md)
 - [CreateTwitterWebhook](docs/models/CreateTwitterWebhook.md)
 - [EffectsEntry](docs/models/EffectsEntry.md)
 - [Equipment](docs/models/Equipment.md)
 - [EquipmentSet](docs/models/EquipmentSet.md)
 - [ImageUrls](docs/models/ImageUrls.md)
 - [ItemListEntry](docs/models/ItemListEntry.md)
 - [ItemsListEntryTyped](docs/models/ItemsListEntryTyped.md)
 - [ItemsListPaged](docs/models/ItemsListPaged.md)
 - [LinksPaged](docs/models/LinksPaged.md)
 - [Mount](docs/models/Mount.md)
 - [MountListEntry](docs/models/MountListEntry.md)
 - [MountsListPaged](docs/models/MountsListPaged.md)
 - [PutAlmanaxWebhook](docs/models/PutAlmanaxWebhook.md)
 - [PutRSSWebhook](docs/models/PutRSSWebhook.md)
 - [PutTwitterWebhook](docs/models/PutTwitterWebhook.md)
 - [RecipeEntry](docs/models/RecipeEntry.md)
 - [Resource](docs/models/Resource.md)
 - [RssWebhook](docs/models/RssWebhook.md)
 - [SetListEntry](docs/models/SetListEntry.md)
 - [SetsListPaged](docs/models/SetsListPaged.md)
 - [TwitterWebhook](docs/models/TwitterWebhook.md)
 - [Weapon](docs/models/Weapon.md)

## Documentation For Authorization

 All endpoints do not require authorization.

## Author

stelzo@steado.de
stelzo@steado.de
stelzo@steado.de
stelzo@steado.de
stelzo@steado.de
stelzo@steado.de
stelzo@steado.de
stelzo@steado.de
stelzo@steado.de
stelzo@steado.de
stelzo@steado.de

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in dofusdude.apis and dofusdude.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from dofusdude.apis.default_api import DefaultApi`
- `from dofusdude.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import dofusdude
from dofusdude.apis import *
from dofusdude.models import *
```
