# PutTwitterWebhook



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**whitelist** | **List[str]** |  | [optional] 
**blacklist** | **List[str]** |  | [optional] 
**subscriptions** | **List[str]** | Get the available subscriptions with /meta/webhooks/twitter | [optional] 
**preview_length** | **int** |  | [optional] 

## Example

```python
from dofusdude.models.put_twitter_webhook import PutTwitterWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of PutTwitterWebhook from a JSON string
put_twitter_webhook_instance = PutTwitterWebhook.from_json(json)
# print the JSON string representation of the object
print PutTwitterWebhook.to_json()

# convert the object into a dict
put_twitter_webhook_dict = put_twitter_webhook_instance.to_dict()
# create an instance of PutTwitterWebhook from a dict
put_twitter_webhook_form_dict = put_twitter_webhook.from_dict(put_twitter_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


