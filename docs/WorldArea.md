# WorldArea


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | 
**name** | **str** |  | 
**super_area** | [**CombatReference**](CombatReference.md) |  | [optional] 
**area** | [**CombatReference**](CombatReference.md) |  | [optional] 
**subareas** | [**List[CombatReference]**](CombatReference.md) |  | [optional] 
**monsters** | [**List[CombatReference]**](CombatReference.md) |  | [optional] 

## Example

```python
from dofusdude.models.world_area import WorldArea

# TODO update the JSON string below
json = "{}"
# create an instance of WorldArea from a JSON string
world_area_instance = WorldArea.from_json(json)
# print the JSON string representation of the object
print(WorldArea.to_json())

# convert the object into a dict
world_area_dict = world_area_instance.to_dict()
# create an instance of WorldArea from a dict
world_area_from_dict = WorldArea.from_dict(world_area_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


