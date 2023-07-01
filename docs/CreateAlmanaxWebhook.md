# CreateAlmanaxWebhook


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonus_whitelist** | **List[str]** | from all available bonuses (ids) from /dofus2/meta/{language}/almanax/bonuses | [optional] 
**bonus_blacklist** | **List[str]** | from all available bonuses (ids) from /dofus2/meta/{language}/almanax/bonuses | [optional] 
**subscriptions** | **List[str]** | Get the available subscriptions with /meta/webhooks/almanax | 
**format** | **str** |  | 
**callback** | **str** | Discord Webhook URL | 
**daily_settings** | [**CreateAlmanaxWebhookDailySettings**](CreateAlmanaxWebhookDailySettings.md) |  | [optional] 
**iso_date** | **bool** | If false, it will use common local time formats and weekday translations. If true, the format is YYYY-MM-DD. | [optional] [default to False]
**mentions** | **Dict[str, List[CreateAlmanaxWebhookMentionsValueInner]]** | Almanax bonus ids mapped to array of mentions. | [optional] 
**intervals** | **List[str]** | - Daily posts each day, filtering with Black/Whitelist and mentions are applied daily. - Weekly posts the next 7 days (excluding the posting day) once per week at the specified time. With only weekly selected, of all mentions, only prior notices will come through daily. The 7 day preview gets filtered by the Black/Whitelist. - Monthly posts a preview of the next month from first to last date. The post will be on the last day of a month (ignoring day of the week) at the specified time. Mentions and filtering works like weekly. The biggest difference between daily and the other two is that daily always posts the current day while monthly and weekly only show future days. You can always combine the intervals by selecting multiple intervals for one hook or create multiple hooks for the same channel with different settings to get every highly specific combination you want. | 
**weekly_weekday** | **str** | When to post the weekly preview at the specified time. | [optional] 

## Example

```python
from dofusdude.models.create_almanax_webhook import CreateAlmanaxWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAlmanaxWebhook from a JSON string
create_almanax_webhook_instance = CreateAlmanaxWebhook.from_json(json)
# print the JSON string representation of the object
print CreateAlmanaxWebhook.to_json()

# convert the object into a dict
create_almanax_webhook_dict = create_almanax_webhook_instance.to_dict()
# create an instance of CreateAlmanaxWebhook from a dict
create_almanax_webhook_form_dict = create_almanax_webhook.from_dict(create_almanax_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


