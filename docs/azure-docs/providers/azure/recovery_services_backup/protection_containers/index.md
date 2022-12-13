---
title: protection_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - protection_containers
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
<tr><td><b>Name</b></td><td><code>protection_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.protection_containers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id represents the complete path to the resource. |
| `name` | `string` | Resource name associated with the resource. |
| `properties` | `object` | Base class for container with backup items. Containers with specific workloads are derived from this class. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
| `eTag` | `string` | Optional ETag. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProtectionContainers_Get` | `SELECT` | `api-version, containerName, fabricName, resourceGroupName, subscriptionId, vaultName` | Gets details of the specific container registered to your Recovery Services Vault. |
| `ProtectionContainers_Inquire` | `EXEC` | `api-version, containerName, fabricName, resourceGroupName, subscriptionId, vaultName` | This is an async operation and the results should be tracked using location header or Azure-async-url. |
| `ProtectionContainers_Refresh` | `EXEC` | `api-version, fabricName, resourceGroupName, subscriptionId, vaultName` | Discovers all the containers in the subscription that can be backed up to Recovery Services Vault. This is an<br />asynchronous operation. To know the status of the operation, call GetRefreshOperationResult API. |
| `ProtectionContainers_Register` | `EXEC` | `api-version, containerName, fabricName, resourceGroupName, subscriptionId, vaultName` | Registers the container with Recovery Services vault.<br />This is an asynchronous operation. To track the operation status, use location header to call get latest status of<br />the operation. |
| `ProtectionContainers_Unregister` | `EXEC` | `api-version, containerName, fabricName, resourceGroupName, subscriptionId, vaultName` | Unregisters the given container from your Recovery Services Vault. This is an asynchronous operation. To determine<br />whether the backend service has finished processing the request, call Get Container Operation Result API. |
