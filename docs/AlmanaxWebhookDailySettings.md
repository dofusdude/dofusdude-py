# AlmanaxWebhookDailySettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timezone** | **str** | Timezone of your community to determine midnight. | [optional] [default to 'Europe/Paris']
**midnight_offset** | **int** | Hours added to midnight at the selected timezone. 8 &#x3D; 8:00 in the morning. | [optional] [default to 0]

## Example

```python
from dofusdude.models.almanax_webhook_daily_settings import AlmanaxWebhookDailySettings

# TODO update the JSON string below
json = "{}"
# create an instance of AlmanaxWebhookDailySettings from a JSON string
almanax_webhook_daily_settings_instance = AlmanaxWebhookDailySettings.from_json(json)
# print the JSON string representation of the object
print(AlmanaxWebhookDailySettings.to_json())

# convert the object into a dict
almanax_webhook_daily_settings_dict = almanax_webhook_daily_settings_instance.to_dict()
# create an instance of AlmanaxWebhookDailySettings from a dict
almanax_webhook_daily_settings_form_dict = almanax_webhook_daily_settings.from_dict(almanax_webhook_daily_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


