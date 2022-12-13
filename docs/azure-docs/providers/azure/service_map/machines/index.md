---
title: machines
hide_title: false
hide_table_of_contents: false
keywords:
  - machines
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
<tr><td><b>Name</b></td><td><code>machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_map.machines</code></td></tr>
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
| `Machines_Get` | `SELECT` | `machineName, resourceGroupName, subscriptionId, workspaceName` | Returns the specified machine. |
| `Machines_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Returns a collection of machines matching the specified conditions.  The returned collection represents either machines that are active/live during the specified interval  of time (`live=true` and `startTime`/`endTime` are specified) or that are known to have existed at or  some time prior to the specified point in time (`live=false` and `timestamp` is specified). |
| `Machines_GetLiveness` | `EXEC` | `machineName, resourceGroupName, subscriptionId, workspaceName` | Obtains the liveness status of the machine during the specified time interval. |
| `Machines_ListConnections` | `EXEC` | `machineName, resourceGroupName, subscriptionId, workspaceName` | Returns a collection of connections terminating or originating at the specified machine |
| `Machines_ListMachineGroupMembership` | `EXEC` | `machineName, resourceGroupName, subscriptionId, workspaceName` | Returns a collection of machine groups this machine belongs to during the specified time interval. |
| `Machines_ListPorts` | `EXEC` | `machineName, resourceGroupName, subscriptionId, workspaceName` | Returns a collection of live ports on the specified machine during the specified time interval. |
| `Machines_ListProcesses` | `EXEC` | `machineName, resourceGroupName, subscriptionId, workspaceName` | Returns a collection of processes on the specified machine matching the specified conditions. The returned collection represents either processes that are active/live during the specified interval  of time (`live=true` and `startTime`/`endTime` are specified) or that are known to have existed at or  some time prior to the specified point in time (`live=false` and `timestamp` is specified).         |
