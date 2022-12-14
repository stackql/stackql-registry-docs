---
title: account
hide_title: false
hide_table_of_contents: false
keywords:
  - account
  - batch
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
<tr><td><b>Name</b></td><td><code>account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.batch.account</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | Account specific properties. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
| `identity` | `object` | The identity of the Batch account, if configured. This is used when the user specifies 'Microsoft.KeyVault' as their Batch account encryption configuration or when `ManagedIdentity` is selected as the auto-storage authentication mode. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BatchAccount_Get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets information about the specified Batch account. |
| `BatchAccount_List` | `SELECT` | `subscriptionId` | Gets information about the Batch accounts associated with the subscription. |
| `BatchAccount_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets information about the Batch accounts associated with the specified resource group. |
| `BatchAccount_Create` | `INSERT` | `accountName, resourceGroupName, subscriptionId, data__location` | Creates a new Batch account with the specified parameters. Existing accounts cannot be updated with this API and should instead be updated with the Update Batch Account API. |
| `BatchAccount_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes the specified Batch account. |
| `BatchAccount_GetDetector` | `EXEC` | `accountName, detectorId, resourceGroupName, subscriptionId` | Gets information about the given detector for a given Batch account. |
| `BatchAccount_GetKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | This operation applies only to Batch accounts with allowedAuthenticationModes containing 'SharedKey'. If the Batch account doesn't contain 'SharedKey' in its allowedAuthenticationMode, clients cannot use shared keys to authenticate, and must use another allowedAuthenticationModes instead. In this case, getting the keys will fail. |
| `BatchAccount_ListDetectors` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Gets information about the detectors available for a given Batch account. |
| `BatchAccount_ListOutboundNetworkDependenciesEndpoints` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the endpoints that a Batch Compute Node under this Batch Account may call as part of Batch service administration. If you are deploying a Pool inside of a virtual network that you specify, you must make sure your network allows outbound access to these endpoints. Failure to allow access to these endpoints may cause Batch to mark the affected nodes as unusable. For more information about creating a pool inside of a virtual network, see https://docs.microsoft.com/azure/batch/batch-virtual-network |
| `BatchAccount_RegenerateKey` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__keyName` | This operation applies only to Batch accounts with allowedAuthenticationModes containing 'SharedKey'. If the Batch account doesn't contain 'SharedKey' in its allowedAuthenticationMode, clients cannot use shared keys to authenticate, and must use another allowedAuthenticationModes instead. In this case, regenerating the keys will fail. |
| `BatchAccount_SynchronizeAutoStorageKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Synchronizes access keys for the auto-storage account configured for the specified Batch account, only if storage key authentication is being used. |
| `BatchAccount_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates the properties of an existing Batch account. |
