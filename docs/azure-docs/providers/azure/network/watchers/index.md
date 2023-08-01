---
title: watchers
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers
  - network
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
<tr><td><b>Name</b></td><td><code>watchers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.watchers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `location` | `string` | Resource location. |
| `properties` | `object` | The network watcher properties. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NetworkWatchers_Get` | `SELECT` | `networkWatcherName, resourceGroupName, subscriptionId` | Gets the specified network watcher by resource group. |
| `NetworkWatchers_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all network watchers by resource group. |
| `NetworkWatchers_ListAll` | `SELECT` | `subscriptionId` | Gets all network watchers by subscription. |
| `NetworkWatchers_CreateOrUpdate` | `INSERT` | `networkWatcherName, resourceGroupName, subscriptionId` | Creates or updates a network watcher in the specified resource group. |
| `NetworkWatchers_Delete` | `DELETE` | `networkWatcherName, resourceGroupName, subscriptionId` | Deletes the specified network watcher resource. |
| `NetworkWatchers_CheckConnectivity` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId, data__destination, data__source` | Verifies the possibility of establishing a direct TCP connection from a virtual machine to a given endpoint including another VM or an arbitrary remote server. |
| `NetworkWatchers_GetAzureReachabilityReport` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId, data__endTime, data__providerLocation, data__startTime` | NOTE: This feature is currently in preview and still being tested for stability. Gets the relative latency score for internet service providers from a specified location to Azure regions. |
| `NetworkWatchers_GetFlowLogStatus` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId, data__targetResourceId` | Queries status of flow log and traffic analytics (optional) on a specified resource. |
| `NetworkWatchers_GetNetworkConfigurationDiagnostic` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId, data__profiles, data__targetResourceId` | Gets Network Configuration Diagnostic data to help customers understand and debug network behavior. It provides detailed information on what security rules were applied to a specified traffic flow and the result of evaluating these rules. Customers must provide details of a flow like source, destination, protocol, etc. The API returns whether traffic was allowed or denied, the rules evaluated for the specified flow and the evaluation results. |
| `NetworkWatchers_GetNextHop` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId, data__destinationIPAddress, data__sourceIPAddress, data__targetResourceId` | Gets the next hop from the specified VM. |
| `NetworkWatchers_GetTopology` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId` | Gets the current network topology by resource group. |
| `NetworkWatchers_GetTroubleshooting` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId, data__properties, data__targetResourceId` | Initiate troubleshooting on a specified resource. |
| `NetworkWatchers_GetTroubleshootingResult` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId, data__targetResourceId` | Get the last completed troubleshooting result on a specified resource. |
| `NetworkWatchers_GetVMSecurityRules` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId, data__targetResourceId` | Gets the configured and effective security group rules on the specified VM. |
| `NetworkWatchers_ListAvailableProviders` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId` | NOTE: This feature is currently in preview and still being tested for stability. Lists all available internet service providers for a specified Azure region. |
| `NetworkWatchers_SetFlowLogConfiguration` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId, data__properties, data__targetResourceId` | Configures flow log and traffic analytics (optional) on a specified resource. |
| `NetworkWatchers_UpdateTags` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId` | Updates a network watcher tags. |
| `NetworkWatchers_VerifyIPFlow` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId, data__direction, data__localIPAddress, data__localPort, data__protocol, data__remoteIPAddress, data__remotePort, data__targetResourceId` | Verify IP flow from the specified VM to a location given the currently configured NSG rules. |
