# coding: utf-8

"""
    Dofusdude

    # A project for you - the developer. The free, always-up-to-date, low-latency, insert-buzzword-here Ankama API for your next cool project!  ## Client SDKs Don't write types or functions yourself - I already (kinda) did! 😉 - [Javascript](https://github.com/dofusdude/dofusdude-js) npm i dofusdude-js --save - [Typescript](https://github.com/dofusdude/dofusdude-ts) npm i dofusdude-ts --save - [Go](https://github.com/dofusdude/dodugo) go get -u github.com/dofusdude/dodugo - [Python](https://github.com/dofusdude/dofusdude-py) pip install dofusdude  Everything, including this site, is generated out of the [Docs Repo](https://github.com/dofusdude/api-docs). Consider it the Single Source of Truth. If there is a problem with the SDKs, create an issue there.  Your favorite language is missing? Please let me know!  # Main Features - 🥷 **Seamless Auto-Update** load data in the background when a new Dofus version is released and serving it within 2 minutes with atomic data source switching. No downtime and no effects for the user, just always up-to-date.  - ⚡ **Blazingly Fast** all data in-memory, aggressive caching over short time spans, HTTP/2 multiplexing, written in Go, optimized for low latency, hosted on bare metal in 🇩🇪.  - 🩸 **Dofus 2 Beta** from stable to bleeding edge by replacing /dofus2 with /dofus2beta.  - 🗣️ **Multilingual** supporting _en_, _fr_, _es_, _pt_ including the dropped languages from the Dofus website _de_ and _it_.  - 🧠 **Search by Relevance** allowing typos in name and description, handled by language specific text analysis and indexing by the powerful [Meilisearch](https://www.meilisearch.com) written in Rust.  - 🕵️ **Complete** actual data from the game including items invisible to the encyclopedia like quest items.  - 🖼️ **HD Images** rendering vector graphics into PNGs up to 800x800 px in the background.   ## Current state - Weapons ✅ - Equipment ✅ - Sets ✅ - Resources ✅ - Consumables ✅ - Pets ✅ - Mounts ✅ - Cosmetics/Ceremonial Items ✅ - Harnesses ✅ - Quest Items ✅ - Almanax ✅ - Monsters ❌ - Spells ❌  ... and much more on the Roadmap on my Discord.   ## Deploy now. Use forever. Everything you see here on this site, you can use now and forever. Updates could introduce new fields, new paths or parameter but never break backwards compatibility, so no field or parameter will be deleted.  There is one exception! **The API will _always_ choose being up-to-date over everything else**. So if Ankama decides to drop languages from the game like they did with their website, the API will loose support for them, too.  ## Only the beginning... 🤯 I want this project to be useful and not just add plain GET-categories no one needs.  There is a long list of features I want to add (see the Roadmap on my [Discord](https://discord.gg/3EtHskZD8h)). But they are all focussed on you, the developers. So please let me know what you need. I will change the list based on demand.  # Get started! 🥳 Scroll down and try it for yourself!  Or see how these other awesome projects use it: - [KaellyBot](https://github.com/Kaysoro/KaellyBot) by Kaysoro - [Dofus Craftlist](https://dofuscraftlist-dev.netlify.app) by Lystina - [AlmanaxApp](https://almanaxapp.netlify.app) by Lystina - [luwnarya.fr](https://luwnarya.fr)  I highly recommend using the SDKs for quick results. I use them myself for microservices for the API.  ## Thank you! I highly welcome everyone on my [Discord](https://discord.gg/3EtHskZD8h) to just talk about projects and use cases or give feedback of any kind.  The servers have a fixed monthly cost to provide very fast responses. If you want to help me keeping them running or simply  donate, consider becoming a [GitHub Sponsor](https://github.com/sponsors/dofusdude).    # noqa: E501

    The version of the OpenAPI document: 0.5.6
    Contact: stelzo@steado.de
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from dofusdude import schemas  # noqa: F401


class Cosmetic(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            ankama_id = schemas.IntSchema
            name = schemas.StrSchema
            description = schemas.StrSchema
            
            
            class type(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        name = schemas.StrSchema
                        __annotations__ = {
                            "name": name,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'type':
                    return super().__new__(
                        cls,
                        *args,
                        name=name,
                        _configuration=_configuration,
                        **kwargs,
                    )
            level = schemas.IntSchema
            pods = schemas.IntSchema
        
            @staticmethod
            def image_urls() -> typing.Type['ImageUrls']:
                return ImageUrls
            
            
            class effects(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EffectsEntry']:
                        return EffectsEntry
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'effects':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class conditions(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ConditionEntry']:
                        return ConditionEntry
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'conditions':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class recipe(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['RecipeEntry']:
                        return RecipeEntry
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'recipe':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "ankama_id": ankama_id,
                "name": name,
                "description": description,
                "type": type,
                "level": level,
                "pods": pods,
                "image_urls": image_urls,
                "effects": effects,
                "conditions": conditions,
                "recipe": recipe,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ankama_id"]) -> MetaOapg.properties.ankama_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["level"]) -> MetaOapg.properties.level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pods"]) -> MetaOapg.properties.pods: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_urls"]) -> 'ImageUrls': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effects"]) -> MetaOapg.properties.effects: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions"]) -> MetaOapg.properties.conditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipe"]) -> MetaOapg.properties.recipe: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ankama_id", "name", "description", "type", "level", "pods", "image_urls", "effects", "conditions", "recipe", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ankama_id"]) -> typing.Union[MetaOapg.properties.ankama_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["level"]) -> typing.Union[MetaOapg.properties.level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pods"]) -> typing.Union[MetaOapg.properties.pods, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_urls"]) -> typing.Union['ImageUrls', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effects"]) -> typing.Union[MetaOapg.properties.effects, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions"]) -> typing.Union[MetaOapg.properties.conditions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipe"]) -> typing.Union[MetaOapg.properties.recipe, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ankama_id", "name", "description", "type", "level", "pods", "image_urls", "effects", "conditions", "recipe", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ankama_id: typing.Union[MetaOapg.properties.ankama_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        level: typing.Union[MetaOapg.properties.level, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pods: typing.Union[MetaOapg.properties.pods, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        image_urls: typing.Union['ImageUrls', schemas.Unset] = schemas.unset,
        effects: typing.Union[MetaOapg.properties.effects, list, tuple, None, schemas.Unset] = schemas.unset,
        conditions: typing.Union[MetaOapg.properties.conditions, list, tuple, None, schemas.Unset] = schemas.unset,
        recipe: typing.Union[MetaOapg.properties.recipe, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Cosmetic':
        return super().__new__(
            cls,
            *args,
            ankama_id=ankama_id,
            name=name,
            description=description,
            type=type,
            level=level,
            pods=pods,
            image_urls=image_urls,
            effects=effects,
            conditions=conditions,
            recipe=recipe,
            _configuration=_configuration,
            **kwargs,
        )

from dofusdude.model.condition_entry import ConditionEntry
from dofusdude.model.effects_entry import EffectsEntry
from dofusdude.model.image_urls import ImageUrls
from dofusdude.model.recipe_entry import RecipeEntry
