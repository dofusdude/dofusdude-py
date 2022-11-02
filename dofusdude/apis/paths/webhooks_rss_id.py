from dofusdude.paths.webhooks_rss_id.get import ApiForget
from dofusdude.paths.webhooks_rss_id.put import ApiForput
from dofusdude.paths.webhooks_rss_id.delete import ApiFordelete


class WebhooksRssId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
