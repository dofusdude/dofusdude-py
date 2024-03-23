# PutAlmanaxWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonus_whitelist** | **List[str]** | from all available bonuses (ids) from /dofus2/meta/{language}/almanax/bonuses. Delete old entries with empty array []. Just null changes nothing. | [optional] 
**bonus_blacklist** | **List[str]** | from all available bonuses (ids) from /dofus2/meta/{language}/almanax/bonuses. Delete old entries with empty array []. Just null changes nothing. | [optional] 
**subscriptions** | **List[str]** | Get the available subscriptions with /meta/webhooks/almanax | [optional] 
**daily_settings** | [**CreateAlmanaxWebhookDailySettings**](CreateAlmanaxWebhookDailySettings.md) |  | [optional] 
**iso_date** | **bool** | If false, it will use common local time formats and weekday translations. If true, the format is YYYY-MM-DD. | [optional] [default to False]
**mentions** | **Dict[str, List[CreateAlmanaxWebhookMentionsValueInner]]** | Almanax bonus ids mapped to array of mentions. | [optional] 
**intervals** | **List[str]** |  | [optional] 
**weekly_weekday** | **str** | When to post the weekly preview at the specified time. | [optional] 

## Example

```python
from dofusdude.models.put_almanax_webhook import PutAlmanaxWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of PutAlmanaxWebhook from a JSON string
put_almanax_webhook_instance = PutAlmanaxWebhook.from_json(json)
# print the JSON string representation of the object
print(PutAlmanaxWebhook.to_json())

# convert the object into a dict
put_almanax_webhook_dict = put_almanax_webhook_instance.to_dict()
# create an instance of PutAlmanaxWebhook from a dict
put_almanax_webhook_form_dict = put_almanax_webhook.from_dict(put_almanax_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


