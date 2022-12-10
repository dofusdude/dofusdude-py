# dofusdude.model.effects_entry.EffectsEntry

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**int_minimum** | decimal.Decimal, int,  | decimal.Decimal,  | minimum int value, can be a single if ignore_int_max and no ignore_int_min | [optional] 
**int_maximum** | decimal.Decimal, int,  | decimal.Decimal,  | maximum int value, if not ignore_int_max and not ignore_int_min, the effect has a range value | [optional] 
**[type](#type)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**ignore_int_min** | bool,  | BoolClass,  | ignore the int min field because the actual value is a string. For readability the templated field is the only important field in this case.  | [optional] 
**ignore_int_max** | bool,  | BoolClass,  | ignore the int max field, if ignore_int_min is true, int min is a single value | [optional] 
**formatted** | str,  | str,  | all fields from above encoded in a single string | [optional] 
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
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**is_meta** | bool,  | BoolClass,  | true if a type is generated from the Api instead of Ankama. In that case, always prefer showing the templated string and omit everything else. The \&quot;name\&quot; field will have an english description of the meta type. An example for such effects are class sets effects. | [optional] 
**is_active** | bool,  | BoolClass,  | Affects target or source actively. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

