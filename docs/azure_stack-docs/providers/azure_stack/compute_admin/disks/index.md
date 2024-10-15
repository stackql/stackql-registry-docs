---
title: disks
hide_title: false
hide_table_of_contents: false
keywords:
  - disks
  - compute_admin
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

Creates, updates, deletes, gets or lists a <code>disks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.compute_admin.disks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_disks', value: 'view', },
        { label: 'disks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="actual_size_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_option" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_source_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="diskId" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="exclusive_allocated_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource. |
| <CopyableCode code="managed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="provision_size_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="share_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of Resource. |
| <CopyableCode code="user_resource_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Managed disk properties. |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diskId, location, subscriptionId" /> | Returns the disk. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Returns a list of disks. |

## `SELECT` examples

Returns a list of disks.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_disks', value: 'view', },
        { label: 'disks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
actual_size_gb,
creation_option,
creation_source_uri,
diskId,
disk_id,
disk_sku,
disk_type,
exclusive_allocated_size,
location,
managed_by,
provision_size_gb,
share_path,
status,
subscriptionId,
type,
user_resource_id
FROM azure_stack.compute_admin.vw_disks
WHERE location = '{{ location }}'
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
type
FROM azure_stack.compute_admin.disks
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

