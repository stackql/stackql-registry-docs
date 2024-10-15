---
title: scale_units
hide_title: false
hide_table_of_contents: false
keywords:
  - scale_units
  - fabric_admin
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

Creates, updates, deletes, gets or lists a <code>scale_units</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scale_units</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.fabric_admin.scale_units" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scale_units', value: 'view', },
        { label: 'scale_units', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="is_multi_node" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The region where the resource is located. |
| <CopyableCode code="logical_fault_domain" /> | `text` | field from the `properties` object |
| <CopyableCode code="model" /> | `text` | field from the `properties` object |
| <CopyableCode code="nodes" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scaleUnit" /> | `text` | field from the `properties` object |
| <CopyableCode code="scale_unit_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key-value pairs. |
| <CopyableCode code="total_capacity" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | The region where the resource is located. |
| <CopyableCode code="properties" /> | `object` | Properties of a scale unit. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, scaleUnit, subscriptionId" /> | Returns the requested scale unit. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a list of all scale units at a location. |
| <CopyableCode code="scale_out" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, scaleUnit, subscriptionId" /> | Scales out a scale unit. |
| <CopyableCode code="set_gpu_partition_size" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, scaleUnit, subscriptionId" /> | Set GPU partition size. |

## `SELECT` examples

Returns a list of all scale units at a location.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scale_units', value: 'view', },
        { label: 'scale_units', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
is_multi_node,
location,
logical_fault_domain,
model,
nodes,
resourceGroupName,
scaleUnit,
scale_unit_type,
state,
subscriptionId,
tags,
total_capacity,
type
FROM azure_stack.fabric_admin.vw_scale_units
WHERE location = '{{ location }}'
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
tags,
type
FROM azure_stack.fabric_admin.scale_units
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

