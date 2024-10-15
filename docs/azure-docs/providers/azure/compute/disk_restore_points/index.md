---
title: disk_restore_points
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_restore_points
  - compute
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

Creates, updates, deletes, gets or lists a <code>disk_restore_points</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disk_restore_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.disk_restore_points" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_disk_restore_points', value: 'view', },
        { label: 'disk_restore_points', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="completion_percent" /> | `text` | field from the `properties` object |
| <CopyableCode code="diskRestorePointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_access_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="family_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="hyper_v_generation" /> | `text` | field from the `properties` object |
| <CopyableCode code="logical_sector_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_access_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="purchase_plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restorePointCollectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_resource_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_unique_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_capabilities" /> | `text` | field from the `properties` object |
| <CopyableCode code="supports_hibernation" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="vmRestorePointName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Properties of an incremental disk restore point |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diskRestorePointName, resourceGroupName, restorePointCollectionName, subscriptionId, vmRestorePointName" /> | Get disk restorePoint resource |
| <CopyableCode code="list_by_restore_point" /> | `SELECT` | <CopyableCode code="resourceGroupName, restorePointCollectionName, subscriptionId, vmRestorePointName" /> | Lists diskRestorePoints under a vmRestorePoint. |
| <CopyableCode code="grant_access" /> | `EXEC` | <CopyableCode code="diskRestorePointName, resourceGroupName, restorePointCollectionName, subscriptionId, vmRestorePointName, data__access, data__durationInSeconds" /> | Grants access to a diskRestorePoint. |
| <CopyableCode code="revoke_access" /> | `EXEC` | <CopyableCode code="diskRestorePointName, resourceGroupName, restorePointCollectionName, subscriptionId, vmRestorePointName" /> | Revokes access to a diskRestorePoint. |

## `SELECT` examples

Lists diskRestorePoints under a vmRestorePoint.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_disk_restore_points', value: 'view', },
        { label: 'disk_restore_points', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
completion_percent,
diskRestorePointName,
disk_access_id,
encryption,
family_id,
hyper_v_generation,
logical_sector_size,
network_access_policy,
os_type,
public_network_access,
purchase_plan,
replication_state,
resourceGroupName,
restorePointCollectionName,
security_profile,
source_resource_id,
source_resource_location,
source_unique_id,
subscriptionId,
supported_capabilities,
supports_hibernation,
time_created,
type,
vmRestorePointName
FROM azure.compute.vw_disk_restore_points
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND restorePointCollectionName = '{{ restorePointCollectionName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmRestorePointName = '{{ vmRestorePointName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.compute.disk_restore_points
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND restorePointCollectionName = '{{ restorePointCollectionName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmRestorePointName = '{{ vmRestorePointName }}';
```
</TabItem></Tabs>

