# dofusdude.EquipmentApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_items_equipment_list**](EquipmentApi.md#get_all_items_equipment_list) | **GET** /{game}/{language}/items/equipment/all | List All Equipment
[**get_items_equipment_list**](EquipmentApi.md#get_items_equipment_list) | **GET** /{game}/{language}/items/equipment | List Equipment
[**get_items_equipment_search**](EquipmentApi.md#get_items_equipment_search) | **GET** /{game}/{language}/items/equipment/search | Search Equipment
[**get_items_equipment_single**](EquipmentApi.md#get_items_equipment_single) | **GET** /{game}/{language}/items/equipment/{ankama_id} | Single Equipment


# **get_all_items_equipment_list**
> ItemsListPaged get_all_items_equipment_list(language, game, sort_level=sort_level, filter_type_name=filter_type_name, filter_min_level=filter_min_level, filter_max_level=filter_max_level, accept_encoding=accept_encoding)

List All Equipment

Retrieve all equipment items with one request. This endpoint is just an alias for the a list with disabled pagination (page[size]=-1) and all fields[type] set.  If you want everything unfiltered, delete the other query parameters.  Be careful with testing or (god forbid) using /all in your browser, the returned json is huge and will slow down the browser!  Tip: set the HTTP Header 'Accept-Encoding: gzip' for saving bandwidth. You will need to uncompress it on your end. Example with cURL: ``` curl -sH 'Accept-Encoding: gzip' <api-endpoint> | gunzip - ```

### Example

```python
import time
import os
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
    api_instance = dofusdude.EquipmentApi(api_client)
    language = 'en' # str | a valid language code
    game = 'dofus2' # str | 
    sort_level = 'desc' # str | sort the resulting list by level, default unsorted (optional)
    filter_type_name = 'Sword' # str | only results with the translated type name (optional)
    filter_min_level = 10 # int | only results which level is equal or above this value (optional)
    filter_max_level = 60 # int | only results which level is equal or below this value (optional)
    accept_encoding = 'accept_encoding_example' # str | optional compression for saving bandwidth (optional)

    try:
        # List All Equipment
        api_response = api_instance.get_all_items_equipment_list(language, game, sort_level=sort_level, filter_type_name=filter_type_name, filter_min_level=filter_min_level, filter_max_level=filter_max_level, accept_encoding=accept_encoding)
        print("The response of EquipmentApi->get_all_items_equipment_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EquipmentApi->get_all_items_equipment_list: %s\n" % e)
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
**200** | Equipment Found |  -  |
**400** | Bad Request  |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_equipment_list**
> ItemsListPaged get_items_equipment_list(language, game, sort_level=sort_level, filter_type_name=filter_type_name, filter_min_level=filter_min_level, filter_max_level=filter_max_level, page_size=page_size, page_number=page_number, fields_item=fields_item)

List Equipment

Retrieve a list of equipment items.

### Example

```python
import time
import os
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
    api_instance = dofusdude.EquipmentApi(api_client)
    language = 'en' # str | a valid language code
    game = 'dofus2' # str | 
    sort_level = 'desc' # str | sort the resulting list by level, default unsorted (optional)
    filter_type_name = 'Sword' # str | only results with the translated type name (optional)
    filter_min_level = 10 # int | only results which level is equal or above this value (optional)
    filter_max_level = 60 # int | only results which level is equal or below this value (optional)
    page_size = 5 # int | size of the results from the list. -1 disables pagination and gets all in one response. (optional)
    page_number = 1 # int | page number based on the current page[size]. So you could get page 1 with 8 entrys and page 2 would have entries 8 to 16. (optional)
    fields_item = ['[\"is_weapon\"]'] # List[str] | adds fields from their detail endpoint to the item list entries. Multiple comma separated values allowed. (optional)

    try:
        # List Equipment
        api_response = api_instance.get_items_equipment_list(language, game, sort_level=sort_level, filter_type_name=filter_type_name, filter_min_level=filter_min_level, filter_max_level=filter_max_level, page_size=page_size, page_number=page_number, fields_item=fields_item)
        print("The response of EquipmentApi->get_items_equipment_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EquipmentApi->get_items_equipment_list: %s\n" % e)
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
**200** | Equipment Found |  -  |
**400** | Bad Request  |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_equipment_search**
> List[ItemListEntry] get_items_equipment_search(language, game, query, filter_type_name=filter_type_name, filter_min_level=filter_min_level, filter_max_level=filter_max_level, limit=limit)

Search Equipment

Search in all names and descriptions of equipment items with a query.

### Example

```python
import time
import os
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
    api_instance = dofusdude.EquipmentApi(api_client)
    language = 'language_example' # str | a valid language code
    game = 'dofus2' # str | 
    query = 'nidas' # str | case sensitive search query
    filter_type_name = 'boots' # str | only results with the translated type name (optional)
    filter_min_level = 150 # int | only results which level is equal or above this value (optional)
    filter_max_level = 200 # int | only results which level is equal or below this value (optional)
    limit = 8 # int | maximum number of returned results (optional) (default to 8)

    try:
        # Search Equipment
        api_response = api_instance.get_items_equipment_search(language, game, query, filter_type_name=filter_type_name, filter_min_level=filter_min_level, filter_max_level=filter_max_level, limit=limit)
        print("The response of EquipmentApi->get_items_equipment_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EquipmentApi->get_items_equipment_search: %s\n" % e)
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
**200** | Equipment Found |  -  |
**400** | Bad Request  Possibilities: - empty or no query  |  -  |
**404** | Not Found  Possibilities: - no hits for query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_equipment_single**
> Weapon get_items_equipment_single(language, ankama_id, game)

Single Equipment

Retrieve a specific equipment item with id.

### Example

```python
import time
import os
import dofusdude
from dofusdude.models.weapon import Weapon
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
    api_instance = dofusdude.EquipmentApi(api_client)
    language = 'language_example' # str | a valid language code
    ankama_id = 26009 # int | identifier
    game = 'dofus2' # str | 

    try:
        # Single Equipment
        api_response = api_instance.get_items_equipment_single(language, ankama_id, game)
        print("The response of EquipmentApi->get_items_equipment_single:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EquipmentApi->get_items_equipment_single: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code | 
 **ankama_id** | **int**| identifier | 
 **game** | **str**|  | 

### Return type

[**Weapon**](Weapon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Equipment Found |  -  |
**400** | Bad Request  Possibilities: - invalid ankama id format  |  -  |
**404** | Not Found  Possibilities: - nothing found for this ankama_id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

