---
title: deleted_backup_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_backup_instances
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

Creates, updates, deletes, gets or lists a <code>deleted_backup_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deleted_backup_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.deleted_backup_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deleted_backup_instances', value: 'view', },
        { label: 'deleted_backup_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `text` | Resource name associated with the resource. |
| <CopyableCode code="backupInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_protection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_source_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_source_set_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="datasource_auth_credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="deletion_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="object_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="protection_error_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="protection_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guard_operation_requests" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
| <CopyableCode code="validation_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `string` | Resource name associated with the resource. |
| <CopyableCode code="properties" /> | `object` | Deleted Backup Instance |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> | Gets a deleted backup instance with name in a backup vault |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Gets deleted backup instances belonging to a backup vault |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> |  |

## `SELECT` examples

Gets deleted backup instances belonging to a backup vault

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deleted_backup_instances', value: 'view', },
        { label: 'deleted_backup_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backupInstanceName,
current_protection_state,
data_source_info,
data_source_set_info,
datasource_auth_credentials,
deletion_info,
friendly_name,
identity_details,
object_type,
policy_info,
protection_error_details,
protection_status,
provisioning_state,
resourceGroupName,
resource_guard_operation_requests,
subscriptionId,
system_data,
type,
validation_type,
vaultName
FROM azure.data_protection.vw_deleted_backup_instances
WHERE resourceGroupName = '{{ resourceGroupName }}'
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
FROM azure.data_protection.deleted_backup_instances
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>

