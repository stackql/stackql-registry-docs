---
title: inventory_items
hide_title: false
hide_table_of_contents: false
keywords:
  - inventory_items
  - system_center_vm_manager
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
<tr><td><b>Name</b></td><td><code>inventory_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.system_center_vm_manager.inventory_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| `properties` | `object` | Defines the resource properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `inventoryItemResourceName, resourceGroupName, subscriptionId, vmmServerName` | Shows an inventory item. |
| `list_by_vm_m_server` | `SELECT` | `resourceGroupName, subscriptionId, vmmServerName` | Returns the list of inventoryItems in the given VMMServer. |
| `create` | `INSERT` | `inventoryItemResourceName, resourceGroupName, subscriptionId, vmmServerName, data__properties` | Create Or Update InventoryItem. |
| `delete` | `DELETE` | `inventoryItemResourceName, resourceGroupName, subscriptionId, vmmServerName` | Deletes an inventoryItem. |
| `_list_by_vm_m_server` | `EXEC` | `resourceGroupName, subscriptionId, vmmServerName` | Returns the list of inventoryItems in the given VMMServer. |
