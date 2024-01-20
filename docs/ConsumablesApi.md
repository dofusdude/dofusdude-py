# dofusdude.ConsumablesApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_items_consumables_list**](ConsumablesApi.md#get_all_items_consumables_list) | **GET** /{game}/{language}/items/consumables/all | List All Consumables
[**get_items_consumables_list**](ConsumablesApi.md#get_items_consumables_list) | **GET** /{game}/{language}/items/consumables | List Consumables
[**get_items_consumables_search**](ConsumablesApi.md#get_items_consumables_search) | **GET** /{game}/{language}/items/consumables/search | Search Consumables
[**get_items_consumables_single**](ConsumablesApi.md#get_items_consumables_single) | **GET** /{game}/{language}/items/consumables/{ankama_id} | Single Consumables


# **get_all_items_consumables_list**
> ItemsListPaged get_all_items_consumables_list(language, game, sort_level=sort_level, filter_type_name=filter_type_name, filter_min_level=filter_min_level, filter_max_level=filter_max_level, accept_encoding=accept_encoding)

List All Consumables

Retrieve all consumable items with one request. This endpoint is just an alias for the a list with disabled pagination (page[size]=-1) and all fields[type] set.  If you want everything unfiltered, delete the other query parameters.  Be careful with testing or (god forbid) using /all in your browser, the returned json is huge and will slow down the browser!  Tip: set the HTTP Header 'Accept-Encoding: gzip' for saving bandwidth. You will need to uncompress it on your end. Example with cURL: ``` curl -sH 'Accept-Encoding: gzip' <api-endpoint> | gunzip - ```

### Example


```python
import dofusdude
from dofusdude.models.items_list_paged import ItemsListPaged
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
    api_instance = dofusdude.ConsumablesApi(api_client)
    language = 'language_example' # str | a valid language code
    game = 'dofus2' # str | 
    sort_level = 'asc' # str | sort the resulting list by level, default unsorted (optional)
    filter_type_name = 'Chest' # str | only results with the translated type name (optional)
    filter_min_level = 150 # int | only results which level is equal or above this value (optional)
    filter_max_level = 180 # int | only results which level is equal or below this value (optional)
    accept_encoding = 'accept_encoding_example' # str | optional compression for saving bandwidth (optional)

    try:
        # List All Consumables
        api_response = api_instance.get_all_items_consumables_list(language, game, sort_level=sort_level, filter_type_name=filter_type_name, filter_min_level=filter_min_level, filter_max_level=filter_max_level, accept_encoding=accept_encoding)
        print("The response of ConsumablesApi->get_all_items_consumables_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumablesApi->get_all_items_consumables_list: %s\n" % e)
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
 **accept_encoding** | **str**| optional compression for saving bandwidth | [optional] 

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
**200** | Consumables Found |  -  |
**400** | Bad Request  |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_consumables_list**
> ItemsListPaged get_items_consumables_list(language, game, sort_level=sort_level, filter_type_name=filter_type_name, filter_min_level=filter_min_level, filter_max_level=filter_max_level, page_size=page_size, page_number=page_number, fields_item=fields_item)

List Consumables

Retrieve a list of consumable items.

### Example


```python
import dofusdude
from dofusdude.models.items_list_paged import ItemsListPaged
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
    api_instance = dofusdude.ConsumablesApi(api_client)
    language = 'language_example' # str | a valid language code
    game = 'dofus2' # str | 
    sort_level = 'asc' # str | sort the resulting list by level, default unsorted (optional)
    filter_type_name = 'Chest' # str | only results with the translated type name (optional)
    filter_min_level = 150 # int | only results which level is equal or above this value (optional)
    filter_max_level = 180 # int | only results which level is equal or below this value (optional)
    page_size = 2 # int | size of the results from the list. -1 disables pagination and gets all in one response. (optional)
    page_number = 1 # int | page number based on the current page[size]. So you could get page 1 with 8 entrys and page 2 would have entries 8 to 16. (optional)
    fields_item = ['[\"recipe\"]'] # List[str] | adds fields from their detail endpoint to the item list entries. Multiple comma separated values allowed. (optional)

    try:
        # List Consumables
        api_response = api_instance.get_items_consumables_list(language, game, sort_level=sort_level, filter_type_name=filter_type_name, filter_min_level=filter_min_level, filter_max_level=filter_max_level, page_size=page_size, page_number=page_number, fields_item=fields_item)
        print("The response of ConsumablesApi->get_items_consumables_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumablesApi->get_items_consumables_list: %s\n" % e)
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
 **fields_item** | [**List[str]**](str.md)| adds fields from their detail endpoint to the item list entries. Multiple comma separated values allowed. | [optional] 

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
**200** | Consumables Found |  -  |
**400** | Bad Request  |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_consumables_search**
> List[ItemListEntry] get_items_consumables_search(language, game, query, filter_type_name=filter_type_name, filter_min_level=filter_min_level, filter_max_level=filter_max_level, limit=limit)

Search Consumables

Search in all names and descriptions of consumable items with a query.

### Example


```python
import dofusdude
from dofusdude.models.item_list_entry import ItemListEntry
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
    api_instance = dofusdude.ConsumablesApi(api_client)
    language = 'language_example' # str | a valid language code
    game = 'dofus2' # str | 
    query = 'Wholewrite' # str | case sensitive search query
    filter_type_name = 'Bread' # str | only results with the translated type name (optional)
    filter_min_level = 1 # int | only results which level is equal or above this value (optional)
    filter_max_level = 200 # int | only results which level is equal or below this value (optional)
    limit = 8 # int | maximum number of returned results (optional) (default to 8)

    try:
        # Search Consumables
        api_response = api_instance.get_items_consumables_search(language, game, query, filter_type_name=filter_type_name, filter_min_level=filter_min_level, filter_max_level=filter_max_level, limit=limit)
        print("The response of ConsumablesApi->get_items_consumables_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumablesApi->get_items_consumables_search: %s\n" % e)
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
 **limit** | **int**| maximum number of returned results | [optional] [default to 8]

### Return type

[**List[ItemListEntry]**](ItemListEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consumables Found |  -  |
**400** | Bad Request  Possibilities: - empty or no query  |  -  |
**404** | Not Found  Possibilities: - no hits for query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_consumables_single**
> Resource get_items_consumables_single(language, ankama_id, game)

Single Consumables

Retrieve a specific consumable item with id.

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
    api_instance = dofusdude.ConsumablesApi(api_client)
    language = 'language_example' # str | a valid language code
    ankama_id = 17206 # int | identifier
    game = 'dofus2' # str | 

    try:
        # Single Consumables
        api_response = api_instance.get_items_consumables_single(language, ankama_id, game)
        print("The response of ConsumablesApi->get_items_consumables_single:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumablesApi->get_items_consumables_single: %s\n" % e)
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
**200** | Consumable Found |  -  |
**400** | Bad Request  Possibilities: - invalid ankama id format  |  -  |
**404** | Not Found  Possibilities: - nothing found for this ankama_id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

