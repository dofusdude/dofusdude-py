# dofusdude.model.put_almanax_webhook.PutAlmanaxWebhook

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[bonus_whitelist](#bonus_whitelist)** | list, tuple, None,  | tuple, NoneClass,  | from all available bonuses (ids) from /dofus2/meta/{language}/almanax/bonuses. Delete old entries with empty array []. Just null changes nothing. | [optional] 
**[bonus_blacklist](#bonus_blacklist)** | list, tuple, None,  | tuple, NoneClass,  | from all available bonuses (ids) from /dofus2/meta/{language}/almanax/bonuses. Delete old entries with empty array []. Just null changes nothing. | [optional] 
**[subscriptions](#subscriptions)** | list, tuple, None,  | tuple, NoneClass,  | Get the available subscriptions with /meta/webhooks/almanax | [optional] 
**[daily_settings](#daily_settings)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | [optional] 
**iso_date** | None, bool,  | NoneClass, BoolClass,  | If false, it will use common local time formats and weekday translations. If true, the format is YYYY-MM-DD. | [optional] if omitted the server will use the default value of False
**[mentions](#mentions)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Almanax bonus ids mapped to array of mentions. | [optional] 
**[intervals](#intervals)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**weekly_weekday** | None, str,  | NoneClass, str,  | When to post the weekly preview at the specified time. | [optional] must be one of ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# bonus_whitelist

from all available bonuses (ids) from /dofus2/meta/{language}/almanax/bonuses. Delete old entries with empty array []. Just null changes nothing.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | from all available bonuses (ids) from /dofus2/meta/{language}/almanax/bonuses. Delete old entries with empty array []. Just null changes nothing. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# bonus_blacklist

from all available bonuses (ids) from /dofus2/meta/{language}/almanax/bonuses. Delete old entries with empty array []. Just null changes nothing.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | from all available bonuses (ids) from /dofus2/meta/{language}/almanax/bonuses. Delete old entries with empty array []. Just null changes nothing. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# subscriptions

Get the available subscriptions with /meta/webhooks/almanax

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Get the available subscriptions with /meta/webhooks/almanax | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# daily_settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**timezone** | None, str,  | NoneClass, str,  | Timezone of your community to determine midnight. | [optional] if omitted the server will use the default value of "Europe/Paris"
**midnight_offset** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Hours added to midnight at the selected timezone. 8 &#x3D; 8:00 in the morning. | [optional] if omitted the server will use the default value of 0
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mentions

Almanax bonus ids mapped to array of mentions.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Almanax bonus ids mapped to array of mentions. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | list, tuple,  | tuple,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Mention | 

# items

Mention

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Mention | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**discord_id** | decimal.Decimal, int,  | decimal.Decimal,  | User or role ID directly from Discord. Activate developer mode and right click a user or role to get them. | [optional] 
**is_role** | bool,  | BoolClass,  | Whether an ID describes a role (true) or user (false). This is needed for formatting the mention command so Discord understands it. | [optional] 
**ping_days_before** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Get a mention days before the bonus comes up. It will post on the specified time. Also works when the interval is not daily. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# intervals

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["daily", "weekly", "monthly", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

