---
title: storage_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_accounts
  - data_box_edge
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>storage_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_box_edge.storage_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The object name. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The hierarchical type of the object. |
| `properties` | `object` | The storage account properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `StorageAccounts_Get` | `SELECT` | `deviceName, resourceGroupName, storageAccountName, subscriptionId` |  |
| `StorageAccounts_ListByDataBoxEdgeDevice` | `SELECT` | `deviceName, resourceGroupName, subscriptionId` |  |
| `StorageAccounts_CreateOrUpdate` | `INSERT` | `deviceName, resourceGroupName, storageAccountName, subscriptionId, data__properties` |  |
| `StorageAccounts_Delete` | `DELETE` | `deviceName, resourceGroupName, storageAccountName, subscriptionId` | Deletes the StorageAccount on the Data Box Edge/Data Box Gateway device. |
