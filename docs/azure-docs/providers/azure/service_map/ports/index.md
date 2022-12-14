---
title: ports
hide_title: false
hide_table_of_contents: false
keywords:
  - ports
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
<tr><td><b>Name</b></td><td><code>ports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_map.ports</code></td></tr>
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
| `Ports_Get` | `SELECT` | `machineName, portName, resourceGroupName, subscriptionId, workspaceName` | Returns the specified port. The port must be live during the specified time interval. If the port is not live during the interval, status 404 (Not Found) is returned. |
| `Ports_GetLiveness` | `EXEC` | `machineName, portName, resourceGroupName, subscriptionId, workspaceName` | Obtains the liveness status of the port during the specified time interval. |
| `Ports_ListAcceptingProcesses` | `EXEC` | `machineName, portName, resourceGroupName, subscriptionId, workspaceName` | Returns a collection of processes accepting on the specified port |
| `Ports_ListConnections` | `EXEC` | `machineName, portName, resourceGroupName, subscriptionId, workspaceName` | Returns a collection of connections established via the specified port. |
