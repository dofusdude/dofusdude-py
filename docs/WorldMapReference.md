# WorldMapReference

A map ID and its position within a world-map context. Maps can share coordinates in different contexts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**position_x** | **int** |  | [optional] 
**position_y** | **int** |  | [optional] 
**world_map_id** | **int** |  | [optional] 

## Example

```python
from dofusdude.models.world_map_reference import WorldMapReference

# TODO update the JSON string below
json = "{}"
# create an instance of WorldMapReference from a JSON string
world_map_reference_instance = WorldMapReference.from_json(json)
# print the JSON string representation of the object
print(WorldMapReference.to_json())

# convert the object into a dict
world_map_reference_dict = world_map_reference_instance.to_dict()
# create an instance of WorldMapReference from a dict
world_map_reference_from_dict = WorldMapReference.from_dict(world_map_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


