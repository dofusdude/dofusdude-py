# dofusdude.model.weapon.Weapon

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ankama_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**[type](#type)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**is_weapon** | bool,  | BoolClass,  | always true when the item is a weapon. Many fields are now available. Always check for this flag first when getting single equipment items. | [optional] 
**level** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**pods** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**image_urls** | [**ImageUrls**](ImageUrls.md) | [**ImageUrls**](ImageUrls.md) |  | [optional] 
**[effects](#effects)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**[conditions](#conditions)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**critical_hit_probability** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**critical_hit_bonus** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**is_two_handed** | bool,  | BoolClass,  |  | [optional] 
**max_cast_per_turn** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ap_cost** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[range](#range)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[recipe](#recipe)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**[parent_set](#parent_set)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# effects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EffectsEntry**](EffectsEntry.md) | [**EffectsEntry**](EffectsEntry.md) | [**EffectsEntry**](EffectsEntry.md) |  | 

# conditions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ConditionEntry**](ConditionEntry.md) | [**ConditionEntry**](ConditionEntry.md) | [**ConditionEntry**](ConditionEntry.md) |  | 

# range

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**min** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**max** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# recipe

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RecipeEntry**](RecipeEntry.md) | [**RecipeEntry**](RecipeEntry.md) | [**RecipeEntry**](RecipeEntry.md) |  | 

# parent_set

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

