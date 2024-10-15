---
title: backup_instances_backup_instance_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_instances_backup_instance_operation_results
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

Creates, updates, deletes, gets or lists a <code>backup_instances_backup_instance_operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_instances_backup_instance_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.backup_instances_backup_instance_operation_results" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_instances_backup_instance_operation_results', value: 'view', },
        { label: 'backup_instances_backup_instance_operation_results', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Proxy Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `text` | Proxy Resource name associated with the resource. |
| <CopyableCode code="backupInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_protection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_source_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_source_set_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="datasource_auth_credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="object_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="operationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="protection_error_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="protection_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guard_operation_requests" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Proxy Resource tags. |
| <CopyableCode code="type" /> | `text` | Proxy Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
| <CopyableCode code="validation_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Proxy Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `string` | Proxy Resource name associated with the resource. |
| <CopyableCode code="properties" /> | `object` | Backup Instance |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Proxy Resource tags. |
| <CopyableCode code="type" /> | `string` | Proxy Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupInstanceName, operationId, resourceGroupName, subscriptionId, vaultName" /> | Get result of backup instance creation operation |

## `SELECT` examples

Get result of backup instance creation operation

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_instances_backup_instance_operation_results', value: 'view', },
        { label: 'backup_instances_backup_instance_operation_results', value: 'resource', },
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
friendly_name,
identity_details,
object_type,
operationId,
policy_info,
protection_error_details,
protection_status,
provisioning_state,
resourceGroupName,
resource_guard_operation_requests,
subscriptionId,
system_data,
tags,
type,
validation_type,
vaultName
FROM azure.data_protection.vw_backup_instances_backup_instance_operation_results
WHERE backupInstanceName = '{{ backupInstanceName }}'
AND operationId = '{{ operationId }}'
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
tags,
type
FROM azure.data_protection.backup_instances_backup_instance_operation_results
WHERE backupInstanceName = '{{ backupInstanceName }}'
AND operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>

