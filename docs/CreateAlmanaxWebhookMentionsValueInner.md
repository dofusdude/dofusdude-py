# CreateAlmanaxWebhookMentionsValueInner

Mention

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discord_id** | **int** | User or role ID directly from Discord. Activate developer mode and right click a user or role to get them. | [optional] 
**is_role** | **bool** | Whether an ID describes a role (true) or user (false). This is needed for formatting the mention command so Discord understands it. | [optional] 
**ping_days_before** | **int** | Get a mention days before the bonus comes up. It will post on the specified time. Also works when the interval is not daily. | [optional] 

## Example

```python
from dofusdude.models.create_almanax_webhook_mentions_value_inner import CreateAlmanaxWebhookMentionsValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAlmanaxWebhookMentionsValueInner from a JSON string
create_almanax_webhook_mentions_value_inner_instance = CreateAlmanaxWebhookMentionsValueInner.from_json(json)
# print the JSON string representation of the object
print(CreateAlmanaxWebhookMentionsValueInner.to_json())

# convert the object into a dict
create_almanax_webhook_mentions_value_inner_dict = create_almanax_webhook_mentions_value_inner_instance.to_dict()
# create an instance of CreateAlmanaxWebhookMentionsValueInner from a dict
create_almanax_webhook_mentions_value_inner_form_dict = create_almanax_webhook_mentions_value_inner.from_dict(create_almanax_webhook_mentions_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


