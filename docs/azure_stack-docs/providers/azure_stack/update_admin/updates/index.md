---
title: updates
hide_title: false
hide_table_of_contents: false
keywords:
  - updates
  - update_admin
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
<tr><td><b>Name</b></td><td><code>updates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.update_admin.updates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Region location of resource. |
| `properties` | `object` | Properties of an update. |
| `tags` | `object` | List of key-value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, updateLocation, updateName` | Get a specific update at an update location. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, updateLocation` | Get the list of updates at an update locations |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, updateLocation` | Get the list of updates at an update locations |
| `apply` | `EXEC` | `resourceGroupName, subscriptionId, updateLocation, updateName` | Apply a specific update at an update location. |
| `health_check` | `EXEC` | `resourceGroupName, subscriptionId, updateLocation, updateName` | Run health check for a specified update at an update location. |
| `prepare` | `EXEC` | `resourceGroupName, subscriptionId, updateLocation, updateName` | Prepare a specified update at an update location. |
