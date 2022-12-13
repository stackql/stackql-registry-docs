---
title: vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - vaults
  - recovery_services
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
<tr><td><b>Name</b></td><td><code>vaults</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services.vaults</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `sku` | `object` | Identifies the unique system identifier for each Azure resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of the vault. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Vaults_Get` | `SELECT` | `api-version, resourceGroupName, subscriptionId, vaultName` | Get the Vault details. |
| `Vaults_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Retrieve a list of Vaults. |
| `Vaults_ListBySubscriptionId` | `SELECT` | `api-version, subscriptionId` | Fetches all the resources of the specified type in the subscription. |
| `Vaults_CreateOrUpdate` | `INSERT` | `api-version, resourceGroupName, subscriptionId, vaultName` | Creates or updates a Recovery Services vault. |
| `Vaults_Delete` | `DELETE` | `api-version, resourceGroupName, subscriptionId, vaultName` | Deletes a vault. |
| `GetOperationResult` | `EXEC` | `api-version, operationId, resourceGroupName, subscriptionId, vaultName` | Gets the operation result for a resource. |
| `GetOperationStatus` | `EXEC` | `api-version, operationId, resourceGroupName, subscriptionId, vaultName` | Gets the operation status for a resource. |
| `Vaults_Update` | `EXEC` | `api-version, resourceGroupName, subscriptionId, vaultName` | Updates the vault. |
