# dofusdude.SetsApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_sets_list**](SetsApi.md#get_all_sets_list) | **GET** /{game}/{language}/sets/all | List All Sets
[**get_sets_list**](SetsApi.md#get_sets_list) | **GET** /{game}/{language}/sets | List Sets
[**get_sets_search**](SetsApi.md#get_sets_search) | **GET** /{game}/{language}/sets/search | Search Sets
[**get_sets_single**](SetsApi.md#get_sets_single) | **GET** /{game}/{language}/sets/{ankama_id} | Single Sets


# **get_all_sets_list**
> SetsListPaged get_all_sets_list(language, game, sort_level=sort_level, filter_min_highest_equipment_level=filter_min_highest_equipment_level, filter_max_highest_equipment_level=filter_max_highest_equipment_level, accept_encoding=accept_encoding)

List All Sets

Retrieve all sets with one request. This endpoint is just an alias for the a list with disabled pagination (page[size]=-1) and all fields[type] set.  If you want everything unfiltered, delete the other query parameters.  Be careful with testing or (god forbid) using /all in your browser, the returned json is huge and will slow down the browser!  Tip: set the HTTP Header 'Accept-Encoding: gzip' for saving bandwidth. You will need to uncompress it on your end. Example with cURL: ``` curl -sH 'Accept-Encoding: gzip' <api-endpoint> | gunzip - ```

### Example

```python
import time
import os
import dofusdude
from dofusdude.models.sets_list_paged import SetsListPaged
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
    api_instance = dofusdude.SetsApi(api_client)
    language = 'language_example' # str | a valid language code
    game = 'dofus2' # str | 
    sort_level = 'asc' # str | sort the resulting list by level, default unsorted (optional)
    filter_min_highest_equipment_level = 190 # int | only results where the equipment with the highest level is above or equal to this value (optional)
    filter_max_highest_equipment_level = 200 # int | only results where the equipment with the highest level is below or equal to this value (optional)
    accept_encoding = 'accept_encoding_example' # str | optional compression for saving bandwidth (optional)

    try:
        # List All Sets
        api_response = api_instance.get_all_sets_list(language, game, sort_level=sort_level, filter_min_highest_equipment_level=filter_min_highest_equipment_level, filter_max_highest_equipment_level=filter_max_highest_equipment_level, accept_encoding=accept_encoding)
        print("The response of SetsApi->get_all_sets_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetsApi->get_all_sets_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code | 
 **game** | **str**|  | 
 **sort_level** | **str**| sort the resulting list by level, default unsorted | [optional] 
 **filter_min_highest_equipment_level** | **int**| only results where the equipment with the highest level is above or equal to this value | [optional] 
 **filter_max_highest_equipment_level** | **int**| only results where the equipment with the highest level is below or equal to this value | [optional] 
 **accept_encoding** | **str**| optional compression for saving bandwidth | [optional] 

### Return type

[**SetsListPaged**](SetsListPaged.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Set Found |  -  |
**400** | Bad Request  |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sets_list**
> SetsListPaged get_sets_list(language, game, sort_level=sort_level, filter_min_highest_equipment_level=filter_min_highest_equipment_level, filter_max_highest_equipment_level=filter_max_highest_equipment_level, page_size=page_size, page_number=page_number, fields_set=fields_set)

List Sets

Retrieve a list of sets.

### Example

```python
import time
import os
import dofusdude
from dofusdude.models.sets_list_paged import SetsListPaged
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
    api_instance = dofusdude.SetsApi(api_client)
    language = 'language_example' # str | a valid language code
    game = 'dofus2' # str | 
    sort_level = 'asc' # str | sort the resulting list by level, default unsorted (optional)
    filter_min_highest_equipment_level = 190 # int | only results where the equipment with the highest level is above or equal to this value (optional)
    filter_max_highest_equipment_level = 200 # int | only results where the equipment with the highest level is below or equal to this value (optional)
    page_size = 20 # int | size of the results from the list. -1 disables pagination and gets all in one response. (optional)
    page_number = 1 # int | page number based on the current page[size]. So you could get page 1 with 8 entrys and page 2 would have entries 8 to 16. (optional)
    fields_set = ['[\"equipment_ids\"]'] # List[str] | adds fields from their detail endpoint to the item list entries. Multiple comma separated values allowed. (optional)

    try:
        # List Sets
        api_response = api_instance.get_sets_list(language, game, sort_level=sort_level, filter_min_highest_equipment_level=filter_min_highest_equipment_level, filter_max_highest_equipment_level=filter_max_highest_equipment_level, page_size=page_size, page_number=page_number, fields_set=fields_set)
        print("The response of SetsApi->get_sets_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetsApi->get_sets_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code | 
 **game** | **str**|  | 
 **sort_level** | **str**| sort the resulting list by level, default unsorted | [optional] 
 **filter_min_highest_equipment_level** | **int**| only results where the equipment with the highest level is above or equal to this value | [optional] 
 **filter_max_highest_equipment_level** | **int**| only results where the equipment with the highest level is below or equal to this value | [optional] 
 **page_size** | **int**| size of the results from the list. -1 disables pagination and gets all in one response. | [optional] 
 **page_number** | **int**| page number based on the current page[size]. So you could get page 1 with 8 entrys and page 2 would have entries 8 to 16. | [optional] 
 **fields_set** | [**List[str]**](str.md)| adds fields from their detail endpoint to the item list entries. Multiple comma separated values allowed. | [optional] 

### Return type

[**SetsListPaged**](SetsListPaged.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Set Found |  -  |
**400** | Bad Request  |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sets_search**
> List[SetListEntry] get_sets_search(language, game, query, filter_min_highest_equipment_level=filter_min_highest_equipment_level, filter_max_highest_equipment_level=filter_max_highest_equipment_level, limit=limit)

Search Sets

Search in all names and descriptions of sets with a query.

### Example

```python
import time
import os
import dofusdude
from dofusdude.models.set_list_entry import SetListEntry
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
    api_instance = dofusdude.SetsApi(api_client)
    language = 'language_example' # str | a valid language code
    game = 'dofus2' # str | 
    query = 'Des' # str | case sensitive search query
    filter_min_highest_equipment_level = 195 # int | only results where the equipment with the highest level is above or equal to this value (optional)
    filter_max_highest_equipment_level = 200 # int | only results where the equipment with the highest level is below or equal to this value (optional)
    limit = 8 # int | maximum number of returned results (optional) (default to 8)

    try:
        # Search Sets
        api_response = api_instance.get_sets_search(language, game, query, filter_min_highest_equipment_level=filter_min_highest_equipment_level, filter_max_highest_equipment_level=filter_max_highest_equipment_level, limit=limit)
        print("The response of SetsApi->get_sets_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetsApi->get_sets_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code | 
 **game** | **str**|  | 
 **query** | **str**| case sensitive search query | 
 **filter_min_highest_equipment_level** | **int**| only results where the equipment with the highest level is above or equal to this value | [optional] 
 **filter_max_highest_equipment_level** | **int**| only results where the equipment with the highest level is below or equal to this value | [optional] 
 **limit** | **int**| maximum number of returned results | [optional] [default to 8]

### Return type

[**List[SetListEntry]**](SetListEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sets Found |  -  |
**400** | Bad Request  Possibilities: - empty or no query  |  -  |
**404** | Not Found  Possibilities: - no hits for query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sets_single**
> EquipmentSet get_sets_single(language, ankama_id, game)

Single Sets

Retrieve a specific set with id.

### Example

```python
import time
import os
import dofusdude
from dofusdude.models.equipment_set import EquipmentSet
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
    api_instance = dofusdude.SetsApi(api_client)
    language = 'language_example' # str | a valid language code
    ankama_id = 499 # int | identifier
    game = 'dofus2' # str | 

    try:
        # Single Sets
        api_response = api_instance.get_sets_single(language, ankama_id, game)
        print("The response of SetsApi->get_sets_single:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetsApi->get_sets_single: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code | 
 **ankama_id** | **int**| identifier | 
 **game** | **str**|  | 

### Return type

[**EquipmentSet**](EquipmentSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Set Found |  -  |
**400** | Bad Request  Possibilities: - invalid ankama id format  |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

