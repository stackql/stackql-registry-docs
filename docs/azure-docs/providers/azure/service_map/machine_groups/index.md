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
| `properties` | `object` | Resource properties. |
| `etag` | `string` | Resource ETAG. |
| `kind` | `string` | Additional resource type qualifier. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `MachineGroups_Get` | `SELECT` | `machineGroupName, resourceGroupName, subscriptionId, workspaceName` | Returns the specified machine group as it existed during the specified time interval. |
| `MachineGroups_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Returns all machine groups during the specified time interval. |
| `MachineGroups_Create` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName` | Creates a new machine group. |
| `MachineGroups_Delete` | `DELETE` | `machineGroupName, resourceGroupName, subscriptionId, workspaceName` | Deletes the specified Machine Group. |
| `MachineGroups_Update` | `EXEC` | `machineGroupName, resourceGroupName, subscriptionId, workspaceName` | Updates a machine group. |
