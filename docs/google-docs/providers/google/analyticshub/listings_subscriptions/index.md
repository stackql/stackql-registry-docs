---
title: listings_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - listings_subscriptions
  - analyticshub
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listings_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="analyticshub.listings_subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the subscription. e.g. `projects/myproject/locations/US/subscriptions/123`. |
| <CopyableCode code="creationTime" /> | `string` | Output only. Timestamp when the subscription was created. |
| <CopyableCode code="dataExchange" /> | `string` | Output only. Resource name of the source Data Exchange. e.g. projects/123/locations/US/dataExchanges/456 |
| <CopyableCode code="lastModifyTime" /> | `string` | Output only. Timestamp when the subscription was last modified. |
| <CopyableCode code="linkedDatasetMap" /> | `object` | Output only. Map of listing resource names to associated linked resource, e.g. projects/123/locations/US/dataExchanges/456/listings/789 -&gt; projects/123/datasets/my_dataset For listing-level subscriptions, this is a map of size 1. Only contains values if state == STATE_ACTIVE. |
| <CopyableCode code="listing" /> | `string` | Output only. Resource name of the source Listing. e.g. projects/123/locations/US/dataExchanges/456/listings/789 |
| <CopyableCode code="organizationDisplayName" /> | `string` | Output only. Display name of the project of this subscription. |
| <CopyableCode code="organizationId" /> | `string` | Output only. Organization of the project this subscription belongs to. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the subscription. |
| <CopyableCode code="subscriberContact" /> | `string` | Output only. Email of the subscriber. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_locations_data_exchanges_listings_list_subscriptions" /> | `SELECT` | <CopyableCode code="dataExchangesId, listingsId, locationsId, projectsId" /> |
| <CopyableCode code="_projects_locations_data_exchanges_listings_list_subscriptions" /> | `EXEC` | <CopyableCode code="dataExchangesId, listingsId, locationsId, projectsId" /> |
