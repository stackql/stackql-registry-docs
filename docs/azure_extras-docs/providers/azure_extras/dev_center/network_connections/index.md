---
title: network_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - network_connections
  - dev_center
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>network_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_center.network_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Network properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NetworkConnections_Get` | `SELECT` |  | Gets a network connection resource |
| `NetworkConnections_ListByResourceGroup` | `SELECT` |  | Lists network connections in a resource group |
| `NetworkConnections_ListBySubscription` | `SELECT` |  | Lists network connections in a subscription |
| `NetworkConnections_CreateOrUpdate` | `INSERT` |  | Creates or updates a Network Connections resource |
| `NetworkConnections_Delete` | `DELETE` |  | Deletes a Network Connections resource |
| `NetworkConnections_GetHealthDetails` | `EXEC` | `networkConnectionName, resourceGroupName, subscriptionId` | Gets health check status details. |
| `NetworkConnections_ListHealthDetails` | `EXEC` |  | Lists health check status details |
| `NetworkConnections_RunHealthChecks` | `EXEC` | `networkConnectionName, resourceGroupName, subscriptionId` | Triggers a new health check run. The execution and health check result can be tracked via the network Connection health check details |
| `NetworkConnections_Update` | `EXEC` |  | Partially updates a Network Connection |
