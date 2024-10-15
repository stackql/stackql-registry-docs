---
title: drives
hide_title: false
hide_table_of_contents: false
keywords:
  - drives
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

Creates, updates, deletes, gets or lists a <code>drives</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>drives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.fabric_admin.drives" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_drives', value: 'view', },
        { label: 'drives', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="action" /> | `text` | field from the `properties` object |
| <CopyableCode code="capacity_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="drive" /> | `text` | field from the `properties` object |
| <CopyableCode code="firmware_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_indication_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The region where the resource is located. |
| <CopyableCode code="manufacturer" /> | `text` | field from the `properties` object |
| <CopyableCode code="media_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="model" /> | `text` | field from the `properties` object |
| <CopyableCode code="operational_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="physical_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scaleUnit" /> | `text` | field from the `properties` object |
| <CopyableCode code="serial_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageSubSystem" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_node" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_pool" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key-value pairs. |
| <CopyableCode code="type" /> | `text` | Type of resource. |
| <CopyableCode code="usage" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | The region where the resource is located. |
| <CopyableCode code="properties" /> | `object` | Properties of a drive. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="drive, location, resourceGroupName, scaleUnit, storageSubSystem, subscriptionId" /> | Return the requested a storage drive. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, scaleUnit, storageSubSystem, subscriptionId" /> | Returns a list of all storage drives at a location. |

## `SELECT` examples

Returns a list of all storage drives at a location.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_drives', value: 'view', },
        { label: 'drives', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
action,
capacity_gb,
drive,
firmware_version,
health_status,
is_indication_enabled,
location,
manufacturer,
media_type,
model,
operational_status,
physical_location,
resourceGroupName,
scaleUnit,
serial_number,
storageSubSystem,
storage_node,
storage_pool,
subscriptionId,
tags,
type,
usage
FROM azure_stack.fabric_admin.vw_drives
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
FROM azure_stack.fabric_admin.drives
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND scaleUnit = '{{ scaleUnit }}'
AND storageSubSystem = '{{ storageSubSystem }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

