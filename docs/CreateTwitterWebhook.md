# CreateTwitterWebhook



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**whitelist** | **List[str]** |  | [optional] 
**blacklist** | **List[str]** |  | [optional] 
**subscriptions** | **List[str]** | Get the available subscriptions with /meta/webhooks/twitter | 
**format** | **str** |  | 
**preview_length** | **int** |  | [optional] 
**callback** | **str** | Discord Webhook URL | 

## Example

```python
from dofusdude.models.create_twitter_webhook import CreateTwitterWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTwitterWebhook from a JSON string
create_twitter_webhook_instance = CreateTwitterWebhook.from_json(json)
# print the JSON string representation of the object
print(CreateTwitterWebhook.to_json())

# convert the object into a dict
create_twitter_webhook_dict = create_twitter_webhook_instance.to_dict()
# create an instance of CreateTwitterWebhook from a dict
create_twitter_webhook_form_dict = create_twitter_webhook.from_dict(create_twitter_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


