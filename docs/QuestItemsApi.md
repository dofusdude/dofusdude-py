# dofusdude.QuestItemsApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_items_quest_list**](QuestItemsApi.md#get_all_items_quest_list) | **GET** /{game}/v1/{language}/items/quest/all | List All Quest Items
[**get_item_quest_single**](QuestItemsApi.md#get_item_quest_single) | **GET** /{game}/v1/{language}/items/quest/{ankama_id} | Single Quest Items
[**get_items_quest_list**](QuestItemsApi.md#get_items_quest_list) | **GET** /{game}/v1/{language}/items/quest | List Quest Items
[**get_items_quest_search**](QuestItemsApi.md#get_items_quest_search) | **GET** /{game}/v1/{language}/items/quest/search | Search Quest Items


# **get_all_items_quest_list**
> ListItems get_all_items_quest_list(language, game, sort_level=sort_level, filter_min_level=filter_min_level, filter_max_level=filter_max_level, accept_encoding=accept_encoding, filter_type_name_id=filter_type_name_id)

List All Quest Items

Retrieve all quest items with one request. This endpoint is just an alias for the a list with disabled pagination (page[size]=-1) and all fields[type] set.

If you want everything unfiltered, delete the other query parameters.

Be careful with testing or (god forbid) using /all in your browser, the returned json is huge and will slow down the browser!

Tip: set the HTTP Header 'Accept-Encoding: gzip' for saving bandwidth. You will need to uncompress it on your end.
Example with cURL:
```
curl -sH 'Accept-Encoding: gzip' <api-endpoint> | gunzip -
```

### Example


```python
import dofusdude
from dofusdude.models.list_items import ListItems
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
    api_instance = dofusdude.QuestItemsApi(api_client)
    language = 'fr' # str | a valid language code
    game = 'dofus3' # str | game main 'dofus3' or beta channel 'dofus3beta'
    sort_level = 'desc' # str | sort the resulting list by level, default unsorted (optional)
    filter_min_level = 1 # int | only results which level is equal or above this value (optional)
    filter_max_level = 50 # int | only results which level is equal or below this value (optional)
    accept_encoding = 'accept_encoding_example' # str | optional compression for saving bandwidth (optional)
    filter_type_name_id = ['[\"kwismas-island\"]'] # List[str] | multi-filter results with the english type name. Add with \"wood\" or \"+wood\" and exclude with \"-wood\". (optional)

    try:
        # List All Quest Items
        api_response = api_instance.get_all_items_quest_list(language, game, sort_level=sort_level, filter_min_level=filter_min_level, filter_max_level=filter_max_level, accept_encoding=accept_encoding, filter_type_name_id=filter_type_name_id)
        print("The response of QuestItemsApi->get_all_items_quest_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestItemsApi->get_all_items_quest_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code | 
 **game** | **str**| game main &#39;dofus3&#39; or beta channel &#39;dofus3beta&#39; | 
 **sort_level** | **str**| sort the resulting list by level, default unsorted | [optional] 
 **filter_min_level** | **int**| only results which level is equal or above this value | [optional] 
 **filter_max_level** | **int**| only results which level is equal or below this value | [optional] 
 **accept_encoding** | **str**| optional compression for saving bandwidth | [optional] 
 **filter_type_name_id** | [**List[str]**](str.md)| multi-filter results with the english type name. Add with \&quot;wood\&quot; or \&quot;+wood\&quot; and exclude with \&quot;-wood\&quot;. | [optional] 

### Return type

[**ListItems**](ListItems.md)

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

# **get_item_quest_single**
> Resource get_item_quest_single(language, ankama_id, game)

Single Quest Items

Retrieve a specific quest item with id.

### Example


```python
import dofusdude
from dofusdude.models.resource import Resource
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
    api_instance = dofusdude.QuestItemsApi(api_client)
    language = 'language_example' # str | a valid language code
    ankama_id = 25256 # int | identifier
    game = 'dofus3' # str | game main 'dofus3' or beta channel 'dofus3beta'

    try:
        # Single Quest Items
        api_response = api_instance.get_item_quest_single(language, ankama_id, game)
        print("The response of QuestItemsApi->get_item_quest_single:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestItemsApi->get_item_quest_single: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code | 
 **ankama_id** | **int**| identifier | 
 **game** | **str**| game main &#39;dofus3&#39; or beta channel &#39;dofus3beta&#39; | 

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
**200** |  |  -  |
**400** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_quest_list**
> ListItems get_items_quest_list(language, game, sort_level=sort_level, filter_min_level=filter_min_level, filter_max_level=filter_max_level, page_size=page_size, page_number=page_number, fields_item=fields_item, filter_type_name_id=filter_type_name_id)

List Quest Items

Retrieve a list of quest items.

### Example


```python
import dofusdude
from dofusdude.models.list_items import ListItems
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
    api_instance = dofusdude.QuestItemsApi(api_client)
    language = 'fr' # str | a valid language code
    game = 'dofus3' # str | game main 'dofus3' or beta channel 'dofus3beta'
    sort_level = 'desc' # str | sort the resulting list by level, default unsorted (optional)
    filter_min_level = 1 # int | only results which level is equal or above this value (optional)
    filter_max_level = 50 # int | only results which level is equal or below this value (optional)
    page_size = 5 # int | size of the results from the list. -1 disables pagination and gets all in one response. (optional)
    page_number = 1 # int | page number based on the current page[size]. So you could get page 1 with 8 entrys and page 2 would have entries 8 to 16. (optional)
    fields_item = ['[\"recipe\"]'] # List[str] | adds fields from their detail endpoint to the item list entries. Multiple comma separated values allowed. (optional)
    filter_type_name_id = ['[\"sufokia\"]'] # List[str] | multi-filter results with the english type name. Add with \"wood\" or \"+wood\" and exclude with \"-wood\". (optional)

    try:
        # List Quest Items
        api_response = api_instance.get_items_quest_list(language, game, sort_level=sort_level, filter_min_level=filter_min_level, filter_max_level=filter_max_level, page_size=page_size, page_number=page_number, fields_item=fields_item, filter_type_name_id=filter_type_name_id)
        print("The response of QuestItemsApi->get_items_quest_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestItemsApi->get_items_quest_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code | 
 **game** | **str**| game main &#39;dofus3&#39; or beta channel &#39;dofus3beta&#39; | 
 **sort_level** | **str**| sort the resulting list by level, default unsorted | [optional] 
 **filter_min_level** | **int**| only results which level is equal or above this value | [optional] 
 **filter_max_level** | **int**| only results which level is equal or below this value | [optional] 
 **page_size** | **int**| size of the results from the list. -1 disables pagination and gets all in one response. | [optional] 
 **page_number** | **int**| page number based on the current page[size]. So you could get page 1 with 8 entrys and page 2 would have entries 8 to 16. | [optional] 
 **fields_item** | [**List[str]**](str.md)| adds fields from their detail endpoint to the item list entries. Multiple comma separated values allowed. | [optional] 
 **filter_type_name_id** | [**List[str]**](str.md)| multi-filter results with the english type name. Add with \&quot;wood\&quot; or \&quot;+wood\&quot; and exclude with \&quot;-wood\&quot;. | [optional] 

### Return type

[**ListItems**](ListItems.md)

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

# **get_items_quest_search**
> List[ListItem] get_items_quest_search(language, game, query, filter_min_level=filter_min_level, filter_max_level=filter_max_level, limit=limit, filter_type_name_id=filter_type_name_id)

Search Quest Items

Search in all names and descriptions of quest items with a query.

### Example


```python
import dofusdude
from dofusdude.models.list_item import ListItem
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
    api_instance = dofusdude.QuestItemsApi(api_client)
    language = 'es' # str | a valid language code
    game = 'dofus3' # str | game main 'dofus3' or beta channel 'dofus3beta'
    query = 'Ficha' # str | case sensitive search query
    filter_min_level = 60 # int | only results which level is equal or above this value (optional)
    filter_max_level = 70 # int | only results which level is equal or below this value (optional)
    limit = 8 # int | maximum number of returned results (optional) (default to 8)
    filter_type_name_id = ['[\"vigilantes\"]'] # List[str] | multi-filter results with the english type name. Add with \"wood\" or \"+wood\" and exclude with \"-wood\". (optional)

    try:
        # Search Quest Items
        api_response = api_instance.get_items_quest_search(language, game, query, filter_min_level=filter_min_level, filter_max_level=filter_max_level, limit=limit, filter_type_name_id=filter_type_name_id)
        print("The response of QuestItemsApi->get_items_quest_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestItemsApi->get_items_quest_search: %s\n" % e)
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

[**List[ListItem]**](ListItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quest Items Found |  -  |
**400** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

