---
title: processes
hide_title: false
hide_table_of_contents: false
keywords:
  - processes
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
<tr><td><b>Name</b></td><td><code>processes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_map.processes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Additional resource type qualifier. |
| `properties` | `object` | Resource properties. |
| `etag` | `string` | Resource ETAG. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Processes_Get` | `SELECT` | `machineName, processName, resourceGroupName, subscriptionId, workspaceName` | Returns the specified process. |
| `Processes_GetLiveness` | `EXEC` | `machineName, processName, resourceGroupName, subscriptionId, workspaceName` | Obtains the liveness status of the process during the specified time interval. |
| `Processes_ListAcceptingPorts` | `EXEC` | `machineName, processName, resourceGroupName, subscriptionId, workspaceName` | Returns a collection of ports on which this process is accepting |
| `Processes_ListConnections` | `EXEC` | `machineName, processName, resourceGroupName, subscriptionId, workspaceName` | Returns a collection of connections terminating or originating at the specified process |
