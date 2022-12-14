---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - time_series_insights
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.time_series_insights.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` | Properties of the PrivateEndpointConnectProperties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnections_Get` | `SELECT` | `environmentName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Gets the details of the private endpoint connection of the environment in the given resource group. |
| `PrivateEndpointConnections_ListByEnvironment` | `SELECT` | `environmentName, resourceGroupName, subscriptionId` | Gets a list of all private endpoint connections in the given environment. |
| `PrivateEndpointConnections_CreateOrUpdate` | `INSERT` | `environmentName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Updates a Private Endpoint connection of the environment in the given resource group. |
| `PrivateEndpointConnections_Delete` | `DELETE` | `environmentName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Disconnects the private endpoint connection and deletes it from the environment. |
