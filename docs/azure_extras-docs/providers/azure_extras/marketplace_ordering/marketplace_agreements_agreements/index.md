---
title: marketplace_agreements_agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplace_agreements_agreements
  - marketplace_ordering
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

Creates, updates, deletes, gets or lists a <code>marketplace_agreements_agreements</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>marketplace_agreements_agreements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.marketplace_ordering.marketplace_agreements_agreements" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_marketplace_agreements_agreements', value: 'view', },
        { label: 'marketplace_agreements_agreements', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="cancel_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="offer" /> | `text` | field from the `properties` object |
| <CopyableCode code="offerId" /> | `text` | field from the `properties` object |
| <CopyableCode code="planId" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisherId" /> | `text` | field from the `properties` object |
| <CopyableCode code="sign_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | Old Agreement Terms definition |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="offerId, planId, publisherId, subscriptionId" /> | Get marketplace agreement. |

## `SELECT` examples

Get marketplace agreement.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_marketplace_agreements_agreements', value: 'view', },
        { label: 'marketplace_agreements_agreements', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
cancel_date,
offer,
offerId,
planId,
publisher,
publisherId,
sign_date,
state,
subscriptionId,
type
FROM azure_extras.marketplace_ordering.vw_marketplace_agreements_agreements
WHERE offerId = '{{ offerId }}'
AND planId = '{{ planId }}'
AND publisherId = '{{ publisherId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure_extras.marketplace_ordering.marketplace_agreements_agreements
WHERE offerId = '{{ offerId }}'
AND planId = '{{ planId }}'
AND publisherId = '{{ publisherId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

