# ZoneShape


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**name** | **str** | Resolved shape name, such as point, circle, cross, line, or cone. | 

## Example

```python
from dofusdude.models.zone_shape import ZoneShape

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneShape from a JSON string
zone_shape_instance = ZoneShape.from_json(json)
# print the JSON string representation of the object
print(ZoneShape.to_json())

# convert the object into a dict
zone_shape_dict = zone_shape_instance.to_dict()
# create an instance of ZoneShape from a dict
zone_shape_from_dict = ZoneShape.from_dict(zone_shape_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


