---
title: storage_movers
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_movers
  - storage_mover
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
<tr><td><b>Name</b></td><td><code>storage_movers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_mover.storage_movers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The resource specific properties for the Storage Mover resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, storageMoverName, subscriptionId` | Gets a Storage Mover resource. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Storage Movers in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all Storage Movers in a subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, storageMoverName, subscriptionId` | Creates or updates a top-level Storage Mover resource. |
| `delete` | `DELETE` | `resourceGroupName, storageMoverName, subscriptionId` | Deletes a Storage Mover resource. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all Storage Movers in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all Storage Movers in a subscription. |
| `update` | `EXEC` | `resourceGroupName, storageMoverName, subscriptionId` | Updates properties for a Storage Mover resource. Properties not specified in the request body will be unchanged. |
