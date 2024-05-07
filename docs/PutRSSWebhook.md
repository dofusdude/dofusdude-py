# PutRSSWebhook



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**whitelist** | **List[str]** |  | [optional] 
**blacklist** | **List[str]** |  | [optional] 
**subscriptions** | **List[str]** | Get the available subscriptions with /meta/webhooks/rss | [optional] 
**preview_length** | **int** |  | [optional] 

## Example

```python
from dofusdude.models.put_rss_webhook import PutRSSWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of PutRSSWebhook from a JSON string
put_rss_webhook_instance = PutRSSWebhook.from_json(json)
# print the JSON string representation of the object
print(PutRSSWebhook.to_json())

# convert the object into a dict
put_rss_webhook_dict = put_rss_webhook_instance.to_dict()
# create an instance of PutRSSWebhook from a dict
put_rss_webhook_from_dict = PutRSSWebhook.from_dict(put_rss_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


