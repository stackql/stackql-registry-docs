---
title: topologies
hide_title: false
hide_table_of_contents: false
keywords:
  - topologies
  - security
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

Creates, updates, deletes, gets or lists a <code>topologies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topologies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.topologies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_topologies', value: 'view', },
        { label: 'topologies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="ascLocation" /> | `text` | field from the `properties` object |
| <CopyableCode code="calculated_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location where the resource is stored |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="topologyResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="topology_resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Location where the resource is stored |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ascLocation, resourceGroupName, subscriptionId, topologyResourceName" /> | Gets a specific topology component. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list that allows to build a topology view of a subscription. |
| <CopyableCode code="list_by_home_region" /> | `SELECT` | <CopyableCode code="ascLocation, subscriptionId" /> | Gets a list that allows to build a topology view of a subscription and location. |

## `SELECT` examples

Gets a list that allows to build a topology view of a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_topologies', value: 'view', },
        { label: 'topologies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
ascLocation,
calculated_date_time,
location,
resourceGroupName,
subscriptionId,
topologyResourceName,
topology_resources,
type
FROM azure.security.vw_topologies
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure.security.topologies
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

