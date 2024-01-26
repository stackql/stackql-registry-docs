---
title: infra_role_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - infra_role_instances
  - fabric_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>infra_role_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.fabric_admin.infra_role_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | The region where the resource is located. |
| `properties` | `object` | All properties of an infrastructure role instance. |
| `tags` | `object` | List of key-value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `infraRoleInstance, location, resourceGroupName, subscriptionId` | Return the requested infrastructure role instance. |
| `list` | `SELECT` | `location, resourceGroupName, subscriptionId` | Returns a list of all infrastructure role instances at a location. |
| `_list` | `EXEC` | `location, resourceGroupName, subscriptionId` | Returns a list of all infrastructure role instances at a location. |
| `power_off` | `EXEC` | `infraRoleInstance, location, resourceGroupName, subscriptionId` | Power off an infrastructure role instance. |
| `power_on` | `EXEC` | `infraRoleInstance, location, resourceGroupName, subscriptionId` | Power on an infrastructure role instance. |
| `reboot` | `EXEC` | `infraRoleInstance, location, resourceGroupName, subscriptionId` | Reboot an infrastructure role instance. |
| `shutdown` | `EXEC` | `infraRoleInstance, location, resourceGroupName, subscriptionId` | Shut down an infrastructure role instance. |
