---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - analysis_services
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
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.analysis_services.servers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | An identifier that represents the Analysis Services resource. |
| `name` | `string` | The name of the Analysis Services resource. |
| `properties` | `object` | Properties of Analysis Services resource. |
| `sku` | `object` | Represents the SKU name and Azure pricing tier for Analysis Services resource. |
| `tags` | `object` | Key-value pairs of additional resource provisioning properties. |
| `type` | `string` | The type of the Analysis Services resource. |
| `location` | `string` | Location of the Analysis Services resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Servers_List` | `SELECT` | `subscriptionId` | Lists all the Analysis Services servers for the given subscription. |
| `Servers_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the Analysis Services servers for the given resource group. |
| `Servers_Create` | `INSERT` | `resourceGroupName, serverName, subscriptionId` | Provisions the specified Analysis Services server based on the configuration specified in the request. |
| `Servers_Delete` | `DELETE` | `resourceGroupName, serverName, subscriptionId` | Deletes the specified Analysis Services server. |
| `Servers_CheckNameAvailability` | `EXEC` | `location, subscriptionId` | Check the name availability in the target location. |
| `Servers_DissociateGateway` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Dissociates a Unified Gateway associated with the server. |
| `Servers_GetDetails` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Gets details about the specified Analysis Services server. |
| `Servers_ListGatewayStatus` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Return the gateway status of the specified Analysis Services server instance. |
| `Servers_ListOperationResults` | `EXEC` | `location, operationId, subscriptionId` | List the result of the specified operation. |
| `Servers_ListOperationStatuses` | `EXEC` | `location, operationId, subscriptionId` | List the status of operation. |
| `Servers_ListSkusForExisting` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Lists eligible SKUs for an Analysis Services resource. |
| `Servers_ListSkusForNew` | `EXEC` | `subscriptionId` | Lists eligible SKUs for Analysis Services resource provider. |
| `Servers_Resume` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Resumes operation of the specified Analysis Services server instance. |
| `Servers_Suspend` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Suspends operation of the specified Analysis Services server instance. |
| `Servers_Update` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Updates the current state of the specified Analysis Services server. |
