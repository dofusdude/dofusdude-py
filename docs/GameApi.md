# dofusdude.GameApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_game_search**](GameApi.md#get_game_search) | **GET** /{game}/v1/{language}/search | Game Search
[**get_items_all_search**](GameApi.md#get_items_all_search) | **GET** /{game}/v1/{language}/items/search | Search All Items


# **get_game_search**
> List[GameSearch] get_game_search(language, game, query, filter_search_index=filter_search_index, limit=limit, fields_item=fields_item, filter_type_name_id=filter_type_name_id)

Game Search

Search in all names and descriptions of all supported types in the game. For the list of supported types see the endpoint /dofus3/meta/search/types.

### Example


```python
import dofusdude
from dofusdude.models.game_search import GameSearch
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
    game = 'dofus3beta' # str | game main 'dofus3' or beta channel 'dofus3beta'
    query = 'paztek' # str | search query
    filter_search_index = ['[\"items-equipment\"]'] # List[str] | only results with all specific type (optional)
    limit = 8 # int | maximum number of returned results (optional) (default to 8)
    fields_item = ['[\"level\"]'] # List[str] | adds fields from the item search to the list entries if the hit is a item. Multiple comma separated values allowed. (optional)
    filter_type_name_id = ['[\"boots\"]'] # List[str] | multi-filter results with the english item type name, including \"mount\" and \"set\" from filter[type]. Add with \"wood\" or \"+wood\" and exclude with \"-wood\". (optional)

    try:
        # Game Search
        api_response = api_instance.get_game_search(language, game, query, filter_search_index=filter_search_index, limit=limit, fields_item=fields_item, filter_type_name_id=filter_type_name_id)
        print("The response of GameApi->get_game_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->get_game_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code | 
 **game** | **str**| game main &#39;dofus3&#39; or beta channel &#39;dofus3beta&#39; | 
 **query** | **str**| search query | 
 **filter_search_index** | [**List[str]**](str.md)| only results with all specific type | [optional] 
 **limit** | **int**| maximum number of returned results | [optional] [default to 8]
 **fields_item** | [**List[str]**](str.md)| adds fields from the item search to the list entries if the hit is a item. Multiple comma separated values allowed. | [optional] 
 **filter_type_name_id** | [**List[str]**](str.md)| multi-filter results with the english item type name, including \&quot;mount\&quot; and \&quot;set\&quot; from filter[type]. Add with \&quot;wood\&quot; or \&quot;+wood\&quot; and exclude with \&quot;-wood\&quot;. | [optional] 

### Return type

[**List[GameSearch]**](GameSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_all_search**
> List[ListItemGeneral] get_items_all_search(language, game, query, filter_min_level=filter_min_level, filter_max_level=filter_max_level, limit=limit, filter_type_name_id=filter_type_name_id)

Search All Items

Search in all names and descriptions of Dofus items (including all subtypes) with a query.

### Example


```python
import dofusdude
from dofusdude.models.list_item_general import ListItemGeneral
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
    game = 'dofus3beta' # str | game main 'dofus3' or beta channel 'dofus3beta'
    query = 'atcham' # str | case sensitive search query
    filter_min_level = 190 # int | only results which level is equal or above this value (optional)
    filter_max_level = 200 # int | only results which level is equal or below this value (optional)
    limit = 8 # int | maximum number of returned results (optional) (default to 8)
    filter_type_name_id = ['[\"boots\"]'] # List[str] | multi-filter results with the english type name. Add with \"wood\" or \"+wood\" and exclude with \"-wood\". (optional)

    try:
        # Search All Items
        api_response = api_instance.get_items_all_search(language, game, query, filter_min_level=filter_min_level, filter_max_level=filter_max_level, limit=limit, filter_type_name_id=filter_type_name_id)
        print("The response of GameApi->get_items_all_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->get_items_all_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code | 
 **game** | **str**| game main &#39;dofus3&#39; or beta channel &#39;dofus3beta&#39; | 
 **query** | **str**| case sensitive search query | 
 **filter_min_level** | **int**| only results which level is equal or above this value | [optional] 
 **filter_max_level** | **int**| only results which level is equal or below this value | [optional] 
 **limit** | **int**| maximum number of returned results | [optional] [default to 8]
 **filter_type_name_id** | [**List[str]**](str.md)| multi-filter results with the english type name. Add with \&quot;wood\&quot; or \&quot;+wood\&quot; and exclude with \&quot;-wood\&quot;. | [optional] 

### Return type

[**List[ListItemGeneral]**](ListItemGeneral.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

