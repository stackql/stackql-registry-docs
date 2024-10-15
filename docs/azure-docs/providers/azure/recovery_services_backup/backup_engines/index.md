---
title: backup_engines
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_engines
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

Creates, updates, deletes, gets or lists a <code>backup_engines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_engines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.backup_engines" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_engines', value: 'view', },
        { label: 'backup_engines', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="azure_backup_agent_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="backupEngineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_engine_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_engine_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_engine_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_management_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="can_re_register" /> | `text` | field from the `properties` object |
| <CopyableCode code="dpm_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_azure_backup_agent_upgrade_available" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_dpm_upgrade_available" /> | `text` | field from the `properties` object |
| <CopyableCode code="registration_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | The base backup engine class. All workload specific backup engines derive from this class. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupEngineName, resourceGroupName, subscriptionId, vaultName" /> | Returns backup management server registered to Recovery Services Vault. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Backup management servers registered to Recovery Services Vault. Returns a pageable list of servers. |

## `SELECT` examples

Backup management servers registered to Recovery Services Vault. Returns a pageable list of servers.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_engines', value: 'view', },
        { label: 'backup_engines', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
azure_backup_agent_version,
backupEngineName,
backup_engine_id,
backup_engine_state,
backup_engine_type,
backup_management_type,
can_re_register,
dpm_version,
extended_info,
friendly_name,
health_status,
is_azure_backup_agent_upgrade_available,
is_dpm_upgrade_available,
registration_status,
resourceGroupName,
subscriptionId,
type,
vaultName
FROM azure.recovery_services_backup.vw_backup_engines
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
FROM azure.recovery_services_backup.backup_engines
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>

