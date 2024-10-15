---
title: subscription_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_usages
  - sql
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

Creates, updates, deletes, gets or lists a <code>subscription_usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscription_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.subscription_usages" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_subscription_usages', value: 'view', },
        { label: 'subscription_usages', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="current_value" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="locationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="unit" /> | `text` | field from the `properties` object |
| <CopyableCode code="usageName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a subscription usage. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId, usageName" /> | Gets a subscription usage metric. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId" /> | Gets all subscription usage metrics in a given location. |

## `SELECT` examples

Gets all subscription usage metrics in a given location.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_subscription_usages', value: 'view', },
        { label: 'subscription_usages', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
current_value,
display_name,
limit,
locationName,
subscriptionId,
unit,
usageName
FROM azure.sql.vw_subscription_usages
WHERE locationName = '{{ locationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.subscription_usages
WHERE locationName = '{{ locationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

