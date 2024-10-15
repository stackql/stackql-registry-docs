---
title: offers
hide_title: false
hide_table_of_contents: false
keywords:
  - offers
  - edge_marketplace
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>offers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>offers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.edge_marketplace.offers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_offers', value: 'view', },
        { label: 'offers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="content_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="marketplace_skus" /> | `text` | field from the `properties` object |
| <CopyableCode code="offerId" /> | `text` | field from the `properties` object |
| <CopyableCode code="offer_content" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The offer properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="offerId, resourceUri" /> | Get a Offer |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | List Offer resources by parent |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Offer resources by subscription |
| <CopyableCode code="generate_access_token" /> | `EXEC` | <CopyableCode code="offerId, resourceUri, data__edgeMarketPlaceRegion" /> | A long-running resource action. |

## `SELECT` examples

List Offer resources by parent

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_offers', value: 'view', },
        { label: 'offers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
content_url,
content_version,
marketplace_skus,
offerId,
offer_content,
provisioning_state,
resourceUri,
subscriptionId
FROM azure_extras.edge_marketplace.vw_offers
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.edge_marketplace.offers
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem></Tabs>

