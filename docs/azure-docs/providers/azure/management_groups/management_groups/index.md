---
title: management_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - management_groups
  - management_groups
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
<tr><td><b>Name</b></td><td><code>management_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.management_groups.management_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The fully qualified ID for the management group.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000 |
| `name` | `string` | The name of the management group. For example, 00000000-0000-0000-0000-000000000000 |
| `type` | `string` | The type of the resource.  For example, Microsoft.Management/managementGroups |
| `properties` | `object` | The generic properties of a management group. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagementGroups_Get` | `SELECT` | `groupId` | Get the details of the management group.<br /> |
| `ManagementGroups_List` | `SELECT` |  | List management groups for the authenticated user.<br /> |
| `ManagementGroups_CreateOrUpdate` | `INSERT` | `groupId` | Create or update a management group.<br />If a management group is already created and a subsequent create request is issued with different properties, the management group properties will be updated.<br /> |
| `ManagementGroups_Delete` | `DELETE` | `groupId` | Delete management group.<br />If a management group contains child resources, the request will fail.<br /> |
| `ManagementGroups_GetDescendants` | `EXEC` | `groupId` | List all entities that descend from a management group.<br /> |
| `ManagementGroups_Update` | `EXEC` | `groupId` | Update a management group.<br /> |
