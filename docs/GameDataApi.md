# dofusdude.GameDataApi

All URIs are relative to *https://beta.api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_areas**](GameDataApi.md#get_all_areas) | **GET** /{game}/v1/{language}/areas/all | Get all areas
[**get_all_classes**](GameDataApi.md#get_all_classes) | **GET** /{game}/v1/{language}/classes/all | Get all classes
[**get_all_monsters**](GameDataApi.md#get_all_monsters) | **GET** /{game}/v1/{language}/monsters/all | Get all monsters
[**get_all_spells**](GameDataApi.md#get_all_spells) | **GET** /{game}/v1/{language}/spells/all | Get all spells
[**get_all_subareas**](GameDataApi.md#get_all_subareas) | **GET** /{game}/v1/{language}/subareas/all | Get all subareas
[**get_all_super_areas**](GameDataApi.md#get_all_super_areas) | **GET** /{game}/v1/{language}/super-areas/all | Get all super-areas
[**get_area_by_id**](GameDataApi.md#get_area_by_id) | **GET** /{game}/v1/{language}/areas/{ankama_id} | Get one area
[**get_areas**](GameDataApi.md#get_areas) | **GET** /{game}/v1/{language}/areas | List areas
[**get_class_by_id**](GameDataApi.md#get_class_by_id) | **GET** /{game}/v1/{language}/classes/{ankama_id} | Get one class
[**get_classes**](GameDataApi.md#get_classes) | **GET** /{game}/v1/{language}/classes | List classes
[**get_monster_by_id**](GameDataApi.md#get_monster_by_id) | **GET** /{game}/v1/{language}/monsters/{ankama_id} | Get one monster
[**get_monsters**](GameDataApi.md#get_monsters) | **GET** /{game}/v1/{language}/monsters | List monsters
[**get_spell_by_id**](GameDataApi.md#get_spell_by_id) | **GET** /{game}/v1/{language}/spells/{ankama_id} | Get one spell
[**get_spells**](GameDataApi.md#get_spells) | **GET** /{game}/v1/{language}/spells | List spells
[**get_subarea_by_id**](GameDataApi.md#get_subarea_by_id) | **GET** /{game}/v1/{language}/subareas/{ankama_id} | Get one subarea
[**get_subareas**](GameDataApi.md#get_subareas) | **GET** /{game}/v1/{language}/subareas | List subareas
[**get_super_area_by_id**](GameDataApi.md#get_super_area_by_id) | **GET** /{game}/v1/{language}/super-areas/{ankama_id} | Get one super-area
[**get_super_areas**](GameDataApi.md#get_super_areas) | **GET** /{game}/v1/{language}/super-areas | List super-areas
[**search_areas**](GameDataApi.md#search_areas) | **GET** /{game}/v1/{language}/areas/search | Search areas
[**search_classes**](GameDataApi.md#search_classes) | **GET** /{game}/v1/{language}/classes/search | Search classes
[**search_monsters**](GameDataApi.md#search_monsters) | **GET** /{game}/v1/{language}/monsters/search | Search monsters
[**search_spells**](GameDataApi.md#search_spells) | **GET** /{game}/v1/{language}/spells/search | Search spells
[**search_subareas**](GameDataApi.md#search_subareas) | **GET** /{game}/v1/{language}/subareas/search | Search subareas
[**search_super_areas**](GameDataApi.md#search_super_areas) | **GET** /{game}/v1/{language}/super-areas/search | Search super-areas


# **get_all_areas**
> MappedEntityCollection get_all_areas(game, language)

Get all areas

### Example


```python
import dofusdude
from dofusdude.models.mapped_entity_collection import MappedEntityCollection
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 

    try:
        # Get all areas
        api_response = api_instance.get_all_areas(game, language)
        print("The response of GameDataApi->get_all_areas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->get_all_areas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 

### Return type

[**MappedEntityCollection**](MappedEntityCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Every complete localized area document. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_classes**
> MappedEntityCollection get_all_classes(game, language)

Get all classes

### Example


```python
import dofusdude
from dofusdude.models.mapped_entity_collection import MappedEntityCollection
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 

    try:
        # Get all classes
        api_response = api_instance.get_all_classes(game, language)
        print("The response of GameDataApi->get_all_classes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->get_all_classes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 

### Return type

[**MappedEntityCollection**](MappedEntityCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Every complete localized class document. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_monsters**
> MappedEntityCollection get_all_monsters(game, language, include=include)

Get all monsters

### Example


```python
import dofusdude
from dofusdude.models.mapped_entity_collection import MappedEntityCollection
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    include = 'include_example' # str | Optional spell expansion for monster responses. Leave include unset to return spell URLs. Use `spells.grade` to embed the assigned spell grade. Use `spells` to embed every available grade of each assigned spell. (optional)

    try:
        # Get all monsters
        api_response = api_instance.get_all_monsters(game, language, include=include)
        print("The response of GameDataApi->get_all_monsters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->get_all_monsters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **include** | **str**| Optional spell expansion for monster responses. Leave include unset to return spell URLs. Use &#x60;spells.grade&#x60; to embed the assigned spell grade. Use &#x60;spells&#x60; to embed every available grade of each assigned spell. | [optional] 

### Return type

[**MappedEntityCollection**](MappedEntityCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Every complete localized monster document. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_spells**
> MappedEntityCollection get_all_spells(game, language)

Get all spells

### Example


```python
import dofusdude
from dofusdude.models.mapped_entity_collection import MappedEntityCollection
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 

    try:
        # Get all spells
        api_response = api_instance.get_all_spells(game, language)
        print("The response of GameDataApi->get_all_spells:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->get_all_spells: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 

### Return type

[**MappedEntityCollection**](MappedEntityCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Every complete localized spell document. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_subareas**
> MappedEntityCollection get_all_subareas(game, language)

Get all subareas

### Example


```python
import dofusdude
from dofusdude.models.mapped_entity_collection import MappedEntityCollection
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 

    try:
        # Get all subareas
        api_response = api_instance.get_all_subareas(game, language)
        print("The response of GameDataApi->get_all_subareas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->get_all_subareas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 

### Return type

[**MappedEntityCollection**](MappedEntityCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Every complete localized subarea document. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_super_areas**
> MappedEntityCollection get_all_super_areas(game, language)

Get all super-areas

### Example


```python
import dofusdude
from dofusdude.models.mapped_entity_collection import MappedEntityCollection
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 

    try:
        # Get all super-areas
        api_response = api_instance.get_all_super_areas(game, language)
        print("The response of GameDataApi->get_all_super_areas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->get_all_super_areas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 

### Return type

[**MappedEntityCollection**](MappedEntityCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Every complete localized super-area document. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_area_by_id**
> WorldArea get_area_by_id(game, language, ankama_id)

Get one area

### Example


```python
import dofusdude
from dofusdude.models.world_area import WorldArea
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    ankama_id = 0 # int | 

    try:
        # Get one area
        api_response = api_instance.get_area_by_id(game, language, ankama_id)
        print("The response of GameDataApi->get_area_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->get_area_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **ankama_id** | **int**|  | 

### Return type

[**WorldArea**](WorldArea.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complete localized area document. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_areas**
> MappedEntityCollection get_areas(game, language, page_number=page_number, page_size=page_size, fields_areas=fields_areas)

List areas

### Example


```python
import dofusdude
from dofusdude.models.mapped_entity_collection import MappedEntityCollection
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    page_number = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)
    fields_areas = 'fields_areas_example' # str |  (optional)

    try:
        # List areas
        api_response = api_instance.get_areas(game, language, page_number=page_number, page_size=page_size, fields_areas=fields_areas)
        print("The response of GameDataApi->get_areas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->get_areas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **page_number** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]
 **fields_areas** | **str**|  | [optional] 

### Return type

[**MappedEntityCollection**](MappedEntityCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated areas. |  -  |
**400** | Invalid pagination or field selection. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_class_by_id**
> ModelClass get_class_by_id(game, language, ankama_id)

Get one class

### Example


```python
import dofusdude
from dofusdude.models.model_class import ModelClass
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    ankama_id = 1 # int | 

    try:
        # Get one class
        api_response = api_instance.get_class_by_id(game, language, ankama_id)
        print("The response of GameDataApi->get_class_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->get_class_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **ankama_id** | **int**|  | 

### Return type

[**ModelClass**](ModelClass.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complete localized class document. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classes**
> MappedEntityCollection get_classes(game, language, page_number=page_number, page_size=page_size, fields_classes=fields_classes)

List classes

### Example


```python
import dofusdude
from dofusdude.models.mapped_entity_collection import MappedEntityCollection
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    page_number = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)
    fields_classes = 'fields_classes_example' # str |  (optional)

    try:
        # List classes
        api_response = api_instance.get_classes(game, language, page_number=page_number, page_size=page_size, fields_classes=fields_classes)
        print("The response of GameDataApi->get_classes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->get_classes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **page_number** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]
 **fields_classes** | **str**|  | [optional] 

### Return type

[**MappedEntityCollection**](MappedEntityCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated classes. |  -  |
**400** | Invalid pagination or field selection. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monster_by_id**
> Monster get_monster_by_id(game, language, ankama_id, include=include)

Get one monster

### Example


```python
import dofusdude
from dofusdude.models.monster import Monster
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    ankama_id = 31 # int | 
    include = 'include_example' # str | Optional spell expansion for monster responses. Leave include unset to return spell URLs. Use `spells.grade` to embed the assigned spell grade. Use `spells` to embed every available grade of each assigned spell. (optional)

    try:
        # Get one monster
        api_response = api_instance.get_monster_by_id(game, language, ankama_id, include=include)
        print("The response of GameDataApi->get_monster_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->get_monster_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **ankama_id** | **int**|  | 
 **include** | **str**| Optional spell expansion for monster responses. Leave include unset to return spell URLs. Use &#x60;spells.grade&#x60; to embed the assigned spell grade. Use &#x60;spells&#x60; to embed every available grade of each assigned spell. | [optional] 

### Return type

[**Monster**](Monster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complete localized monster document. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monsters**
> MappedEntityCollection get_monsters(game, language, page_number=page_number, page_size=page_size, fields_monsters=fields_monsters, include=include)

List monsters

### Example


```python
import dofusdude
from dofusdude.models.mapped_entity_collection import MappedEntityCollection
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    page_number = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)
    fields_monsters = 'fields_monsters_example' # str |  (optional)
    include = 'include_example' # str | Optional spell expansion for monster responses. Leave include unset to return spell URLs. Use `spells.grade` to embed the assigned spell grade. Use `spells` to embed every available grade of each assigned spell. (optional)

    try:
        # List monsters
        api_response = api_instance.get_monsters(game, language, page_number=page_number, page_size=page_size, fields_monsters=fields_monsters, include=include)
        print("The response of GameDataApi->get_monsters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->get_monsters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **page_number** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]
 **fields_monsters** | **str**|  | [optional] 
 **include** | **str**| Optional spell expansion for monster responses. Leave include unset to return spell URLs. Use &#x60;spells.grade&#x60; to embed the assigned spell grade. Use &#x60;spells&#x60; to embed every available grade of each assigned spell. | [optional] 

### Return type

[**MappedEntityCollection**](MappedEntityCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated monsters. |  -  |
**400** | Invalid pagination or field selection. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spell_by_id**
> Spell get_spell_by_id(game, language, ankama_id, grade=grade)

Get one spell

### Example


```python
import dofusdude
from dofusdude.models.spell import Spell
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    ankama_id = 201 # int | 
    grade = 56 # int | Select the spell variant identified by its explicit grade number, not its spell-level record ID or a player level. Returns the spell object with only that grade in levels. An unavailable grade returns 404. (optional)

    try:
        # Get one spell
        api_response = api_instance.get_spell_by_id(game, language, ankama_id, grade=grade)
        print("The response of GameDataApi->get_spell_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->get_spell_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **ankama_id** | **int**|  | 
 **grade** | **int**| Select the spell variant identified by its explicit grade number, not its spell-level record ID or a player level. Returns the spell object with only that grade in levels. An unavailable grade returns 404. | [optional] 

### Return type

[**Spell**](Spell.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complete localized spell document. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spells**
> MappedEntityCollection get_spells(game, language, page_number=page_number, page_size=page_size, fields_spells=fields_spells)

List spells

### Example


```python
import dofusdude
from dofusdude.models.mapped_entity_collection import MappedEntityCollection
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    page_number = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)
    fields_spells = 'fields_spells_example' # str |  (optional)

    try:
        # List spells
        api_response = api_instance.get_spells(game, language, page_number=page_number, page_size=page_size, fields_spells=fields_spells)
        print("The response of GameDataApi->get_spells:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->get_spells: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **page_number** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]
 **fields_spells** | **str**|  | [optional] 

### Return type

[**MappedEntityCollection**](MappedEntityCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated spells. |  -  |
**400** | Invalid pagination or field selection. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subarea_by_id**
> WorldArea get_subarea_by_id(game, language, ankama_id)

Get one subarea

### Example


```python
import dofusdude
from dofusdude.models.world_area import WorldArea
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    ankama_id = 1 # int | 

    try:
        # Get one subarea
        api_response = api_instance.get_subarea_by_id(game, language, ankama_id)
        print("The response of GameDataApi->get_subarea_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->get_subarea_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **ankama_id** | **int**|  | 

### Return type

[**WorldArea**](WorldArea.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complete localized subarea document. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subareas**
> MappedEntityCollection get_subareas(game, language, page_number=page_number, page_size=page_size, fields_subareas=fields_subareas)

List subareas

### Example


```python
import dofusdude
from dofusdude.models.mapped_entity_collection import MappedEntityCollection
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    page_number = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)
    fields_subareas = 'fields_subareas_example' # str |  (optional)

    try:
        # List subareas
        api_response = api_instance.get_subareas(game, language, page_number=page_number, page_size=page_size, fields_subareas=fields_subareas)
        print("The response of GameDataApi->get_subareas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->get_subareas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **page_number** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]
 **fields_subareas** | **str**|  | [optional] 

### Return type

[**MappedEntityCollection**](MappedEntityCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated subareas. |  -  |
**400** | Invalid pagination or field selection. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_super_area_by_id**
> WorldArea get_super_area_by_id(game, language, ankama_id)

Get one super-area

### Example


```python
import dofusdude
from dofusdude.models.world_area import WorldArea
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    ankama_id = 0 # int | 

    try:
        # Get one super-area
        api_response = api_instance.get_super_area_by_id(game, language, ankama_id)
        print("The response of GameDataApi->get_super_area_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->get_super_area_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **ankama_id** | **int**|  | 

### Return type

[**WorldArea**](WorldArea.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complete localized super-area document. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_super_areas**
> MappedEntityCollection get_super_areas(game, language, page_number=page_number, page_size=page_size, fields_super_areas=fields_super_areas)

List super-areas

### Example


```python
import dofusdude
from dofusdude.models.mapped_entity_collection import MappedEntityCollection
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    page_number = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)
    fields_super_areas = 'fields_super_areas_example' # str |  (optional)

    try:
        # List super-areas
        api_response = api_instance.get_super_areas(game, language, page_number=page_number, page_size=page_size, fields_super_areas=fields_super_areas)
        print("The response of GameDataApi->get_super_areas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->get_super_areas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **page_number** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]
 **fields_super_areas** | **str**|  | [optional] 

### Return type

[**MappedEntityCollection**](MappedEntityCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated super-areas. |  -  |
**400** | Invalid pagination or field selection. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_areas**
> List[MappedEntityListEntry] search_areas(game, language, query, limit=limit)

Search areas

### Example


```python
import dofusdude
from dofusdude.models.mapped_entity_list_entry import MappedEntityListEntry
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    query = 'query_example' # str | 
    limit = 8 # int |  (optional) (default to 8)

    try:
        # Search areas
        api_response = api_instance.search_areas(game, language, query, limit=limit)
        print("The response of GameDataApi->search_areas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->search_areas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **query** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 8]

### Return type

[**List[MappedEntityListEntry]**](MappedEntityListEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Matching localized summaries. |  -  |
**404** | No matching entities. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_classes**
> List[MappedEntityListEntry] search_classes(game, language, query, limit=limit)

Search classes

### Example


```python
import dofusdude
from dofusdude.models.mapped_entity_list_entry import MappedEntityListEntry
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    query = 'query_example' # str | 
    limit = 8 # int |  (optional) (default to 8)

    try:
        # Search classes
        api_response = api_instance.search_classes(game, language, query, limit=limit)
        print("The response of GameDataApi->search_classes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->search_classes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **query** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 8]

### Return type

[**List[MappedEntityListEntry]**](MappedEntityListEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Matching localized summaries. |  -  |
**404** | No matching entities. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_monsters**
> List[MappedEntityListEntry] search_monsters(game, language, query, limit=limit)

Search monsters

### Example


```python
import dofusdude
from dofusdude.models.mapped_entity_list_entry import MappedEntityListEntry
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    query = 'query_example' # str | 
    limit = 8 # int |  (optional) (default to 8)

    try:
        # Search monsters
        api_response = api_instance.search_monsters(game, language, query, limit=limit)
        print("The response of GameDataApi->search_monsters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->search_monsters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **query** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 8]

### Return type

[**List[MappedEntityListEntry]**](MappedEntityListEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Matching localized summaries. |  -  |
**404** | No matching entities. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_spells**
> List[MappedEntityListEntry] search_spells(game, language, query, limit=limit)

Search spells

### Example


```python
import dofusdude
from dofusdude.models.mapped_entity_list_entry import MappedEntityListEntry
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    query = 'query_example' # str | 
    limit = 8 # int |  (optional) (default to 8)

    try:
        # Search spells
        api_response = api_instance.search_spells(game, language, query, limit=limit)
        print("The response of GameDataApi->search_spells:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->search_spells: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **query** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 8]

### Return type

[**List[MappedEntityListEntry]**](MappedEntityListEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Matching localized summaries. |  -  |
**404** | No matching entities. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_subareas**
> List[MappedEntityListEntry] search_subareas(game, language, query, limit=limit)

Search subareas

### Example


```python
import dofusdude
from dofusdude.models.mapped_entity_list_entry import MappedEntityListEntry
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    query = 'query_example' # str | 
    limit = 8 # int |  (optional) (default to 8)

    try:
        # Search subareas
        api_response = api_instance.search_subareas(game, language, query, limit=limit)
        print("The response of GameDataApi->search_subareas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->search_subareas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **query** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 8]

### Return type

[**List[MappedEntityListEntry]**](MappedEntityListEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Matching localized summaries. |  -  |
**404** | No matching entities. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_super_areas**
> List[MappedEntityListEntry] search_super_areas(game, language, query, limit=limit)

Search super-areas

### Example


```python
import dofusdude
from dofusdude.models.mapped_entity_list_entry import MappedEntityListEntry
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://beta.api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.GameDataApi(api_client)
    game = 'game_example' # str | 
    language = 'language_example' # str | 
    query = 'query_example' # str | 
    limit = 8 # int |  (optional) (default to 8)

    try:
        # Search super-areas
        api_response = api_instance.search_super_areas(game, language, query, limit=limit)
        print("The response of GameDataApi->search_super_areas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameDataApi->search_super_areas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  | 
 **language** | **str**|  | 
 **query** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 8]

### Return type

[**List[MappedEntityListEntry]**](MappedEntityListEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Matching localized summaries. |  -  |
**404** | No matching entities. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

