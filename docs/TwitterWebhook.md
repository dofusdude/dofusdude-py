# TwitterWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
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
from dofusdude.models.twitter_webhook import TwitterWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterWebhook from a JSON string
twitter_webhook_instance = TwitterWebhook.from_json(json)
# print the JSON string representation of the object
print(TwitterWebhook.to_json())

# convert the object into a dict
twitter_webhook_dict = twitter_webhook_instance.to_dict()
# create an instance of TwitterWebhook from a dict
twitter_webhook_from_dict = TwitterWebhook.from_dict(twitter_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


