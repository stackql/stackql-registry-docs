---
title: managed_hsms
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_hsms
  - key_vault
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
<tr><td><b>Name</b></td><td><code>managed_hsms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.key_vault.managed_hsms</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The Azure Resource Manager resource ID for the managed HSM Pool. |
| `name` | `string` | The name of the managed HSM Pool. |
| `location` | `string` | The supported Azure location where the managed HSM Pool should be created. |
| `properties` | `object` | Properties of the managed HSM Pool |
| `sku` | `object` | SKU details |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the key vault resource. |
| `tags` | `object` | Resource tags |
| `type` | `string` | The resource type of the managed HSM Pool. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedHsms_Get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Gets the specified managed HSM Pool. |
| `ManagedHsms_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | The List operation gets information about the managed HSM Pools associated with the subscription and within the specified resource group. |
| `ManagedHsms_ListBySubscription` | `SELECT` | `subscriptionId` | The List operation gets information about the managed HSM Pools associated with the subscription. |
| `ManagedHsms_CreateOrUpdate` | `INSERT` | `name, resourceGroupName, subscriptionId` | Create or update a managed HSM Pool in the specified subscription. |
| `ManagedHsms_Delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Deletes the specified managed HSM Pool. |
| `ManagedHsms_CheckMhsmNameAvailability` | `EXEC` | `subscriptionId, data__name` | Checks that the managed hsm name is valid and is not already in use. |
| `ManagedHsms_GetDeleted` | `EXEC` | `location, name, subscriptionId` | Gets the specified deleted managed HSM. |
| `ManagedHsms_ListDeleted` | `EXEC` | `subscriptionId` | The List operation gets information about the deleted managed HSMs associated with the subscription. |
| `ManagedHsms_PurgeDeleted` | `EXEC` | `location, name, subscriptionId` | Permanently deletes the specified managed HSM. |
| `ManagedHsms_Update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Update a managed HSM Pool in the specified subscription. |
