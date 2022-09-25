<a name="__pageTop"></a>
# dofusdude.apis.tags.sets_api.SetsApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sets_list**](#get_sets_list) | **get** /{game}/{language}/sets | List Sets
[**get_sets_search**](#get_sets_search) | **get** /{game}/{language}/sets/search | Search Sets
[**get_sets_single**](#get_sets_single) | **get** /{game}/{language}/sets/{ankama_id} | Single Sets

# **get_sets_list**
<a name="get_sets_list"></a>
> SetsListPaged get_sets_list(languagegame)

List Sets

Retrieve a list of sets.

### Example

```python
import dofusdude
from dofusdude.apis.tags import sets_api
from dofusdude.model.sets_list_paged import SetsListPaged
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)

# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sets_api.SetsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
    }
    try:
        # List Sets
        api_response = api_instance.get_sets_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling SetsApi->get_sets_list: %s\n" % e)

    # example passing only optional values
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
        'sort[level]': "asc",
        'filter[min_highest_equipment_level]': 190,
        'filter[max_highest_equipment_level]': 200,
        'page[size]': 20,
        'page[number]': 1,
    }
    try:
        # List Sets
        api_response = api_instance.get_sets_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling SetsApi->get_sets_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
sort[level] | SortLevelSchema | | optional
filter[min_highest_equipment_level] | FilterMinHighestEquipmentLevelSchema | | optional
filter[max_highest_equipment_level] | FilterMaxHighestEquipmentLevelSchema | | optional
page[size] | PageSizeSchema | | optional
page[number] | PageNumberSchema | | optional


# SortLevelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["asc", "desc", ] 

# FilterMinHighestEquipmentLevelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# FilterMaxHighestEquipmentLevelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# PageNumberSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
language | LanguageSchema | | 
game | GameSchema | | 

# LanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["en", "fr", "de", "it", "es", "pt", ] 

# GameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["dofus2", "dofus2beta", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sets_list.ApiResponseFor200) | Set Found
400 | [ApiResponseFor400](#get_sets_list.ApiResponseFor400) | Bad Request 
404 | [ApiResponseFor404](#get_sets_list.ApiResponseFor404) | Not Found

#### get_sets_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SetsListPaged**](../../models/SetsListPaged.md) |  | 


#### get_sets_list.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sets_list.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sets_search**
<a name="get_sets_search"></a>
> [SetListEntry] get_sets_search(languagegamequery)

Search Sets

Search in all names and descriptions of sets with a query.

### Example

```python
import dofusdude
from dofusdude.apis.tags import sets_api
from dofusdude.model.set_list_entry import SetListEntry
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)

# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sets_api.SetsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
        'query': "Des",
    }
    try:
        # Search Sets
        api_response = api_instance.get_sets_search(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling SetsApi->get_sets_search: %s\n" % e)

    # example passing only optional values
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
        'query': "Des",
        'filter[min_highest_equipment_level]': 195,
        'filter[max_highest_equipment_level]': 200,
    }
    try:
        # Search Sets
        api_response = api_instance.get_sets_search(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling SetsApi->get_sets_search: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query | QuerySchema | | 
filter[min_highest_equipment_level] | FilterMinHighestEquipmentLevelSchema | | optional
filter[max_highest_equipment_level] | FilterMaxHighestEquipmentLevelSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FilterMinHighestEquipmentLevelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# FilterMaxHighestEquipmentLevelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
language | LanguageSchema | | 
game | GameSchema | | 

# LanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["en", "fr", "de", "it", "es", "pt", ] 

# GameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["dofus2", "dofus2beta", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sets_search.ApiResponseFor200) | Sets Found
400 | [ApiResponseFor400](#get_sets_search.ApiResponseFor400) | Bad Request  Possibilities: - empty or no query 
404 | [ApiResponseFor404](#get_sets_search.ApiResponseFor404) | Not Found  Possibilities: - no hits for query

#### get_sets_search.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SetListEntry**]({{complexTypePrefix}}SetListEntry.md) | [**SetListEntry**]({{complexTypePrefix}}SetListEntry.md) | [**SetListEntry**]({{complexTypePrefix}}SetListEntry.md) |  | 

#### get_sets_search.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sets_search.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sets_single**
<a name="get_sets_single"></a>
> EquipmentSet get_sets_single(languageankama_idgame)

Single Sets

Retrieve a specific set with id.

### Example

```python
import dofusdude
from dofusdude.apis.tags import sets_api
from dofusdude.model.equipment_set import EquipmentSet
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)

# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sets_api.SetsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'language': "en",
        'ankama_id': 499,
        'game': "dofus2",
    }
    try:
        # Single Sets
        api_response = api_instance.get_sets_single(
            path_params=path_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling SetsApi->get_sets_single: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
language | LanguageSchema | | 
ankama_id | AnkamaIdSchema | | 
game | GameSchema | | 

# LanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["en", "fr", "de", "it", "es", "pt", ] 

# AnkamaIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["dofus2", "dofus2beta", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sets_single.ApiResponseFor200) | Set Found
400 | [ApiResponseFor400](#get_sets_single.ApiResponseFor400) | Bad Request  Possibilities: - invalid ankama id format 
404 | [ApiResponseFor404](#get_sets_single.ApiResponseFor404) | Not Found

#### get_sets_single.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EquipmentSet**](../../models/EquipmentSet.md) |  | 


#### get_sets_single.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sets_single.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

