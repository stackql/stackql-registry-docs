---
title: machine_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - machine_groups
  - service_map
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
<tr><td><b>Name</b></td><td><code>machine_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_map.machine_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Resource ETAG. |
| `kind` | `string` | Additional resource type qualifier. |
| `properties` | `object` | Resource properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `machineGroupName, resourceGroupName, subscriptionId, workspaceName` | Returns the specified machine group as it existed during the specified time interval. |
| `list_by_workspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Returns all machine groups during the specified time interval. |
| `create` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName` | Creates a new machine group. |
| `delete` | `DELETE` | `machineGroupName, resourceGroupName, subscriptionId, workspaceName` | Deletes the specified Machine Group. |
| `_list_by_workspace` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Returns all machine groups during the specified time interval. |
| `update` | `EXEC` | `machineGroupName, resourceGroupName, subscriptionId, workspaceName` | Updates a machine group. |
