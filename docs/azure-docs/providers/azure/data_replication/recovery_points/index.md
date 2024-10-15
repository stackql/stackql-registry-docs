---
title: recovery_points
hide_title: false
hide_table_of_contents: false
keywords:
  - recovery_points
  - data_replication
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_replication.recovery_points" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | Gets or sets the Id of the resource. |
| <CopyableCode code="name" /> | `text` | Gets or sets the name of the resource. |
| <CopyableCode code="custom_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="protectedItemName" /> | `text` | field from the `properties` object |
| <CopyableCode code="recoveryPointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_point_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_point_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets or sets the type of the resource. |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the Id of the resource. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name of the resource. |
| <CopyableCode code="properties" /> | `object` | Recovery point model properties. |
| <CopyableCode code="systemData" /> | `object` | System data required to be defined for Azure resources. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="protectedItemName, recoveryPointName, resourceGroupName, subscriptionId, vaultName" /> | Gets the details of the recovery point of a protected item. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="protectedItemName, resourceGroupName, subscriptionId, vaultName" /> | Gets the list of recovery points of the given protected item. |

## `SELECT` examples

Gets the list of recovery points of the given protected item.

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
custom_properties,
protectedItemName,
recoveryPointName,
recovery_point_time,
recovery_point_type,
resourceGroupName,
subscriptionId,
system_data,
type,
vaultName
FROM azure.data_replication.vw_recovery_points
WHERE protectedItemName = '{{ protectedItemName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.data_replication.recovery_points
WHERE protectedItemName = '{{ protectedItemName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>

