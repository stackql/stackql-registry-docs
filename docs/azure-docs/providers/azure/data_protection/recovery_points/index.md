---
title: recovery_points
hide_title: false
hide_table_of_contents: false
keywords:
  - recovery_points
  - data_protection
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.recovery_points" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `text` | Resource name associated with the resource. |
| <CopyableCode code="backupInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="object_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="recoveryPointId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `string` | Resource name associated with the resource. |
| <CopyableCode code="properties" /> | `object` | Azure backup recoveryPoint |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupInstanceName, recoveryPointId, resourceGroupName, subscriptionId, vaultName" /> | Gets a Recovery Point using recoveryPointId for a Datasource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> | Returns a list of Recovery Points for a DataSource in a vault. |

## `SELECT` examples

Returns a list of Recovery Points for a DataSource in a vault.

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
backupInstanceName,
object_type,
recoveryPointId,
resourceGroupName,
subscriptionId,
system_data,
type,
vaultName
FROM azure.data_protection.vw_recovery_points
WHERE backupInstanceName = '{{ backupInstanceName }}'
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
FROM azure.data_protection.recovery_points
WHERE backupInstanceName = '{{ backupInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>

