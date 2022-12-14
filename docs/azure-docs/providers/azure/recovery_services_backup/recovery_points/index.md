---
title: recovery_points
hide_title: false
hide_table_of_contents: false
keywords:
  - recovery_points
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
<tr><td><b>Name</b></td><td><code>recovery_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.recovery_points</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id represents the complete path to the resource. |
| `name` | `string` | Resource name associated with the resource. |
| `properties` | `object` | Base class for backup copies. Workload-specific backup copies are derived from this class. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
| `eTag` | `string` | Optional ETag. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RecoveryPoints_Get` | `SELECT` | `api-version, containerName, fabricName, protectedItemName, recoveryPointId, resourceGroupName, subscriptionId, vaultName` | Provides the information of the backed up data identified using RecoveryPointID. This is an asynchronous operation.<br />To know the status of the operation, call the GetProtectedItemOperationResult API. |
| `RecoveryPoints_List` | `SELECT` | `api-version, containerName, fabricName, protectedItemName, resourceGroupName, subscriptionId, vaultName` | Lists the backup copies for the backed up item. |
