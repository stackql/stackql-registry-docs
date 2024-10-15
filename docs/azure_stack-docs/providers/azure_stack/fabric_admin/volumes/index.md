---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
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

Creates, updates, deletes, gets or lists a <code>volumes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.fabric_admin.volumes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volumes', value: 'view', },
        { label: 'volumes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="action" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The region where the resource is located. |
| <CopyableCode code="operational_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="remaining_capacity_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="repair_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scaleUnit" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageSubSystem" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key-value pairs. |
| <CopyableCode code="total_capacity_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of resource. |
| <CopyableCode code="volume" /> | `text` | field from the `properties` object |
| <CopyableCode code="volume_label" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | The region where the resource is located. |
| <CopyableCode code="properties" /> | `object` | Properties of a volume. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, scaleUnit, storageSubSystem, subscriptionId, volume" /> | Return the requested a storage volume. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, scaleUnit, storageSubSystem, subscriptionId" /> | Returns a list of all storage volumes at a location. |

## `SELECT` examples

Returns a list of all storage volumes at a location.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volumes', value: 'view', },
        { label: 'volumes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
action,
health_status,
location,
operational_status,
remaining_capacity_gb,
repair_status,
resourceGroupName,
scaleUnit,
storageSubSystem,
subscriptionId,
tags,
total_capacity_gb,
type,
volume,
volume_label
FROM azure_stack.fabric_admin.vw_volumes
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND scaleUnit = '{{ scaleUnit }}'
AND storageSubSystem = '{{ storageSubSystem }}'
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
FROM azure_stack.fabric_admin.volumes
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND scaleUnit = '{{ scaleUnit }}'
AND storageSubSystem = '{{ storageSubSystem }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

