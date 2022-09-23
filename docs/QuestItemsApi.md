# dofusdude.QuestItemsApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_item_quest_single**](QuestItemsApi.md#get_item_quest_single) | **GET** /{game}/{language}/items/quest/{ankama_id} | Single Quest Items
[**get_items_quest_list**](QuestItemsApi.md#get_items_quest_list) | **GET** /{game}/{language}/items/quest | List Quest Items
[**get_items_quest_search**](QuestItemsApi.md#get_items_quest_search) | **GET** /{game}/{language}/items/quest/search | Search Quest Items


# **get_item_quest_single**
> Resource get_item_quest_single(language, ankama_id, game)

Single Quest Items

Retrieve a specific quest item with id.

### Example


```python
import time
import dofusdude
from dofusdude.api import quest_items_api
from dofusdude.model.resource import Resource
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = quest_items_api.QuestItemsApi(api_client)
    language = "en" # str | a valid language code
    ankama_id = 25256 # int | identifier
    game = "dofus2" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Single Quest Items
        api_response = api_instance.get_item_quest_single(language, ankama_id, game)
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling QuestItemsApi->get_item_quest_single: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code |
 **ankama_id** | **int**| identifier |
 **game** | **str**|  |

### Return type

[**Resource**](Resource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quest Item Found |  -  |
**400** | Bad Request  Possibilities: - invalid ankama id format  |  -  |
**404** | Not Found  Possibilities: - nothing found for this ankama_id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_quest_list**
> ItemsListPaged get_items_quest_list(language, game)

List Quest Items

Retrieve a list of quest items.

### Example


```python
import time
import dofusdude
from dofusdude.api import quest_items_api
from dofusdude.model.items_list_paged import ItemsListPaged
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = quest_items_api.QuestItemsApi(api_client)
    language = "en" # str | a valid language code
    game = "dofus2" # str | 
    sort_level = "asc" # str | sort the resulting list by level, default unsorted (optional)
    filter_type_name = "filter[type_name]_example" # str | only results with the translated type name (optional)
    filter_min_level = 1 # int | only results which level is equal or above this value (optional)
    filter_max_level = 1 # int | only results which level is equal or below this value (optional)
    page_size = -1 # int | size of the results from the list. -1 disables pagination and gets all in one response. (optional)
    page_number = 0 # int | page number based on the current page[size]. So you could get page 1 with 8 entrys and page 2 would have entries 8 to 16. (optional)
    fields_item = "recipe" # str | adds fields from their detail endpoint to the item list entries. Multiple comma separated values allowed. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Quest Items
        api_response = api_instance.get_items_quest_list(language, game)
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling QuestItemsApi->get_items_quest_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Quest Items
        api_response = api_instance.get_items_quest_list(language, game, sort_level=sort_level, filter_type_name=filter_type_name, filter_min_level=filter_min_level, filter_max_level=filter_max_level, page_size=page_size, page_number=page_number, fields_item=fields_item)
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling QuestItemsApi->get_items_quest_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code |
 **game** | **str**|  |
 **sort_level** | **str**| sort the resulting list by level, default unsorted | [optional]
 **filter_type_name** | **str**| only results with the translated type name | [optional]
 **filter_min_level** | **int**| only results which level is equal or above this value | [optional]
 **filter_max_level** | **int**| only results which level is equal or below this value | [optional]
 **page_size** | **int**| size of the results from the list. -1 disables pagination and gets all in one response. | [optional]
 **page_number** | **int**| page number based on the current page[size]. So you could get page 1 with 8 entrys and page 2 would have entries 8 to 16. | [optional]
 **fields_item** | **str**| adds fields from their detail endpoint to the item list entries. Multiple comma separated values allowed. | [optional]

### Return type

[**ItemsListPaged**](ItemsListPaged.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quest Items Found |  -  |
**400** | Bad Request  |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_quest_search**
> [ItemListEntry] get_items_quest_search(language, game, query)

Search Quest Items

Search in all names and descriptions of quest items with a query.

### Example


```python
import time
import dofusdude
from dofusdude.api import quest_items_api
from dofusdude.model.item_list_entry import ItemListEntry
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = quest_items_api.QuestItemsApi(api_client)
    language = "en" # str | a valid language code
    game = "dofus2" # str | 
    query = "sufo" # str | case sensitive search query
    filter_type_name = "filter[type_name]_example" # str | only results with the translated type name (optional)
    filter_min_level = 1 # int | only results which level is equal or above this value (optional)
    filter_max_level = 1 # int | only results which level is equal or below this value (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search Quest Items
        api_response = api_instance.get_items_quest_search(language, game, query)
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling QuestItemsApi->get_items_quest_search: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Quest Items
        api_response = api_instance.get_items_quest_search(language, game, query, filter_type_name=filter_type_name, filter_min_level=filter_min_level, filter_max_level=filter_max_level)
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling QuestItemsApi->get_items_quest_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code |
 **game** | **str**|  |
 **query** | **str**| case sensitive search query |
 **filter_type_name** | **str**| only results with the translated type name | [optional]
 **filter_min_level** | **int**| only results which level is equal or above this value | [optional]
 **filter_max_level** | **int**| only results which level is equal or below this value | [optional]

### Return type

[**[ItemListEntry]**](ItemListEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quest Items Found |  -  |
**400** | Bad Request  Possibilities: - empty or no query  |  -  |
**404** | Not Found  Possibilities: - no hits for query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

