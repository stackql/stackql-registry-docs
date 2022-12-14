---
title: private_endpoint_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connection
  - api_management
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.private_endpoint_connection</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of the PrivateEndpointConnectProperties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnection_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists all private endpoint connections of the API Management service instance. |
| `PrivateEndpointConnection_CreateOrUpdate` | `INSERT` | `privateEndpointConnectionName, resourceGroupName, serviceName, subscriptionId` | Creates a new Private Endpoint Connection or updates an existing one. |
| `PrivateEndpointConnection_Delete` | `DELETE` | `privateEndpointConnectionName, resourceGroupName, serviceName, subscriptionId` | Deletes the specified Private Endpoint Connection. |
| `PrivateEndpointConnection_GetByName` | `EXEC` | `privateEndpointConnectionName, resourceGroupName, serviceName, subscriptionId` | Gets the details of the Private Endpoint Connection specified by its identifier. |
| `PrivateEndpointConnection_GetPrivateLinkResource` | `EXEC` | `privateLinkSubResourceName, resourceGroupName, serviceName, subscriptionId` | Gets the private link resources |
| `PrivateEndpointConnection_ListPrivateLinkResources` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Gets the private link resources |
