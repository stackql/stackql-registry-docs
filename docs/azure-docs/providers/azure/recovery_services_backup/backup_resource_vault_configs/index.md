---
title: backup_resource_vault_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_resource_vault_configs
  - recovery_services_backup
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

Creates, updates, deletes, gets or lists a <code>backup_resource_vault_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_resource_vault_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.backup_resource_vault_configs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_resource_vault_configs', value: 'view', },
        { label: 'backup_resource_vault_configs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="enhanced_security_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_soft_delete_feature_state_editable" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guard_operation_requests" /> | `text` | field from the `properties` object |
| <CopyableCode code="soft_delete_feature_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="soft_delete_retention_period_in_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_model_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_type_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Backup resource vault config details. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Fetches resource vault config. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Updates vault security config. |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Updates vault security config.  |

## `SELECT` examples

Fetches resource vault config.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_resource_vault_configs', value: 'view', },
        { label: 'backup_resource_vault_configs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
enhanced_security_state,
is_soft_delete_feature_state_editable,
resourceGroupName,
resource_guard_operation_requests,
soft_delete_feature_state,
soft_delete_retention_period_in_days,
storage_model_type,
storage_type,
storage_type_state,
subscriptionId,
type,
vaultName
FROM azure.recovery_services_backup.vw_backup_resource_vault_configs
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
type
FROM azure.recovery_services_backup.backup_resource_vault_configs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>backup_resource_vault_configs</code> resource.

```sql
/*+ update */
UPDATE azure.recovery_services_backup.backup_resource_vault_configs
SET 
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>backup_resource_vault_configs</code> resource.

```sql
/*+ update */
REPLACE azure.recovery_services_backup.backup_resource_vault_configs
SET 
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
