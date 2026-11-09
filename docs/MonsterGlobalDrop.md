# MonsterGlobalDrop

A separate global-drop entry with a base percentage range. It is not the per-monster-grade rates table and does not by itself define a final player-specific drop chance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_conditions** | **bool** |  | [optional] 
**item** | [**CombatReference**](CombatReference.md) |  | 
**min_percent** | **float** |  | 
**max_percent** | **float** |  | 
**condition** | **Dict[str, object]** |  | [optional] 
**alteration_id** | **int** |  | [optional] 
**disable_drop_modifier** | **bool** |  | [optional] 

## Example

```python
from dofusdude.models.monster_global_drop import MonsterGlobalDrop

# TODO update the JSON string below
json = "{}"
# create an instance of MonsterGlobalDrop from a JSON string
monster_global_drop_instance = MonsterGlobalDrop.from_json(json)
# print the JSON string representation of the object
print(MonsterGlobalDrop.to_json())

# convert the object into a dict
monster_global_drop_dict = monster_global_drop_instance.to_dict()
# create an instance of MonsterGlobalDrop from a dict
monster_global_drop_from_dict = MonsterGlobalDrop.from_dict(monster_global_drop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


