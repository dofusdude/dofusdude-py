# coding: utf-8

"""
    Dofusdude

    # A project for you - the developer. The free, always-up-to-date, low-latency, insert-buzzword-here Ankama API for your next cool project!  ## Client SDKs Don't write types or functions yourself - I already (kinda) did! 😉 - [Javascript](https://github.com/dofusdude/dofusdude-js) npm i dofusdude-js --save - [Typescript](https://github.com/dofusdude/dofusdude-ts) npm i dofusdude-ts --save - [Go](https://github.com/dofusdude/dodugo) go get -u github.com/dofusdude/dodugo - [Python](https://github.com/dofusdude/dofusdude-py) pip install dofusdude  Everything, including this site, is generated out of the [Docs Repo](https://github.com/dofusdude/api-docs). Consider it the Single Source of Truth. If there is a problem with the SDKs, create an issue there.  Your favorite language is missing? Please let me know!  # Main Features - 🥷 **Seamless Auto-Update** load data in the background when a new Dofus version is released and serving it within 2 minutes with atomic data source switching. No downtime and no effects for the user, just always up-to-date.  - ⚡ **Blazingly Fast** all data in-memory, aggressive caching over short time spans, HTTP/2 multiplexing, written in Go, optimized for low latency, hosted on bare metal in 🇩🇪.  - 📨 **Discord Integration** Ankama related Twitter, RSS and Almanax feeds to post to Discord servers with advanced features like filters or mentions. Use the endpoints as a dev or the official [Web Client](https://discord.dofusdude.com) as a user.  - 🩸 **Dofus 2 Beta** from stable to bleeding edge by replacing /dofus2 with /dofus2beta.  - 🗣️ **Multilingual** supporting _en_, _fr_, _es_, _pt_ including the dropped languages from the Dofus website _de_ and _it_.  - 🧠 **Search by Relevance** allowing typos in name and description, handled by language specific text analysis and indexing by the powerful [Meilisearch](https://www.meilisearch.com) written in Rust.  - 🕵️ **Complete** actual data from the game including items invisible to the encyclopedia like quest items.  - 🖼️ **HD Images** rendering vector graphics into PNGs up to 800x800 px in the background.   ## Current state - Weapons ✅ - Equipment ✅ - Sets ✅ - Resources ✅ - Consumables ✅ - Pets ✅ - Mounts ✅ - Cosmetics/Ceremonial Items ✅ - Harnesses ✅ - Quest Items ✅ - Almanax ✅ - Monsters ❌ - Spells ❌  ... and much more on the Roadmap on my Discord.   ## Deploy now. Use forever. Everything you see here on this site, you can use now and forever. Updates could introduce new fields, new paths or parameter but never break backwards compatibility, so no field or parameter will be deleted.  There is one exception! **The API will _always_ choose being up-to-date over everything else**. So if Ankama decides to drop languages from the game like they did with their website, the API will loose support for them, too.  ## Only the beginning... 🤯 I want this project to be useful and not just add plain GET-categories no one needs.  There is a long list of features I want to add (see the Roadmap on my [Discord](https://discord.gg/3EtHskZD8h)). But they are all focussed on you, the developers. So please let me know what you need. I will change the list based on demand.  # Get started! 🥳 Scroll down and try it for yourself!  Or see how these other awesome projects use it: - [KaellyBot](https://github.com/Kaysoro/KaellyBot) by Kaysoro - [Dofus Craftlist](https://dofuscraftlist-dev.netlify.app) by Lystina - [AlmanaxApp](https://almanaxapp.netlify.app) by Lystina - [luwnarya.fr](https://luwnarya.fr)  I highly recommend using the SDKs for quick results. I use them myself for microservices for the API.  ## Thank you! I highly welcome everyone on my [Discord](https://discord.gg/3EtHskZD8h) to just talk about projects and use cases or give feedback of any kind.  The servers have a fixed monthly cost to provide very fast responses. If you want to help me keeping them running or simply  donate, consider becoming a [GitHub Sponsor](https://github.com/sponsors/dofusdude).    # noqa: E501

    The version of the OpenAPI document: 0.7.0
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


class PutAlmanaxWebhook(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class bonus_whitelist(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'bonus_whitelist':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class bonus_blacklist(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'bonus_blacklist':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class subscriptions(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'subscriptions':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class daily_settings(
                schemas.DictBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneFrozenDictMixin
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class timezone(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'timezone':
                                return super().__new__(
                                    cls,
                                    *args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class midnight_offset(
                            schemas.IntBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneDecimalMixin
                        ):
                        
                        
                            class MetaOapg:
                        
                        
                            def __new__(
                                cls,
                                *args: typing.Union[None, decimal.Decimal, int, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'midnight_offset':
                                return super().__new__(
                                    cls,
                                    *args,
                                    _configuration=_configuration,
                                )
                        __annotations__ = {
                            "timezone": timezone,
                            "midnight_offset": midnight_offset,
                        }
            
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["midnight_offset"]) -> MetaOapg.properties.midnight_offset: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["timezone", "midnight_offset", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["timezone"]) -> typing.Union[MetaOapg.properties.timezone, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["midnight_offset"]) -> typing.Union[MetaOapg.properties.midnight_offset, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["timezone", "midnight_offset", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, None, ],
                    timezone: typing.Union[MetaOapg.properties.timezone, None, str, schemas.Unset] = schemas.unset,
                    midnight_offset: typing.Union[MetaOapg.properties.midnight_offset, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'daily_settings':
                    return super().__new__(
                        cls,
                        *args,
                        timezone=timezone,
                        midnight_offset=midnight_offset,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class iso_date(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'iso_date':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class mentions(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class additional_properties(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class items(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    
                                    class properties:
                                        discord_id = schemas.IntSchema
                                        is_role = schemas.BoolSchema
                                        
                                        
                                        class ping_days_before(
                                            schemas.IntBase,
                                            schemas.NoneBase,
                                            schemas.Schema,
                                            schemas.NoneDecimalMixin
                                        ):
                                        
                                        
                                            class MetaOapg:
                                        
                                        
                                            def __new__(
                                                cls,
                                                *args: typing.Union[None, decimal.Decimal, int, ],
                                                _configuration: typing.Optional[schemas.Configuration] = None,
                                            ) -> 'ping_days_before':
                                                return super().__new__(
                                                    cls,
                                                    *args,
                                                    _configuration=_configuration,
                                                )
                                        __annotations__ = {
                                            "discord_id": discord_id,
                                            "is_role": is_role,
                                            "ping_days_before": ping_days_before,
                                        }
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["discord_id"]) -> MetaOapg.properties.discord_id: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["is_role"]) -> MetaOapg.properties.is_role: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["ping_days_before"]) -> MetaOapg.properties.ping_days_before: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["discord_id", "is_role", "ping_days_before", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["discord_id"]) -> typing.Union[MetaOapg.properties.discord_id, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["is_role"]) -> typing.Union[MetaOapg.properties.is_role, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["ping_days_before"]) -> typing.Union[MetaOapg.properties.ping_days_before, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["discord_id", "is_role", "ping_days_before", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, ],
                                    discord_id: typing.Union[MetaOapg.properties.discord_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                    is_role: typing.Union[MetaOapg.properties.is_role, bool, schemas.Unset] = schemas.unset,
                                    ping_days_before: typing.Union[MetaOapg.properties.ping_days_before, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'items':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        discord_id=discord_id,
                                        is_role=is_role,
                                        ping_days_before=ping_days_before,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'additional_properties':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, list, tuple, ],
                ) -> 'mentions':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class intervals(
                schemas.EnumBase,
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "daily": "DAILY",
                        "weekly": "WEEKLY",
                        "monthly": "MONTHLY",
                    }
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def DAILY(cls):
                            return cls("daily")
                        
                        @schemas.classproperty
                        def WEEKLY(cls):
                            return cls("weekly")
                        
                        @schemas.classproperty
                        def MONTHLY(cls):
                            return cls("monthly")
                
                @schemas.classproperty
                def DAILY(cls):
                    return cls("daily")
                
                @schemas.classproperty
                def WEEKLY(cls):
                    return cls("weekly")
                
                @schemas.classproperty
                def MONTHLY(cls):
                    return cls("monthly")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'intervals':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class weekly_weekday(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "sunday": "SUNDAY",
                        "monday": "MONDAY",
                        "tuesday": "TUESDAY",
                        "wednesday": "WEDNESDAY",
                        "thursday": "THURSDAY",
                        "friday": "FRIDAY",
                        "saturday": "SATURDAY",
                    }
                
                @schemas.classproperty
                def SUNDAY(cls):
                    return cls("sunday")
                
                @schemas.classproperty
                def MONDAY(cls):
                    return cls("monday")
                
                @schemas.classproperty
                def TUESDAY(cls):
                    return cls("tuesday")
                
                @schemas.classproperty
                def WEDNESDAY(cls):
                    return cls("wednesday")
                
                @schemas.classproperty
                def THURSDAY(cls):
                    return cls("thursday")
                
                @schemas.classproperty
                def FRIDAY(cls):
                    return cls("friday")
                
                @schemas.classproperty
                def SATURDAY(cls):
                    return cls("saturday")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'weekly_weekday':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "bonus_whitelist": bonus_whitelist,
                "bonus_blacklist": bonus_blacklist,
                "subscriptions": subscriptions,
                "daily_settings": daily_settings,
                "iso_date": iso_date,
                "mentions": mentions,
                "intervals": intervals,
                "weekly_weekday": weekly_weekday,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bonus_whitelist"]) -> MetaOapg.properties.bonus_whitelist: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bonus_blacklist"]) -> MetaOapg.properties.bonus_blacklist: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriptions"]) -> MetaOapg.properties.subscriptions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["daily_settings"]) -> MetaOapg.properties.daily_settings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iso_date"]) -> MetaOapg.properties.iso_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mentions"]) -> MetaOapg.properties.mentions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["intervals"]) -> MetaOapg.properties.intervals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weekly_weekday"]) -> MetaOapg.properties.weekly_weekday: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bonus_whitelist", "bonus_blacklist", "subscriptions", "daily_settings", "iso_date", "mentions", "intervals", "weekly_weekday", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bonus_whitelist"]) -> typing.Union[MetaOapg.properties.bonus_whitelist, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bonus_blacklist"]) -> typing.Union[MetaOapg.properties.bonus_blacklist, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriptions"]) -> typing.Union[MetaOapg.properties.subscriptions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["daily_settings"]) -> typing.Union[MetaOapg.properties.daily_settings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iso_date"]) -> typing.Union[MetaOapg.properties.iso_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mentions"]) -> typing.Union[MetaOapg.properties.mentions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["intervals"]) -> typing.Union[MetaOapg.properties.intervals, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weekly_weekday"]) -> typing.Union[MetaOapg.properties.weekly_weekday, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bonus_whitelist", "bonus_blacklist", "subscriptions", "daily_settings", "iso_date", "mentions", "intervals", "weekly_weekday", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bonus_whitelist: typing.Union[MetaOapg.properties.bonus_whitelist, list, tuple, None, schemas.Unset] = schemas.unset,
        bonus_blacklist: typing.Union[MetaOapg.properties.bonus_blacklist, list, tuple, None, schemas.Unset] = schemas.unset,
        subscriptions: typing.Union[MetaOapg.properties.subscriptions, list, tuple, None, schemas.Unset] = schemas.unset,
        daily_settings: typing.Union[MetaOapg.properties.daily_settings, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
        iso_date: typing.Union[MetaOapg.properties.iso_date, None, bool, schemas.Unset] = schemas.unset,
        mentions: typing.Union[MetaOapg.properties.mentions, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        intervals: typing.Union[MetaOapg.properties.intervals, list, tuple, None, schemas.Unset] = schemas.unset,
        weekly_weekday: typing.Union[MetaOapg.properties.weekly_weekday, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PutAlmanaxWebhook':
        return super().__new__(
            cls,
            *args,
            bonus_whitelist=bonus_whitelist,
            bonus_blacklist=bonus_blacklist,
            subscriptions=subscriptions,
            daily_settings=daily_settings,
            iso_date=iso_date,
            mentions=mentions,
            intervals=intervals,
            weekly_weekday=weekly_weekday,
            _configuration=_configuration,
            **kwargs,
        )
