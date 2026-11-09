# Condition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** | Comparison to apply to the interpreted requirement value. | [optional] 
**int_value** | **int** |  | [optional] 
**element** | [**TranslatedId**](TranslatedId.md) |  | [optional] 
**kind** | **str** | Interpreted requirement category, such as profession_level or item_received_age. Use this with the operator, values and references rather than decoding original condition tokens. | [optional] 
**unit** | **str** | Unit associated with the requirement value when the interpreted condition supplies one. | [optional] 
**quantity** | **int** |  | [optional] 
**string_value** | **str** |  | [optional] 
**value_label** | **str** |  | [optional] 
**reference** | [**CombatReference**](CombatReference.md) |  | [optional] 
**secondary_reference** | [**CombatReference**](CombatReference.md) |  | [optional] 

## Example

```python
from dofusdude.models.condition import Condition

# TODO update the JSON string below
json = "{}"
# create an instance of Condition from a JSON string
condition_instance = Condition.from_json(json)
# print the JSON string representation of the object
print(Condition.to_json())

# convert the object into a dict
condition_dict = condition_instance.to_dict()
# create an instance of Condition from a dict
condition_from_dict = Condition.from_dict(condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


