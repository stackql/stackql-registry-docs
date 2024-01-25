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
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the vault. |
| `sku` | `object` | The resource model definition representing SKU |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, vaultName` | Get the Vault details. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieve a list of Vaults. |
| `list_by_subscription_id` | `SELECT` | `subscriptionId` | Fetches all the resources of the specified type in the subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, vaultName` | Creates or updates a Recovery Services vault. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, vaultName` | Deletes a vault. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Retrieve a list of Vaults. |
| `_list_by_subscription_id` | `EXEC` | `subscriptionId` | Fetches all the resources of the specified type in the subscription. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, vaultName` | Updates the vault. |
| `vaults` | `EXEC` | `operationId, resourceGroupName, subscriptionId, vaultName` | Gets the operation result for a resource. |
