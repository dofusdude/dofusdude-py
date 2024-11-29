# dofusdude.WebhooksApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_webhooks_almanax_id**](WebhooksApi.md#delete_webhooks_almanax_id) | **DELETE** /webhooks/almanax/{id} | Unregister Almanax Hook
[**delete_webhooks_rss_id**](WebhooksApi.md#delete_webhooks_rss_id) | **DELETE** /webhooks/rss/{id} | Unregister RSS Hook
[**delete_webhooks_twitter_id**](WebhooksApi.md#delete_webhooks_twitter_id) | **DELETE** /webhooks/twitter/{id} | Unregister Twitter Hook
[**get_meta_webhooks_almanax**](WebhooksApi.md#get_meta_webhooks_almanax) | **GET** /meta/webhooks/almanax | Get Almanax Hook Metainfo
[**get_meta_webhooks_rss**](WebhooksApi.md#get_meta_webhooks_rss) | **GET** /meta/webhooks/rss | Get RSS Hook Metainfo
[**get_meta_webhooks_twitter**](WebhooksApi.md#get_meta_webhooks_twitter) | **GET** /meta/webhooks/twitter | Get Twitter Hook Metainfo
[**get_webhooks_almanax_id**](WebhooksApi.md#get_webhooks_almanax_id) | **GET** /webhooks/almanax/{id} | Get Almanax Hook
[**get_webhooks_rss_id**](WebhooksApi.md#get_webhooks_rss_id) | **GET** /webhooks/rss/{id} | Get RSS Hook
[**get_webhooks_twitter_id**](WebhooksApi.md#get_webhooks_twitter_id) | **GET** /webhooks/twitter/{id} | Get Twitter Hook
[**post_webhooks_almanax**](WebhooksApi.md#post_webhooks_almanax) | **POST** /webhooks/almanax | Register Almanax Hook
[**post_webhooks_rss**](WebhooksApi.md#post_webhooks_rss) | **POST** /webhooks/rss | Register RSS Hook
[**post_webhooks_twitter**](WebhooksApi.md#post_webhooks_twitter) | **POST** /webhooks/twitter | Register Twitter Hook
[**put_webhooks_almanax_id**](WebhooksApi.md#put_webhooks_almanax_id) | **PUT** /webhooks/almanax/{id} | Update Almanax Hook
[**put_webhooks_rss_id**](WebhooksApi.md#put_webhooks_rss_id) | **PUT** /webhooks/rss/{id} | Update RSS Hook
[**put_webhooks_twitter_id**](WebhooksApi.md#put_webhooks_twitter_id) | **PUT** /webhooks/twitter/{id} | Update Twitter Hook


# **delete_webhooks_almanax_id**
> delete_webhooks_almanax_id(id)

Unregister Almanax Hook

Delete a Webhook from the service.

### Example


```python
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
    api_instance = dofusdude.WebhooksApi(api_client)
    id = 'id_example' # str | the ID returned from the API when creating the webhook

    try:
        # Unregister Almanax Hook
        api_instance.delete_webhooks_almanax_id(id)
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_webhooks_almanax_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID returned from the API when creating the webhook | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhooks_rss_id**
> delete_webhooks_rss_id(id)

Unregister RSS Hook

Delete a Webhook from the service.

### Example


```python
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
    api_instance = dofusdude.WebhooksApi(api_client)
    id = 'id_example' # str | the ID returned from the API when creating the webhook

    try:
        # Unregister RSS Hook
        api_instance.delete_webhooks_rss_id(id)
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_webhooks_rss_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID returned from the API when creating the webhook | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhooks_twitter_id**
> delete_webhooks_twitter_id(id)

Unregister Twitter Hook

Delete a Webhook from the service.

### Example


```python
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
    api_instance = dofusdude.WebhooksApi(api_client)
    id = 'id_example' # str | the ID returned from the API when creating the webhook

    try:
        # Unregister Twitter Hook
        api_instance.delete_webhooks_twitter_id(id)
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_webhooks_twitter_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID returned from the API when creating the webhook | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta_webhooks_almanax**
> GetMetaWebhooksTwitter200Response get_meta_webhooks_almanax()

Get Almanax Hook Metainfo

Get a list of all available subscriptions. 

### Example


```python
import dofusdude
from dofusdude.models.get_meta_webhooks_twitter200_response import GetMetaWebhooksTwitter200Response
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
    api_instance = dofusdude.WebhooksApi(api_client)

    try:
        # Get Almanax Hook Metainfo
        api_response = api_instance.get_meta_webhooks_almanax()
        print("The response of WebhooksApi->get_meta_webhooks_almanax:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_meta_webhooks_almanax: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMetaWebhooksTwitter200Response**](GetMetaWebhooksTwitter200Response.md)

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

# **get_meta_webhooks_rss**
> GetMetaWebhooksTwitter200Response get_meta_webhooks_rss()

Get RSS Hook Metainfo

Get a list of all available subscriptions. 

### Example


```python
import dofusdude
from dofusdude.models.get_meta_webhooks_twitter200_response import GetMetaWebhooksTwitter200Response
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
    api_instance = dofusdude.WebhooksApi(api_client)

    try:
        # Get RSS Hook Metainfo
        api_response = api_instance.get_meta_webhooks_rss()
        print("The response of WebhooksApi->get_meta_webhooks_rss:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_meta_webhooks_rss: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMetaWebhooksTwitter200Response**](GetMetaWebhooksTwitter200Response.md)

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

# **get_meta_webhooks_twitter**
> GetMetaWebhooksTwitter200Response get_meta_webhooks_twitter()

Get Twitter Hook Metainfo

Get a list of all available subscriptions. 

### Example


```python
import dofusdude
from dofusdude.models.get_meta_webhooks_twitter200_response import GetMetaWebhooksTwitter200Response
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
    api_instance = dofusdude.WebhooksApi(api_client)

    try:
        # Get Twitter Hook Metainfo
        api_response = api_instance.get_meta_webhooks_twitter()
        print("The response of WebhooksApi->get_meta_webhooks_twitter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_meta_webhooks_twitter: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMetaWebhooksTwitter200Response**](GetMetaWebhooksTwitter200Response.md)

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

# **get_webhooks_almanax_id**
> AlmanaxWebhook get_webhooks_almanax_id(id)

Get Almanax Hook

Retrieve details about an existing Almanax Webhook with a given uuid.

### Example


```python
import dofusdude
from dofusdude.models.almanax_webhook import AlmanaxWebhook
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
    api_instance = dofusdude.WebhooksApi(api_client)
    id = 'id_example' # str | the ID returned from the API when creating the webhook

    try:
        # Get Almanax Hook
        api_response = api_instance.get_webhooks_almanax_id(id)
        print("The response of WebhooksApi->get_webhooks_almanax_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhooks_almanax_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID returned from the API when creating the webhook | 

### Return type

[**AlmanaxWebhook**](AlmanaxWebhook.md)

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

# **get_webhooks_rss_id**
> RssWebhook get_webhooks_rss_id(id)

Get RSS Hook

Retrieve details about an existing RSS Webhook with a given uuid.

### Example


```python
import dofusdude
from dofusdude.models.rss_webhook import RssWebhook
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
    api_instance = dofusdude.WebhooksApi(api_client)
    id = 'id_example' # str | the ID returned from the API when creating the webhook

    try:
        # Get RSS Hook
        api_response = api_instance.get_webhooks_rss_id(id)
        print("The response of WebhooksApi->get_webhooks_rss_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhooks_rss_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID returned from the API when creating the webhook | 

### Return type

[**RssWebhook**](RssWebhook.md)

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

# **get_webhooks_twitter_id**
> TwitterWebhook get_webhooks_twitter_id(id)

Get Twitter Hook

Retrieve details about an existing Twitter Webhook with a given uuid.

### Example


```python
import dofusdude
from dofusdude.models.twitter_webhook import TwitterWebhook
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
    api_instance = dofusdude.WebhooksApi(api_client)
    id = 'id_example' # str | the ID returned from the API when creating the webhook

    try:
        # Get Twitter Hook
        api_response = api_instance.get_webhooks_twitter_id(id)
        print("The response of WebhooksApi->get_webhooks_twitter_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhooks_twitter_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID returned from the API when creating the webhook | 

### Return type

[**TwitterWebhook**](TwitterWebhook.md)

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

# **post_webhooks_almanax**
> post_webhooks_almanax(create_almanax_webhook=create_almanax_webhook)

Register Almanax Hook

Register a new Webhook to post Almanax updates.

### Example


```python
import dofusdude
from dofusdude.models.create_almanax_webhook import CreateAlmanaxWebhook
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
    api_instance = dofusdude.WebhooksApi(api_client)
    create_almanax_webhook = {"bonus_whitelist":null,"bonus_blacklist":null,"subscriptions":["dofus3_fr"],"format":"discord","callback":"https://discord.com/api/webhooks/XYZ","daily_settings":{"timezone":"Europe/Paris","midnight_offset":0},"iso_date":false,"mentions":{"kolossium-experience":[{"discord_id":1234,"is_role":true,"ping_days_before":null}]},"intervals":["daily"],"weekly_weekday":"sunday"} # CreateAlmanaxWebhook |  (optional)

    try:
        # Register Almanax Hook
        api_instance.post_webhooks_almanax(create_almanax_webhook=create_almanax_webhook)
    except Exception as e:
        print("Exception when calling WebhooksApi->post_webhooks_almanax: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_almanax_webhook** | [**CreateAlmanaxWebhook**](CreateAlmanaxWebhook.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_webhooks_rss**
> post_webhooks_rss(create_rss_webhook=create_rss_webhook)

Register RSS Hook

Register a new Webhook to post RSS news as soon as they are posted.

### Example


```python
import dofusdude
from dofusdude.models.create_rss_webhook import CreateRSSWebhook
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
    api_instance = dofusdude.WebhooksApi(api_client)
    create_rss_webhook = {"whitelist":["retro"],"blacklist":null,"subscriptions":["dofus3-en-official-news"],"format":"discord","preview_length":2000,"callback":"https://discord.com/api/webhooks/XYZ"} # CreateRSSWebhook |  (optional)

    try:
        # Register RSS Hook
        api_instance.post_webhooks_rss(create_rss_webhook=create_rss_webhook)
    except Exception as e:
        print("Exception when calling WebhooksApi->post_webhooks_rss: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_rss_webhook** | [**CreateRSSWebhook**](CreateRSSWebhook.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_webhooks_twitter**
> post_webhooks_twitter(create_twitter_webhook=create_twitter_webhook)

Register Twitter Hook

Register a new Webhook to post Twitter updates as soon as they are posted.

### Example


```python
import dofusdude
from dofusdude.models.create_twitter_webhook import CreateTwitterWebhook
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
    api_instance = dofusdude.WebhooksApi(api_client)
    create_twitter_webhook = {"whitelist":null,"blacklist":null,"subscriptions":["DOFUSfr"],"format":"discord","preview_length":280,"callback":"https://discord.com/api/webhooks/XYZ"} # CreateTwitterWebhook |  (optional)

    try:
        # Register Twitter Hook
        api_instance.post_webhooks_twitter(create_twitter_webhook=create_twitter_webhook)
    except Exception as e:
        print("Exception when calling WebhooksApi->post_webhooks_twitter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_twitter_webhook** | [**CreateTwitterWebhook**](CreateTwitterWebhook.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_webhooks_almanax_id**
> AlmanaxWebhook put_webhooks_almanax_id(id, put_almanax_webhook=put_almanax_webhook)

Update Almanax Hook

Update the details of an Almanax Webhook. All fields are optional and arrays will be overwritten, so always put all selected items of an array.

### Example


```python
import dofusdude
from dofusdude.models.almanax_webhook import AlmanaxWebhook
from dofusdude.models.put_almanax_webhook import PutAlmanaxWebhook
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
    api_instance = dofusdude.WebhooksApi(api_client)
    id = 'id_example' # str | the ID returned from the API when creating the webhook
    put_almanax_webhook = {"bonus_whitelist":[],"bonus_blacklist":null,"subscriptions":null,"daily_settings":{"timezone":"Europe/Paris","midnight_offset":0},"iso_date":false,"mentions":{"kolossium-experience":[{"discord_id":1234,"is_role":true,"ping_days_before":null}]},"intervals":["daily"],"weekly_weekday":"sunday"} # PutAlmanaxWebhook |  (optional)

    try:
        # Update Almanax Hook
        api_response = api_instance.put_webhooks_almanax_id(id, put_almanax_webhook=put_almanax_webhook)
        print("The response of WebhooksApi->put_webhooks_almanax_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->put_webhooks_almanax_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID returned from the API when creating the webhook | 
 **put_almanax_webhook** | [**PutAlmanaxWebhook**](PutAlmanaxWebhook.md)|  | [optional] 

### Return type

[**AlmanaxWebhook**](AlmanaxWebhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_webhooks_rss_id**
> RssWebhook put_webhooks_rss_id(id, put_rss_webhook=put_rss_webhook)

Update RSS Hook

Update the details of a RSS Webhook. All fields are optional and arrays will be overwritten, so always put all selected items of an array.

### Example


```python
import dofusdude
from dofusdude.models.put_rss_webhook import PutRSSWebhook
from dofusdude.models.rss_webhook import RssWebhook
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
    api_instance = dofusdude.WebhooksApi(api_client)
    id = 'id_example' # str | the ID returned from the API when creating the webhook
    put_rss_webhook = {"whitelist":null,"blacklist":null,"subscriptions":null,"preview_length":60} # PutRSSWebhook |  (optional)

    try:
        # Update RSS Hook
        api_response = api_instance.put_webhooks_rss_id(id, put_rss_webhook=put_rss_webhook)
        print("The response of WebhooksApi->put_webhooks_rss_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->put_webhooks_rss_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID returned from the API when creating the webhook | 
 **put_rss_webhook** | [**PutRSSWebhook**](PutRSSWebhook.md)|  | [optional] 

### Return type

[**RssWebhook**](RssWebhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_webhooks_twitter_id**
> TwitterWebhook put_webhooks_twitter_id(id, put_twitter_webhook=put_twitter_webhook)

Update Twitter Hook

Update the details of a Twitter Webhook. All fields are optional and arrays will be overwritten, so always put all selected items of an array.

### Example


```python
import dofusdude
from dofusdude.models.put_twitter_webhook import PutTwitterWebhook
from dofusdude.models.twitter_webhook import TwitterWebhook
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
    api_instance = dofusdude.WebhooksApi(api_client)
    id = 'id_example' # str | the ID returned from the API when creating the webhook
    put_twitter_webhook = {"whitelist":["retro"],"blacklist":null,"subscriptions":["dofus3-en-official-changelog"],"preview_length":null} # PutTwitterWebhook |  (optional)

    try:
        # Update Twitter Hook
        api_response = api_instance.put_webhooks_twitter_id(id, put_twitter_webhook=put_twitter_webhook)
        print("The response of WebhooksApi->put_webhooks_twitter_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->put_webhooks_twitter_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID returned from the API when creating the webhook | 
 **put_twitter_webhook** | [**PutTwitterWebhook**](PutTwitterWebhook.md)|  | [optional] 

### Return type

[**TwitterWebhook**](TwitterWebhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

