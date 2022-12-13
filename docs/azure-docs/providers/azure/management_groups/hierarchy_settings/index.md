---
title: hierarchy_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - hierarchy_settings
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
<tr><td><b>Name</b></td><td><code>hierarchy_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.management_groups.hierarchy_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The fully qualified ID for the settings object.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000/settings/default. |
| `name` | `string` | The name of the object. In this case, default. |
| `properties` | `object` | The generic properties of hierarchy settings. |
| `type` | `string` | The type of the resource.  For example, Microsoft.Management/managementGroups/settings. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `HierarchySettings_List` | `SELECT` | `groupId` | Gets all the hierarchy settings defined at the Management Group level. Settings can only be set on the root Management Group of the hierarchy.<br /> |
| `HierarchySettings_CreateOrUpdate` | `INSERT` | `groupId` | Creates or updates the hierarchy settings defined at the Management Group level.<br /> |
| `HierarchySettings_Delete` | `DELETE` | `groupId` | Deletes the hierarchy settings defined at the Management Group level.<br /> |
| `HierarchySettings_Get` | `EXEC` | `groupId` | Gets the hierarchy settings defined at the Management Group level. Settings can only be set on the root Management Group of the hierarchy.<br /> |
| `HierarchySettings_Update` | `EXEC` | `groupId` | Updates the hierarchy settings defined at the Management Group level.<br /> |
