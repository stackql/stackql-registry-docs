---
title: role_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - role_assignments
  - customer_insights
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
<tr><td><b>Name</b></td><td><code>role_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.role_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `type` | `string` | Resource type. |
| `properties` | `object` | The Role Assignment definition. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RoleAssignments_Get` | `SELECT` | `assignmentName, hubName, resourceGroupName, subscriptionId` | Gets the role assignment in the hub. |
| `RoleAssignments_ListByHub` | `SELECT` | `hubName, resourceGroupName, subscriptionId` | Gets all the role assignments for the specified hub. |
| `RoleAssignments_CreateOrUpdate` | `INSERT` | `assignmentName, hubName, resourceGroupName, subscriptionId` | Creates or updates a role assignment in the hub. |
| `RoleAssignments_Delete` | `DELETE` | `assignmentName, hubName, resourceGroupName, subscriptionId` | Deletes the role assignment in the hub. |
