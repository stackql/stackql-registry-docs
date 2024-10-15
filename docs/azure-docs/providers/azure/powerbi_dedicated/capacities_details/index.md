---
title: capacities_details
hide_title: false
hide_table_of_contents: false
keywords:
  - capacities_details
  - powerbi_dedicated
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

Creates, updates, deletes, gets or lists a <code>capacities_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacities_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbi_dedicated.capacities_details" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_capacities_details', value: 'view', },
        { label: 'capacities_details', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | An identifier that represents the PowerBI Dedicated resource. |
| <CopyableCode code="name" /> | `text` | The name of the PowerBI Dedicated resource. |
| <CopyableCode code="administration" /> | `text` | field from the `properties` object |
| <CopyableCode code="dedicatedCapacityName" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the PowerBI Dedicated resource. |
| <CopyableCode code="mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Represents the SKU name and Azure pricing tier for PowerBI Dedicated capacity resource. |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Key-value pairs of additional resource provisioning properties. |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the PowerBI Dedicated resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | An identifier that represents the PowerBI Dedicated resource. |
| <CopyableCode code="name" /> | `string` | The name of the PowerBI Dedicated resource. |
| <CopyableCode code="location" /> | `string` | Location of the PowerBI Dedicated resource. |
| <CopyableCode code="properties" /> | `object` | Properties of Dedicated Capacity resource. |
| <CopyableCode code="sku" /> | `object` | Represents the SKU name and Azure pricing tier for PowerBI Dedicated capacity resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Key-value pairs of additional resource provisioning properties. |
| <CopyableCode code="type" /> | `string` | The type of the PowerBI Dedicated resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dedicatedCapacityName, resourceGroupName, subscriptionId" /> | Gets details about the specified dedicated capacity. |

## `SELECT` examples

Gets details about the specified dedicated capacity.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_capacities_details', value: 'view', },
        { label: 'capacities_details', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
administration,
dedicatedCapacityName,
friendly_name,
location,
mode,
provisioning_state,
resourceGroupName,
sku,
state,
subscriptionId,
system_data,
tags,
tenant_id,
type
FROM azure.powerbi_dedicated.vw_capacities_details
WHERE dedicatedCapacityName = '{{ dedicatedCapacityName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
sku,
systemData,
tags,
type
FROM azure.powerbi_dedicated.capacities_details
WHERE dedicatedCapacityName = '{{ dedicatedCapacityName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

