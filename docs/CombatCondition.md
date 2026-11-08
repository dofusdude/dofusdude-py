# CombatCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** |  | [optional] 
**negated** | **bool** |  | [optional] 
**subject** | **str** |  | [optional] 
**reference** | [**CombatReference**](CombatReference.md) |  | [optional] 

## Example

```python
from dofusdude.models.combat_condition import CombatCondition

# TODO update the JSON string below
json = "{}"
# create an instance of CombatCondition from a JSON string
combat_condition_instance = CombatCondition.from_json(json)
# print the JSON string representation of the object
print(CombatCondition.to_json())

# convert the object into a dict
combat_condition_dict = combat_condition_instance.to_dict()
# create an instance of CombatCondition from a dict
combat_condition_from_dict = CombatCondition.from_dict(combat_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


