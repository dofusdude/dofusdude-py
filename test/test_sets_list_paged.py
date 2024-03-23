# coding: utf-8

"""
    dofusdude

    # A project for you - the developer. The all-in-one toolbelt for your next Ankama related project.  ## Client SDKs - [Javascript](https://github.com/dofusdude/dofusdude-js) npm i dofusdude-js --save - [Typescript](https://github.com/dofusdude/dofusdude-ts) npm i dofusdude-ts --save - [Go](https://github.com/dofusdude/dodugo) go get -u github.com/dofusdude/dodugo - [Python](https://github.com/dofusdude/dofusdude-py) pip install dofusdude - [PHP](https://github.com/dofusdude/dofusdude-php)  Everything, including this site, is generated out of the [Docs Repo](https://github.com/dofusdude/api-docs). Consider it the Single Source of Truth. If there is a problem with the SDKs, create an issue there.  Your favorite language is missing? Please let me know!  # Main Features - 🥷 **Seamless Auto-Update** load data in the background when a new Dofus version is released and serving it within 2 minutes with atomic data source switching. No downtime and no effects for the user, just always up-to-date.  - ⚡ **Blazingly Fast** all data in-memory, aggressive caching over short time spans, HTTP/2 multiplexing, written in Go, optimized for low latency, hosted on bare metal in 🇩🇪.  - 📨 **Discord Integration** Ankama related RSS and Almanax feeds to post to Discord servers with advanced features like filters or mentions. Use the endpoints as a dev or the official [Web Client](https://discord.dofusdude.com) as a user.  - 🩸 **Dofus 2 Beta** from stable to bleeding edge by replacing /dofus2 with /dofus2beta.  - 🗣️ **Multilingual** supporting _en_, _fr_, _es_, _pt_ including the dropped languages from the Dofus website _de_ and _it_.  - 🧠 **Search by Relevance** allowing typos in name and description, handled by language specific text analysis and indexing.  - 🕵️ **Complete** actual data from the game including items invisible to the encyclopedia like quest items.  - 🖼️ **HD Images** rendering game assets to high-res images with up to 800x800 px.  ... and much more on the Roadmap on my Discord.   ## Deploy now. Use forever. Everything you see here on this site, you can use now and forever. Updates could introduce new fields, new paths or parameter but never break backwards compatibility.  There is one exception! **The API will _always_ choose being up-to-date over everything else**. So if Ankama decides to drop languages from the game like they did with their website, the API will loose support for them, too.  ## Thank you! I highly welcome everyone on my [Discord](https://discord.gg/3EtHskZD8h) to just talk about projects and use cases or give feedback of any kind.  The servers have a fixed monthly cost to provide very fast responses. If you want to help me keeping them running or simply donate to that cause, consider becoming a [GitHub Sponsor](https://github.com/sponsors/dofusdude).

    The version of the OpenAPI document: 0.8.3
    Contact: stelzo@steado.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dofusdude.models.sets_list_paged import SetsListPaged

class TestSetsListPaged(unittest.TestCase):
    """SetsListPaged unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SetsListPaged:
        """Test SetsListPaged
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SetsListPaged`
        """
        model = SetsListPaged()
        if include_optional:
            return SetsListPaged(
                links = dofusdude.models.links_paged.Links-Paged(
                    first = '', 
                    prev = '', 
                    next = '', 
                    last = '', ),
                items = [
                    dofusdude.models.set_list_entry.Set-List-Entry(
                        ankama_id = 56, 
                        name = '', 
                        items = 56, 
                        level = 56, 
                        effects = [
                            [
                                dofusdude.models.set_effects_entry.Set-Effects-Entry(
                                    int_minimum = 56, 
                                    int_maximum = 56, 
                                    type = dofusdude.models.set_effects_entry_type.Set_Effects_Entry_type(
                                        name = '', 
                                        id = 56, 
                                        is_meta = True, 
                                        is_active = True, ), 
                                    ignore_int_min = True, 
                                    ignore_int_max = True, 
                                    formatted = '', 
                                    item_combination = 56, )
                                ]
                            ], 
                        equipment_ids = [
                            56
                            ], )
                    ]
            )
        else:
            return SetsListPaged(
        )
        """

    def testSetsListPaged(self):
        """Test SetsListPaged"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
