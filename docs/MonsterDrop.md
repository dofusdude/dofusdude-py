# MonsterDrop

A possible item drop with base rates indexed by monster grade. Final player-specific chances also depend on conditions and game modifiers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**CombatReference**](CombatReference.md) |  | 
**rates_percent** | [**List[MonsterDropRatesPercentInner]**](MonsterDropRatesPercentInner.md) | Base drop percentages indexed by MonsterGrade.grade, not spell grade or array position. A value of 5 means 5 percent, not 0.05 percent. These are not spawn percentages. | 
**has_conditions** | **bool** | The source reports restrictions. Can be true without a complete client-side condition tree because server-only predicates are not exposed. | 
**drop_id** | **int** |  | [optional] 
**count** | **int** |  | [optional] 
**condition** | **Dict[str, object]** |  | [optional] 
**hidden_if_invalid_conditions** | **bool** |  | [optional] 
**disable_drop_modifier** | **bool** |  | [optional] 
**specific_coefficients** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from dofusdude.models.monster_drop import MonsterDrop

# TODO update the JSON string below
json = "{}"
# create an instance of MonsterDrop from a JSON string
monster_drop_instance = MonsterDrop.from_json(json)
# print the JSON string representation of the object
print(MonsterDrop.to_json())

# convert the object into a dict
monster_drop_dict = monster_drop_instance.to_dict()
# create an instance of MonsterDrop from a dict
monster_drop_from_dict = MonsterDrop.from_dict(monster_drop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


