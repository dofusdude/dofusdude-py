<a name="__pageTop"></a>
# dofusdude.apis.tags.cosmetics_api.CosmeticsApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cosmetics_list**](#get_cosmetics_list) | **get** /{game}/{language}/items/cosmetics | List Cosmetics
[**get_cosmetics_search**](#get_cosmetics_search) | **get** /{game}/{language}/items/cosmetics/search | Search Cosmetics
[**get_cosmetics_single**](#get_cosmetics_single) | **get** /{game}/{language}/items/cosmetics/{ankama_id} | Single Cosmetics

# **get_cosmetics_list**
<a name="get_cosmetics_list"></a>
> ItemsListPaged get_cosmetics_list(languagegame)

List Cosmetics

Retrieve a list of cosmetic items.

### Example

```python
import dofusdude
from dofusdude.apis.tags import cosmetics_api
from dofusdude.model.items_list_paged import ItemsListPaged
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)

# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmetics_api.CosmeticsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'language': "fr",
        'game': "dofus2",
    }
    query_params = {
    }
    try:
        # List Cosmetics
        api_response = api_instance.get_cosmetics_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling CosmeticsApi->get_cosmetics_list: %s\n" % e)

    # example passing only optional values
    path_params = {
        'language': "fr",
        'game': "dofus2",
    }
    query_params = {
        'sort[level]': "asc",
        'filter[type_name]': "Chapeau d'apparat",
        'filter[min_level]': 1,
        'filter[max_level]': 5,
        'page[size]': 5,
        'page[number]': 1,
        'fields[item]': "recipe",
    }
    try:
        # List Cosmetics
        api_response = api_instance.get_cosmetics_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling CosmeticsApi->get_cosmetics_list: %s\n" % e)
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
filter[type_name] | FilterTypeNameSchema | | optional
filter[min_level] | FilterMinLevelSchema | | optional
filter[max_level] | FilterMaxLevelSchema | | optional
page[size] | PageSizeSchema | | optional
page[number] | PageNumberSchema | | optional
fields[item] | FieldsItemSchema | | optional


# SortLevelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["asc", "desc", ] 

# FilterTypeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FilterMinLevelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FilterMaxLevelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PageNumberSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FieldsItemSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
200 | [ApiResponseFor200](#get_cosmetics_list.ApiResponseFor200) | Cosmetics Found
400 | [ApiResponseFor400](#get_cosmetics_list.ApiResponseFor400) | Bad Request 
404 | [ApiResponseFor404](#get_cosmetics_list.ApiResponseFor404) | Not Found

#### get_cosmetics_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ItemsListPaged**](../../models/ItemsListPaged.md) |  | 


#### get_cosmetics_list.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_cosmetics_list.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_cosmetics_search**
<a name="get_cosmetics_search"></a>
> [ItemListEntry] get_cosmetics_search(languagegamequery)

Search Cosmetics

Search in all names and descriptions of cosmetic items with a query.

### Example

```python
import dofusdude
from dofusdude.apis.tags import cosmetics_api
from dofusdude.model.item_list_entry import ItemListEntry
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)

# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmetics_api.CosmeticsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
        'query': "nedora",
    }
    try:
        # Search Cosmetics
        api_response = api_instance.get_cosmetics_search(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling CosmeticsApi->get_cosmetics_search: %s\n" % e)

    # example passing only optional values
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
        'query': "nedora",
        'filter[type_name]': "Costume",
        'filter[min_level]': 1,
        'filter[max_level]': 2,
    }
    try:
        # Search Cosmetics
        api_response = api_instance.get_cosmetics_search(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling CosmeticsApi->get_cosmetics_search: %s\n" % e)
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
filter[type_name] | FilterTypeNameSchema | | optional
filter[min_level] | FilterMinLevelSchema | | optional
filter[max_level] | FilterMaxLevelSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FilterTypeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FilterMinLevelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# FilterMaxLevelSchema

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
200 | [ApiResponseFor200](#get_cosmetics_search.ApiResponseFor200) | Cosmetics found
400 | [ApiResponseFor400](#get_cosmetics_search.ApiResponseFor400) | Bad Request  Possibilities: - empty or no query 
404 | [ApiResponseFor404](#get_cosmetics_search.ApiResponseFor404) | Not Found  Possibilities: - no hits for query

#### get_cosmetics_search.ApiResponseFor200
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
[**ItemListEntry**]({{complexTypePrefix}}ItemListEntry.md) | [**ItemListEntry**]({{complexTypePrefix}}ItemListEntry.md) | [**ItemListEntry**]({{complexTypePrefix}}ItemListEntry.md) |  | 

#### get_cosmetics_search.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_cosmetics_search.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_cosmetics_single**
<a name="get_cosmetics_single"></a>
> Cosmetic get_cosmetics_single(languageankama_idgame)

Single Cosmetics

Retrieve a specific cosmetic item with id.

### Example

```python
import dofusdude
from dofusdude.apis.tags import cosmetics_api
from dofusdude.model.cosmetic import Cosmetic
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)

# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmetics_api.CosmeticsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'language': "en",
        'ankama_id': 24132,
        'game': "dofus2",
    }
    try:
        # Single Cosmetics
        api_response = api_instance.get_cosmetics_single(
            path_params=path_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling CosmeticsApi->get_cosmetics_single: %s\n" % e)
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
200 | [ApiResponseFor200](#get_cosmetics_single.ApiResponseFor200) | Cosmetic Found
400 | [ApiResponseFor400](#get_cosmetics_single.ApiResponseFor400) | Bad Request  Possibilities: - invalid ankama id format 
404 | [ApiResponseFor404](#get_cosmetics_single.ApiResponseFor404) | Not Found  Possibilities: - nothing found for this ankama_id

#### get_cosmetics_single.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Cosmetic**](../../models/Cosmetic.md) |  | 


#### get_cosmetics_single.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_cosmetics_single.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

