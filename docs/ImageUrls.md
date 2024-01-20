# ImageUrls

All images except icon are rendered in the background which can take some time (up to hours if all data is completely generated from scratch). Because of this, they can be null if they are not yet rendered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon** | **str** | 60x60 px, always available | [optional] 
**sd** | **str** | 200x200 px | [optional] 
**hq** | **str** | 400x400 px | [optional] 
**hd** | **str** | 800x800 px | [optional] 

## Example

```python
from dofusdude.models.image_urls import ImageUrls

# TODO update the JSON string below
json = "{}"
# create an instance of ImageUrls from a JSON string
image_urls_instance = ImageUrls.from_json(json)
# print the JSON string representation of the object
print ImageUrls.to_json()

# convert the object into a dict
image_urls_dict = image_urls_instance.to_dict()
# create an instance of ImageUrls from a dict
image_urls_form_dict = image_urls.from_dict(image_urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


