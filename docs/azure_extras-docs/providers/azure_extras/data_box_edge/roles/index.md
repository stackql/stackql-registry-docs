---
title: roles
hide_title: false
hide_table_of_contents: false
keywords:
  - roles
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
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_box_edge.roles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The object name. |
| `kind` | `string` | Role type. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Roles_Get` | `SELECT` | `deviceName, name, resourceGroupName, subscriptionId` | Gets a specific role by name. |
| `Roles_ListByDataBoxEdgeDevice` | `SELECT` | `deviceName, resourceGroupName, subscriptionId` | Lists all the roles configured in a Data Box Edge/Data Box Gateway device. |
| `Roles_CreateOrUpdate` | `INSERT` | `deviceName, name, resourceGroupName, subscriptionId, data__kind` | Create or update a role. |
| `Roles_Delete` | `DELETE` | `deviceName, name, resourceGroupName, subscriptionId` | Deletes the role on the device. |
