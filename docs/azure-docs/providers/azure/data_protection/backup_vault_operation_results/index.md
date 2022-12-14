---
title: backup_vault_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_vault_operation_results
  - data_protection
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
<tr><td><b>Name</b></td><td><code>backup_vault_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_protection.backup_vault_operation_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id represents the complete path to the resource. |
| `name` | `string` | Resource name associated with the resource. |
| `type` | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
| `identity` | `object` | Identity details |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `eTag` | `string` | Optional ETag. |
| `properties` | `object` | Backup Vault |
| `location` | `string` | Resource location. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `BackupVaultOperationResults_Get` | `SELECT` | `api-version, operationId, resourceGroupName, subscriptionId, vaultName` |
