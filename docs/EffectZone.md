# EffectZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw** | **str** | Original compact zone encoding when the source provides one. | [optional] 
**shape** | [**ZoneShape**](ZoneShape.md) |  | 
**size** | **int** | Effective outer size of the area. A point has size 0. Whole-map and custom-cell shapes omit it. | [optional] 
**min_size** | **int** | Effective inner size for hollow or minimum-size shapes. Omitted when the shape has no inner boundary. | [optional] 
**cell_ids** | **List[int]** |  | 
**damage_decrease_step_percent** | **int** |  | [optional] 
**max_damage_decrease_apply_count** | **int** |  | [optional] 
**forced_direction** | **int** |  | [optional] 
**include_carried** | **bool** |  | [optional] 
**stop_at_target** | **bool** |  | [optional] 
**only_affect_in_sight_line** | **bool** |  | [optional] 

## Example

```python
from dofusdude.models.effect_zone import EffectZone

# TODO update the JSON string below
json = "{}"
# create an instance of EffectZone from a JSON string
effect_zone_instance = EffectZone.from_json(json)
# print the JSON string representation of the object
print(EffectZone.to_json())

# convert the object into a dict
effect_zone_dict = effect_zone_instance.to_dict()
# create an instance of EffectZone from a dict
effect_zone_from_dict = EffectZone.from_dict(effect_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


