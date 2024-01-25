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
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The supported Azure location where the managed HSM Pool should be created. |
| `properties` | `object` | Properties of the managed HSM Pool |
| `sku` | `object` | SKU details |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the key vault resource. |
| `tags` | `object` | Resource tags |
| `type` | `string` | The resource type of the managed HSM Pool. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Gets the specified managed HSM Pool. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | The List operation gets information about the managed HSM Pools associated with the subscription and within the specified resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | The List operation gets information about the managed HSM Pools associated with the subscription. |
| `create_or_update` | `INSERT` | `name, resourceGroupName, subscriptionId` | Create or update a managed HSM Pool in the specified subscription. |
| `delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Deletes the specified managed HSM Pool. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | The List operation gets information about the managed HSM Pools associated with the subscription and within the specified resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | The List operation gets information about the managed HSM Pools associated with the subscription. |
| `check_mhsm_name_availability` | `EXEC` | `subscriptionId, data__name` | Checks that the managed hsm name is valid and is not already in use. |
| `purge_deleted` | `EXEC` | `location, name, subscriptionId` | Permanently deletes the specified managed HSM. |
| `update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Update a managed HSM Pool in the specified subscription. |
