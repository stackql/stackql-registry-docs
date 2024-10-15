---
title: recovery_points
hide_title: false
hide_table_of_contents: false
keywords:
  - recovery_points
  - recovery_services_site_recovery
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

Creates, updates, deletes, gets or lists a <code>recovery_points</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recovery_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.recovery_points" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_recovery_points', value: 'view', },
        { label: 'recovery_points', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="protectionContainerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_specific_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="recoveryPointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_point_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_point_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="replicatedProtectedItemName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Recovery point properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, protectionContainerName, recoveryPointName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Get the details of specified recovery point. |
| <CopyableCode code="list_by_replication_protected_items" /> | `SELECT` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Lists the available recovery points for a replication protected item. |

## `SELECT` examples

Lists the available recovery points for a replication protected item.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_recovery_points', value: 'view', },
        { label: 'recovery_points', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
fabricName,
location,
protectionContainerName,
provider_specific_details,
recoveryPointName,
recovery_point_time,
recovery_point_type,
replicatedProtectedItemName,
resourceGroupName,
resourceName,
subscriptionId,
type
FROM azure.recovery_services_site_recovery.vw_recovery_points
WHERE fabricName = '{{ fabricName }}'
AND protectionContainerName = '{{ protectionContainerName }}'
AND replicatedProtectedItemName = '{{ replicatedProtectedItemName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
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
FROM azure.recovery_services_site_recovery.recovery_points
WHERE fabricName = '{{ fabricName }}'
AND protectionContainerName = '{{ protectionContainerName }}'
AND replicatedProtectedItemName = '{{ replicatedProtectedItemName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

