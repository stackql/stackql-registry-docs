---
title: roles
hide_title: false
hide_table_of_contents: false
keywords:
  - roles
  - postgresql_hsc
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
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.postgresql_hsc.roles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The properties of a server group role. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Roles_ListByServerGroup` | `SELECT` | `resourceGroupName, serverGroupName, subscriptionId` | List all the roles in a given server group. |
| `Roles_Create` | `INSERT` | `resourceGroupName, roleName, serverGroupName, subscriptionId` | Creates a new role or updates an existing role. |
| `Roles_Delete` | `DELETE` | `resourceGroupName, roleName, serverGroupName, subscriptionId` | Deletes a server group role. |
