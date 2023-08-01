---
title: addons
hide_title: false
hide_table_of_contents: false
keywords:
  - addons
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
<tr><td><b>Name</b></td><td><code>addons</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_box_edge.addons</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The object name. |
| `type` | `string` | The hierarchical type of the object. |
| `kind` | `string` | Addon type. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Addons_Get` | `SELECT` | `addonName, deviceName, resourceGroupName, roleName, subscriptionId` | Gets a specific addon by name. |
| `Addons_ListByRole` | `SELECT` | `deviceName, resourceGroupName, roleName, subscriptionId` | Lists all the addons configured in the role. |
| `Addons_CreateOrUpdate` | `INSERT` | `addonName, deviceName, resourceGroupName, roleName, subscriptionId, data__kind` | Create or update a addon. |
| `Addons_Delete` | `DELETE` | `addonName, deviceName, resourceGroupName, roleName, subscriptionId` | Deletes the addon on the device. |
