---
title: protected_item
hide_title: false
hide_table_of_contents: false
keywords:
  - protected_item
  - data_replication
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
<tr><td><b>Name</b></td><td><code>protected_item</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_replication.protected_item</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the Id of the resource. |
| `name` | `string` | Gets or sets the name of the resource. |
| `properties` | `object` | Protected item model properties. |
| `systemData` | `object` | System data required to be defined for Azure resources. |
| `type` | `string` | Gets or sets the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `protectedItemName, resourceGroupName, subscriptionId, vaultName` | Gets the details of the protected item. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, vaultName` | Gets the list of protected items in the given vault. |
| `create` | `INSERT` | `protectedItemName, resourceGroupName, subscriptionId, vaultName, data__properties` | Creates the protected item. |
| `delete` | `DELETE` | `protectedItemName, resourceGroupName, subscriptionId, vaultName` | Removes the protected item. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, vaultName` | Gets the list of protected items in the given vault. |
| `planned_failover` | `EXEC` | `protectedItemName, resourceGroupName, subscriptionId, vaultName, data__properties` | Performs the planned failover on the protected item. |
