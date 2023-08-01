---
title: role_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - role_instances
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>role_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.role_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ARM ID of the resource. |
| `name` | `string` | The role instance name. |
| `properties` | `object` | The role instance properties of the network function. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RoleInstances_Get` | `SELECT` | `locationName, roleInstanceName, serviceKey, subscriptionId, vendorName` | Gets the information of role instance of vendor network function. |
| `RoleInstances_List` | `SELECT` | `locationName, serviceKey, subscriptionId, vendorName` | Lists the information of role instances of vendor network function. |
| `RoleInstances_Restart` | `EXEC` | `locationName, roleInstanceName, serviceKey, subscriptionId, vendorName` | Restarts a role instance of a vendor network function. |
| `RoleInstances_Start` | `EXEC` | `locationName, roleInstanceName, serviceKey, subscriptionId, vendorName` | Starts a role instance of a vendor network function. |
| `RoleInstances_Stop` | `EXEC` | `locationName, roleInstanceName, serviceKey, subscriptionId, vendorName` | Powers off (stop) a role instance of a vendor network function. |
