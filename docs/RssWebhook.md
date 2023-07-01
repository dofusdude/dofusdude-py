# RssWebhook


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**whitelist** | **List[str]** |  | [optional] 
**blacklist** | **List[str]** |  | [optional] 
**subscriptions** | **List[str]** |  | [optional] 
**format** | **str** |  | [optional] 
**preview_length** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**last_fired_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from dofusdude.models.rss_webhook import RssWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of RssWebhook from a JSON string
rss_webhook_instance = RssWebhook.from_json(json)
# print the JSON string representation of the object
print RssWebhook.to_json()

# convert the object into a dict
rss_webhook_dict = rss_webhook_instance.to_dict()
# create an instance of RssWebhook from a dict
rss_webhook_form_dict = rss_webhook.from_dict(rss_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


