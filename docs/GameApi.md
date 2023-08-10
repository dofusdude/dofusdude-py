# dofusdude.GameApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_game_search**](GameApi.md#get_game_search) | **GET** /{game}/{language}/search | Game Search
[**get_items_all_search**](GameApi.md#get_items_all_search) | **GET** /{game}/{language}/items/search | Search All Items


# **get_game_search**
> List[GetGameSearch200ResponseInner] get_game_search(language, game, query, filter_type=filter_type, limit=limit, fields_item=fields_item)

Game Search

Search in all names and descriptions of all supported types in the game. For the list of supported types see the endpoint /dofus2/meta/search/types.

### Example

```python
import time
import os
import dofusdude
from dofusdude.models.get_game_search200_response_inner import GetGameSearch200ResponseInner
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
    api_instance = dofusdude.GameApi(api_client)
    language = 'language_example' # str | a valid language code
    game = 'dofus2' # str | 
    query = 'paztek' # str | search query
    filter_type = ['[\"items-equipment\"]'] # List[str] | only results with all specific type (optional)
    limit = 8 # int | maximum number of returned results (optional) (default to 8)
    fields_item = ['[\"level\"]'] # List[str] | adds fields from the item search to the list entries if the hit is a item. Multiple comma separated values allowed. (optional)

    try:
        # Game Search
        api_response = api_instance.get_game_search(language, game, query, filter_type=filter_type, limit=limit, fields_item=fields_item)
        print("The response of GameApi->get_game_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->get_game_search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code | 
 **game** | **str**|  | 
 **query** | **str**| search query | 
 **filter_type** | [**List[str]**](str.md)| only results with all specific type | [optional] 
 **limit** | **int**| maximum number of returned results | [optional] [default to 8]
 **fields_item** | [**List[str]**](str.md)| adds fields from the item search to the list entries if the hit is a item. Multiple comma separated values allowed. | [optional] 

### Return type

[**List[GetGameSearch200ResponseInner]**](GetGameSearch200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Game Search Result |  -  |
**400** | Bad Request  Possibilities: - empty or no query - filter[type] does not exist  |  -  |
**404** | Not Found  Possibilities: - no hits for query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_all_search**
> List[ItemsListEntryTyped] get_items_all_search(language, game, query, filter_type_name=filter_type_name, filter_min_level=filter_min_level, filter_max_level=filter_max_level, limit=limit)

Search All Items

Search in all names and descriptions of Dofus items (including all subtypes) with a query.

### Example

```python
import time
import os
import dofusdude
from dofusdude.models.items_list_entry_typed import ItemsListEntryTyped
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
    api_instance = dofusdude.GameApi(api_client)
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
        print("The response of GameApi->get_items_all_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->get_items_all_search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code | 
 **game** | **str**|  | 
 **query** | **str**| case sensitive search query | 
 **filter_type_name** | **str**| only results with the translated type name across all item_subtypes | [optional] 
 **filter_min_level** | **int**| only results which level is equal or above this value | [optional] 
 **filter_max_level** | **int**| only results which level is equal or below this value | [optional] 
 **limit** | **int**| maximum number of returned results | [optional] [default to 8]

### Return type

[**List[ItemsListEntryTyped]**](ItemsListEntryTyped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Items Found |  -  |
**400** | Bad Request  Possibilities: - empty or no query  |  -  |
**404** | Not Found  Possibilities: - no hits for query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

