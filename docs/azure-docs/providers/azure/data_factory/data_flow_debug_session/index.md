---
title: data_flow_debug_session
hide_title: false
hide_table_of_contents: false
keywords:
  - data_flow_debug_session
  - data_factory
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
<tr><td><b>Name</b></td><td><code>data_flow_debug_session</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.data_flow_debug_session</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataFlowDebugSession_Create` | `INSERT` | `api-version, factoryName, resourceGroupName, subscriptionId` | Creates a data flow debug session. |
| `DataFlowDebugSession_Delete` | `DELETE` | `api-version, factoryName, resourceGroupName, subscriptionId` | Deletes a data flow debug session. |
| `DataFlowDebugSession_AddDataFlow` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId` | Add a data flow into debug session. |
| `DataFlowDebugSession_ExecuteCommand` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId` | Execute a data flow debug command. |
| `DataFlowDebugSession_QueryByFactory` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId` | Query all active data flow debug sessions. |
