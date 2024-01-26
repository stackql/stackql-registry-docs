---
title: inventory_items
hide_title: false
hide_table_of_contents: false
keywords:
  - inventory_items
  - connected_vsphere
  - azure_isv    
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
<tr><td><b>Id</b></td><td><code>azure_isv.connected_vsphere.inventory_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| `properties` | `object` | Describes the properties of an Inventory Item. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, inventoryItemName, resourceGroupName, subscriptionId, vcenterName` | Implements InventoryItem GET method. |
| `list_by_v_center` | `SELECT` | `api-version, resourceGroupName, subscriptionId, vcenterName` | Returns the list of inventoryItems of the given vCenter. |
| `create` | `INSERT` | `api-version, inventoryItemName, resourceGroupName, subscriptionId, vcenterName, data__properties` | Create Or Update InventoryItem. |
| `delete` | `DELETE` | `api-version, inventoryItemName, resourceGroupName, subscriptionId, vcenterName` | Implements inventoryItem DELETE method. |
| `_list_by_v_center` | `EXEC` | `api-version, resourceGroupName, subscriptionId, vcenterName` | Returns the list of inventoryItems of the given vCenter. |
