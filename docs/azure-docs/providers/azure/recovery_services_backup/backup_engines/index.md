---
title: backup_engines
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_engines
  - recovery_services_backup
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_engines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.backup_engines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id represents the complete path to the resource. |
| `name` | `string` | Resource name associated with the resource. |
| `type` | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
| `eTag` | `string` | Optional ETag. |
| `location` | `string` | Resource location. |
| `properties` | `object` | The base backup engine class. All workload specific backup engines derive from this class. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BackupEngines_Get` | `SELECT` | `api-version, backupEngineName, resourceGroupName, subscriptionId, vaultName` | Returns backup management server registered to Recovery Services Vault. |
| `BackupEngines_List` | `SELECT` | `api-version, resourceGroupName, subscriptionId, vaultName` | Backup management servers registered to Recovery Services Vault. Returns a pageable list of servers. |
