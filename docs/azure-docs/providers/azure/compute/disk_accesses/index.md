---
title: disk_accesses
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_accesses
  - compute
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
<tr><td><b>Name</b></td><td><code>disk_accesses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.disk_accesses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `extendedLocation` | `object` | The complex type of the extended location. |
| `location` | `string` | Resource location |
| `properties` | `object` |  |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `diskAccessName, resourceGroupName, subscriptionId` | Gets information about a disk access resource. |
| `list` | `SELECT` | `subscriptionId` | Lists all the disk access resources under a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the disk access resources under a resource group. |
| `create_or_update` | `INSERT` | `diskAccessName, resourceGroupName, subscriptionId` | Creates or updates a disk access resource |
| `delete` | `DELETE` | `diskAccessName, resourceGroupName, subscriptionId` | Deletes a disk access resource. |
| `_list` | `EXEC` | `subscriptionId` | Lists all the disk access resources under a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the disk access resources under a resource group. |
| `update` | `EXEC` | `diskAccessName, resourceGroupName, subscriptionId` | Updates (patches) a disk access resource. |
