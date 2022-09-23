# dofusdude.MetaApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_meta_almanax_bonuses**](MetaApi.md#get_meta_almanax_bonuses) | **GET** /dofus2/meta/{language}/almanax/bonuses | Available Almanax Bonuses
[**get_meta_elements**](MetaApi.md#get_meta_elements) | **GET** /dofus2/meta/elements | Effects and Condition Elements


# **get_meta_almanax_bonuses**
> [GetMetaAlmanaxBonuses200ResponseInner] get_meta_almanax_bonuses(language)

Available Almanax Bonuses

Get all the available bonuses and their id for filtering them in the range endpoint.

### Example


```python
import time
import dofusdude
from dofusdude.api import meta_api
from dofusdude.model.get_meta_almanax_bonuses200_response_inner import GetMetaAlmanaxBonuses200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = meta_api.MetaApi(api_client)
    language = "en" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Available Almanax Bonuses
        api_response = api_instance.get_meta_almanax_bonuses(language)
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling MetaApi->get_meta_almanax_bonuses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  |

### Return type

[**[GetMetaAlmanaxBonuses200ResponseInner]**](GetMetaAlmanaxBonuses200ResponseInner.md)

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
> [str] get_meta_elements()

Effects and Condition Elements

Get the mappings for all specific elements that are linked in the dataset. All names are english. Translations are not needed because of a global unique id which is the index inside the array. Future elements will get a higher id.

### Example


```python
import time
import dofusdude
from dofusdude.api import meta_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = meta_api.MetaApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Effects and Condition Elements
        api_response = api_instance.get_meta_elements()
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling MetaApi->get_meta_elements: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[str]**

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

