# dofusdude.MetaApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_game_search_types**](MetaApi.md#get_game_search_types) | **GET** /dofus2/meta/search/types | Available Game Search Types
[**get_meta_almanax_bonuses**](MetaApi.md#get_meta_almanax_bonuses) | **GET** /dofus2/meta/{language}/almanax/bonuses | Available Almanax Bonuses
[**get_meta_elements**](MetaApi.md#get_meta_elements) | **GET** /dofus2/meta/elements | Effects and Condition Elements


# **get_game_search_types**
> List[str] get_game_search_types()

Available Game Search Types

Get all types for /{game}/{lang}/search available for filtering. All names are english for comparing them inside applications. Order is fixed so you can compare indices instead of strings.

### Example

```python
import time
import os
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
    api_instance = dofusdude.MetaApi(api_client)

    try:
        # Available Game Search Types
        api_response = api_instance.get_game_search_types()
        print("The response of MetaApi->get_game_search_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->get_game_search_types: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta_almanax_bonuses**
> List[GetMetaAlmanaxBonuses200ResponseInner] get_meta_almanax_bonuses(language)

Available Almanax Bonuses

Get all the available bonuses and their id for filtering them in the range endpoint.

### Example

```python
import time
import os
import dofusdude
from dofusdude.models.get_meta_almanax_bonuses200_response_inner import GetMetaAlmanaxBonuses200ResponseInner
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
    api_instance = dofusdude.MetaApi(api_client)
    language = 'fr' # str | 

    try:
        # Available Almanax Bonuses
        api_response = api_instance.get_meta_almanax_bonuses(language)
        print("The response of MetaApi->get_meta_almanax_bonuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->get_meta_almanax_bonuses: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | 

### Return type

[**List[GetMetaAlmanaxBonuses200ResponseInner]**](GetMetaAlmanaxBonuses200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta_elements**
> List[str] get_meta_elements()

Effects and Condition Elements

Get the mappings for all specific elements that are linked in the dataset. All names are english. Translations are not needed because of a global unique id which is the index inside the array. Future elements will get a higher id.

### Example

```python
import time
import os
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
    api_instance = dofusdude.MetaApi(api_client)

    try:
        # Effects and Condition Elements
        api_response = api_instance.get_meta_elements()
        print("The response of MetaApi->get_meta_elements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->get_meta_elements: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

