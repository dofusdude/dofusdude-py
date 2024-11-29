# Almanax


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonus** | [**AlmanaxBonus**](AlmanaxBonus.md) |  | [optional] 
**var_date** | **str** |  | [optional] 
**tribute** | [**AlmanaxTribute**](AlmanaxTribute.md) |  | [optional] 
**reward_kamas** | **int** | Amount of Kamas you get as reward for finishing this Almanax quest. | [optional] 

## Example

```python
from dofusdude.models.almanax import Almanax

# TODO update the JSON string below
json = "{}"
# create an instance of Almanax from a JSON string
almanax_instance = Almanax.from_json(json)
# print the JSON string representation of the object
print(Almanax.to_json())

# convert the object into a dict
almanax_dict = almanax_instance.to_dict()
# create an instance of Almanax from a dict
almanax_from_dict = Almanax.from_dict(almanax_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


