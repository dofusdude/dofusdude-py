# AlmanaxWebhook



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**daily_settings** | [**AlmanaxWebhookDailySettings**](AlmanaxWebhookDailySettings.md) |  | [optional] 
**bonus_whitelist** | **List[str]** | Only post when these bonuses come up. From all available bonuses (ids) from /dofus2/meta/{language}/almanax/bonuses. | [optional] 
**bonus_blacklist** | **List[str]** | Skip the day when these bonuses come up. From all available bonuses (ids) from /dofus2/meta/{language}/almanax/bonuses | [optional] 
**subscriptions** | **List[str]** | Get the available subscriptions with /meta/webhooks/almanax | [optional] 
**iso_date** | **bool** | If false, it will use common local time formats and weekday translations. If true, the format is YYYY-MM-DD. | [optional] [default to False]
**mentions** | **Dict[str, List[CreateAlmanaxWebhookMentionsValueInner]]** | Almanax bonus ids mapped to array of mentions. | [optional] 
**intervals** | **List[str]** | - Daily posts each day, filtering with Black/Whitelist and mentions are applied daily. - Weekly posts the next 7 days (excluding the posting day) once per week at the specified time. With only weekly selected, of all mentions, only prior notices will come through daily. The 7 day preview gets filtered by the Black/Whitelist. - Monthly posts a preview of the next month from first to last date. The post will be on the last day of a month (ignoring day of the week) at the specified time. Mentions and filtering works like weekly. The biggest difference between daily and the other two is that daily always posts the current day while monthly and weekly only show future days. You can always combine the intervals by selecting multiple intervals for one hook or create multiple hooks for the same channel with different settings to get every highly specific combination you want. | [optional] 
**weekly_weekday** | **str** | When to post the weekly preview at the specified time. | [optional] 
**created_at** | **datetime** |  | [optional] 
**last_fired_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from dofusdude.models.almanax_webhook import AlmanaxWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of AlmanaxWebhook from a JSON string
almanax_webhook_instance = AlmanaxWebhook.from_json(json)
# print the JSON string representation of the object
print AlmanaxWebhook.to_json()

# convert the object into a dict
almanax_webhook_dict = almanax_webhook_instance.to_dict()
# create an instance of AlmanaxWebhook from a dict
almanax_webhook_form_dict = almanax_webhook.from_dict(almanax_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


