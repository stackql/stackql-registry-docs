---
title: backup_resource_encryption_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_resource_encryption_configs
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

Creates, updates, deletes, gets or lists a <code>backup_resource_encryption_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_resource_encryption_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.backup_resource_encryption_configs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_resource_encryption_configs', value: 'view', },
        { label: 'backup_resource_encryption_configs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="encryption_at_rest_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="infrastructure_encryption_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_update_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="use_system_assigned_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_assigned_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Fetches Vault Encryption config. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Updates Vault encryption config. |

## `SELECT` examples

Fetches Vault Encryption config.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_resource_encryption_configs', value: 'view', },
        { label: 'backup_resource_encryption_configs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
encryption_at_rest_type,
infrastructure_encryption_state,
key_uri,
last_update_status,
resourceGroupName,
subscriptionId,
subscription_id,
type,
use_system_assigned_identity,
user_assigned_identity,
vaultName
FROM azure.recovery_services_backup.vw_backup_resource_encryption_configs
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
FROM azure.recovery_services_backup.backup_resource_encryption_configs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>backup_resource_encryption_configs</code> resource.

```sql
/*+ update */
REPLACE azure.recovery_services_backup.backup_resource_encryption_configs
SET 
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
